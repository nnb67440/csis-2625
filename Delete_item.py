import boto3
# Get the service resource.
dydb = boto3.resource('dynamodb')
# Instantiate a table resource object
table = dydb.Table('users')
# delete the item using DynamoDB.Table.delete_item()
table.delete_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)

# Print out items in the table.
print(table.item_count)
