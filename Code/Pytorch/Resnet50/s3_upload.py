import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIA2DJVFUEBHPROMQVW'
SECRET_KEY = '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'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('/Users/shreyassetlurarun/Documents/SA_project/cats/cat.4006.jpg', 'pytorch-resnet50', 'cat9.jpg')
