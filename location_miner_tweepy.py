# -*- coding: UTF-8 -*-
__author__ = 'Michael'

'''
making a geolocation based twitter bot,

current bounding box is set to DC

'''
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv
import tweepy
import sys
from time import sleep

#import codecs
#sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
#print u"Stöcker"                # works
#print "Stöcker".decode("utf-8") # works
#print "Stöcker"                 # fails

#Variables that contains the user credentials to access Twitter API
access_token = "XXXX"
access_token_secret = "XXXXXX"
consumer_key = "XXXXXXXXXXX"
consumer_secret = "XXXXXXXXXX"

#currently set to DC
bounding_box = [-77.119759,38.7916449,-76.909393,38.995548]

#This is a basic listener that just prints received tweets to stdout.

class CustomStreamListener(tweepy.StreamListener):



    def on_status(self, status):


        #print status.author.screen_name, status.created_at, status.text
        if (status.coordinates is not None):
            print status.author.screen_name, status.created_at, status.text, status.geo
            
            #have it appending to a file... which exists within my directory, may have to write it
            # you could definatly just have it write if the file doesnt exist, but this is fine for now
            with open('test_washington_Dc.csv', 'ab') as f:
                writer = csv.writer(f)
                
                #could do this better, but is fine for now
                screen_name = status.author.screen_name.encode("utf-8")
                s_id = status.id_str#.encode("utf-8")
                geo = status.geo#.encode("utf-8")
                txt =  status.text.encode("utf-8")
                source =status.source.encode("utf-8")
                cord = status.coordinates
                time = status.created_at
                data = status
                writer.writerow([screen_name,s_id, time,txt,source,geo,cord,data])

    # inserted 5min sleep timers for time outs and errors, will hopefully avoid bot being throttled
    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        sleep(5*60)
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        sleep(5*60)
        return True # Don't kill the stream


if __name__ == '__main__':


    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = CustomStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    # can do a filter on terms, but it wont filter on both... but you could probably have it filter with
    # conditional statements
    #stream.filter(track=['python', 'javascript', 'ruby'])
    # just filter down to a geographic location
    stream.filter(locations=bounding_box)





















