#!/usr/bin/python

# 1. Use https://support.mozilla.org/en-US/questions/1077630#answer-834769
#    to save Firefox' passwords to JSON
# 2. If saving the text from the dialog box to the clipboard does not work,
#    save the object from the developer console to a file (right click in
#    the developer console output, after unfolding the object using the
#    little arrow on the left).
# 3. Afterwards pipe the file through this script.
# 4. Finally, follow https://help.bitwarden.com/article/import-data/ to
#    import the data as Bitwarden JSON file.

import json
import sys

bw = {
	"folders":[],
	"items":[],
}
ff = json.load(sys.stdin)
for e in ff:
	assert(e["guid"][0] == "{")
	assert(e["guid"][-1] == "}")
	bw["items"] += [
		{
			"id": e["guid"][1:-2],
			"type": 1,
			"name": e["displayOrigin"],
			"login": {
				"uris": [
					{
						"uri": e["origin"],
					}
				],
				"username": e["username"],
				"password": e["password"],
			},
		}
	]
json.dump(bw, sys.stdout)
