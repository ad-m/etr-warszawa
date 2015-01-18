#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import sys
import requests
from BeautifulSoup import BeautifulSoup
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
data = {'wydzial_orzeczniczy':'---',
'symbol':'',
'sygnatura':'',
'sortowanie':'3',
'sala_rozpraw':'---',
'opis':'',
'guzik':'Filtruj / Sortuj',
'data_posiedzenia':'',
'act':'szukaj',}
soup = BeautifulSoup(requests.post('http://www.warszawa.wsa.gov.pl/183/elektroniczny-terminarz-rozpraw.html',data=data).text)
print soup.find('table').prettify()
