import boto3
import sys

def lambda_handler(event, context):
	s3 = boto3.resource('s3')
	buckets = [bucket.name for bucket in s3.buckets.all()]
	for i in buckets:
		if str(sys.argv[1]) and str(sys.argv[2]) in i:
			print(i)
		else:
			pass

lambda_handler("event", "context")

# This script works to output the info as Jordi requested, but it is kind of hardcoded to look for the first and second CLI argument that the user inputs. Going to
# try and make it better in v2_receiver.py.
