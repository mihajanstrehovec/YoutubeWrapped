import requests
import json
import pickle
from datetime import datetime

#Opening file with watch history data - JSON
f = open('zgodovina_ogledov.json', encoding ="cp850")
 
#Converting JSON file format to a Python dictionary
data = json.load(f)

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

#Loop that creates dictionaries with author names as keys and num. of watched videos as value
for video in data:
    if "titleUrl" in video:

        # Getting the video author from noembed API
        vidUrl = video["titleUrl"]
        result = requests.get("https://noembed.com/embed?url= {}".format(vidUrl))
        result = json.loads(result.text)
        
        if "error" in result or not result["author_name"]:
            print("noAuth")

        else:

            videoAuthor = result["author_name"]

            # Counting number of videos watched from a channel
            if videoAuthor in mostWatchedChannel:
                mostWatchedChannel[videoAuthor] = mostWatchedChannel[videoAuthor] + 1
            else:
                mostWatchedChannel[videoAuthor] = 1

            print(videoAuthor)

            # Counting most watched video 
            if vidUrl in mostWatchedVideo:
                mostWatchedVideo[vidUrl] = mostWatchedVideo[vidUrl] + 1
            else:
                mostWatchedVideo[vidUrl] = 1 

            # Sorting video by time of day | MORNING/DAY/EVENING/NIGHT
            if "time" in video:
                
                # Removing unnecessary characters (T and Z)
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




        i = i + 1
        prevAuth = videoAuthor
    
    else:

        i=i+1

        
    
    
    
    if i >= 29100:

        break

    print(i)
    


print(sorted(mostWatchedVideo.items(), key =
             lambda kv:(kv[1], kv[0]))) 


print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

print(sorted(longestChannelStreak.items(), key =
             lambda kv:(kv[1], kv[0]))) 
# Saving data dictionaries to files for later use
dictFile  = open("historyData2.pkl", "wb")
pickle.dump(mostWatchedChannel, dictFile)
dictFile.close()

dictFile  = open("historyData_morning.pkl", "wb")
pickle.dump(mornWatch, dictFile)
dictFile.close()

dictFile  = open("historyData_day.pkl", "wb")
pickle.dump(dayWatch, dictFile)
dictFile.close()

dictFile  = open("historyData_eve.pkl", "wb")
pickle.dump(eveWatch, dictFile)
dictFile.close()

dictFile  = open("historyData_night.pkl", "wb")
pickle.dump(nightOwl, dictFile)
dictFile.close()

dictFile  = open("historyData_channelStreak.pkl", "wb")
pickle.dump(longestChannelStreak, dictFile)
dictFile.close()



