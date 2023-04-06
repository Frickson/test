import json
  
# Opening JSON file
f = open('abc.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
print(data["ref"])
print(data["commits"][0])
# Closing file
f.close()