import requests
import sys

res = requests.put("http://challenges.clusterfights.com/challenge/" + sys.argv[1], json={
		"solution": { 
			"secret": sys.argv[2]
		}
	})

print(res.json()['runtime'])
