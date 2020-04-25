sample_event = {
  "account":"876557376893",
  "detailType":"CodeBuild Build Phase Change",
  "region":"us-east-2",
  "source":"aws.codebuild",
  "time":"2020-04-23T00:59:22Z",
  "notificationRuleArn":"arn:aws:codestar-notifications:us-east-2:876557376893:notificationrule/ebe6e1acb9a18b7654b37b2a9a8f82e6a2a00b71",
  "detail":{"completed-phase":"SUBMITTED",
            "project-name":"ecs-devops-sandbox",
            "build-id":"arn:aws:codebuild:us-east-2:876557376893:build/ecs-devops-sandbox:93c1edb4-81eb-4669-b6ac-b82a6ccdcbd9",
            "completed-phase-context":"[]",
            "additional-information":{"cache":{"type":"NO_CACHE"},
                                      "build-number":5.0,
                                      "timeout-in-minutes":60.0,
                                      "build-complete":False,
                                      "initiator":"AWSReservedSSO_AdministratorAccess_f356718c3664b8b4/thaddeus",
                                      "build-start-time":"Apr 23, 2020 12:59:22 AM",
                                      "source":{"location":"https://github.com/Covert-Operations/aws_codebuild_test.git",
                                                "type":"GITHUB"},
                                      "artifact":{"location":""},
                                      "environment":{"image":"aws/codebuild/standard:4.0",
                                                     "privileged-mode":False,
                                                     "image-pull-credentials-type":"CODEBUILD",
                                                     "compute-type":"BUILD_GENERAL1_SMALL",
                                                     "type":"LINUX_CONTAINER",
                                                     "environment-variables":[]},
                                      "logs":{"deep-link":"https://console.aws.amazon.com/cloudwatch/home?region=us-east-2#logEvent:group=null;stream=null"},
                                      "phases":[{"phase-context":[],
                                                 "start-time":"Apr 23, 2020 12:59:22 AM",
                                                 "end-time":"Apr 23, 2020 12:59:22 AM",
                                                 "duration-in-seconds":0.0,
                                                 "phase-type":"SUBMITTED",
                                                 "phase-status":"SUCCEEDED"},
                                                {"start-time":"Apr 23, 2020 12:59:22 AM",
                                                 "phase-type":"QUEUED"}],
                                      "queued-timeout-in-minutes":480.0},
            "completed-phase-status":"SUCCEEDED",
            "completed-phase-duration-seconds":0.0,
            "version":"1",
            "completed-phase-start":"Apr 23, 2020 12:59:22 AM",
            "completed-phase-end":"Apr 23, 2020 12:59:22 AM"},
  "resources":["arn:aws:codebuild:us-east-2:876557376893:build/ecs-devops-sandbox:93c1edb4-81eb-4669-b6ac-b82a6ccdcbd9"],
  "additionalAttributes":{}
}

