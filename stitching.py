# import the necessary packages
from panorama import Stitcher
import cv2
import boto3

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL': 'public-read'})
    except ClientError as e:
        logging.error(e)
        return False
    return True

def get_object(bucket_name, object_name):
    """Retrieve an object from an Amazon S3 bucket

    :param bucket_name: string
    :param object_name: string
    :return: botocore.response.StreamingBody object. If error, return None.
    """

    # Retrieve the object
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_name)
    except ClientError as e:
        # AllAccessDisabled error == bucket or object not found
        logging.error(e)
        return None
    # Return an open StreamingBody object
    return response['Body']


boto3.resource('s3').Bucket('pro-drone').download_file('04.png', '/tmp/04.jpg')
          
imageA = cv2.imread('/tmp/04.jpg')

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
# imageA = cv2.imread('images/04.png')
imageB = cv2.imread('images/05.png')
# imageA = imutils.resize(imageA, width=400)
# imageB = imutils.resize(imageB, width=400)
# imageC = imutils.resize(imageB, width=400)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
# cv2.imshow('Image A', imageA)
# cv2.imshow('Image B', imageB)
# cv2.imshow('Keypoint Matches', vis)


cv2.imwrite('images/result.png', result)

s3 = boto3.client('s3')
with open('images/result.png', 'rb') as f:
    s3.upload_fileobj(f, 'pro-drone', 'result.png')
    
cv2.imshow('Result', result)
cv2.waitKey(0)
