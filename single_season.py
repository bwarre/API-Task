from single_season_model import SingleSeasonModel
import requests
import json

class SingleSeason():

    def __init__(self, season):

        self.url = "http://ergast.com/api/f1/"+season+"/drivers.json"
        self.request = requests.get(self.url)

        s = ''.join(map(chr, self.request.content))  #converting from a method into a string
        dict = json.loads(s)    #dict should be the dictionary

        self.resp = dict   # converting from a string into a dictionary.

    def response_data(self):
        return SingleSeasonModel(self.resp)


