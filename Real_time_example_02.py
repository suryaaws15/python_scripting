# 1)use request module
# 2)API call (for pull request)
# 3) json to dictionaries
# 4) print

import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_deatail = response.json()

for i in range(len(complete_deatail)):
 print(complete_deatail[i]["user"]["login"])


