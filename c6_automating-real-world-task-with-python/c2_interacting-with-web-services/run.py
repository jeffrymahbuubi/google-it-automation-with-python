#! /usr/bin/env python3

import os
import requests

current_dir = os.path.dirname(os.path.abspath(__file__))

# Directory containing feedback files
feedback_dir = os.path.join(current_dir, "data", "feedback")

# List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
for file in os.listdir(feedback_dir):
    # Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
    format = ["title", "name", "date", "feedback"]

    # Now, you need to have a dictionary with keys and their respective values (content from feedback files). This will be uploaded through the Django REST API.
    feedback_data = {}

    # Open each file in read mode and read all lines into a list.
    with open(os.path.join(feedback_dir, file), 'r') as txtfile:
        for index, line in enumerate(txtfile):
            line = line.strip() # Remove leading/trailing whitespace
            feedback_data[format[index]] = line # Add line to dictionary
    
    # Define the URL of the Django REST API for posting feedback
    api_url = 'http://34.73.151.136//feedback'  # Replace with the actual URL
    
    # Make a POST request to the API with the feedback data
    response = requests.post(api_url, json=feedback_data)
    
    # Check the response status code
    if response.status_code == 201:
        print(f"Feedback successfully posted: {feedback_data['title']}")
    else:
        print(f"Failed to post feedback: {feedback_data['title']}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")
