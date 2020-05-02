#!/usr/bin/env python3


import requests
from pygeocoder import Geocoder
def geocod(address):
    parameters={'address':address,'sensor':'false'}
    base='http://maps.googleapis.com/maps/api/geocode/json'
    response=requests.get(base,params=parameters)
    result=response.json()
    print(result['results'][0]['geometry']['location'])


if __name__=='__main__':
        address1='Millbank Tower, 21 – 24 Millbank, Westminster, London SW1P 4QP, United Kingdom'
        geocod(address1)