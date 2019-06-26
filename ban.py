import praw

information = []
bannedsub = []
limit = ""
postlimit = ""
commentlimit = ""

#Reading info.txt
read = open("info.txt", "r")
line = read.readlines()
for info in line:
    information.append(info)

read2 = open("bannedsub.txt", "r")
line2 = read2.readlines()
for info in line2:
    bannedsub.append(info)

read3 = open("settings.txt", "r")
line3 = read3.readlines()
count = 0
for info in line3:
    if count == 0:
        limit = info.replace('objects_scanned=', '')
    elif count == 1:
        postlimit = info.replace('post_limit=', '')
    elif count == 2:
        commentlimit = info.replace('comment_limit=', '')
    count += 1

print(limit + " " + postlimit + " " + commentlimit)

#Storing info into strings
id = information[2].replace('\n', '')
secret = information[3].replace('\n', '')
username = information[0].replace('\n', '')
password = information[1].replace('\n', '')
#Logging in

reddit = praw.Reddit(client_id=id,
                     client_secret=secret,
                     password=password,
                     user_agent='modules bot',
                     username=username)

subreddit = reddit.subreddit('upautomodevader')

if not subreddit.user_is_moderator:
    print("You are not a moderator of this subreddit. Please login as a moderator")

for submission in subreddit.stream.submissions():
    author = submission.author
    bansub = 0
    bancomment = 0
    count = 0

    for post in author.submissions.new(limit=int(limit)):
        sub = str(post.subreddit).lower()
        if bannedsub.count(sub) == 1:
            bansub += 1

    if bansub >= int(postlimit):
        subreddit.banned.add(str(author), ban_reason='Participation in unauthorized subreddits')
        print(str(author) + " banned for too many illegal posts")

    for comment in author.comments.new(limit=int(limit)):
        comm = str(comment.subreddit).lower()
        if bannedsub.count(comm) == 1:
            bancomment += 1

    if bancomment >= int(commentlimit):
        subreddit.banned.add(str(author), ban_reason='Participation in unauthorized subreddits')
        print(str(author) + " banned for too many illegal comments")
