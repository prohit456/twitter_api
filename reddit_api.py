import praw

r_handle = praw.Reddit(user_agent = 'search example');
posts = r_handle.search("alex", subreddit=None, sort=None, syntax=None, limit=None);
print posts.__getattribute__;
