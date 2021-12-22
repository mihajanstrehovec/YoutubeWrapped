import pickle

f = open("historyData_night.pkl", "rb")

data = pickle.load(f)


print(sorted(data.items(), key =
             lambda kv:(kv[1], kv[0]))) 

numOfVids = 0

for watches in data:
    numOfVids += data[watches]

print(numOfVids)

# parsedData = {}
# for author in data:
#     parsedData[author.lower()] = data[author]
    
#     #print (author)
# #print(data)

# topicArr = []

# for author in parsedData:
#     if "topic" in author:
#         topicArr.append(author)

# #print(len(parsedData))

# print(sorted(parsedData.items(), key =
#              lambda kv:(kv[1], kv[0]))) 

# print("------------------------------------------------------------------------ \n")
# print("------------------------------------------------------------------------ \n")
# print("------------------------------------------------------------------------ \n")
# print("------------------------------------------------------------------------ \n")
# print("------------------------------------------------------------------------ \n")
# print("------------------------------------------------------------------------ \n")
# # print(parsedData["IDK - Topic"])


# for authorTopic in topicArr:
#     if authorTopic.split(" -",1)[0] in parsedData:
#         parsedData[authorTopic.split(" -",1)[0]] += parsedData[authorTopic]
#         parsedData.pop(authorTopic)

# print(sorted(parsedData.items(), key =
#             lambda kv:(kv[1], kv[0]))) 

# # print(parsedData["idk"])

# #print(topicArr)
    