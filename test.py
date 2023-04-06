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

for x in 
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