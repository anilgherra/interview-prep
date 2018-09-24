from botocore.exceptions import ClientError
import boto3
import uuid
import json
import os


def stream_put(env,stream_name, message):
    if env=="dev":
        region = "us-west-2"
        aws_access_key_id = "AKIAJ6QAR3AU54YRWDRA"
        aws_secret_access_key = "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"
    elif env=="stg":
        region = "us-west-2"
        aws_access_key_id = "AKIAJ6QAR3AU54YRWDRA"
        aws_secret_access_key = "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"
    elif env=="prd":
        region = "us-west-2"
        aws_access_key_id = "AKIAJ6QAR3AU54YRWDRA"
        aws_secret_access_key = "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"

    client = boto3.client("kinesis",aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key,region_name=region)
    try:
        res = client.put_record(StreamName=stream_name, Data=json.dumps(message), PartitionKey=str(uuid.uuid4()))

        if res["ResponseMetadata"]["HTTPStatusCode"] == 200:
            return "status 200: {} inserted!".format(stream_name)
        else:
            return "status !200: {} insert failed!!".format(stream_name)
    except ClientError as ce:
        print(ce)
    except Exception as e:
        print(e)
