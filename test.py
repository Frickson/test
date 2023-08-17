import json
import re

def execute_pipeline(filename):
    for x in filename:
        execute
f = open('abc.json')
testlist = ['added', 'modified']
exclude_list = ["README.md"]
commit =[]
# returns JSON object as 
# a dictionary
data = json.load(f)
  
ref = data["ref"]
branch_match = re.match(r"refs/heads/(.*)", ref)
if branch_match:
    # If the ref matches the regex pattern "refs/heads/(.*)", extract the branch name
    branch_name = branch_match.group(1)
    print(f"Found branch '{branch_name}'")
else:
    # If the ref doesn't match the regex pattern, print an error message
    print(f"Error: Could not extract branch name from ref '{ref}'")
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

output_list = []
repository_name = data['repository']['name']
commit_sha = data['after']
commit_data = data['commits'][0]
commit_files = commit_data['added'] + commit_data['modified']
print(commit_files)
print(commit_sha)

input_list = ['abc/test.txt', 'test.py', 'abc.json', 'authapi/abc.txt', 'abc/test1.txt']

# Filter out the strings that contain '/'
filtered_list = list(filter(lambda x: '/' in x, input_list))

# Split the remaining strings into two parts
split_list = [s.split('/') for s in filtered_list]

# Extract the first and second parts of each split string
output_list = [[s[0], s[1]] for s in split_list]

print(output_list)
run_list =[]
for file in output_list:
    if file[1] not in exclude_list:
        run_list.append(file[0])

print(run_list)       
res = [*set(run_list)]
print(res)
    # if re.search(r'abc/', x):
    #     output_list.append(x)


# Print the output list
# print(output_list)
# 
# folder')
#     }
# print(commit)
# if ref=="refs/heads/master":
#     if

# "refs/heads/main [\"authapi/README.md\"]"
# commit= ''.join(commit)
# print(ref, commit)xx
# Closing file
f.close()
