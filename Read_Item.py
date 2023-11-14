import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('users')
# retrieve a table item using DynamoDB.Table.get_item()
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    })
# print(type(response))
# print(response)
item = response['Item']
print(item)