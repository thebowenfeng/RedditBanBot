# RedditBanBot
A ban bot for moderators, to ban users who participate in particular subreddits.
# Pre-requisites
* Python 3.6
# How to setup
1. Install the requirements by `pip install -r requirements.txt`
2. Go to "bannedsub.txt". Add any subreddit that you don't want users to participate in (if a user partcipate in this subreddit then you ban them). **One line must ONLY contain one subreddit's name**. **Subreddit name must be in lower case letters**. 
3. Go to "settings.txt". In there, you will find three settings: objects_scanned, post_limit and comment_limit. 
* objects_scanned is how many posts/comments you want to scan in each person's post history (i.e how far back you want to go). The bot will scan from the newest post/comments.
* post_limit is how many violations a user can have before he/she is banned. A violation is when a user post(or comment) in a banned subreddit.
* comment_limit is similar to post_limit but for comments instead. 

  Enter only an integer after each "=" sign. **Do not add any extra space at the end, or in front, of the integer. Do not add a new line.**
  
4. [Create a bot](https://www.reddit.com/prefs/apps/) and add your bot info to "info.txt". Simply follow the prompts. **Do not add spaces and a new line at the end**. If you don't know how to create a bot just Google it.
5. Run `python ban.py`
