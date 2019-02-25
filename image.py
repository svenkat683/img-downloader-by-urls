import json
from pprint import pprint
import urllib
with open('urls.json') as f:
    data = json.load(f)

for url in range(0,len(data["photoUrls"])):
  pprint(data["photoUrls"][url])
  urllib.urlretrieve(data["photoUrls"][url], "photos/" + str(url) + ".jpg")
  
