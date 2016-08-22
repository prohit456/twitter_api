#from TwitterAPI import TwitterAPI
#api = TwitterAPI("8EX7AbBLOyZhutxTpUcvkt9L3", "djLkuMbMlLGzPL7gR7ea0M446N4uyYrHNVSbU0dLGFlFTjsVo6", "100119498-Nux7knuCBBkBt82Pur8xc3pemO3z0U09T3sm6L6O", "J6VnMUjUhqgUUgSsQNUQ5TYaXitOuwELfWO0MEhYR2lFv");
#stat = api.request('statuses/update', {'status':'Hello World'});
#print (stat.status_code);

import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener;

auth = OAuthHandler ("rohit", "rohit");
auth.set_access_token("rohit", "rohit");

class MyStreamListener (StreamListener):
  
  def on_status(self, status):
    print status.text;
def paginate(iterable, page_size):
  while True:
    i1, i2 = itertools.tee(iterable)
    iterable, page = (itertools.islice(i1, page_size, None),
    list(itertools.islice(i2, page_size)))
    if len(page) == 0:
      break
    yield page

api = tweepy.API(auth);
streaml = MyStreamListener();
stream = tweepy.Stream(auth = auth, listener=streaml);
for stat in api.user_timeline(id='Pvsindhu1'):
  print stat.text.encode('utf-8').strip();
#for tweet_item in tweepy.Cursor(api.user_timeline(id='Pvsindhu1', allowed_param='page', pagination_mode = 'page'), count=100, include_entities=True).pages():
#    print tweet_item;
  

#stream.filter(track=['sindhu', 'FlipkartAssured']);
#for status in tweepy.Cursor(api.home_timeline).items(10):
#  print (status._json);
