import boto3
import asyncio
import aioschedule as schedule
import time

start_time = time.time()
ACCESS_KEY = ''
SECRET_KEY = ''
trace_list = [12, 11, 11, 10, 10]

async def job(message='stuff', n=1):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    s3.upload_file('abc.jpg', 'pytorch-resnet50', 'cat1.jpg')
    print("Upload successful")
    print("--- %s seconds ---" % (time.time() - start_time))
    asyncio.sleep(1)

for i in trace_list:
    schedule.every(60).seconds.do(job, n=i)

loop = asyncio.get_event_loop()
while True:
    loop.run_until_complete(schedule.run_pending())
    time.sleep(0.1)
