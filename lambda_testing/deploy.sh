#!/usr/bin/env bash
set -x

cd package
zip -r9 ${OLDPWD}/function.zip .
cd ..
zip -g function.zip pushCBSNStoTeams.py
aws lambda update-function-code --function-name updateTeamsOnBuild --zip-file fileb://~/work/covert_consulting/aws_codebuild_test/lambda_testing/function.zip --profile lambdadev

