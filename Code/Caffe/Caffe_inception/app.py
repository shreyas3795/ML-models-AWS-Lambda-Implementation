import json
import numpy as np
import time
from PIL import Image
import boto3
import cv2
import os
import botocore


nh,nw = 224,224
img_mean = (103.94, 116.78, 123.68) 

labels= np.array(open('label/ImageNetLabels.txt').read().splitlines())
s3 = boto3.resource('s3')


def lambda_handler(event, context):
  # defining s3 bucket object
  s3 = boto3.client("s3")
  bucket_name = "caffe-inception"
    # fetching object from bucket
  file_obj = s3.get_object(Bucket=bucket_name, Key="cat.jpeg")
    # reading the file content in bytes
  file_content = file_obj["Body"].read()

    # creating 1D array from bytes data range between[0,255]
  np_array = np.fromstring(file_content, np.uint8)
    # decoding array
  image_np = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

  tic = time.perf_counter()
  blob = cv2.dnn.blobFromImage(image_np, size=(nh, nw), mean=img_mean)
  net = cv2.dnn.readNetFromCaffe('/model/inception_v2_deploy.prototxt','/model/inception21k.caffemodel')
  toc = time.perf_counter()
  print(f"Time for prediction is {toc - tic:0.4f} seconds")


  tic = time.perf_counter()
  net.setInput(blob)
  pred = net.forward()
  print('Prediction: {0}'.format(labels[np.argmax(pred)]))
  toc = time.perf_counter()
  print(f"Time for prediction is {toc - tic:0.4f} seconds")
  

def readImageFromBucket(key, bucket_name):
  bucket = s3.Bucket(bucket_name)
  object = bucket.Object(key)
  response = object.get()
  return Image.open(response['Body'])