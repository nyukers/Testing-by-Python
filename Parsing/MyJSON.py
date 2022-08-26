# Workshop, 2022
# 3.6.6 Lab – Parse Different Data Types with Python Answers

import json
import yaml

# Step 1:Build a script to parse the JSON data.
with open('myfile.json','r') as json_file:
	ourjson = json.load(json_file)
print(ourjson)

# Step 2: Run the script to print the JSON data and then modify it to print data of interest.
print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))

# Step 3: Output the parsed JSON data in a YAML data format.
print("\n\n---")
print(yaml.dump(ourjson))