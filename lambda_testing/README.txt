How to deploy the lambda_test (needs to be renamed now that it'll likely work) to the aws cloud.

pkg install zip # if you don't already have it installed
zip -r ../lambdatest.zip .
pkg install awscli

$ aws ec2 describe-instances --profile aspire
$ aws lambda list-functions --profile aspire 
$ aws lambda update-function-code --function-name updateTeamsOnBuild --zip-file fileb://~/work/covert_consulting/aws_codebuild_test/lambdatest.zip --profile lambdadev




###############3
trying again
############

For this example, go to the lambda page and create a new funciton. Under the edit area, the Handler info you need ot have the filename.name_handler 
of your function, so it can find what it needs to execute.


pip install boto3
cd lambda_testing
pip install --target ./package -r requirements.txt


## create an archive of the dependencies
cd package
zip -r9 ${OLDPWD}/function.zip .

## add your function to the archive
cd ..
zip -g function.zip pushCBSNStoTeams.py

# update the function code

$ aws lambda update-function-code --function-name updateTeamsOnBuild --zip-file fileb://~/work/covert_consulting/aws_codebuild_test/function.zip --profile lambdadev
