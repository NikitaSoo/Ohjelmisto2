import json
import requests

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana
vastaus = requests.get(pyynto).json()

#print(json.dumps(vastaus, indent=2))

for a in vastaus:
    print(a["show"]["name"])