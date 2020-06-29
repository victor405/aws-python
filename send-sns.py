import boto3

def send_sns(arn, sub, msg):
	sns = boto3.client('sns')
	sns.publish(TargetArn=arn,Subject=sub,Message=msg)

def lambda_handler(event, context):
    arn = 'arn:aws:sns:us-east-1:<AWS_ACCOUNT_NUMBER>:SelfNotifications'
    sub = 'Go To Sleep'
    msg = 'You should go to Sleep.'

    send_sns(arn, sub, msg)