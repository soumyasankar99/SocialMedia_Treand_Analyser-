# Social Media Hashtag Trend Analyzer Application

### Overview
The **Social Media Hashtag Trend Analyzer** is a Streamlit-based application that allows users to compose and publish posts containing text and hashtags. The application integrates with AWS Lambda for backend processing and DynamoDB for storing and analyzing hashtag trends. It enables users to gain insights into trending hashtags in real-time, offering a seamless social media posting experience.

### Technology Stack
- **Python**
- **SQL**
- **AWS Lambda**
- **DynamoDB**
- **Streamlit**

---

### Problem Statement
In today's fast-paced world of social media, users need platforms that not only allow smooth posting but also offer insights into what’s trending. This project aims to fulfill this need by creating an application that enables users to:
- Compose and publish posts with hashtags.
- Analyze hashtag usage across posts.
- Display trending hashtags in real-time.

---
### Data Pipeline:
![Social Media Trend analyzer Project](https://github.com/user-attachments/assets/578e5824-c2f3-44d0-8a88-95d150aa408c)


### Features

1. **Post Composition**  
   Users can write posts with suitable hashtags using a simple interface.

2. **Post Submission**  
   Upon clicking the "Post" button, the post content is sent to AWS Lambda for backend processing.

3. **AWS Lambda Integration**  
   AWS Lambda handles the post processing, extracting hashtags and saving the data in DynamoDB.

4. **Hashtag Analysis**  
   The application analyzes hashtags from all posts stored in DynamoDB and ranks them to identify which ones are trending.

5. **Trending Hashtags Display**  
   Users can view trending hashtags by clicking the "Show Trending Hashtags" button. The results are dynamically updated based on real-time data from DynamoDB.

6. **Real-time Updates**  
   The trending section updates as new posts are made, providing real-time insights into the most popular hashtags.

---
### IAM Setup Guidelines:
![Social Media Trend analyzer Project](https://github.com/user-attachments/assets/917e46bb-70bf-4357-8e60-479839fee295)

![Social Media Trend analyzer Project (1)](https://github.com/user-attachments/assets/80cd0634-bb1f-477f-a66c-ad1fb4675c78)

### Required Setups:
![Social Media Trend analyzer Project (2)](https://github.com/user-attachments/assets/d8541149-aeaf-40f3-a2a0-d7046e481c8c)


### Architecture Overview

1. **Frontend (Streamlit)**:  
   Provides a user-friendly interface for post composition and viewing trending hashtags.
   <img width="958" alt="TrendyTalks-1" src="https://github.com/user-attachments/assets/5e66fcb0-6b2f-4ce2-8588-5fe896ed5788">

2. **Backend (AWS Lambda)**:  
   Triggered when a user submits a post. It processes the post and stores the extracted data in DynamoDB.

3. **Storage (DynamoDB)**:  
   Stores post content and hashtags in a scalable NoSQL database.
<img width="959" alt="TrendyDynamoDB-1" src="https://github.com/user-attachments/assets/9b971d5e-a982-445d-aa25-f1ab170f8793">

<img width="959" alt="TrendyDynamoDB-2" src="https://github.com/user-attachments/assets/941a0add-27a2-48b1-b4a6-f0771505e517">

<img width="959" alt="TrendyDynamoDB-3" src="https://github.com/user-attachments/assets/890b6b53-f437-4169-9640-098f8872a61b">

<img width="959" alt="TrendyDynamoDB-4" src="https://github.com/user-attachments/assets/66883665-bdac-4101-bdc2-1c37a452084d">

4. **Trending Analysis**:  
   Hashtags are aggregated and ranked based on their frequency in the database, and the trending hashtags are displayed in real-time.
<img width="959" alt="TrendyTalk-2" src="https://github.com/user-attachments/assets/019a4579-0596-4db2-a23b-67c19334a0f4">

---

### Installation and Setup

To run this application locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/soumyasankar99/Dynamic-data-integration---storage-with-HDFS.git
   
2. **Run the Program:**
   ```bash
   streamlit run streamlit_app.py
