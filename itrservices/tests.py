
# Disabling Django tests because they require an actual database implementation :(
# from django.test import TestCase

from unittest import TestCase
from github.r351574nc3.internet_traffic_report.models import TrafficReport
from github.r351574nc3.internet_traffic_report.backends.base import ItrDispatcher
from github.r351574nc3.internet_traffic_report.backends.http import ItrHttpDatasource


# Create your tests here.
class TrafficReportApiTests(TestCase):
    """
    Class of test methods for testing the Traffic Report API
    """

    def setUp(self):
        self.datasource = ItrHttpDatasource()
        self.datasource.dispatcher = MockItrDispatcher()

    def tearDown(self):
        pass
    
    def test_lookup_most_recent_results(self):
        """Tests the method to retrieve the most recent internet traffic test results"""
        
        test_report = self.datasource.lookup_most_recent_results()

        self.assertTrue(test_report is not None)
        self.assertTrue(isinstance(test_report, TrafficReport))
        self.assertTrue(len(test_report.entries) == 75)

    def test_lookup_most_recent_results2(self):
        """Testing the usage of a datasource with no dispatcher"""
        
        temp_datasource = ItrHttpDatasource()
        temp_datasource.dispatcher = None

        test_report = self.datasource.lookup_most_recent_results()
        

    def test_lookup_results_by_router(self):
        """Basic test for executing lookup_results_by_router"""
        test_report = self.datasource.lookup_results_by_router('wormhole.homeisp.com')
        self.assertTrue(test_report is not None)
        self.assertTrue(isinstance(test_report, TrafficReport))
        self.assertEqual(len(test_report.entries), 1)

        test_entry = test_report.entries[0]
        self.assertEqual(test_entry.location, 'Missouri (Kansas City)')
        self.assertEqual(test_entry.index, 95)
        self.assertEqual(test_entry.response_time, 42)
        self.assertEqual(test_entry.packet_loss, 0)

    def test_lookup_results_by_router2(self):
        """Test lookup_results_by_router given a router that doesn't exist"""
        
        test_report = self.datasource.lookup_results_by_router('flickr.com')
        self.assertTrue(test_report is not None)
        self.assertEqual(len(test_report.entries), 0)
        
    def test_lookup_top_router_by_continent(self):
        """Basic test for executing lookup_top_routers. Verifies that 5 results are returned."""
        test_report = self.datasource.lookup_top_routers()
        self.assertTrue(test_report is not None)
        self.assertTrue(isinstance(test_report, TrafficReport))
        self.assertEqual(len(test_report.entries), 5)
        self.assertEqual
        
#########################################################################################
# End of Tests                                                                          #
# Fixtures are below
#########################################################################################

