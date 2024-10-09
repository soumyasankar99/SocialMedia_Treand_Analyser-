import streamlit as st
import boto3
import uuid
import json
import re
from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd


# Set the theme for the UI with warm-tone colors
st.set_page_config(page_title="Trendy Talks", layout="wide")
st.markdown(
    """
    <style>
    .main {
        background-color: #FFF3E0;  /* Light orange background */
    }
    h1, h2, h3, h4 {
        color: #2E7D32;  /* Dark green for headings */
        font-weight: bold;
    }
    .stTextInput, .stTextArea, .stButton>button {
        background-color: #FFCC80 !important;  /* Light orange for inputs/buttons */
        color: #000000 !important;  /* Dark text for high contrast */
        border: none;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #4CAF50 !important;  /* Green hover effect for buttons */
        color: white !important;
    }
    .stMarkdown {
        color: #424242 !important;  /* Dark gray for post content */
    }
    .stSlider>div>div>div {
        background-color: #4CAF50 !important;  /* Green for slider */
    }
    .stSlider label {
        color: #2E7D32 !important;  /* Green slider labels */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Define the AWS region and credentials
AWS_REGION = 'us-east-1'
AWS_ACC_KEY_ID = '----'
AWS_SEC_ACC_KEY = '----'

# Initialize Lambda client
lambda_client = boto3.client(
    'lambda',
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACC_KEY_ID,
    aws_secret_access_key=AWS_SEC_ACC_KEY
)

# Function to extract hashtags from content
def extract_hashtags(content):
    return re.findall(r"#(\w+)", content)

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
st.title("Trendy Talks")

content = st.text_area("Write your Thoughts!")
if st.button("Post"):
    post_id = str(uuid.uuid4())
    hashtags = extract_hashtags(content)  # Automatically extract hashtags from content
    response_payload = invoke_lambda(post_id, content, hashtags)
    st.write(response_payload['body'])

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION, aws_access_key_id=AWS_ACC_KEY_ID,
                          aws_secret_access_key=AWS_SEC_ACC_KEY)
table = dynamodb.Table('SocialMediaPosts')

# Function to get top 5 trending hashtags
def get_trending_hashtags():
    response = table.scan()
    items = response['Items']
    hashtag_list = []
    for item in items:
        hashtags = item.get('Hashtags', [])
        if isinstance(hashtags, str):
            hashtags = re.findall(r"#(\w+)", hashtags)  # Handle string case
        hashtag_list.extend([hashtag.strip().lower() for hashtag in hashtags])
    
    trending_hashtags = Counter(hashtag_list).most_common(5)  # Top 5 hashtags
    return trending_hashtags

# Display top 5 trending hashtags
st.subheader("Top 5 Trending Hashtags")
trending_hashtags = get_trending_hashtags()

# Create a dynamically sized bar chart for the trending hashtags
if trending_hashtags:
    hashtags, counts = zip(*trending_hashtags)
    df = pd.DataFrame({'Hashtags': hashtags, 'Count': counts})
    
    # Allow user to adjust bar plot size
    bar_width = st.slider('Adjust Bar Plot Width', min_value=5, max_value=15, value=10)
    bar_height = st.slider('Adjust Bar Plot Height', min_value=3, max_value=10, value=5)
    
    # Plot the dynamic bar chart
    fig, ax = plt.subplots(figsize=(bar_width, bar_height))  # Dynamic plot size
    ax.barh(df['Hashtags'], df['Count'], color='#FF6F61')  # Use warm-tone bar color
    ax.set_xlabel("Count")
    ax.set_ylabel("Hashtags")
    ax.set_title("Top 5 Trending Hashtags")
    st.pyplot(fig)
else:
    st.write("No trending hashtags available.")

# Display all posts
st.subheader("Posts")
response = table.scan()
posts = response['Items']
for post in posts:
    st.write(f"**{post['Timestamp']}**")
    st.write(post['Content'])
    st.write(f"Hashtags: {post['Hashtags']}")
    st.write("---")


