"""
http backend datastore for Internet Traffic Reports. This is really a facade to represent the content on the internet
traffic reports website as a read-only datastore.

"""

try:
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    
except ImportError:
    # TODO: Cannot parse results. Need to handle this.
    pass

from django.conf import settings
from github.r351574nc3.internet_traffic_report.backends.base import ItrDatasource
from github.r351574nc3.internet_traffic_report.backends.base import ItrDispatcher
from github.r351574nc3.internet_traffic_report.models import ReportEntry
from github.r351574nc3.internet_traffic_report.models import TrafficReport

class ItrHttpDispatcher(ItrDispatcher):
    """Generic HTTP dispatcher implementation. Handles making the HTTP request to internet traffic reports and retrieving the data
     for the datasource.
    """
    def dispatch(self):
        """Does the actual dispatch, communication and retrieval of data. Any data is stored in the contents property"""

        html = urlopen(self.url)
        return html

class ItrHttpDatasource(ItrDatasource):
    """Implementation of ItrDatasource using HTTP."""

    """When parsing, the number of children in the row will be this number"""
    CONTINENT_COL_LENGTH = 3
    EXPECTED_COL_LENGTH  = 11
    ROUTER_IDX           = 0
    LOCATION_IDX         = 1
    INDEX_IDX            = 2
    RT_IDX               = 3
    PACKET_LOSS_IDX      = 4

    def __init__(self):
        # Assign a default
        url = settings.ITRSERVICES['default']['URL']
        self.dispatcher = ItrHttpDispatcher()
        self.dispatcher.url = url


     def lookup_most_recent_results(self):
        """Queries ALL of the most recent results of the Internet Traffic Results details page. Using the beautifulsoup4 module, 
        the data from an HTTP Request will be parsed for the string 'Most recent test results:'. It then creates a JSON formatted
        representation of the parsed data, and returns it. 
        
        Args:
            self: calling instance
     
        Returns:
            An instance of TrafficReport with each router as a record of type ReportEntry.
        Raises:"""
        retval = TrafficReport()        
        
        if self.dispatcher is None:
            raise AttributeError("The Dispatcher is incorrectly configured.")

        self.dispatcher.dispatch()
        soup = BeautifulSoup(self.dispatcher.contents)
        
        rows = soup.find(text = 'Most recent test results:').find_parent('table').contents
        continent = None
        
        for row in rows:
            if (hasattr(row, 'contents')):
                if (len(row.contents) == ItrHttpDatasource.EXPECTED_COL_LENGTH
                    and row.find('b') is not None):
                    retval.entries.append(self.convert2entry(row, continent))
                elif (len(row.contents) == ItrHttpDatasource.CONTINENT_COL_LENGTH):
                    continent = row.find('b').string
        return retval
                
        
    def lookup_results_by_router(self, router):
        """Queries the most recent results and filters them by router name.

        Args:
            self: calling instance
            router: string name of the router to get results for

        Returns:
           An instance of TrafficReport containing ReportEntry instances for each router that matches.

        Raises:"""
        data = self.lookup_most_recent_results()

        retval = TrafficReport()
        retval.entries = [record for record in data.entries if record.router == router]

        return retval

    def lookup_top_routers(self):
        """Queries the most recent results for the top router in each continent.

        Args:
            self: calling instance

        Returns:
            Instance of TrafficReport containing a top router from each continent
        Raises:"""
        retval = TrafficReport()
        data = self.lookup_most_recent_results()
        data_map = {}
        sorted_entries = sorted(data.entries, key = lambda entry: entry.index)

        for entry in sorted_entries:
            if entry.continent not in data_map:
                data_map[entry.continent] = entry

        for k, entry in data_map.items():
            retval.entries.append(entry)
                
        return retval

    def convert2entry(self, row, continent):
        """Takes a row Tag from BeautifulSoup and creates a ReportEntry instance from it
        Args:
            row: The row to parse into a Report Entry
            continent: A row represents a router. This is the continent the router belongs to.
        Returns:
            A handy, dandy, new ReportEntry instance
        """
        columns = row.find_all('td')
        response_time = int(columns[ItrHttpDatasource.RT_IDX].contents[0])
        packet_loss = int(columns[ItrHttpDatasource.PACKET_LOSS_IDX].contents[0])
        entry = ReportEntry.Builder().with_router(columns[ItrHttpDatasource.ROUTER_IDX].find('b').string).with_location(columns[ItrHttpDatasource.LOCATION_IDX].find('b').string).with_index(columns[ItrHttpDatasource.INDEX_IDX].find('b').string).with_response_time(response_time).with_packet_loss(packet_loss).with_continent(continent)
        return entry

    
def lookup_most_recent_results(self):
    """Queries ALL of the most recent results of the Internet Traffic Results details page. Using the beautifulsoup4 module, 
    the data from an HTTP Request will be parsed for the string 'Most recent test results:'. It then creates a JSON formatted
    representation of the parsed data, and returns it. 
    
    Args:
        self: calling instance

    Returns:
        a JSON string representation of the data. Here is an example:

        [
           {
               "router": "misschaos.chaos-studio.com",
               "location": "China (Shanghai)",
               "index": 0,
               "response_time": 0,
               "packet_loss": 100,
               "continent": "Asia"
           },
           {
               "router": "cisco.syssrc.com",
               "location": "Maryland",
               "index": 88,
               "response_time": 112,
               "packet_loss": 0,
               "continent": "North America"
           },
         
           etc ...
        ]

    Raises:"""
    pass

def lookup_top_routers(self):
    """Queries the most recent results for the top router in each continent.

    Args:
        self: calling instance

    Returns:
        a JSON string representation of the data. Here is an example

        [
           {
               "router": "misschaos.chaos-studio.com",
               "location": "China (Shanghai)",
               "index": 0,
               "response_time": 0,
               "packet_loss": 100,
               "continent": "Asia"
           },
           {
               "router": "cisco.syssrc.com",
               "location": "Maryland",
               "index": 88,
               "response_time": 112,
               "packet_loss": 0,
               "continent": "North America"
           },
         
           etc ...
        ]
    Raises:"""
    pass

def lookup_results_by_router(self, router):
    """Queries the most recent results and filters them by router name.

    Args:
        self: calling instance
        router: string name of the router to get results for

    Returns:
        a JSON string representation of the data. Here is an example

        [
           {
               "router": "misschaos.chaos-studio.com",
               "location": "China (Shanghai)",
               "index": 0,
               "response_time": 0,
               "packet_loss": 100,
               "continent": "Asia"
           },
           {
               "router": "cisco.syssrc.com",
               "location": "Maryland",
               "index": 88,
               "response_time": 112,
               "packet_loss": 0,
               "continent": "North America"
           },
         
           etc ...
        ]
    Raises:"""
    pass
