# YoutubeWrapped

Since YouTube rewind is long dead and a year recap or "YouTube Wrapped" is not available I've decided to create my own. 
Because I think others are also interested in this I'm sharing my code here, so anyone can create their own 2021 YouTube Rewind!

# How To

First you'll have to install Python on your computer, then download the file youtube_wrapped.py from this repository and put it in a folder of your choosing. 
That's it you're all set, all you have to do now is acquire your YouTube watch history and liked videos data via Google Takeout. Follow this tutorial to do so:

1. Go to https://takeout.google.com and makee sure you're loged in with the gmail account on which you usually watch YouTube
2. Select only YouTube and YouTube Music (easiest way is to click deselect all and then select just the YouTube and Youtube Music)
3. Change the file format of the history file (click on "Multiple formats" button -> from the dropdown menu next to history select JSON instead of HTML)
4. Make sure you're downloading just the watch history and liked videos (click on "All YouTue data included" button -> select wanted data)
5. Click on "Next step" button
6. Finally click on "Create export" button and you should get a download link with all the needed data to your email.

Once you've completed all the above steps and have all the necessary files put them all in the same folder (youtube_wrapped.py, watch_history.json and liked_videos.csv). 
If you're watch_history.json and liked_videos.csv files have a different name, make sure to change them to match the ones just described. All that is left is to run the youtube_wrapped.py and wait for the result.
