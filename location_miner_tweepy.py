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
access_token = "836555563-c7sobiPA90KCs79QC9mMMPb7PUHJAGM9PvUvJt2o"
access_token_secret = "ZOME6MRuQtHyDB1Gsoa2rjX4LfYwXrbDvkuU3eNy4Dq6v"
consumer_key = "dK71YWjKQbZyOPdePbgNGDNxT"
consumer_secret = "DpkM7f15s3sHfZD6SL9n5gf0zAEoSO8anVIsDmcwLGa92iPQSE"


#This is a basic listener that just prints received tweets to stdout.

class CustomStreamListener(tweepy.StreamListener):


    #def on_data(self, data):
    #    print data
    #    return True



    def on_status(self, status):


        #print status.author.screen_name, status.created_at, status.text
        if (status.coordinates is not None):
            print status.author.screen_name, status.created_at, status.text, status.geo

            with open('test_washington_Dc.csv', 'ab') as f:
                #f.write( INSERT THINGS MAYBE
                writer = csv.writer(f)

                screen_name = status.author.screen_name.encode("utf-8")
                s_id = status.id_str#.encode("utf-8")
                geo = status.geo#.encode("utf-8")
                txt =  status.text.encode("utf-8")
                source =status.source.encode("utf-8")
                cord = status.coordinates
                time = status .created_at
                data = status
                writer.writerow([screen_name,s_id, time,txt,source,geo,cord,data])


    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        sleep(5*60)
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        sleep(5*60)
        return True # Don't kill the stream


if __name__ == '__main__':


    #with open('presidential_debate_10_7_17.csv', 'wb') as f:
    #    writer = csv.writer(f)
            #This handles Twitter authetification and the connection to Twitter Streaming API
    l = CustomStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    #stream.filter(track=['python', 'javascript', 'ruby'])
    stream.filter(locations=[-77.119759,38.7916449,-76.909393,38.995548])





















