import os
import requests
import sys

TOKEN= str(sys.argv[1])
OWNER= str(sys.argv[2])
REPO= str(sys.argv[3])
workflowname= str(sys.argv[4])
parameter1= str(sys.argv[5])
parameter2 = str(sys.argv[6])

print( "the toke value is")
def trigger_workflow(workflowname,parameter1,parameter2):

      headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}",
      }

      data = {
        "event_type": workflowname,
        "client_payload": {
          'parameter1': parameter1,
          'parameter2': parameter2
        }
      }

      responsevalue=requests.post(f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches",json=data,headers=headers)
      print(responsevalue.content)

trigger_workflow(workflowname,parameter1,parameter2)