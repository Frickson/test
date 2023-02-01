import yaml

with open("dep.yaml", "r") as stream:
    files = yaml.safe_load_(stream)
    files = list(files)
    # print(files['spec']['template']['spec']['containers'][0]['image'])
    files[0]['spec']['template']['spec']['containers'][0]['image'] = "frickson/app:version3"
    # print(files['spec']['template']['spec']['containers'][0]['image'])

with open("example.yaml", "w") as outfile:   
    yaml.dump(files, outfile, default_flow_style=False)
       