sample_sns_event = {
  "Records": [
    {
      "EventSource": "aws:sns",
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:us-east-2:{{{accountId}}}:ExampleTopic",
      "Sns": {
        "Type": "Notification",
        "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
        "TopicArn": "arn:aws:sns:us-east-2:123456789012:ExampleTopic",
        "Subject": "example subject",
        "Message": {
          "account": "876557376893",
          "detailType": "CodeBuild Build Phase Change",
          "region": "us-east-2",
          "source": "aws.codebuild",
          "time": "2020-04-23T00:59:22Z",
          "notificationRuleArn": "arn:aws:codestar-notifications:us-east-2:876557376893:notificationrule/ebe6e1acb9a18b7654b37b2a9a8f82e6a2a00b71",
          "detail": {
            "completed-phase": "SUBMITTED",
            "project-name": "ecs-devops-sandbox",
            "build-id": "arn:aws:codebuild:us-east-2:876557376893:build/ecs-devops-sandbox:93c1edb4-81eb-4669-b6ac-b82a6ccdcbd9",
            "completed-phase-context": "[]",
            "additional-information": {
              "cache": {
                "type": "NO_CACHE"
              },
              "build-number": 5,
              "timeout-in-minutes": 60,
              "build-complete": False,
              "initiator": "AWSReservedSSO_AdministratorAccess_f356718c3664b8b4/thaddeus",
              "build-start-time": "Apr 23, 2020 12:59:22 AM",
              "source": {
                "location": "https://github.com/Covert-Operations/aws_codebuild_test.git",
                "type": "GITHUB"
              },
              "artifact": {
                "location": ""
              },
              "environment": {
                "image": "aws/codebuild/standard:4.0",
                "privileged-mode": False,
                "image-pull-credentials-type": "CODEBUILD",
                "compute-type": "BUILD_GENERAL1_SMALL",
                "type": "LINUX_CONTAINER",
                "environment-variables": []
              },
              "logs": {
                "deep-link": "https://console.aws.amazon.com/cloudwatch/home?region=us-east-2#logEvent:group=null;stream=null"
              },
              "phases": [
                {
                  "phase-context": [],
                  "start-time": "Apr 23, 2020 12:59:22 AM",
                  "end-time": "Apr 23, 2020 12:59:22 AM",
                  "duration-in-seconds": 0,
                  "phase-type": "SUBMITTED",
                  "phase-status": "SUCCEEDED"
                },
                {
                  "start-time": "Apr 23, 2020 12:59:22 AM",
                  "phase-type": "QUEUED"
                }
              ],
              "queued-timeout-in-minutes": 480
            },
            "completed-phase-status": "SUCCEEDED",
            "completed-phase-duration-seconds": 0,
            "version": "1",
            "completed-phase-start": "Apr 23, 2020 12:59:22 AM",
            "completed-phase-end": "Apr 23, 2020 12:59:22 AM"
          },
          "resources": [
            "arn:aws:codebuild:us-east-2:876557376893:build/ecs-devops-sandbox:93c1edb4-81eb-4669-b6ac-b82a6ccdcbd9"
          ],
          "additionalAttributes": {}
        },
        "Timestamp": "1970-01-01T00:00:00.000Z",
        "SignatureVersion": "1",
        "Signature": "EXAMPLE",
        "SigningCertUrl": "EXAMPLE",
        "UnsubscribeUrl": "EXAMPLE",
        "MessageAttributes": {
          "Test": {
            "Type": "String",
            "Value": "TestString"
          },
          "TestBinary": {
            "Type": "Binary",
            "Value": "TestBinary"
          }
        }
      }
    }
  ]
}

