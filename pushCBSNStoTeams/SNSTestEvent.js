{
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
              "build-complete": false,
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
                "privileged-mode": false,
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

