__author__  = 'Leo Przybylski'
__license__ = 'MIT'
__version__ = '0.0.1'

def unsupported():
    raise NotImplementedError("The chosen backend for internet traffic reports services is unavailable.")


try:
    import github.r351574nc3.internet_traffic_report.backends.base
    import github.r351574nc3.internet_traffic_report.backends.http
except ImportError:
    unsupported()
