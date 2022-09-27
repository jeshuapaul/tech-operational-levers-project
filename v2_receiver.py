import boto3
import sys

# What I want this script to be able to do is the following:
# ---> if there is only one argument, only search for the one.
# ---> if there are more than one added argument, search for them all.

def lambda_handler(event, context):
	s3 = boto3.resource('s3')
	buckets = [bucket.name for bucket in s3.buckets.all()]
	# The len(sys.argv) must be more than 2, because setting it to 1 won't work, because the script will always make it 1.
	print("Number of arguments:", len(sys.argv) - 1)
	print("----------------------")
	if ( (len(sys.argv) - 1) == 0 ):
		print("No arguments supplied, only the script name !")
	elif ( (len(sys.argv) - 1) == 1 ):
		for i in buckets:
			if str(sys.argv[1]) in i:
				print(i)
			else:
				pass
	elif ( (len(sys.argv) - 1) >= 2 ):
		for i in buckets:
			for a in sys.argv[1:]:
				if a in i:
					print(i)
				else:
					pass

lambda_handler("event", "context")


