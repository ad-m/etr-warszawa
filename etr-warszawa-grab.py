#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys
import requests
from BeautifulSoup import BeautifulSoup
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
soup = BeautifulSoup(requests.post('http://www.warszawa.wsa.gov.pl/183/elektroniczny-terminarz-rozpraw.html',data={'data_posiedzenia':''}).text)
print soup.find('table').prettify()
