import requests
import base64
import sys

challenge = requests.post("http://challenges.clusterfights.com/challenge/create",
	json={
		"cluster": "<YOUR CLUSTER>",
		"cohort": "<YOUR CURRENT EXPERIMENT>",
		"type": "dungeon_master",
		"params": {}
	})

print(challenge.content)
ch = challenge.json()
with open('a.zip', 'wb') as f:
    f.write(base64.b64decode(ch['challenge']['filedata']))

#
# READ
#
# THIS
#
# PART
#
############################## NOTE: the password for the first zip is "fight!"
#
############################## the zip file will reveal a look.txt file and some .zip files
############################## the zip file passwords are the gutenhash solutions of the 
############################## hashes in look.txt
#
#
#
