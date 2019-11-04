import boto3

session =boto3.Session(profile_name="aws_root")

def get_client():
    s=session.resource('s3')
    return s

def list_s3_buckets():

    s= get_client()

    for bucket in s.buckets.all():
        print(bucket.name)

def list_s3_objects(bucket):

    s= get_client()
    bucket = s.Bucket(bucket)
    ob=[]

    for o in bucket.objects.all():
        ob.append(o.key)
    return (ob)

def put_object_to_s3(key,body):
    s = get_client()
    #s.Bucket('ayush-third-bucket').put_object(Key='beta2', Body='beta2file')
    s.Bucket('ayush-third-bucket').put_object(Key=key, Body=body)
    return(key)

list_s3_objects('ayush-third-bucket')
#put_object_to_s3('beta3','beta3file')