from Tweeter import Tweeter
from Retriever import Retriever
from datetime import date

# API Key for the football-data.org API 
api_key = "Use your credentials"

# Twitter developer credentials for use of Twitter API 
consumer_key = "Use your credentials"
consumer_secret = "Use your credentials"
access_token = "Use your credentials"
access_token_secret = "Use your credentials"

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
