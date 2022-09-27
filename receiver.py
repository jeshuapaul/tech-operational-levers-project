import boto3

def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    buckets = [bucket.name for bucket in s3.buckets.all()]
    print(buckets)

lambda_handler("event", "context")
