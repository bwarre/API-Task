import SingleSeasonModel from single_season_model

class SingleSeason():

    def __init__(self, season):

        self.url = "http://ergast.com/api/f1/"+season+"/drivers.json"
        self.request = request.get(self.url)

        s = ''.join(map(chr, self.url.content))  #converting from a method into a string

        self.resp =json.loads(s)   # converting from a string into a dictionary.

    def response_data(self):
        return SingleSeasonModel(self.resp)


