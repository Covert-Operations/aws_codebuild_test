from urllib import request as urlrequest
import json
import os
import re
import sys
import logging
import requests
import datetime

logger = logging.getLogger()
try:
  log_level = os.environ['LOG_LEVEL']
except:
    log_level = logging.ERROR

logger.setLevel(log_level)

"""
  To execute this, it expects that the event object will have standard CodeBuild SNS object values passed in as a hash. Additonally, you'll need to have the following environment variables defined beforehand.
  TEAMS_WEBHOOK_URL
  env_name = "some identifying name you can use"
"""

IN_PROGRESS_IMAGE = """data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4QBmRXhpZgAATU0AKgAAAAgABAEaAAUAAAABAAAAPgEbAAUAAAABAAAARgEoAAMAAAABAAIAAAExAAIAAAAQAAAATgAAAAAAAABgAAAAAQAAAGAAAAABcGFpbnQubmV0IDQuMi44AP/bAEMABgQFBgUEBgYFBgcHBggKEAoKCQkKFA4PDBAXFBgYFxQWFhodJR8aGyMcFhYgLCAjJicpKikZHy0wLSgwJSgpKP/bAEMBBwcHCggKEwoKEygaFhooKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKP/AABEIACgAKAMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APpTxJrtp4f05ru9YnJ2xxr96RvQf4151FP4u8bM0lrJ/Z+mkkAq5jQj0yPmb+X0ouIz42+I0lvKxOm2O5SAeCqnB/76b9PpXrEMaQxJHEipGgCqqjAAHYV7LcMuhFKKdRq+v2f+CfOxjUzepJuTjRi7JLRya3bfY8v/AOFXXf8ArP7c/f8A/XE/z3ZqvLP4u8Essl1J/aGmggEs5kQD0yfmX+X1q38apZIn0R4nZGHnYZTgj/V1T8AeM557pNH11/tVvcfuo5JfmIJ42t6g9Oa9Cm8TWwyxFS1SOt4tJOyfRo8mrHB4bGvCUealNWtJSbTbSeqfTWx6N4b1208Qact3ZMRg7ZI2+9G3of8AGivOreM+CfiNHbxMRpt9tUAngKxwP++W/T60V4uNwipTUqOsJK6/y+R9Jl2PdaDhiLKpB2f+a9Sx8Gv+Qhrnm/675P5tn9cV6lXktxIfBPxGkuJVI02+3MSBwFY5P/fLfp9a6v4gzaxNoCnw6nnQzDMskLZk2EcbQOoPqOa68fQeIxMKkXaNRKze22p5+VYlYPBzpSTc6Td0t3rdP0d9ziPi3rlpqmo2lpZN5n2LzBJIPulm28D6ba4ez8z7XD5GfN3rsx13Z4o+zT+d5Xky+bnGzYd35V6H8P8AwZNBdJrGup9lt7f97HHL8pJHO5s9AOvNfRuVHLsMoX2Wndv/AIc+PUMRm+NdTls29eyS/wAkWfjL/wAhDQ/K/wBd8/8ANcfrmiq9tIfG3xGjuIlJ02x2sCRwVU5H/fTfp9KK8h41ZfSp0JxvK135Xd7H0Cy15tXq4qnLli3Zedklc9F8SaFaeINOa0vVIwd0ci/ejb1H+FedRQeLvBLNHax/2hpoJICoZEHvgfMv8vrRRXmYDEzTWHklKD6P9D281wUJReKg3GpFbp2+T7lj/haN3/q/7D/f/wDXY/y25qvLB4u8bMsd1H/Z+mkgkMhjQ++D8zfy+lFFexjadLL4KrQgubzu7el2fO5dWr5tUdDFVG49lZX9bI9F8N6FaeH9OW0slJyd0kjfekb1P+FFFFfLznKpJzm7tn29KlCjBU6askf/2Q=="""

SUCCEEDED_IMAGE = """data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4QBmRXhpZgAATU0AKgAAAAgABAEaAAUAAAABAAAAPgEbAAUAAAABAAAARgEoAAMAAAABAAIAAAExAAIAAAAQAAAATgAAAAAAAABgAAAAAQAAAGAAAAABcGFpbnQubmV0IDQuMi44AP/bAEMABgQFBgUEBgYFBgcHBggKEAoKCQkKFA4PDBAXFBgYFxQWFhodJR8aGyMcFhYgLCAjJicpKikZHy0wLSgwJSgpKP/bAEMBBwcHCggKEwoKEygaFhooKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKP/AABEIACgAKAMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APpPxNr1n4e01ru9YnJ2xxr96RvQf414n4g8c61rErf6S9pbHgQ27FRj3PU/y9qPiPrT6x4nucNm2tWMEQB4wDyfxOfwxXL15levKUuWOx+d51nVXEVZUqUrQWmnXzJPPl8zf5sm/wDvbjmuk8P+Oda0eVf9Je7thwYbhiwx7HqP5e1cvXo/gXwXAbNtb8TBYrBU3xxSHaGH95vb0Hf+eVJTcvcPOy2GKq1ksNJp7t30S7vyPTfDOvWfiHTVu7JiMHbJG33o29D/AI0V494N1q20fxz/AMS1pRpV1L5GJTztJ+Un6H9M0V6VGrzx13PvspzNYyjeo1zRdn2fmvU5uz+zf21H/a/m/ZfO/f8AlfexnnFdx468FwCzXW/DIWWwZN8kUZ3BR/eX29R2/lgfEjRX0fxPc4XFtdMZ4iBxgnkfgc/hip/APjKbw7c/Z7rdLpkjfOnUxn+8v9R3rgjyxbpz+8+JoRoUalTBYyNrv4uqfR+hteAfBsKW39veJNsVlGvmRRS8Bh/fb29B3+nXF8feMpvEVz9ntd0WmRt8idDIf7zf0Hajx94ym8RXP2e13RaZG3yJ0Mh/vN/Qdq5CipUUVyQ2/MMbjadKn9Twfwfal1k/8uyJLbd9oi8v7+8bfrmiuk+G+ivrHie2yuba1YTykjjAPA/E4/DNFXQoOcb3OrJ8mqYyk6vNyq/3ntnibQbPxDprWl6pGDujkX70beo/wrxPxB4G1rR5W/0Z7u2HImt1LDHuOo/l70UV1V6UZrme59NnWV4fE03WmrSS3X6nN+RL5mzypN/93ac10nh/wNrWsSrm2e0tjyZrhSox7Dqf5e9FFcVClGcrM+SyfLqWMr8lW9ke2eGdBs/D2mraWSk5O6SRvvSN6n/CiiivUSSVkfo9OnClBU6askf/2Q=="""

