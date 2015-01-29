
# Disabling Django tests because they require an actual database implementation :(
# from django.test import TestCase

from unittest import TestCase

import github.r351574nc3.internet_traffic_report.backends.http

# Create your tests here.
class TrafficReportApiTests(TestCase):
    """
    Class of test methods for testing the Traffic Report API
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def test_lookup_most_recent_results(self):
        """Tests the method to retrieve the most recent internet traffic test results"""
        pass
    
