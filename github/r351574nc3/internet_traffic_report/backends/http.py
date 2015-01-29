"""
http backend datastore for Internet Traffic Reports. This is really a facade to represent the content on the internet
traffic reports website as a read-only datastore.

"""

try:
    import urllib2
    from bs4 import BeautifulSoup
    
except ImportError:
    # TODO: Cannot parse results. Need to handle this.
    pass

from django.conf import settings
from github.r351574nc3.internet_traffic_report.backends.base import ItrDatasource
from github.r351574nc3.internet_traffic_report.backends.base import ItrDispatcher

class ItrHttpDispatcher(ItrDispatcher):
    """Generic HTTP dispatcher implementation. Handles making the HTTP request to internet traffic reports and retrieving the data
     for the datasource.
    """
    def dispatch(self):
        """Does the actual dispatch, communication and retrieval of data. Any data is stored in the contents property"""
        
        req = urllib2.Request(url = self.url)
        f.urllib2.urlopen(req)

        return f.read()

class ItrHttpDatasource(ItrDatasource):
    """Implementation of ItrDatasource using HTTP."""

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
        if self.dispatcher is None:
            raise AttributeError("The Dispatcher is incorrectly configured.")

        self.dispatcher.dispatch()

    def lookup_results_by_router(self, router):
        """Queries the most recent results and filters them by router name.

        Args:
            self: calling instance
            router: string name of the router to get results for

        Returns:
            a JSON string representation of the data. Here is an example
            {
                "router": "misschaos.chaos-studio.com",
                "location": "China (Shanghai)",
                "index": 0,
                "response_time": 0,
                "packet_loss": 100,
                "continent": "Asia"
            }

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