FAILED_IMAGE = """data:image/jpeg;base64,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"""




def detectSourceType(source):
  branch = source or ""
  retStr = "/tree/{}".format(branch)

  # created by, > echo "hello world" | sha256 | cut -c 1-40
  # True == shaRegex.match("a948904f2f0f479b8f8197694b30184b0d2ed1c1")
  shaRegex = re.compile('(\w|\d){40}')
  # True == prRegex.match("pr12345")
  prRegex = re.compile('pr\/(\d+)')

  if shaRegex.match(branch) is not None:
    retStr = '/commit/{}'.format(branch)
  elif prRegex.match(branch) is not None:
    retStr = '/pull/{}'.format(prRegex.group(1))

  return retStr

def snspush_handler(event, context):
  webhook_url = os.environ["TEAMS_WEBHOOK_URL"]
  
  if( event is not None and
      event["Records"] is not None and
      len(event["Records"]) > 0):
    records = event['Records']

    for record in records:
      print("checking records")
      raw_msg = record["Sns"]["Message"]
      msg = raw_msg

      detail = msg["detail"]

      logger.info("CodeBuild Event payload.\n{}".format(json.dumps(detail)))

      completed_phase = detail['completed-phase']
      project_name    = detail['project-name']
      completed_phase_status = detail['completed-phase-status']
      completed_phase_end    = detail['completed-phase-end']
      buildId = detail['build-id'].split('/')[1]
      region = msg["region"]
      project = detail["project-name"]
      summary = "[build [{}] notification](https://console.aws.amazon.com/codesuite/codebuild/projects/{}/build/{}/log?region={}".format(project, project, buildId, region)
      additional = detail['additional-information']
      build_number    = int(additional['build-number'])
      build_complete  = bool(additional['build-complete'])
      build_start_t   = additional['build-start-time']
      try:
        status          = additional["build-status"]
      except:
        status = completed_phase_status

      try:
        branch = additional['source-version']
      except:
        branch = "master"
      branch_url = additional["source"]["location"].replace(".git", 
                                                            detectSourceType(branch))
      source = additional["source"]["location"]
      environment = additional["environment"]
      env_var = environment["environment-variables"]
      env = ""
      try:
        env = env_var["env_name"]
      except:
        env = "default_build"

      image = SUCCEEDED_IMAGE
      themeColor = "#CEDB56"
      if status == "SUCCEEDED":
        themeColor = "#CEDB56"
        image = SUCCEEDED_IMAGE
      elif status == "IN_PROGRESS":
        themeColor = "#76CDD8"
        image = IN_PROGRESS_IMAGE
      else:
        themeColor = "#D35D47"
        image = FAILED_IMAGE

      webhook_payload = json.dumps({"@type": 'MessageCard',
                         '@context': 'http://schema.org/extensions',
                         "themeColor": themeColor,
                         "summary": summary,
                         "sections": [
                           {
                             "activityTitle": summary,
                             "activitySubtitle": 'On project [{}]'.format(project),
                             "activityImage": image,
                             "facts": [
                               {
                                 "name": 'Status',
                                 "value": "{}".format(status)
                               },
                               {
                                 "name": 'Date',
                                 "value": "{}".format(build_start_t)
                                },
                               {
                                 "name": 'Source Branch',
                                 "value": '[{}]({})'.format(branch, branch_url)
                                },
                               {
                                 "name": 'Target Env',
                                 "value": "{}".format(env)
                                }
                               ],
                               "markdown": True
                            }
                        ]
                    })

      print("set_images={}".format(""))

      try:
        print("after try")
        response = requests.post(webhook_url, data = webhook_payload)
        print("after request")

      except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
      
      print(response)


  return { "status" : "SUCCESS" }



if __name__ == "__main__":
  import testpkg.sampleevent

  event = testpkg.sampleevent.sample_sns_event
  context = {"name": "sample"}

  os.environ["TEAMS_WEBHOOK_URL"] = "https://outlook.office.com/webhook/387c2f0b-1220-4955-a2dd-3bac12ab4e1d@169ea2cd-9387-4a99-b50f-39148dd63fdf/IncomingWebhook/58cdf3357b344db0adf29e7de2c95334/cb29463c-3526-4041-bab7-c8373b5a79dd"
  os.environ["env_name"] = "production"
  snspush_handler(event, context)


