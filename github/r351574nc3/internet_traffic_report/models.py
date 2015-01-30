import json

# Create your models here.
class TrafficReport(object):
    """A representation of a traffic report from http://www.internettrafficreport.com/details.htm as a python object. Generically,
    speaking, it is a immutable wrapper around a list that only supports ReportEntry instances.

    """
    
    def __init__(self):
        self._entries = []

    def __get_entries(self):
        """Calculates the 'entries' property."""
        return self._entries

    def ___get_entries(self):
        """Indirect accessor for 'entries' property."""
        return self.__get_entries()

    def __set_entries(self, entries):
        """Sets the 'entries' property."""
        self._entries = entries

    def ___set_entries(self, entries):
        """Indirect setter for 'entries' property."""
        self.__set_entries(entries)

    entries = property(___get_entries, ___set_entries,
        doc="""Gets or sets the entries of the traffic report.""")

    def __str__(self):
        """
        Converts the report to a JSON string representation of the data. Here is an example:

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
        
        It does this by converting each ReportEntry instance to its entry.__dict__ and adding it to a list. This list of 
        primitives is then converted to json.
        """
        primitives = []
        for entry in self.entries:
            primitives.append(entry.__dict__)
        return json.dump(primitives)
        
        

class ReportEntry(object):
    """An individual Entry used in Traffic Report. It consists of router, location, index, response time, packet loss, and 
    continent attributes which make up a single entry for a site in the report.

    """
    def __init__(self):
        self._router        = None
        self._location      = None
        self._index         = None
        self._response_time = None
        self._packet_loss   = None
        self._continent     = None

    @classmethod
    def create(cls, **kwargs):
        retval = cls()
        
        for prop in kwargs:
            attr = '_' + prop
            if hasattr(retval, attr):
                setattr(retval, attr, kwargs[prop])
            else:
                raise AttributeErrror
            
    @classmethod
    def Builder(cls):
        return ReportEntryBuilder()

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

    def __get_location(self):
        """Calculates the 'location' property."""
        return self._location

    def ___get_location(self):
        """Indirect accessor for 'location' property."""
        return self.__get_location()

    def __set_location(self, location):
        """Sets the 'location' property."""
        self._location = location

    def ___set_location(self, location):
        """Indirect setter for 'location' property."""
        self.__set_location(location)

    location = property(___get_location, ___set_location,
        doc="""Gets or sets the location of the report entry.""")
    
    def __get_index(self):
        """Calculates the 'index' property."""
        return self._index

    def ___get_index(self):
        """Indirect accessor for 'index' property."""
        return self.__get_index()

    def __set_index(self, index):
        """Sets the 'index' property."""
        self._index = index

    def ___set_index(self, index):
        """Indirect setter for 'index' property."""
        self.__set_index(index)

    index = property(___get_index, ___set_index,
        doc="""Gets or sets the index of the report entry.""") 

    def __get_response_time(self):
        """Calculates the 'response_time' property."""
        return self._response_time

    def ___get_response_time(self):
        """Indirect accessor for 'response_time' property."""
        return self.__get_response_time()

    def __set_response_time(self, response_time):
        """Sets the 'response_time' property."""
        self._response_time = response_time

    def ___set_response_time(self, response_time):
        """Indirect setter for 'response_time' property."""
        self.__set_response_time(response_time)

    response_time = property(___get_response_time, ___set_response_time,
        doc="""Gets or sets the response_time of the report entry.""")

    def __get_packet_loss(self):
        """Calculates the 'packet_loss' property."""
        return self._packet_loss

    def ___get_packet_loss(self):
        """Indirect accessor for 'packet_loss' property."""
        return self.__get_packet_loss()

    def __set_packet_loss(self, packet_loss):
        """Sets the 'packet_loss' property."""
        self._packet_loss = packet_loss

    def ___set_packet_loss(self, packet_loss):
        """Indirect setter for 'packet_loss' property."""
        self.__set_packet_loss(packet_loss)

    packet_loss = property(___get_packet_loss, ___set_packet_loss,
        doc="""Gets or sets the packet_loss of the report entry.""")

    def __get_continent(self):
        """Calculates the 'continent' property."""
        return self._continent

    def ___get_continent(self):
        """Indirect accessor for 'continent' property."""
        return self.__get_continent()

    def __set_continent(self, continent):
        """Sets the 'continent' property."""
        self._continent = continent

    def ___set_continent(self, continent):
        """Indirect setter for 'continent' property."""
        self.__set_continent(continent)

    continent = property(___get_continent, ___set_continent,
        doc="""Gets or sets the continent of the report entry.""")
        
    
class ReportEntryBuilder(object):
    def __init__(self):
        self.router        = None
        self.location      = None
        self.index         = None
        self.response_time = None
        self.packet_loss   = None
        self.continent     = None
    
    def with_router(self, router):
        self.router = router
        return self

    def with_location(self, location):
        self.location = location
        return self

    def with_index(self, index):
        self.index = index
        return self

    def with_response_time(self, response_time):
        self.response_time = response_time
        return self

    def with_packet_loss(self, packet_loss):
        self.packet_loss = packet_loss
        return self

    def with_continent(self, continent):
        self.continent = continent
        return self

    def build(self):
        retval = ReportEntry.create(       router = self.router,
                                         location = self.location,
                                            index = self.index,
                                    response_time = self.response_time,
                                      packet_loss = self.packet_loss,
                                        continent = self.continent     )
        return retval
