import requests
import json
from datetime import datetime
import csv
import pickle

#Opening file with watch history data - needs to be a JSON, change file name to your history JSON file
f = open('zgodovina_ogledov.json', encoding ="cp850")
 
#Converting JSON file format to a Python dictionary
data = json.load(f)


#Opening file with liked videos data - needs to be a JSON
liked_videos = csv.DictReader(open('Liked videos.csv'))
#print(liked_videos)
likedVid = list(liked_videos)[2]
lvKey = list(likedVid.keys())[0]
liked_videos = list(liked_videos)

liked_videos = csv.DictReader(open('Liked videos.csv'))
#print(liked_videos)
likedVid = list(liked_videos)[2]
lvKey2 = list(likedVid.keys())[1]


liked_videos = csv.DictReader(open('Liked videos.csv'))

liked_videos = list(liked_videos)



mostLikedChannel = {}

#print(liked_videos)
#liked_videos = csv.DictReader(open('Liked videos.csv'))
print("Processing liked video data")
for i,video in enumerate(liked_videos[2:]):
   
    if lvKey in video:
        # Getting the video author from noembed API
        vidUrl = video[lvKey]
        result = requests.get("https://noembed.com/embed?url=https://www.youtube.com/watch?v={}".format(vidUrl))
        result = json.loads(result.text)

        date = datetime.strptime(video[lvKey2], "%Y-%m-%d %H:%M:%S UTC")

        if "error" in result or not result["author_name"]:
            print("noAuth")

        else:

            videoAuthor = result["author_name"]

            # Counting number of videos watched from a channel
            if videoAuthor in mostLikedChannel:
                mostLikedChannel[videoAuthor] = mostLikedChannel[videoAuthor] + 1
            else:
                mostLikedChannel[videoAuthor] = 1

            
     
    if date.year < 2021:
        break 
    
  


    likecount = i
    print(i)
    


# Saving data dictionaries to files for later use
dictFile  = open("mostLikedChannel.pkl", "wb")
pickle.dump(mostLikedChannel, dictFile)
dictFile.close()


# Initializing all the dictionaries
mostWatchedChannel = {}
mornWatch = {}
dayWatch = {}
eveWatch = {}
nightOwl = {}
mostWatchedVideo = {}
longestChannelStreak = {}
prevAuth = ""
streakAuth = ""
streakCount = 0
i = 0
firstVideo = ""
lastVideoAdded = ""


#Loop that creates dictionaries with author names as keys and num. of watched videos as value
print("Processing history data")
for i, video in enumerate(data):
    
    if "titleUrl" in video:

        # Getting the video author from noembed API
        vidUrl = video["titleUrl"]
        result = requests.get("https://noembed.com/embed?url= {}".format(vidUrl))
        result = json.loads(result.text)
        lastVideoAdded = vidUrl
        
        if "error" in result or not result["author_name"]:
            print("noAuth")

        else:

            videoAuthor = result["author_name"]

            # Counting number of videos watched from a channel
            if videoAuthor in mostWatchedChannel:
                mostWatchedChannel[videoAuthor] = mostWatchedChannel[videoAuthor] + 1
            else:
                mostWatchedChannel[videoAuthor] = 1

            

            # Counting most watched video 
            if vidUrl in mostWatchedVideo:
                mostWatchedVideo[vidUrl] = mostWatchedVideo[vidUrl] + 1
            else:
                mostWatchedVideo[vidUrl] = 1 

            # Sorting video by time of day | MORNING/DAY/EVENING/NIGHT
            if "time" in video:
                
                # Removing unnecessary characters (T and Z) from date format 2021-12-03T09:44:14.018Z
                if "." in video["time"]:
                    date_time = video["time"].replace("T", " ").split(".", 1)
                else:
                    date_time = video["time"].replace("T", " ").split("Z", 1)
                
                time = datetime.strptime(date_time[0], "%Y-%m-%d %H:%M:%S")

                if(time.hour >= 6 and time.hour <= 10):
                    if videoAuthor in mornWatch:
                        mornWatch[videoAuthor] = mornWatch[videoAuthor] + 1
                    else:
                        mornWatch[videoAuthor] = 1

                if(time.hour >= 11 and time.hour <= 17):
                    if videoAuthor in dayWatch:
                        dayWatch[videoAuthor] = dayWatch[videoAuthor] + 1
                    else:
                        dayWatch[videoAuthor] = 1
                
                if(time.hour >= 18 and time.hour <= 23):
                    if videoAuthor in eveWatch:
                        eveWatch[videoAuthor] = eveWatch[videoAuthor] + 1
                    else:
                        eveWatch[videoAuthor] = 1

                if(time.hour >= 0 and time.hour <= 5):
                    if videoAuthor in nightOwl:
                        nightOwl[videoAuthor] = nightOwl[videoAuthor] + 1
                    else:
                        nightOwl[videoAuthor] = 1 

            # Tracking longest channel streak 
            if videoAuthor == prevAuth:
                streakAuth = videoAuthor
                streakCount += 1

            else:
                if videoAuthor not in longestChannelStreak:
                    longestChannelStreak[videoAuthor] = streakCount
                else:
                    if longestChannelStreak[videoAuthor] < streakCount:
                        longestChannelStreak[videoAuthor] = streakCount
                    streakCount = 0

        prevAuth = videoAuthor
    

    if time.year != datetime.now().year:
            firstVideo = lastVideoAdded
            break

    print(i)



        
    
    


