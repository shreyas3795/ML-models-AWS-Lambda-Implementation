FROM public.ecr.aws/lambda/python:3.8

COPY app.py requirements.txt ./
COPY model /opt/ml/model

RUN mkdir label
RUN curl https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt -o ./label/ImageNetLabels.txt

RUN python3.8 -m pip install -r requirements.txt -t .

# Download ImageNet labels


CMD ["app.lambda_handler"]