aws_build_event = {'Records': 
                   [{'EventSource': 'aws:sns', 
                     'EventVersion': '1.0', 
                     'EventSubscriptionArn': 'arn:aws:sns:us-east-2:876557376893:codestar-notifications-to-teams:326cf852-0c29-416e-8e2b-395666db58ed', 
                     'Sns': {
                       'Type': 'Notification', 
                       'MessageId': '37b13ceb-a433-53a9-8e87-6bf6de1693dc', 
                       'TopicArn': 'arn:aws:sns:us-east-2:876557376893:codestar-notifications-to-teams', 
                       'Subject': None, 
                       'Message': '{"account":"876557376893","detailType":"CodeBuild Build Phase Change","region":"us-east-2","source":"aws.codebuild","time":"2020-04-24T23:35:53Z","notificationRuleArn":"arn:aws:codestar-notifications:us-east-2:876557376893:notificationrule/ebe6e1acb9a18b7654b37b2a9a8f82e6a2a00b71","detail":{"completed-phase":"SUBMITTED","project-name":"ecs-devops-sandbox","build-id":"arn:aws:codebuild:us-east-2:876557376893:build/ecs-devops-sandbox:55292dda-3f86-43ea-9a3e-be08b987ec6f","completed-phase-context":"[]","additional-information":{"cache":{"type":"NO_CACHE"},"build-number":11.0,"timeout-in-minutes":60.0,"build-complete":false,"initiator":"AWSReservedSSO_AdministratorAccess_f356718c3664b8b4/thaddeus","build-start-time":"Apr 24, 2020 11:35:53 PM","source":{"location":"https://github.com/Covert-Operations/aws_codebuild_test.git","type":"GITHUB"},"artifact":{"location":""},"environment":{"image":"aws/codebuild/standard:4.0","privileged-mode":false,"image-pull-credentials-type":"CODEBUILD","compute-type":"BUILD_GENERAL1_SMALL","type":"LINUX_CONTAINER","environment-variables":[]},"logs":{"deep-link":"https://console.aws.amazon.com/cloudwatch/home?region=us-east-2#logEvent:group=null;stream=null"},"phases":[{"phase-context":[],"start-time":"Apr 24, 2020 11:35:53 PM","end-time":"Apr 24, 2020 11:35:53 PM","duration-in-seconds":0.0,"phase-type":"SUBMITTED","phase-status":"SUCCEEDED"},{"start-time":"Apr 24, 2020 11:35:53 PM","phase-type":"QUEUED"}],"queued-timeout-in-minutes":480.0},"completed-phase-status":"SUCCEEDED","completed-phase-duration-seconds":0.0,"version":"1","completed-phase-start":"Apr 24, 2020 11:35:53 PM","completed-phase-end":"Apr 24, 2020 11:35:53 PM"},"resources":["arn:aws:codebuild:us-east-2:876557376893:build/ecs-devops-sandbox:55292dda-3f86-43ea-9a3e-be08b987ec6f"],"additionalAttributes":{}}', 
                       'Timestamp': '2020-04-24T23:36:05.364Z', 
                       'SignatureVersion': '1', 
                       'Signature': 'Dlhy7UW+M1SFHhFNiskWwQo/uGER3iTlagSShL5H6W7svlzR+1otMCBL1gm8RbmOw94olyvUR5w2LtM/WT1pXZN3HyGiT65FZiy7V80UwipvNCUn2rGtId/E640evww7MzYZycdCtAdHYMRlUFoBubTVn8jC6TU+95L/24/+XbDEDYnm2AlDB/dvFSU2Iq1KfKDR3nVbmMySgO+5FW/ZkYiwQ/R0JnWYfAaVnrokuqcANEaCnG5BIpHuP5MSa+4EnVHv2ElIXRu3RExy5y/lTF3nhyI+yA0Twx8wHtI2ui8J7pJgwfqbPzUUsJFti/RD/3CQhO8U+CDDQSosZzgcWw==', 
                       'SigningCertUrl': 'https://sns.us-east-2.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem', 
                       'UnsubscribeUrl': 'https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:876557376893:codestar-notifications-to-teams:326cf852-0c29-416e-8e2b-395666db58ed', 
                       'MessageAttributes': {}
                       }
                     }]
                   }

