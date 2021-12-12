import pickle 

dict = {
    "key1": 1,
    "key2": 2,
    "key3": 3
}

a_file = open("data.pkl", "wb")
pickle.dump(dict, a_file)
a_file.close()

b_file = open("data.pkl", "rb")
data = pickle.load(b_file)
print(data["key2"])

b_file.close()