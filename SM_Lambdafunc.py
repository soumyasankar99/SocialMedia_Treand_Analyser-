import json
import boto3
from datetime import datetime
from uuid import uuid4

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SocialMediaPosts')

def lambda_handler(event, context):
    # Parse the event for post content and hashtags
    content = event['content']
    hashtags = event['hashtags']
    
    # Create a unique post ID
    post_id = str(uuid4())
    
    # Put item in DynamoDB table
    table.put_item(
        Item={
            'PostID': post_id,
            'Content': content,
            'Hashtags': hashtags,
            'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Post added successfully!')
    }
