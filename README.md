This is the example for the youtube video of how to upload your discord bot to heroku to run your bot 24/7.


### Add your modules that are not pre-installed along with Python inside `requirements.txt` file
discord should be added there if you're hosing your python bot or your discord bot will not work


Video link: https://www.youtube.com/watch?v=Wal2taXZEAY&t=1s

#### Inside the Procfile should be:
`worker: python filename.py`
 
#### Inside current Procfile in repo:
`worker: python bot.py`
  
 #### The BOT_TOKEN should be the name of the config var name in heroku
 <img src="images/token.png" width="600">
