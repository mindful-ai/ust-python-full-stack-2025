import boto3
from botocore.exceptions import ClientError

# Create DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')

# ---------- 1. CREATE TABLE ----------
def create_table():
    try:
        table = dynamodb.create_table(
            TableName='Users',
            KeySchema=[
                {'AttributeName': 'user_id', 'KeyType': 'HASH'}  # Partition key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'user_id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
        print("✅ Table created successfully!")
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            print("⚠️ Table already exists.")
        else:
            print("Error:", e)


# ---------- 2. CREATE (INSERT ITEM) ----------
def insert_item(user_id, name, age):
    table = dynamodb.Table('Users')
    table.put_item(
        Item={
            'user_id': user_id,
            'name': name,
            'age': age
        }
    )
    print(f"✅ Inserted user {user_id}")


# ---------- 3. READ ITEM ----------
def get_item(user_id):
    table = dynamodb.Table('Users')
    response = table.get_item(Key={'user_id': user_id})
    item = response.get('Item')
    if item:
        print(f"📖 Retrieved: {item}")
    else:
        print("❌ Item not found")


# ---------- 4. UPDATE ITEM ----------
def update_item(user_id, new_age):
    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={'user_id': user_id},
        UpdateExpression="set age = :a",
        ExpressionAttributeValues={':a': new_age},
        ReturnValues="UPDATED_NEW"
    )
    print(f"🔄 Updated: {response['Attributes']}")


# ---------- 5. DELETE ITEM ----------
def delete_item(user_id):
    table = dynamodb.Table('Users')
    table.delete_item(Key={'user_id': user_id})
    print(f"🗑️ Deleted user {user_id}")


# ---------- Run Demo ----------
if __name__ == "__main__":
    create_table()

    # Create
    insert_item("u1", "Alice", 25)
    insert_item("u2", "Bob", 30)

    # Read
    get_item("u1")

    # Update
    update_item("u1", 28)

    # Read again to confirm update
    get_item("u1")

    # Delete
    delete_item("u2")

    # Try reading deleted item
    get_item("u2")