aws_build_complete = {
    "Records": [
        {
            "EventSource": "aws:sns",
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:us-east-2:876557376893:codestar-notifications-to-teams:326cf852-0c29-416e-8e2b-395666db58ed",
            "Sns": {
                "Type": "Notification",
                "MessageId": "4f51ec4c-b4d4-5023-bb48-bb51312ec4b3",
                "TopicArn": "arn:aws:sns:us-east-2:876557376893:codestar-notifications-to-teams",
                "Subject": "",
                "Message": "{\"account\":\"876557376893\",\"detailType\":\"CodeBuild Build State Change\",\"region\":\"us-east-2\",\"source\":\"aws.codebuild\",\"time\":\"2020-04-25T00:26:27Z\",\"notificationRuleArn\":\"arn:aws:codestar-notifications:us-east-2:876557376893:notificationrule/ebe6e1acb9a18b7654b37b2a9a8f82e6a2a00b71\",\"detail\":{\"build-status\":\"SUCCEEDED\",\"project-name\":\"ecs-devops-sandbox\",\"build-id\":\"arn:aws:codebuild:us-east-2:876557376893:build/ecs-devops-sandbox:d113f2e0-b017-4707-a20d-2fa92d469a3a\",\"additional-information\":{\"cache\":{\"type\":\"NO_CACHE\"},\"build-number\":13.0,\"timeout-in-minutes\":60.0,\"build-complete\":true,\"initiator\":\"AWSReservedSSO_AdministratorAccess_f356718c3664b8b4/thaddeus\",\"build-start-time\":\"Apr 25, 2020 12:25:32 AM\",\"source\":{\"location\":\"https://github.com/Covert-Operations/aws_codebuild_test.git\",\"type\":\"GITHUB\"},\"artifact\":{\"location\":\"\"},\"environment\":{\"image\":\"aws/codebuild/standard:4.0\",\"privileged-mode\":false,\"image-pull-credentials-type\":\"CODEBUILD\",\"compute-type\":\"BUILD_GENERAL1_SMALL\",\"type\":\"LINUX_CONTAINER\",\"environment-variables\":[]},\"logs\":{\"group-name\":\"/aws/codebuild/ecs-devops-sandbox\",\"stream-name\":\"d113f2e0-b017-4707-a20d-2fa92d469a3a\",\"deep-link\":\"https://console.aws.amazon.com/cloudwatch/home?region=us-east-2#logEvent:group=/aws/codebuild/ecs-devops-sandbox;stream=d113f2e0-b017-4707-a20d-2fa92d469a3a\"},\"phases\":[{\"phase-context\":[],\"start-time\":\"Apr 25, 2020 12:25:32 AM\",\"end-time\":\"Apr 25, 2020 12:25:33 AM\",\"duration-in-seconds\":0.0,\"phase-type\":\"SUBMITTED\",\"phase-status\":\"SUCCEEDED\"},{\"phase-context\":[],\"start-time\":\"Apr 25, 2020 12:25:33 AM\",\"end-time\":\"Apr 25, 2020 12:25:34 AM\",\"duration-in-seconds\":1.0,\"phase-type\":\"QUEUED\",\"phase-status\":\"SUCCEEDED\"},{\"phase-context\":[\": \"],\"start-time\":\"Apr 25, 2020 12:25:34 AM\",\"end-time\":\"Apr 25, 2020 12:26:17 AM\",\"duration-in-seconds\":43.0,\"phase-type\":\"PROVISIONING\",\"phase-status\":\"SUCCEEDED\"},{\"phase-context\":[\": \"],\"start-time\":\"Apr 25, 2020 12:26:17 AM\",\"end-time\":\"Apr 25, 2020 12:26:20 AM\",\"duration-in-seconds\":2.0,\"phase-type\":\"DOWNLOAD_SOURCE\",\"phase-status\":\"SUCCEEDED\"},{\"phase-context\":[\": \"],\"start-time\":\"Apr 25, 2020 12:26:20 AM\",\"end-time\":\"Apr 25, 2020 12:26:20 AM\",\"duration-in-seconds\":0.0,\"phase-type\":\"INSTALL\",\"phase-status\":\"SUCCEEDED\"},{\"phase-context\":[\": \"],\"start-time\":\"Apr 25, 2020 12:26:20 AM\",\"end-time\":\"Apr 25, 2020 12:26:24 AM\",\"duration-in-seconds\":3.0,\"phase-type\":\"PRE_BUILD\",\"phase-status\":\"SUCCEEDED\"},{\"phase-context\":[\": \"],\"start-time\":\"Apr 25, 2020 12:26:24 AM\",\"end-time\":\"Apr 25, 2020 12:26:24 AM\",\"duration-in-seconds\":0.0,\"phase-type\":\"BUILD\",\"phase-status\":\"SUCCEEDED\"},{\"phase-context\":[\": \"],\"start-time\":\"Apr 25, 2020 12:26:24 AM\",\"end-time\":\"Apr 25, 2020 12:26:24 AM\",\"duration-in-seconds\":0.0,\"phase-type\":\"POST_BUILD\",\"phase-status\":\"SUCCEEDED\"},{\"phase-context\":[\": \"],\"start-time\":\"Apr 25, 2020 12:26:24 AM\",\"end-time\":\"Apr 25, 2020 12:26:24 AM\",\"duration-in-seconds\":0.0,\"phase-type\":\"UPLOAD_ARTIFACTS\",\"phase-status\":\"SUCCEEDED\"},{\"phase-context\":[\": \"],\"start-time\":\"Apr 25, 2020 12:26:24 AM\",\"end-time\":\"Apr 25, 2020 12:26:26 AM\",\"duration-in-seconds\":2.0,\"phase-type\":\"FINALIZING\",\"phase-status\":\"SUCCEEDED\"},{\"start-time\":\"Apr 25, 2020 12:26:26 AM\",\"phase-type\":\"COMPLETED\"}],\"queued-timeout-in-minutes\":480.0},\"current-phase\":\"COMPLETED\",\"current-phase-context\":\"[: ]\",\"version\":\"1\"},\"resources\":[\"arn:aws:codebuild:us-east-2:876557376893:build/ecs-devops-sandbox:d113f2e0-b017-4707-a20d-2fa92d469a3a\"],\"additionalAttributes\":{}}",
                "Timestamp": "2020-04-25T00:26:34.043Z",
                "SignatureVersion": "1",
                "Signature": "F2K+dgQ45C/kqUZydZTawkL7f6jst0hB6HWduHzc2GsMQJN8twpDrbIjtLClLj7i1CoYT5gtTdLpAoYy9UyZeG16ByY5n7SVDmzvVqnG2ssi4bR9+PTAjNo2o4GG0uB8FBwpcOPg5z+eA2R2YXhAVDKmABbTRI4ezqLyZMZKljk8/c+8cYUqQBiW5fZA9jBUoOuJmkRqrEDlB3/NNTGQRdP08OaRPMmthbPH4HlZwTPv8c4oGX6+NucTbtGMwcPXiXlE4OF3fIw7f+Sx5OgW5fFSvDzPkQivlYJg5d7g2gWx8XK7Md4i+CHOPIBZwXjV9lFNH2fu6fUyI4GXLHNOtQ==",
                "SigningCertUrl": "https://sns.us-east-2.amazonaws.com/SimpleNotificationService-a86cb10b4e1f29c941702d737128f7b6.pem",
                "UnsubscribeUrl": "https://sns.us-east-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-2:876557376893:codestar-notifications-to-teams:326cf852-0c29-416e-8e2b-395666db58ed",
                "MessageAttributes": {}
            }
        }
    ]
}