class MockItrDispatcher(ItrDispatcher):
    """Mock dispatcher used so we don't actually have to ping the internet 
    """
    def dispatch(self):
        """Does the actual dispatch, communication and retrieval of data. Any data is stored in the contents property"""
        self.contents = """
<HTML>
<HEAD>
    <META NAME="robots" CONTENT="index,follow">
<META HTTP-EQUIV="Pragma" CONTENT="no-cache">
<META NAME="ICBM" content="33.4478, -112.0739">
<META NAME="DC.title" content="Internet Traffic Report">




    <META NAME="description"        CONTENT="View the complete list of routers, and their last reported results.">



    <META NAME="keywords"           CONTENT="itr,internet traffic report,internet,routers,traffic,ping,traceroute,statistics,graphs,outages,performance,overall,current measurement,results">


<META NAME="generator" CONTENT="AnalogX MacroPage">
    <TITLE>Raw Measurements /// Internet Traffic Report</TITLE>
</HEAD>
<BODY bgcolor="#ffffff" text="#000000" link="#226699" alink="#993377" vlink="#337799" marginheight=0 marginwidth=0 topmargin=0 leftmargin=0 rightmargin=0>
<FONT face="Arial, Helvetica" Size=2>

<center>

<table cellpadding=0 cellspacing=0 border=0 width=630>
<tr>
    <td colspan=3>
    &nbsp;<BR>
    </td>
</tr>
<tr>
    <td valign=top>
        <table cellpadding=0 cellspacing=0 border=0 width=485>
        <tr>
            <td width=140>
                <a href="/"><img src="/look/itrlogo.gif" width=179 height=74 border=0></a><br>
            </td>
            <td align=center width=225>
                <font size=1>
                The Internet Traffic Report monitors the flow of data around the world. It then displays a
                value between zero and 100. Higher values indicate faster and more reliable connections.</font><br>
                <img src="/look/blank.gif" width=210 height=1><br>
            </td>
            <td width=120 align=right valign=bottom>
                <img src="/look/blank.gif" width=120 height=1><br>
                <img src="/gifs/tr_index_global.gif" width=110 height=74><BR>
            </td>
        </tr>
        <tr>
            <td align=center colspan=3>
                <table cellpadding=0 cellspacing=0 border=0 width="100%">
<tr>
    <td bgcolor="#000000"><img src="/look/dot.gif" width=1 height=2></td>
</tr>
</table>
                    <A href="/">Home</a>
                    &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;<A href="/faq.htm">FAQ</a>
                    &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;<A href="/event.htm">Events</a>
                    &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;<A href="/contact.htm">Contact</a>
                    &nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;<A href="/links.htm">Links</a>
                <table cellpadding=0 cellspacing=0 border=0 width="100%">
<tr>
    <td bgcolor="#000000"><img src="/look/dot.gif" width=1 height=2></td>
</tr>
</table>
            </td>
        </tr>
        </table>
<BR>

<FONT face="Arial" size=5 color="#919195"><B>Raw measurements</B></FONT><BR>
<BR>

<table cellpadding=0 cellspacing=0 border=0 bgcolor="#99CCFF" width="100%">
<tr>
    <td>
        <table cellpadding=2 cellspacing=2 border=1 width="100%">
        <tr>
            <td colspan=5 bgcolor="#FFFFFF">
                <font size=3>
                <B>Most recent test results:</B></font><br>
            </td>
        </tr>
        <tr bgcolor="#000000">
            <td align=center>
                <font size=1 color="#FFFFFF">Router</font><br>
            </td>
            <td align=center>
                <font size=1 color="#FFFFFF">Location</font><br>
            </td>
            <td align=center>
                <font size=1 color="#FFFFFF">Current Index</font><br>
            </td>
            <td align=center>
                <font size=1 color="#FFFFFF">Response Time (ms)</font><br>
            </td>
            <td align=center>
                <font size=1 color="#FFFFFF">Packet Loss (%)</font><br>
            </td>
        </tr>

<tr>
            <td colspan=5 bgcolor="#CCCCCC">
                <font size=3>
                <B>Asia</B></font><br>
            </td>
        </tr>


<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/296.htm"><B>misschaos.chaos-studio.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>China (Shanghai)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/313.htm"><B>ns2.rilinfo.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>India (Bangalore)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/274.htm"><B>gsrmum.vsnl.net.in</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>India (Mumbai)</b></font><br>
            </td>
            <td align=center bgcolor="#FFFF00">
                <B>74</B><br>
            </td>
            <td align=center>
                256<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/12.htm"><B>core-mgl.cbn.net.id</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Indonesia (Mangole)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>80</B><br>
            </td>
            <td align=center>
                198<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/317.htm"><B>fe0-0.bbr1.bahar.kimianet.ir</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Iran (Karaj)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/308.htm"><B>gi0-1.thr-001-core-1.ctel.ir</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Iran (Tehran)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/267.htm"><B>router1.iust.ac.ir</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Iran (Tehran)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/309.htm"><B>nat.mindu.co.il</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Israel (Tel Aviv)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/293.htm"><B>cs1mr1.comsourceone.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Japan (Tokyo)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>88</B><br>
            </td>
            <td align=center>
                112<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/311.htm"><B>itr-test.isp.qa</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Qatar (Doha)</b></font><br>
            </td>
            <td align=center bgcolor="#FFFF00">
                <B>72</B><br>
            </td>
            <td align=center>
                278<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/26.htm"><B>gateway.ix.singtel.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Singapore</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/277.htm"><B>tpnoc1-osr-transit.ix.giga.net.tw</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Taiwan</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>85</B><br>
            </td>
            <td align=center>
                148<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr>
            <td colspan=5 bgcolor="#CCCCCC">
                <font size=3>
                <B>Australia</B></font><br>
            </td>
        </tr>


<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/314.htm"><B>gigeuplink.ozservers.net.au</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Australia (Brisbane)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>80</B><br>
            </td>
            <td align=center>
                197<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/302.htm"><B>slinky.arc.net.au</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Australia (Melbourne)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>81</B><br>
            </td>
            <td align=center>
                183<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/298.htm"><B>syd-a-bb1.aarnet.net.au</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Australia (Sydney)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>81</B><br>
            </td>
            <td align=center>
                184<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/316.htm"><B>bdr02.syd01.nsw.vocusconnect.net.au</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Australia (Sydney)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/264.htm"><B>io.peace.co.nz</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>New Zealand (Auckland)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/37.htm"><B>b2.sxb.tsnz.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>New Zealand (Auckland)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>85</B><br>
            </td>
            <td align=center>
                145<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr>
            <td colspan=5 bgcolor="#CCCCCC">
                <font size=3>
                <B>Europe</B></font><br>
            </td>
        </tr>


<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/301.htm"><B>ipsec.eskom.co.za</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Africa (Gauteng)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/307.htm"><B>rt1.mps.bg</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Bulgaria (Sofia)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/292.htm"><B>feth1-0-0.utland1.bone2.olivant.fo</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Faroe Island (Torshavn)</b></font><br>
            </td>
            <td align=center bgcolor="#FFFF00">
                <B>79</B><br>
            </td>
            <td align=center>
                208<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/50.htm"><B>n-eb1.n.de.net.dtag.de</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Germany</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>84</B><br>
            </td>
            <td align=center>
                157<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/234.htm"><B>dns1.playnet.it</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Italy (Florence)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>82</B><br>
            </td>
            <td align=center>
                176<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/305.htm"><B>mail.apra.it</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Italy (Jesi)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/59.htm"><B>mil5-loop0.mil.seabone.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Italy (Milano)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/241.htm"><B>am1-gw1.prioritytelecom.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Netherlands (Amsterdam)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/68.htm"><B>router.nomi.com.pl</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Poland</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/74.htm"><B>rb1-feth2-0.vlc.s2k-net.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Spain</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/76.htm"><B>mlm1-core.swip.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Sweden</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>85</B><br>
            </td>
            <td align=center>
                145<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/306.htm"><B>telenor-gw.bengtdahlgren.se</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Sweden (Gothenburg)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/290.htm"><B>nrkp-cr1.patrikweb.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Sweden (Norrkoping)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>83</B><br>
            </td>
            <td align=center>
                170<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/82.htm"><B>gsr01-tl.blueyonder.co.uk</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>United Kingdom</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>85</B><br>
            </td>
            <td align=center>
                145<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/84.htm"><B>gsr01-cr.blueyonder.co.uk</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>United Kingdom</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>85</B><br>
            </td>
            <td align=center>
                143<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/304.htm"><B>kt1-3ja.bdr.ex.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>United Kingdom (London)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>85</B><br>
            </td>
            <td align=center>
                149<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/64.htm"><B>core1-gig2-0.bletchley.ukcore.bt.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>United Kingdom (Milton Keynes)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr>
            <td colspan=5 bgcolor="#CCCCCC">
                <font size=3>
                <B>North America</B></font><br>
            </td>
        </tr>


<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/286.htm"><B>anhm7204.exo.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>California (Anaheim)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/230.htm"><B>mc-gateway.lansmart.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>California (Fresno)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>97</B><br>
            </td>
            <td align=center>
                22<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/231.htm"><B>dnsauth1.sys.gtei.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>California (Los Angeles)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>99</B><br>
            </td>
            <td align=center>
                9<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/312.htm"><B>rx0ar-technicare.ed.bigpipeinc.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Canada (Edmonton)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>92</B><br>
            </td>
            <td align=center>
                72<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/249.htm"><B>gw02.wlfdle.phub.net.cable.rogers.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Canada (Ontario)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/195.htm"><B>anguhub14.net.ubc.ca</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Canada (Vancouver)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/109.htm"><B>loopback0.gw2.den4.alter.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Colorado (Denver)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>96</B><br>
            </td>
            <td align=center>
                38<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/120.htm"><B>router.firstcls.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Georgia</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/295.htm"><B>atl-datacenter-gw2.capitalinternet.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Georgia (Atlanta)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/100.htm"><B>loopback0.gw9.chi2.alter.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Illinois (Chicago)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>95</B><br>
            </td>
            <td align=center>
                49<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/125.htm"><B>cisco-gnarly.n-connect.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Iowa</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>96</B><br>
            </td>
            <td align=center>
                37<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/318.htm"><B>crystal-cavern.ctcco.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Kansas (Lenexa)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>96</B><br>
            </td>
            <td align=center>
                37<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/134.htm"><B>cisco.syssrc.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Maryland</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>93</B><br>
            </td>
            <td align=center>
                62<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/315.htm"><B>router-in.nemetschek.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Maryland (Columbia)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>92</B><br>
            </td>
            <td align=center>
                75<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/92.htm"><B>pos1-0-0-155m.ar1.bos1.gblx.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Massachusetts (Boston)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>92</B><br>
            </td>
            <td align=center>
                73<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/310.htm"><B>lan-d32-0606-0578.uninet-ide.com.mx</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Mexico (Chihuahua)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/139.htm"><B>rr1.torixt.avantel.net.mx</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Mexico (Coahuila)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>95</B><br>
            </td>
            <td align=center>
                45<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/247.htm"><B>rr2.gdlmha.avantel.net.mx</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Mexico (Guadalajara)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>94</B><br>
            </td>
            <td align=center>
                54<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/137.htm"><B>rr1.reyixt.avantel.net.mx</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Mexico (Tamaulipas)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>95</B><br>
            </td>
            <td align=center>
                42<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/303.htm"><B>revenant.netservicesgroup.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Michigan (Saginaw)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>94</B><br>
            </td>
            <td align=center>
                51<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/232.htm"><B>border0-e0.oc48-ypsi.hdl.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Michigan (Ypsilanti)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/235.htm"><B>wormhole.homeisp.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Missouri (Kansas City)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>95</B><br>
            </td>
            <td align=center>
                42<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/256.htm"><B>pwps-core01.powerpulse.cc</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Nevada (Las Vegas)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>98</B><br>
            </td>
            <td align=center>
                16<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/150.htm"><B>isp.state.nh.us</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>New Hampshire</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/151.htm"><B>sugaree.arorapc.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>New Jersey</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>92</B><br>
            </td>
            <td align=center>
                77<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/154.htm"><B>ac-gw.dandy.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>New Jersey (Atlantic City)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/161.htm"><B>180.atm6-0.gw7.nyc9.alter.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>New York (NYC)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>93</B><br>
            </td>
            <td align=center>
                67<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/239.htm"><B>wookie.core.3z.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Ohio (Cincinnati)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/172.htm"><B>sl-bb21-pen-15-0.sprintlink.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Pennsylvania (Philadelphia)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/190.htm"><B>gw-inet.ktc.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Texas</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/238.htm"><B>core-router.centramedia.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Texas (Pampa)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/270.htm"><B>www.xmission.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Utah (Salt Lake City)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>96</B><br>
            </td>
            <td align=center>
                39<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/263.htm"><B>er01.asbn.eli.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Virginia (Ashburn)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/186.htm"><B>core1-sttl.sitespecific.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Washington (Seattle)</b></font><br>
            </td>
            <td align=center bgcolor="#FF6633">
                <B>0</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                100<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/212.htm"><B>gate.netwrx1.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Wisconsin</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/211.htm"><B>core-1601-bmia-elkwpop-1-3.mia.net</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Wisconsin (Elkhorn)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/319.htm"><B>5dl-dst-rt2.5ninesdata.com</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Wisconsin (Madison)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr>
            <td colspan=5 bgcolor="#CCCCCC">
                <font size=3>
                <B>South America</B></font><br>
            </td>
        </tr>


<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/213.htm"><B>rcorelma1-rcoreats1.impsat.net.ar</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Argentina</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>100</B><br>
            </td>
            <td align=center>
                0<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/273.htm"><B>router-ut1.uniweb.net.co</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Colombia (Valle del Cauca)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>86</B><br>
            </td>
            <td align=center>
                132<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

<tr bgcolor="#FFFFFF">
            <td>
                <font size=1>
                <A href="/history/284.htm"><B>div-core-rtr1.americatelnet.com.pe</B></a></font><br>
            </td>
            <td align=center>
                <font size=1><b>Peru (Lima)</b></font><br>
            </td>
            <td align=center bgcolor="#00FF00">
                <B>88</B><br>
            </td>
            <td align=center>
                119<br>
            </td>
            <td align=center>
                0<br>
            </td>
        </tr>

</table>
    </td>
</tr>
</table>
<br>

</td>
    <td width=10>
        &nbsp;
    </td>


    <td valign=top align=center width=135>

        <img src="/look/top.gif" width=135 height=10><br>

        <table cellpadding=2 width=135 cellspacing=0 border=0>
        <tr>
            <td valign=top align=center bgcolor="#99CCFF">
                <FONT SIZE=1>


                <A HREF="http://www.analogx.com/" style="color:3333FF">
                <img alt="AnalogX" src="/look/analogxlogo.gif" width="101" height="62" border="0"><BR>
                AnalogX<BR>
                </a>
                </FONT>
            </TD>
        </TR>
        </TABLE>

        <img src="/look/bottom.gif" width=135 height=10><br><br>

        <img src="/look/top.gif" width=135 height=10><br>
        <table cellpadding=2 width=135 cellspacing=0 border=0>
        <tr>
            <td valign=top align=left bgcolor="#99CCFF">
                <table cellpadding=2 cellspacing=0 border=0>
                <tr>
                    <td valign=top align=center bgcolor="#99CCFF">

<script type="text/javascript"><!--
google_ad_client = "pub-5623084330058329";
//ITR Tower
google_ad_slot = "3070468962";
google_ad_width = 120;
google_ad_height = 600;
//--></script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>

                    </td>
                </tr>
                </table>
            </TD>
        </TR>
        </TABLE>
        <img src="/look/bottom.gif" width=135 height=10><br><br>

        <img src="/look/top.gif" width=135 height=10><br>
        <table cellpadding=2 width=135 cellspacing=0 border=0>
        <tr>
            <td valign=top align=left bgcolor="#99CCFF">
                <table cellpadding=2 cellspacing=0 border=0>
                <tr>
                    <td valign=top align=left bgcolor="#99CCFF">
                        <FONT SIZE=1>
                        The Internet Traffic Report (ITR) wants to continue to provide useful information about
                        networks from around the world. We want to make this information as accurate as possible!<BR>
                        <A HREF="/faq.htm#help" style="color:3333FF">More Information.</A><BR><BR>

                        The free ITR Client for Windows is now available for download, and allows you to monitor ITR
                        in realtime, test your connection when problems occur and more!<BR><A HREF="http://www.analogx.com/files/itrci.exe" style="color:3333FF">Click here</A> to
                        download.<BR>
                        <BR>

                        <B>Want to add a live statistics display to your website?</b><BR><A HREF="/addlink.htm" style="color:3333FF">Click here</A> to
                        select your graphic.<BR>

                        <BR>
                        Got questions?  We've got answers!<BR>
                        Check out the <A HREF="/faq.htm" style="color:3333FF">ITR FAQ</A><BR>
                        </FONT>
                    </td>
                </tr>
                </table>
            </TD>
        </TR>
        </TABLE>

        <img src="/look/bottom.gif" width=135 height=10><br>
        <BR>

    </td>
</tr>
<tr>
    <td colspan=3>
        <table cellpadding=0 cellspacing=0 border=0 width="100%">
<tr>
    <td bgcolor="#000000"><img src="/look/dot.gif" width=1 height=2></td>
</tr>
</table>
<CENTER>
<script type="text/javascript"><!--
google_ad_client = "pub-5623084330058329";
//ITR Links
google_ad_slot = "1448638540";
google_ad_width = 468;
google_ad_height = 15;
//--></script>
<script type="text/javascript"
src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
        &nbsp;<BR>
        &nbsp;<BR>
</CENTER>
    </td>
</tr>
</table>

</center>
</font>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
var pageTracker = _gat._getTracker("UA-3527135-1");
pageTracker._initData();
pageTracker._trackPageview();
</script>
</BODY>
</HTML>



<!-- This site was generated using AnalogX MacroPage http://www.macropage.com/ -->
"""
