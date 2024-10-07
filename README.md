# Social Media Hashtag Trend Analyzer Application

### Technology used : Python, SQL , AWS Lambda , Dynamodb,  Streamlit

### Problem Statement:
In today's world of social media, users seek platforms that provide smooth posting experiences and insights into trending topics. To meet this demand, we plan to create a Streamlit application that enables users to easily compose and publish posts, similar to popular social media platforms. This app will leverage AWS Lambda and DynamoDB for efficient post processing and hashtag analysis.

### What we are doing here?
- Build a simple social Media app with streamlit through which users can post with suitable Hashtags
- The post will be triggered a lambda function in the back-end and stores it to DynamoDB (A NoSQL DB)
- Then we analyze the all the hashtags from all the post and Rank them and find which Hashtags are treanding
- After that the trending Hashtags will be displayed in our Streamlit socialmedia App.

### Features:

Post Composition: Users can write posts containing text and hashtags using the provided interface.

Post Submission: Upon clicking the "Post" button, the application will trigger a backend process sending the post content to AWS Lambda.

AWS Lambda Integration: AWS Lambda will receive the post content and parse it, extracting hashtags and post text. It will then store this data in DynamoDB.

Trending Hashtags: Users can view trending hashtags by clicking the "Show Trending Hashtags" button. This action triggers an analysis of the DynamoDB table to aggregate and identify popular hashtags.

Dynamic Updates: The trending hashtags section will dynamically update as new posts are made and analyzed, providing real-time insights into trending topics.

User Interface: The application will have an intuitive and user-friendly interface, making it easy for users to compose posts and explore trending hashtags.



