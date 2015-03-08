import praw
r = praw.Reddit(user_agent = 'reddit bo test')

sub = ''
sub2 = ''

links = []

def xpost(sub):
    subreddit = r.get_subreddit(sub)
    for submission in subreddit.get_hot(limit = 5):
        print("Getting url..")
        if "i.imgur.com/" not in submission.url:
            continue
        if "i.imgur.com/" in submission.url and links:
            continue
        if "i.imgur.com" in submission.url and not links:
            print ("found url...")
            pic = submission.url()
            links.append(pic)

xpost('learnpython')