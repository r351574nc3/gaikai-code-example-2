Documentation for the Internet Traffic Report API
*************************************************

A python api that gives internet traffic report updates from http://www.internettrafficreport.com/details.htm. There are 3 basic
functions of the API

1. Retrieve all router information from the most recent test results.
2. Retrieve only information about a specific router from the most recent test results.
3. Retrieve only information about the top rated router in each continent from the most recent test results.

There are two ways the API is exposed to users.

1. Python API (normal python functions)
2. JSON API (hope you like to Django)
   
Python API Usage
================

To retrieve all routers with python shell::
  >>> from github.r351574nc3.internet_traffic_report.backends.http import ItrHttpDatasource
  >>> datasource = ItrHttpDatasource()
  >>> test_report = datasource.lookup_all_routers()

  >>> print("Router: %s" % test_report.entries[0].router)
  Router: misschaos.chaos-studio.com

To retrieve the router from cisco.syssrc.com with python shell::
  >>> from github.r351574nc3.internet_traffic_report.backends.http import ItrHttpDatasource
  >>> datasource = ItrHttpDatasource()
  >>> test_report = datasource.lookup_routers_by_name('cisco.syssrc.com')
  >>> print("Router: %s" % test_report.entries[0].router)
  Router: cisco.syssrc.com

To retrieve the top rated routers by continent with python shell::
  >>> from github.r351574nc3.internet_traffic_report.backends.http import ItrHttpDatasource
  >>> datasource = ItrHttpDatasource()
  >>> test_report = datasource.lookup_top_routers()
  >>> test_report.entries = [record for record in test_report.entries if record.continent == 'Asia']
  >>> print("Router: %s" % test_report.entries[0].router)
  Router: misschaos.chaos-studio.com


JSON API Usage
================

The application was also written using Django. Views expose the JSON endpoints. First start the application with::
  python manage.py runserver

  Performing system checks...

  System check identified no issues (0 silenced).
  January 30, 2015 - 16:00:24
  Django version 1.7.4, using settings 'gaikaisample.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CONTROL-C.
   
The API can be accessed from
* http://localhost:8000/routers/ (To retrieve all router information)
* http://localhost:8000/routers/cisco.syssrc.com (To retrieve information about a specific router)
* http://localhost:8000/continents/ (For the top rated routers by content)
 
Below is an example of the output::
  [{"continent": "Asia", "packet_loss": 100, "location": "China (Shanghai)", "index": 0, "response_time": 0, "router": "misschaos.chaos-studio.com"}, {"continent": "Europe", "packet_loss": 100, "location": "Africa (Gauteng)", "index": 0, "response_time": 0, "router": "ipsec.eskom.co.za"}, {"continent": "Australia", "packet_loss": 100, "location": "New Zealand (Auckland)", "index": 0, "response_time": 0, "router": "io.peace.co.nz"}, {"continent": "North America", "packet_loss": 100, "location": "California (Anaheim)", "index": 0, "response_time": 0, "router": "anhm7204.exo.com"}, {"continent": "South America", "packet_loss": 0, "location": "Colombia (Valle del Cauca)", "index": 86, "response_time": 132, "router": "router-ut1.uniweb.net.co"}]

Tests
=====

While the framework used is Django, it was unable to be leveraged for unit testing due to the lack of database. Instead,
`unittest` was used. Tests can be executed with::
  python manage.py test itrservices
  .....
  ----------------------------------------------------------------------
  Ran 5 tests in 0.393s
   
  OK

internet_traffic_report classes
===============================

.. automodule:: github.r351574nc3.internet_traffic_report


.. automodule:: github.r351574nc3.internet_traffic_report.models
   :members:

.. automodule:: github.r351574nc3.internet_traffic_report.backends.base
   :members: 

.. automodule:: github.r351574nc3.internet_traffic_report.backends.http
   :members: lookup_all_routers, lookup_routers_by
