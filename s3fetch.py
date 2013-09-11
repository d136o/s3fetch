import argparse
import boto
from boto.s3.connection import S3Connection
import boto.s3.key

import sys


def s3fetch(s3bucket, s3key, aws_access_key, aws_secret_key, output_filename):
    
    connection = S3Connection(aws_access_key,aws_secret_key)
    bucket = connection.lookup(s3bucket)
    if bucket is None:
        print 'bucket does not exist, may be cause by incorrect credentials'
        return 1

    key = boto.s3.key.Key(bucket, s3key)
    if not key.exists():
        print 'key does not exist within given bucket'
        return 1
        
    key.get_contents_to_filename(output_filename)
    
    return 0


def main(argv=None):
    
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser()
    parser.add_argument('s3bucket')
    parser.add_argument('s3key')
    parser.add_argument('aws_access_key')
    parser.add_argument('aws_secret_key')
    parser.add_argument('output_filename')
    
    args = parser.parse_args(argv[1:])
    
    print args

    return s3fetch(args.s3bucket,
                   args.s3key,
                   args.aws_access_key,
                   args.aws_secret_key,
                   args.output_filename)
    
    

if __name__ == '__main__':
    sys.exit(main())
    
    
