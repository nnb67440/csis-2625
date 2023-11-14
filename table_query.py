import boto3
from boto3.dynamodb.conditions import Key, Attr
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('users')
# retrieve items in a table using DynamoDB.Table.query()
response = table.query(
                  KeyConditionExpression=Key('username').eq('janedoe')
                    )
items = response['Items']
print(items)