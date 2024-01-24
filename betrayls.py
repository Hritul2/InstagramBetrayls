# import the Libraries
import json

# Access all the files locations
followers_loaction= 'followers_1.json'
follwings_location= 'following.json'

# Access all the data from json files
with open(followers_loaction, 'r') as file:
     followers = json.load(file)

with open(follwings_location,'r') as file:
     followings= json.load(file)

# Given below is the interesting data
# followings["relationships_following"][0]["string_list_data"][0]["value"]
# followers[0]["string_list_data"][0]["value"]

followerList=[]
followingList=[]

for itemFollower in followers:
     followerList.append(itemFollower["string_list_data"][0]["value"])

for itemFollowing in followings["relationships_following"]:
     followingList.append(itemFollowing["string_list_data"][0]["value"])

def FollowingButNotFollower(followersList,followingsList):
    ans=[]
    hashMap={}
    for item in  followersList:
         hashMap[item]=True

    for item in followingsList:
         if item not in hashMap:
              ans.append(item)
    return ans


for item in FollowingButNotFollower(followerList,followingList):
     print(item)