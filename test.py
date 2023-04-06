import json
  
f = open('abc.json')
testlist = ['added', 'modified']
commit =[]
# returns JSON object as 
# a dictionary
data = json.load(f)
  
ref = data["ref"]
for x in range(len(testlist)):
    if(data["commits"][0][testlist[x]]):
        commit.append(data["commits"][0][testlist[x]])
        print(ref)
        if len(commit) > 0:
            tmp = ' '.join(commit[x])
            ref = ref + " " + tmp
        else:
            ref = ref + " " + commit[x][0]
print(ref)


repository_name = data['repository']['name']
commit_sha = data['after']
commit_data = data['commits'][0]
commit_files = commit_data['added'] + commit_data['modified']
print(commit_files)
print(commit_sha)
    # Check if any of the modified or added files are in the specific folder
folder_path = "abc/"
folder_files = [f for f in commit_files if f.startswith(folder_path)]
if not folder_files:
    print("lol")
else: 
    print("nice")
#     return {
#         'statusCode': 200,
#         'body': json.dumps('No files modified in the specific folder')
#     }
# print(commit)
# if ref=="refs/heads/master":
#     if

# "refs/heads/main [\"authapi/README.md\"]"
# commit= ''.join(commit)
# print(ref, commit)
# Closing file
f.close()