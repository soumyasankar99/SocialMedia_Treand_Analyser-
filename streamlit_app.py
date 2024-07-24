import streamlit as st
import boto3
import uuid
import json
from collections import Counter

# Define the AWS region
AWS_REGION = 'eu-north-1'  # Replace with your AWS region

# Initialize Lambda client
lambda_client = boto3.client('lambda', region_name=AWS_REGION)

# Function to invoke the Lambda function
def invoke_lambda(post_id, content, hashtags):
    response = lambda_client.invoke(
        FunctionName='StorePostFunction',  
        InvocationType='RequestResponse',
        Payload=json.dumps({
            'post_id': post_id,
            'content': content,
            'hashtags': hashtags
        })
    )
    response_payload = json.load(response['Payload'])
    return response_payload

# Streamlit app layout
st.title("Social Media App")

content = st.text_area("Write your post here")
hashtags = st.text_input("Enter hashtags separated by commas")
if st.button("Post"):
    post_id = str(uuid.uuid4())
    response_payload = invoke_lambda(post_id, content, hashtags)
    st.write(response_payload['body'])

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
table = dynamodb.Table('SocialMediaPosts')

# Function to get trending hashtag
def get_trending_hashtag():
    response = table.scan()
    items = response['Items']
    hashtag_list = []
    for item in items:
        hashtags = item['Hashtags'].split(',')
        hashtag_list.extend([hashtag.strip() for hashtag in hashtags])
    trending_hashtag = Counter(hashtag_list).most_common(1)
    return trending_hashtag[0] if trending_hashtag else ("No hashtags", 0)

# Display trending hashtag
trending_hashtag, count = get_trending_hashtag()
st.subheader(f"Trending Hashtag: {trending_hashtag} (used {count} times)")

# Display all posts
st.subheader("Posts")
response = table.scan()
posts = response['Items']
for post in posts:
    st.write(f"**{post['Timestamp']}**")
    st.write(post['Content'])
    st.write(f"Hashtags: {post['Hashtags']}")
    st.write("---")

