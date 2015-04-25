import json
import urllib2
from pprint import pprint

#key IDs: Aaron, Stux, Tarra
keys = ["a94d9929-7f34-49f1-a95b-90f7c784150c", "52b2cdfd-1e3e-465e-9ab5-da395ba8a694", "bcc94a4e-d3ca-4110-bfea-d0574393462e"]

get_request = urllib2.urlopen("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/noxToken?api_key=a94d9929-7f34-49f1-a95b-90f7c784150c").read()
pprint(json.loads(get_request))


json_object = json.loads(get_request)
pprint(json_object)