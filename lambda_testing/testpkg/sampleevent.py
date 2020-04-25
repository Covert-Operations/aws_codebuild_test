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
