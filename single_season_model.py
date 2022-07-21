class SingleSeasonModel:
    def __init__(self, single_season):

        s = ''.join(map(chr, f1_data_req.content))
        dict = json.loads(s)


        self.status = stat