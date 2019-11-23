from Tweeter import Tweeter
from Retriever import Retriever
from datetime import date

# API Key for the football-data.org API 
api_key = "1f77263fcb0f4c94bd8aa7dbdee94b7c"

# Twitter developer credentials for use of Twitter API 
consumer_key = "wq9wxUWoDqnunVDIL0abJTrX0"
consumer_secret = "ZuQmGvIKrr68bStxQPUiiVPGNzTmSpRsyVMvUYzlB28EpQJK0j"
access_token = "1197269050574819328-GQot0H364WnPWAcdOaXKeod5tHuPwM"
access_token_secret = "VetmFdTbDQTHGdGT8ZwZ3KmWnJ1cGRgEXiK0TDyGZIGwY"

if __name__ == "__main__":
    myTweeter = Tweeter(consumer_key,consumer_secret,access_token,access_token_secret)
    myTweeter.authenticate()

    today = date.today()
    d2 = today.strftime("%B %d, %Y")

    myRetriever = Retriever(api_key)
    for id,league in myRetriever.validIds:
        myRetriever.getStandings(id)
        if myRetriever.table:
            standings = [row["team"]["name"] + " "  + str(row["points"])for index,row in enumerate(myRetriever.table) if index < 11]
            tweet = league + " on " + d2 + "\n" + "\n".join(standings)
            myTweeter.tweet(tweet)