import boto3
dydb = boto3.resource('dynamodb')
print(list(dydb.tables.all()))