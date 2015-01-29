class ItrDispatcher(object):
    """Interface for negotiating protocols and handling data from Internet Traffic Results"""

    def __init__(self, url):
        self.url = url

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
    
class ItrDatasource(object):
    """
    Interface for Internet Traffic Results Datasources. The methods are stubbed out. They need to be implemented by an inheriting class.
    """

    def __get_router(self):
        """Calculates the 'router' property."""
        return self._router

    def ___get_router(self):
        """Indirect accessor for 'router' property."""
        return self.__get_router()

    def __set_router(self, router):
        """Sets the 'router' property."""
        self._router = router

    def ___set_router(self, router):
        """Indirect setter for 'router' property."""
        self.__set_router(router)

    router = property(___get_router, ___set_router,
        doc="""Gets or sets the router of the report entry.""")

    def lookup_most_recent_results(self):
        """Queries ALL of the most recent results of the Internet Traffic Results.

        Args:
            self: calling instance

        Returns:
        Raises:"""
        pass

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

    def lookup_top_router_by_continent(self, continent):
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
