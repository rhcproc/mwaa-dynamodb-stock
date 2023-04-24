from pydantic import BaseSettings
from airflow.models import Variable
from dotenv import load_dotenv
import json
import boto3
import os


load_dotenv(verbose=True)


if os.environ.get('AIRFLOW_ENV') == 'local':
    aws_access_key_id = os.environ['S3_AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['S3_AWS_SECRET_ACCESS_KEY']
else:
    aws_access_key_id = Variable.get("S3_AWS_ACCESS_KEY_ID")
    aws_secret_access_key = Variable.get("S3_AWS_SECRET_ACCESS_KEY")

s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key
                  )


response = s3.get_object(Bucket='xx-config',
                         Key='xx-xx.json')
_content = response['Body'].read().decode('utf-8')
content = json.loads(_content)
for k, v in content.items():
    os.environ[k] = str(v)


class Settings(BaseSettings):
    dynamodb_table_name: str
    dynamodb_partition_key: str
    dynamodb_region: str
    dynamodb_access_key_id: str
    dynamodb_secret_access_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
