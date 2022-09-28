import boto3
import sys

# What I want this script to be able to do is the following:
# ---> if there is only one argument, only search for the one.
# ---> if there are more than one added argument, search for them all.

# Trying to make the script better again by removing the hardcoding for if there is one argument.

def lambda_handler(event, context):
	# Setting the "count" variable to 0 as it will be used later, when counting the amount of lines printed found from the arguments/buckets.
	count = 0
	s3 = boto3.resource('s3')
	buckets = [bucket.name for bucket in s3.buckets.all()]

# The len(sys.argv) must be more than 2 by default, because setting it to index 1 won't work, seeing that the script name will always be at index 1.
# I am using 0,1,2 because I've used (len(sys.argv) - 1), which takes the index of the argument(s) and goes back one index - making it more sensible (for me at least).
# ----- eg. -----
# sudo python3 script.py args1 args2
# Index number:  -0-      -1-   -2-
# Argument pos:  -1-      -2-   -3-

	if ( len(sys.argv) == 1 ):
		print("No arguments supplied - not sure which buckets to look for!")
		print("----------------------")
		user_input = input("List all buckets instead ? (y/n)\n")
		if user_input.lower() == "y":
			print("----------------------")
			print(buckets)
		else:
			print("----------------------")
			print("Ending script.")
			sys.exit()
	elif ( len(sys.argv) > 1 ):
		print("Amount of arguments:", len(sys.argv) - 1)
		print("----------------------")
		# listing buckets
		for i in buckets:
			# listing arguments
			for a in sys.argv[1:]:
				# if the bucket name contains what is in the argument
				if a in i:
					++count
					print(i)
				else:
					pass
		print("----------------------")
		print("Amount of buckets found:", count)

lambda_handler("event", "content")
