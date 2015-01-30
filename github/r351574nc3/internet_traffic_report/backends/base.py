class ItrDispatcher(object):
    """Interface for negotiating protocols and handling data from Internet Traffic Results"""

    def __init__(self):
        self._url = None
        self._contents = None

    def __get_contents(self):
        """Calculates the 'contents' property."""
        return self._contents

    def ___get_contents(self):
        """Indirect accessor for 'contents' property."""
        return self.__get_contents()

    def __set_contents(self, contents):
        """Sets the 'contents' property."""
        self._contents = contents

    def ___set_contents(self, contents):
        """Indirect setter for 'contents' property."""
        self.__set_contents(contents)

    contents = property(___get_contents, ___set_contents,
        doc="""Gets or sets the contents of the report entry.""")
    
    def __get_url(self):
        """Calculates the 'url' property."""
        return self._url

    def ___get_url(self):
        """Indirect accessor for 'url' property."""
        return self.__get_url()

    def __set_url(self, url):
        """Sets the 'url' property."""
        self._url = url

    def ___set_url(self, url):
        """Indirect setter for 'url' property."""
        self.__set_url(url)

    url = property(___get_url, ___set_url,
        doc="""Gets or sets the url of the report entry.""")

    def dispatch(self):
        """Does the actual dispatch, communication and retrieval of data. Any data is stored in the contents property"""
        pass
    
class ItrDatasource(object):
    """
    Interface for Internet Traffic Results Datasources. The methods are stubbed out. They need to be implemented by an inheriting class.
    """

    def __get_dispatcher(self):
        """Calculates the 'dispatcher' property."""
        return self._dispatcher

    def ___get_dispatcher(self):
        """Indirect accessor for 'dispatcher' property."""
        return self.__get_dispatcher()

    def __set_dispatcher(self, dispatcher):
        """Sets the 'dispatcher' property."""
        self._dispatcher = dispatcher

    def ___set_dispatcher(self, dispatcher):
        """Indirect setter for 'dispatcher' property."""
        self.__set_dispatcher(dispatcher)

    dispatcher = property(___get_dispatcher, ___set_dispatcher,
        doc="""Gets or sets the dispatcher of the datasource.""")

    def lookup_all_routers(self):
        """Queries ALL of the most recent results of the Internet Traffic Results.

        Args:
            self: calling instance

        Returns:
        Raises:"""
        pass

    def lookup_routers_by_name(self, router):
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

    def lookup_top_routers(self, continent):
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
