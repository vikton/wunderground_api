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
location = ""
number = None


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
            location + ".xml"

        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        soup = BeautifulSoup(html, 'lxml')
        res = soup.find_all("forecast")
        i = 0
        for elements in res:
            if int(i) >= int(number):
                break
            pretty = elements.find("pretty")
            temp1 = elements.find("temp")
            temp = temp1.find("metric")
            condition = elements.find("condition")
            feelslike1 = elements.find("feelslike")
            feelslike = feelslike1.find("metric")
            snow1 = elements.find("snow")
            snow = snow1.find("metric")
            humidity = elements.find("humidity")
            print "---->Prediction the " + pretty.text + ":"
            print "The temperature will be around " + temp.text + " C, with a feelike of " + feelslike.text + " C. For this reason the condition of the sky will be " + condition.text + "."
            print "The humidity will not exceed " + humidity.text + " and the probability of snowing at " + snow.text + "."
            print "--------------------------"
            i = i + 1


if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "You have to introduce your API wunderground key"
            exit(-1)


print("Introduce the number of hours from now you would like to consult:")
number = input()
print "---You asked for " + str(number) + " hourly weather in Lleida---"
wh = WheatherHourly(api_key)
resultatwh = wh.hourly("Lleida")
