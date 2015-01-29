from django.db import models

# Create your models here.
class TrafficReport(object):
    def __init__(self):
        self.entries = []

class ReportEntry(object):
    def __init__(self):
        pass

    def Builder(self):
        ReportEntryBuilder()

    def __get_router(self):
        """Calculates the 'router' property."""
        return self.side ** 2

    def ___get_router(self):
        """Indirect accessor for 'router' property."""
        return self.__get_router()

    def __set_router(self, router):
        """Sets the 'router' property."""
        self.side = math.sqrt(router)

    def ___set_router(self, router):
        """Indirect setter for 'router' property."""
        self.__set_router(router)

    router = property(___get_router, ___set_router,
        doc="""Gets or sets the router of the square.""")

    def __get_location(self):
        """Calculates the 'location' property."""
        return self.side ** 2

    def ___get_location(self):
        """Indirect accessor for 'location' property."""
        return self.__get_location()

    def __set_location(self, location):
        """Sets the 'location' property."""
        self.side = math.sqrt(location)

    def ___set_location(self, location):
        """Indirect setter for 'location' property."""
        self.__set_location(location)

    location = property(___get_location, ___set_location,
        doc="""Gets or sets the location of the square.""")
    
    def __get_index(self):
        """Calculates the 'index' property."""
        return self.side ** 2

    def ___get_index(self):
        """Indirect accessor for 'index' property."""
        return self.__get_index()

    def __set_index(self, index):
        """Sets the 'index' property."""
        self.side = math.sqrt(index)

    def ___set_index(self, index):
        """Indirect setter for 'index' property."""
        self.__set_index(index)

    index = property(___get_index, ___set_index,
        doc="""Gets or sets the index of the square.""") 

    def __get_response_time(self):
        """Calculates the 'response_time' property."""
        return self.side ** 2

    def ___get_response_time(self):
        """Indirect accessor for 'response_time' property."""
        return self.__get_response_time()

    def __set_response_time(self, response_time):
        """Sets the 'response_time' property."""
        self.side = math.sqrt(response_time)

    def ___set_response_time(self, response_time):
        """Indirect setter for 'response_time' property."""
        self.__set_response_time(response_time)

    response_time = property(___get_response_time, ___set_response_time,
        doc="""Gets or sets the response_time of the square.""")

    def __get_packet_loss(self):
        """Calculates the 'packet_loss' property."""
        return self.side ** 2

    def ___get_packet_loss(self):
        """Indirect accessor for 'packet_loss' property."""
        return self.__get_packet_loss()

    def __set_packet_loss(self, packet_loss):
        """Sets the 'packet_loss' property."""
        self.side = math.sqrt(packet_loss)

    def ___set_packet_loss(self, packet_loss):
        """Indirect setter for 'packet_loss' property."""
        self.__set_packet_loss(packet_loss)

    packet_loss = property(___get_packet_loss, ___set_packet_loss,
        doc="""Gets or sets the packet_loss of the square.""")

    def __get_continent(self):
        """Calculates the 'continent' property."""
        return self.side ** 2

    def ___get_continent(self):
        """Indirect accessor for 'continent' property."""
        return self.__get_continent()

    def __set_continent(self, continent):
        """Sets the 'continent' property."""
        self.side = math.sqrt(continent)

    def ___set_continent(self, continent):
        """Indirect setter for 'continent' property."""
        self.__set_continent(continent)

    continent = property(___get_continent, ___set_continent,
        doc="""Gets or sets the continent of the square.""")

    
class ReportEntryBuilder(object):
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
        retval = ReportEntry()
        retval.router(self.router)
        retval.location(self.location)
        retval.index(self.index)
        retval.response_time(self.response_time)
        retval.packet_loss(self.packet_loss)
        retval.continent(self.continent)
        return retval
