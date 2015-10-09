# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 17:09:25 2015

@author: User
"""

import requests

response = requests.get('http://standardscoring.com/')

# Response
print (response.status_code) # Response Code  
print (response.headers) # Response Headers  
print (response.content) # Response Body Content


# Request
print (response.request.headers) # Headers you sent with the request  


#-----------------------------------------------------------------------------
#Parsing the responses body
import requests  
from lxml import html

response = requests.get('http://standardscoring.com/')

# Parse the body into a tree
parsed_body = html.fromstring(response.text)

# Perform xpaths on the tree
print( parsed_body.xpath('//title/text()') )# Get page title  
print( parsed_body.xpath('//a/@href') )# Get href attribute of all links  


#-----------------------------------------------------------------------------
#Download all images on a page
import requests  
from lxml import html  
import sys  
#import urlparse

response = requests.get('http://standardscoring.com/')  
parsed_body = html.fromstring(response.text)

# Grab links to all images
images = parsed_body.xpath('//img/@src')  
if not images:  
    sys.exit("Found No Images")

# Convert any relative urls to absolute urls
images = [('http://standardscoring.com/' + url) for url in images]  
print ('Found %s images' % len(images))

# Only download first 10
for url in images[0:2]:  
    r = requests.get(url)
    f = open('d:/downloaded_images/%s' % url.split('/')[-1], 'w')
    f.write(r.content)
    f.close()






