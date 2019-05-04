import datetime
import time
import tweepy
import csv
from tweepy import OAuthHandler
import os


C_KEY ='LFy7Gqiq5nDJIsUjoDB1nDiCU'
C_SECRET ='UxDjemiLPdU4DKKvB0FbKqVnFWqgQlIfbyuXS4cJU8iOWVgoHi'
A_TOKEN ='1104333276997509122-nYSPGAFMSJX3FgqLnyQjQodSc5q03a'
A_TOKEN_SECRET = 'MumbW51zSzwK04eKk4A3j0Zgaa5RQOhtA6zBHwM4DzD3V'

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)

api = tweepy.API(auth)

source_file = "C:/Users/admin/source/repos/crawl_twittter/data/"

f = open(source_file + "level1.txt","r")
listUser = f.readline().split()
f.close()

#Kiểm tra xem 1 tweet có phải là retweet hay không
def is_retweet(tweet):
    if(tweet.retweet_count):
       return 1
    else:
       return 0
#Loại bỏ trùng lặp
def duplicate_remove(filename):
    f = open(filename,"r")
    string = f.readline().split()
   
    string = list(set(string))
    #print(len(string))
    f.close()
    os.remove(filename)
    f = open(filename,"a")
    for user in string:
        f.write(user+ " ")
    f.close()
def duplicate_remove_line(filename):
    f = open(filename,"r")
    string = f.readlines()
   
    string = list(set(string))
    f.close()
    os.remove(filename)
    f = open(filename,"a")
    for user in string:
        f.write(user)
    f.close()

#Tạo đồ thị cho level1 
def make_graph(list):
    f = open(source_file+"graph.txt", "a")
    for user in list:
        
        f.write(user + " " + "558797310\n")
    f.close()

#Lấy tác giả của các retweet trong listUser
def user_from_retweet(list):
    i = 1
    backoff_counter = 1
    
    for user in list:
        if (backoff_counter > 20):
            backoff_counter = 15
        while True:
            try: 
                for item in tweepy.Cursor(api.user_timeline, id = user).items(15):
                    #Neu la retweet
                    
                    if(is_retweet(item) and hasattr(item, 'retweeted_status')):
                        print("Tweet " + str(i) + "\n")
                       
                        #ghi vao graph
                        f = open(source_file+"graph.txt", "a")
                        f.write(user +" "+ item.retweeted_status.user.id_str + "\n")
                        f.close()
                        #ghi vao level 2
                        f = open(source_file+"level2.txt", "a")
                        f.write(item.retweeted_status.user.id_str + " ")
                        f.close()
                        #luu text tweet
                        with open(source_file+"text_tweet.csv", "a",encoding='utf-8') as f:
                            writer = csv.writer(f)
                            writer.writerows([[str(i), item.text]])
                        pass
                        i = i + 1
                break
            except tweepy.TweepError as e:
                if (e.api_code == 429):
                    print (e.reason)
                    time.sleep(60*backoff_counter)
                    backoff_counter = backoff_counter + 1
                    continue
                else:
                    print (e.reason)
                    break

make_graph(listUser)
print("Make graph level 1 done\n")
user_from_retweet(listUser)
duplicate_remove(source_file+ "level2.txt")
duplicate_remove_line(source_file+"graph.txt")





























      



        
        









 










