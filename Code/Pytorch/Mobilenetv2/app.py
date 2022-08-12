import torch
import torchvision
import json
import numpy as np
import time
import torchvision
from torchvision import transforms
from PIL import Image
import boto3


# Preprocessing steps for the image
transform = transforms.Compose([transforms.Resize(256),transforms.CenterCrop(224),transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])])

tic = time.perf_counter()
model_file = '/opt/ml/model'
model = torch.jit.load(model_file)
# Put model in evaluation mode for inferencing
model.eval()
toc = time.perf_counter()



categories= np.array(open('label/ImageNetLabels.txt').read().splitlines())
s3 = boto3.resource('s3')


def lambda_handler(event, context):
  bucket_name = event['Records'][0]['s3']['bucket']['name']
  key = event['Records'][0]['s3']['object']['key']

  img = readImageFromBucket(key, bucket_name)
  input_tensor = transform(img)
  input_batch = input_tensor.unsqueeze(0)

  with torch.no_grad():
    output = model(input_batch)
#print(output[0])
  probabilities = torch.nn.functional.softmax(output[0], dim=0)

  tic = time.perf_counter()
  top5_prob, top5_catid = torch.topk(probabilities,5)
  for i in range(top5_prob.size(0)):
    print(categories[top5_catid[i]], top5_prob[i].item())
  toc = time.perf_counter()
  print(f"Time for prediction is {toc - tic:0.4f} seconds")

def readImageFromBucket(key, bucket_name):
  bucket = s3.Bucket(bucket_name)
  object = bucket.Object(key)
  response = object.get()
  return Image.open(response['Body'])