import datetime
import time
import tweepy
import csv
from tweepy import OAuthHandler
import os


C_KEY ='3D3GveliAIWrbGgTg5IZ5NqHo'
C_SECRET ='YvCpDOyp9Bk5av2t9eM9HO08IdP0lZi8NqfGauEXSNPo9bCHls'
A_TOKEN ='1104333276997509122-FivTPlAGoXlxDJIPfi9MBJdYPyAXPX'
A_TOKEN_SECRET = 'OHfHwA98MIXd0E7wPwVHAWcX6zy66TL6nASODH8HLU6qO'

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

api = tweepy.API(auth)

#Lọc trùng lặp
def duplicate_remove(filename):
    f = open(filename,"r")
    string = f.readline().split()
    string = list(set(string))
    f.close()
    os.remove(filename)
    f = open(filename,"a")
    for user in string:
        f.write(user+ " ")
    f.close()

#Lấy danh sách tweet id của MU
source_file = "C:/Users/admin/source/repos/crawl_twittter/data/"

f = open(source_file + "tweet.txt","r")
listTweets = f.readline().split()
f.close()


def user_from_retweet(list):
    i = 1
    users = []
    backoff_counter = 1

        
    for tweet in list:
        if (backoff_counter > 20):
            backoff_counter = 15
        while True:
            try: 
                for item in tweepy.Cursor(api.retweeters, id = tweet).items(20):
                    print("Id  " + str(i) + "\n")
                    file_name = source_file + "level1.txt"
                    f = open(file_name,"a")
                    f.write(str(item) + " ")
                    f.close()
                    i = i + 1
                break
            except tweepy.TweepError as e:
                print (e.reason)
                time.sleep(60*backoff_counter)
                backoff_counter = backoff_counter + 1

user_from_retweet(listTweets)
duplicate_remove(source_file+ "level1.txt")


























      



        
        









 










