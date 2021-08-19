import requests 
from dotenv import load_dotenv                                                                                                                                
import os
import pprint
from requests.auth import HTTPBasicAuth
import urllib
# Getting Token from .env file                                                                                                                                
load_dotenv()                                                                                                                                                 
api_key = os.getenv('geocoding_api_key')

print(type(api_key))

# Geocoding API
# https://positionstack.com/

# resonse = requests.get()
location = "Rishikesh, Uttrakhand, India"
parameters = urllib.parse.urlencode({
    'access_key':api_key,
    'query':location
})
response = requests.get("http://api.positionstack.com/vi/forward?")

print(response.json())