import os
import sys
import os
import urllib2
import json

f = open("abc.txt", 'w')

try:
    _substr = raw_input()
except:
    _substr = None

def getMovieTitles(substr):
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title=%s&page=%s" % (substr, str(1))
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()

res = getMovieTitles(_substr)
for res_cur in res:
    f.write(str(res_cur) + "\n")

f.close()