username='plederer@depaul.edu'
api_key = '37E4B4E6-32F9-437E-CA76-A1BCBD4C7B85'
msg_to = '+16304171011'
msg_from = ''
msg_body = 'This is a test message'

import json, subprocess

request = { "messages" : [ { "source":"rpi", "from":msg_from, "to":msg_to, "body":msg_body } ] }
request = json.dumps(request)
cmd = "curl https://rest.clicksend.com/v3/sms/send -u " + username + ":" + api_key + " -H \"Content-Type: application/json\" -X POST --data-raw '" + request + "'"
p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
(output,err) = p.communicate()
#print output
