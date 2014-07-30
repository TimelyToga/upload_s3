upload_s3
=========

A simple python script that uploads a file to a s3 bucket under a randomly generated key, randomly generated key with a specified extension, or under a given key (optionally with an extension).

Place AWS access credentials in the following lines. Make sure to specify a valid bucket name.

```python
  # AWS ACCESS DETAILS
  AWS_ACCESS_KEY_ID = '<AWS_ACCESS_KEY_ID>'
  AWS_SECRET_ACCESS_KEY = '<AWS_SECRET_ACCESS_KEY>'
  BUCKET = '<BUCKET_NAME>'
```

# Usuage
upload_s3.py usage: 
`python upload_s3.py <filename> [file_extension or file_key]`


*        `filename` is the path to the file to upload [REQUIRED]
*        `file_extension` is a string that specifies any valid file extension (starts with a '.') {OPTIONAL}
*        `file_key` is the key that the file will be stored in s3 under {OPTIONAL}

# Requirements

The only third party dependency for this script is the boto library. To get boto use the following command:

`pip install boto`

[Boto Documentation](http://boto.readthedocs.org/en/latest/getting_started.html)
