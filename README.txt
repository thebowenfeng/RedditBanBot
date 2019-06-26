Thank you for downloading. Original author is u/Fengax.

DO THIS BEFORE YOU START:
#######################################################################################################

Go to info.txt, enter your info in the FOLLOWING ORDER: Username, Password, Client ID, Client Secret. Each information should be on a new line. DO NOT ADD EXTRA NEW LINES AT THE END. Make sure the account you entered is a moderator account with the power to ban people.

Go to bannedsub.txt, enter any subreddit that you think are "illegal" or shoud be monitored. Each subreddit MUST ONLY BE IN LOWER CASE LETTERS. Add a new line for each subreddit, do not add extra lines at the end.

Go to settings.txt, enter the appropriate setting. You must enter a number WITHOUT SPACE after each equal sign. object_scanned means how many comments/posts you would like to scan in that person's post history. comment_limit and post_limit means the minimum amount of post/comment a redditor must post in any illegal subredits, to be banned.

######################################################################
Step 1:
Go to cmd, navigate to this folder, and run "pip install -r requirements.txt"

Step 2:
In the same folder, run "python ban.py

If anyone is banned, the program should print out in the console. 