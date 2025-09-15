import boto3
import os
from dotenv import load_dotenv

AWS_REGION = os.getenv("AWS_REGION")
AWS_KEY_ID = os.getenv("AWS_KEY_ID")
AWS_SECRET = os.getenv("AWS_SECRET")

dynamo = boto3.resource("dynamodb", 
                    region_name = AWS_REGION, 
                    aws_access_key_id = AWS_KEY_ID,
                    aws_secret_access_key = AWS_SECRET)

table = dynamo.Table("QuoteWeb")


