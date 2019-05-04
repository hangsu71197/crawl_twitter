import datetime
import time
import tweepy
from tweepy import OAuthHandler

C_KEY ='3D3GveliAIWrbGgTg5IZ5NqHo'
C_SECRET ='YvCpDOyp9Bk5av2t9eM9HO08IdP0lZi8NqfGauEXSNPo9bCHls'
A_TOKEN ='1104333276997509122-FivTPlAGoXlxDJIPfi9MBJdYPyAXPX'
A_TOKEN_SECRET = 'OHfHwA98MIXd0E7wPwVHAWcX6zy66TL6nASODH8HLU6qO'

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

api = tweepy.API(auth)

source_file = "C:/Users/admin/source/repos/crawl_twittter/data/"

def tweet_from_user(userName, startDate, endDate):
    i = 1
    for tweet in tweepy.Cursor(api.user_timeline, id = userName).items():
        if tweet.created_at < endDate and tweet.created_at > startDate:
            print("Tweet " + str(i) + "\n")
            file_name = source_file + "tweet.txt"
            f = open(file_name,"a")
            f.write(str(tweet.id) + " ")
            f.close()
            i = i + 1

screen_name = "558797310"
startDate = datetime.datetime(2019, 4, 1, 0, 0, 0)
endDate = datetime.datetime(2019, 5, 2,0 , 0, 0)
tweet_from_user(screen_name,startDate,endDate)
























      



        
        









 









