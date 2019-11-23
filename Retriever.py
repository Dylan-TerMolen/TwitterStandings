import requests

class Retriever:
    def __init__(self,key):
        self.key = key
        self.table = None
        self.validIds = [
            (2019,"Serie A"),
            (2017,"Primeira Liga"),
            (2016,"EFL Championship"),
            (2015,"France Ligue 1"),
            (2014,"La Liga"),
            (2013,"Campeonato Brasileiro Série A"),
            (2002,"Bundesliga"),
        ]
    
    def getStandings(self,id=2019):
        headers = { 'X-Auth-Token': self.key }
        link = "http://api.football-data.org/v2/competitions/{}/standings".format(id)
        data = requests.get(link,headers=headers).json()

        try:
            self.table = data["standings"][0]["table"]
        except KeyError as e:
            print("Invalid id","\n",e)
        