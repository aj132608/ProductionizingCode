import os
import boto3


def get_s3_resource(endpoint: str = None,
                    access_id: str = None,
                    access_secret: str = None,
                    region: str = None):
    """
    This function returns a boto3 resource object for
    s3
    :param region:
    :param endpoint: Endpoint of storage
    :param access_id: Creds ID
    :param access_secret: Creds Secret
    :return s3_resource_obj: boto3 resource object
    """
    if not endpoint:
        endpoint = os.environ.get("STORAGE_ENDPOINT")
        if endpoint:
            endpoint = os.path.expandvars(endpoint)
    if not access_id:
        access_id = os.environ.get("AWS_ACCESS_KEY_ID")
        if access_id:
            access_id = os.path.expandvars(access_id)
    if not access_secret:
        access_secret = os.environ.get("AWS_SECRET_ACCESS_KEY")
        if access_secret:
            access_secret = os.path.expandvars(access_secret)
    if not region:
        region = os.environ.get("AWS_DEFAULT_REGION")
        if region:
            region = os.path.expandvars(region)

    s3_resource_obj = boto3.resource("s3", region_name=region,
                                     endpoint_url=endpoint,
                                     aws_access_key_id=access_id,
                                     aws_secret_access_key=access_secret)

    return s3_resource_obj


def get_s3_client(endpoint: str = None,
                  access_id: str = None,
                  access_secret: str = None,
                  region: str = None):
    """
    This function returns a boto3 client object for
    s3
    :param region:
    :param endpoint: Endpoint of storage
    :param access_id: Creds ID
    :param access_secret: Creds Secret
    :return s3_resource_obj: boto3 resource object
    """
    if not endpoint:
        endpoint = os.environ.get("STORAGE_ENDPOINT")
        if endpoint:
            endpoint = os.path.expandvars(endpoint)
    if not access_id:
        access_id = os.environ.get("AWS_ACCESS_KEY_ID")
        if access_id:
            access_id = os.path.expandvars(access_id)
    if not access_secret:
        access_secret = os.environ.get("AWS_SECRET_ACCESS_KEY")
        if access_secret:
            access_secret = os.path.expandvars(access_secret)
    if not region:
        region = os.environ.get("AWS_DEFAULT_REGION")
        if region:
            region = os.path.expandvars(region)

    s3_client_obj = boto3.client("s3", region_name=region,
                                 endpoint_url=endpoint,
                                 aws_access_key_id=access_id,
                                 aws_secret_access_key=access_secret)

    return s3_client_obj


def upload_file(bucket: str, key: str,
                filepath: str, endpoint: str = None,
                access_id: str = None,
                access_secret: str = None,
                region: str = None):
    """
    This function uploads a file to a specified bucket/key
    to S3 based object stores
    :param region:
    :param bucket: Name of bucket
    :param key: Path in the bucket
    :param filepath: Path to the file to upload
    :param endpoint: Endpoint of storage
    :param access_id: Creds ID
    :param access_secret: Creds Secret
    :return nothing:
    """
    # Get S3 Resource object
    s3_resource = get_s3_resource(endpoint,
                                  access_id,
                                  access_secret,
                                  region)
    # Get bucket names
    buckets = [bucket_on_s3.name for bucket_on_s3 in s3_resource.buckets.all()]

    if not bucket in buckets:
        s3_resource.create_bucket(Bucket=bucket)

    # Get S3 Client
    s3_client = get_s3_client(endpoint,
                              access_id,
                              access_secret,
                              region)

    s3_client.upload_file(filepath,
                          bucket,
                          key)


def recursive_upload(bucket: str, key: str,
                     local_folder_path: str, endpoint: str = None,
                     access_id: str = None,
                     access_secret: str = None,
                     region: str = None):
    """
    This function recursively uploads a folder to a specified bucket/key
    to S3 based object stores
    :param region:
    :param bucket: Name of bucket
    :param key: Path in the bucket
    :param local_folder_path: Path to the folder to upload
    :param endpoint: Endpoint of storage
    :param access_id: Creds ID
    :param access_secret: Creds Secret
    :return nothing:
    """
    # Get S3 Resource object
    s3_resource = get_s3_resource(endpoint,
                                  access_id,
                                  access_secret,
                                  region)

    # Get bucket names
    buckets = [bucket_on_s3.name for bucket_on_s3 in s3_resource.buckets.all()]

    if not bucket in buckets:
        s3_resource.create_bucket(Bucket=bucket)

    # Get S3 Client
    s3_client = get_s3_client(endpoint,
                              access_id,
                              access_secret,
                              region)

    # Upload recursively
    for file_base_path, dir, files in os.walk(local_folder_path):
        for file in files:
            file_path = os.path.join(local_folder_path, file_base_path, file)
            upload_key = os.path.join(key, file_base_path.replace(local_folder_path, ''), file)
            s3_client.upload_file(file_path,
                                  bucket,
                                  upload_key)


def download(bucket: str, key: str,
             local_file_path: str, endpoint: str = None,
             access_id: str = None,
             access_secret: str = None,
             region: str = None):
    """
    This function downloads the file from a bucket.
    :param region:
    :param bucket: Bucket where the file is
    :param key: Path to the file on the bucket
    :param local_file_path: File path (including file name) where the file should
    be stored
    :param endpoint: Endpoint of storage
    :param access_id: Creds ID
    :param access_secret: Creds Secret
    :return nothing:
    """
    s3 = get_s3_client(endpoint,
                       access_id,
                       access_secret,
                       region)

    with open(local_file_path, 'wb') as f:
        s3.download_fileobj(bucket, key, f)


def list_bucket_files(bucket: str, key: str, endpoint: str = None,
                      access_id: str = None,
                      access_secret: str = None,
                      region: str = None):

    # Get S3 Resource object
    s3_resource = get_s3_resource(endpoint,
                                  access_id,
                                  access_secret,
                                  region)

    # Get bucket names
    desired_bucket = [bucket_on_s3 for bucket_on_s3 in s3_resource.buckets.all() if bucket_on_s3.name == bucket][0]
    files = [my_bucket_object.key for my_bucket_object in desired_bucket.objects.filter(Prefix=key)]

    return files
