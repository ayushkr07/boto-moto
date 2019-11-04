import boto3
from moto import mock_s3
from testproject.mycode import get_client,list_s3_buckets,list_s3_objects,put_object_to_s3
import unittest


class S3TestCase(unittest.TestCase):

    def setUp(self):
        """
        setUp will run before execution of each test case
        """
        self.key = 'style.css'
        self.value = 'value'
        self.bucket='bucket'


    @mock_s3
    def test_list_s3_objects(self):
        s3=get_client()
        s3.create_bucket(Bucket=self.bucket,
                                  CreateBucketConfiguration={
                                      'LocationConstraint': 'ap-south-1'})
        s3.Bucket(self.bucket).put_object(Key=self.key, Body=self.value)
        res=list_s3_objects(self.bucket)
        self.assertTrue(self.key in res)





