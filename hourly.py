#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

"""
API Access to https://www.wunderground.com/weather/api

@author: victor.ferrer.2012@gmail.com
"""

import sys
import urllib2
from bs4 import BeautifulSoup

api_key = None
location = None

class WheatherHourly(object):
    """Wheather Client."""

    url_base = "http://api.wunderground.com/api/"
    url_service = {
                   "hourly": "/hourly/q/CA/"
                   }

    def __init__(self, api_key):
        """Init Method."""
        super(WheatherHourly, self).__init__()
        self.api_key = api_key

    def hourly(self, location):
        """Read and dowload the web."""
        url = WheatherHourly.url_base + self.api_key + \
            WheatherHourly.url_service["hourly"] + \
            location + ".json"
        return url


class WheatherAlmanac(object):
    """Docstring dor WheatherClient."""

    url_base = "http://api.wunderground.com/api/"
    url_service = {
                   "almanac": "/almanac/q/CA/"
                  }

    def __init__(self, api_key):
        """Init Class."""
        super(WheatherAlmanac, self).__init__()
        self.api_key = api_key

    def almanac(self, location):
        """Almanac dosctring."""
        # baixar-se web
        url = WheatherAlmanac.url_base + self.api_key + \
            WheatherAlmanac.url_service["almanac"] + \
            location + ".xml"
        return url


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "You have to introduce your API wunderground key"
            exit(-1)
wa = WheatherAlmanac(api_key)
wh = WheatherHourly(api_key)
resultatwa = wa.almanac("Lleida")
resultatwh = wh.hourly("Lleida")
# print resultat
