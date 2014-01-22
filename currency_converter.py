__author__ = 'Ayoub J.I'
import urllib2
from bs4 import BeautifulSoup
import sys

currency_list = {'USD': 'American Dollar',
                 'EUR': 'European Euro',
                 'AED': 'Emarati Dirham',
                 }

try:
    # read params
    args = sys.argv

    if len(args) < 2:
        raise ValueError

    amount, currency_from = args[1], args[2]

    for currency_to in currency_list.keys():
        if currency_from != currency_to:
            url = "http://www.x-rates.com/calculator/?from=%s&to=%s&amount=%s" % (str(currency_from), str(currency_to), str(amount))
            url_object = urllib2.urlopen(url)
            url_content = url_object.read()
            soup = BeautifulSoup(url_content)
            currency_div = soup.find("span", {"class": "ccOutputRslt"})
            print amount + " " + currency_from + " [" + currency_list[currency_from] + "] " + " ==> " +  currency_div.text + " [" + currency_list[currency_to] + "] "

except ValueError:
    print "Error usage : params => 14 USD|EUR|AED"
