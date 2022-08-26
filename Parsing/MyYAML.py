# Workshop, 2022
# 3.6.6 Lab – Parse Different Data Types with Python Answers

import json
import yaml

# Step 1:Build a script to parse the YAML data.
with open('myfile.yml','r') as yaml_file:
	ouryaml = yaml.safe_load(yaml_file)
print(ouryaml)

print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))

print("\n\n")
print(json.dumps(ouryaml, indent=4))