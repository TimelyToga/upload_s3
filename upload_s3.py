from boto.s3.key import Key
from boto.s3.connection import S3Connection
import sys
import string
import random
import webbrowser


def create_url(bucket, key):
  if not bucket or not key:
    return None
  return 'https://%s.s3.amazonaws.com/%s' % (bucket, key)

def gen_hash():
	lst = [random.choice(string.ascii_letters + string.digits) for n in xrange(12)]
	str = "".join(lst)
	return str

if(len(sys.argv) == 1):
	print """
		upload_s3.py usage: python upload_s3.py <filename> [file_extension or file_key]

		Specify at least a file to upload. 

		You may also specify a file extension, or a key. If an extension is specified 
		(any string that starts with a "."), then a key will be generated and appended.
		If a key is not specified, then a 12 character one will be randomly generated and used.

		"""

	sys.exit()

# AWS ACCESS DETAILS
AWS_ACCESS_KEY_ID = '<AWS_ACCESS_KEY_ID>'
AWS_SECRET_ACCESS_KEY = '<AWS_SECRET_ACCESS_KEY>'
BUCKET = '<BUCKET_NAME>'

# Generate key or use one specified
if len(sys.argv) >= 3:
	filename = sys.argv[2]
	if(filename.startswith(".")):
		KEY = gen_hash + filename
	else: 
		KEY = filename
else:
	KEY = gen_hash()
print "Hash: " + KEY

conn = S3Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
print "connection made"

b = conn.get_bucket(BUCKET)
print "Gotten reference to bucket named " + BUCKET

uploadfile = sys.argv[1]
print "Uploading " + uploadfile

k = Key(b)
k.key = KEY
k.set_contents_from_filename(uploadfile)
print "Uploaded file"
k.make_public()
print "File public"

# Display URL where file has been uploaded
URL = create_url(BUCKET, KEY)
print URL
print "All done."

# Open the file in the webbrowser
webbrowser.open(URL)