teams_webhook_url = "https://outlook.office.com/webhook/387c2f0b-1220-4955-a2dd-3bac12ab4e1d@169ea2cd-9387-4a99-b50f-39148dd63fdf/IncomingWebhook/58cdf3357b344db0adf29e7de2c95334/cb29463c-3526-4041-bab7-c8373b5a79dd"

outgoing_message="""{
  "@type": "MessageCard", 
  "@context": "http://schema.org/extensions", 
  "themeColor": "#CEDB56", 
  "summary": "[build [ecs-devops-sandbox] notification](https://console.aws.amazon.com/codesuite/codebuild/projects/ecs-devops-sandbox/build/ecs-devops-sandbox:d113f2e0-b017-4707-a20d-2fa92d469a3a/log?region=us-east-2", 
  "sections": [
     {
       "activityTitle": "[build [ecs-devops-sandbox] notification](https://console.aws.amazon.com/codesuite/codebuild/projects/ecs-devops-sandbox/build/ecs-devops-sandbox:d113f2e0-b017-4707-a20d-2fa92d469a3a/log?region=us-east-2", 
       "activitySubtitle": "On project[ecs-devops-sandbox]", 
       "activityImage": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4QBmRXhpZgAATU0AKgAAAAgABAEaAAUAAAABAAAAPgEbAAUAAAABAAAARgEoAAMAAAABAAIAAAExAAIAAAAQAAAATgAAAAAAAABgAAAAAQAAAGAAAAABcGFpbnQubmV0IDQuMi44AP/bAEMABgQFBgUEBgYFBgcHBggKEAoKCQkKFA4PDBAXFBgYFxQWFhodJR8aGyMcFhYgLCAjJicpKikZHy0wLSgwJSgpKP/bAEMBBwcHCggKEwoKEygaFhooKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKP/AABEIACgAKAMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APpPxNr1n4e01ru9YnJ2xxr96RvQf414n4g8c61rErf6S9pbHgQ27FRj3PU/y9qPiPrT6x4nucNm2tWMEQB4wDyfxOfwxXL15levKUuWOx+d51nVXEVZUqUrQWmnXzJPPl8zf5sm/wDvbjmuk8P+Oda0eVf9Je7thwYbhiwx7HqP5e1cvXo/gXwXAbNtb8TBYrBU3xxSHaGH95vb0Hf+eVJTcvcPOy2GKq1ksNJp7t30S7vyPTfDOvWfiHTVu7JiMHbJG33o29D/AI0V494N1q20fxz/AMS1pRpV1L5GJTztJ+Un6H9M0V6VGrzx13PvspzNYyjeo1zRdn2fmvU5uz+zf21H/a/m/ZfO/f8AlfexnnFdx468FwCzXW/DIWWwZN8kUZ3BR/eX29R2/lgfEjRX0fxPc4XFtdMZ4iBxgnkfgc/hip/APjKbw7c/Z7rdLpkjfOnUxn+8v9R3rgjyxbpz+8+JoRoUalTBYyNrv4uqfR+hteAfBsKW39veJNsVlGvmRRS8Bh/fb29B3+nXF8feMpvEVz9ntd0WmRt8idDIf7zf0Hajx94ym8RXP2e13RaZG3yJ0Mh/vN/Qdq5CipUUVyQ2/MMbjadKn9Twfwfal1k/8uyJLbd9oi8v7+8bfrmiuk+G+ivrHie2yuba1YTykjjAPA/E4/DNFXQoOcb3OrJ8mqYyk6vNyq/3ntnibQbPxDprWl6pGDujkX70beo/wrxPxB4G1rR5W/0Z7u2HImt1LDHuOo/l70UV1V6UZrme59NnWV4fE03WmrSS3X6nN+RL5mzypN/93ac10nh/wNrWsSrm2e0tjyZrhSox7Dqf5e9FFcVClGcrM+SyfLqWMr8lW9ke2eGdBs/D2mraWSk5O6SRvvSN6n/CiiivUSSVkfo9OnClBU6askf/2Q==", 
       "facts": [
          {"name": "Status"}, 
          {"value": "SUCCEEDED"}, 
          {"name": "Date"}, 
          {"value": "Apr 25, 2020 12:25:32 AM"}, 
          {"name": "Source Branch"}, 
          {"value": "[master](https://github.com/Covert-Operations/aws_codebuild_test/tree/master)"}, 
          {"name": "Target Env"}, 
          {"value": "default_build"}, 
          {"name": "Build Finished?"}, 
          {"name": true}
          ], 
         "markdown": true
  }
 ]
}
"""


simple_card = """
{
    "@context": "https://schema.org/extensions",
    "@type": "MessageCard",
    "potentialAction": [
        {
            "@type": "OpenUri",
            "name": "View All Tweets",
            "targets": [
                {
                    "os": "default",
                    "uri": "https://twitter.com/search?q=%23MicrosoftTeams"
                }
            ]
        }
    ],
    "sections": [
        {
            "facts": [
                {
                    "name": "Tweet:",
                    "value": "1. Numbered\r2. List\r"
                }
            ],
            "text": "A tweet with #MicrosoftTeams has been posted:"
        }
    ],
    "summary": "Tweet Posted",
    "themeColor": "0072C6",
    "title": "Tweet Posted"
}
"""
