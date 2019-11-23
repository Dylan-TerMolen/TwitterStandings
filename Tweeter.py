import tweepy 

class Tweeter:
    def __init__(self,c_key:str ,c_secret:str, a_token:str, a_token_secret:str):
        self.consumer_key = c_key
        self.consumer_secret = c_secret
        self.access_token = a_token
        self.access_token_secret = a_token_secret
    
    def __str__(self):
        return "Tweeter signed into user: " + self.API.me()._json["name"]

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token,self.access_token_secret)
        try:
            tweepy.API(auth).verify_credentials()
            self.API = tweepy.API(auth)
            print("Authentication succeeded")
            print(self)
        except tweepy.TweepError:
            print("Authentication failed, check credentials or network connection")

    
    def tweet(self,tweet:str):
        try:
            return self.API.update_status(tweet)
        except tweepy.TweepError as e:
            print(e)






