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
    # Check if any of the modified or added files are in the specific folder
folder_path = "abc/"
folder_files = [f for f in commit_files if f.startswith(folder_path)]
if not folder_files:
    print("lol")
else: 
    return{
            'statusCode': 200,
            'body': json.dumps('No files modified in the specific folder')
        }

    # Trigger the CodePipeline if any of the modified or added files are in the specific folder
    client = boto3.client('codepipeline')
    response = client.start_pipeline_execution(
        name='your-pipeline-name',
        clientRequestToken=str(commit_sha),
        trigger={
            'triggerType': 'Custom',
            'triggerDetail': json.dumps({
                'repositoryName': repository_name,
                'commitSha': commit_sha,
                'folderFiles': folder_files
            })
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Pipeline execution triggered successfully')
    }