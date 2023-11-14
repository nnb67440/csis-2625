import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('users')
# retrieve all items in a table using DynamoDB.Table.scan()
response = table.scan()
# print(type(response))
# print(response)
items = response['Items']
print(items)