# Sorting Channels
mostWatchedChannel = list(reversed(sorted(mostWatchedChannel.items(), key =
             lambda kv:(kv[1], kv[0]))))[:10]

# Sorting Channels
mostLikedChannel = list(reversed(sorted(mostLikedChannel.items(), key =
             lambda kv:(kv[1], kv[0]))))[:10]

# Sorting Videos
mostWatchedVideo = list(reversed(sorted(mostWatchedVideo.items(), key =
             lambda kv:(kv[1], kv[0]))))[:10]


# Sorting Channel Streak
longestChannelStreak = list(reversed(sorted(longestChannelStreak.items(), key =
             lambda kv:(kv[1], kv[0]))))[:10]


# Sorting 24H of YouTube
mornWatch = list(reversed(sorted(mornWatch.items(), key =
             lambda kv:(kv[1], kv[0]))))[:3]

dayWatch = list(reversed(sorted(dayWatch.items(), key =
             lambda kv:(kv[1], kv[0]))))[:3]

eveWatch = list(reversed(sorted(eveWatch.items(), key =
             lambda kv:(kv[1], kv[0]))))[:3]

nightOwl = list(reversed(sorted(nightOwl.items(), key =
             lambda kv:(kv[1], kv[0]))))[:3]



print("Here is your 2021 YouTube Wrapped\n")
print("-------------------------------------------------- \n\n")

print("These are your 10 most watched channels of 2021 (channel name and videos watched)\n")
print(mostWatchedChannel, "\n\n\n")

print("These are your 10 most liked channels of 2021 (channel name and number of liked videos)\n")
print(mostLikedChannel, "\n\n\n")

print("These are your 10 most watched videos of 2021 (video url and times watched)\n")
print(mostWatchedVideo, "\n\n\n")

print("These are your 10 longest channel streaks of 2021 (channel name and number of consecutive videos watched)\n")
print(longestChannelStreak, "\n\n\n")

print("These are your favourite channels to watch depending on the time (channel name and videos watched)\n")
print("In the mornign \n")
print(mornWatch, "\n\n")

print("During the day \n")
print(dayWatch, "\n\n")

print("In the evening \n")
print(eveWatch, "\n\n")

print("While everybody else was sleeping \n")
print(nightOwl, "\n\n\n")

print("And you've watched a total of ", i+1, " videos. And out of those ", i, " videos you've pressed the like button on: ", likecount, " of them!")


 
    




