import os
import requests

'''
List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
Hint: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.
'''
dir = "/data/feedback/"
for file in os.listdir(dir): 
    '''
    You should now have a list that contains all of the feedback files from the path /data/feedback. 
    Traverse over each file and, from the contents of these text files, create a dictionary by keeping title, name, date, and feedback as keys for the content value, respectively.
    '''
    format = ["title","name","date","feedback"]

    '''
    Now, you need to have a dictionary with keys and their respective values (content from feedback files). 
    This will be uploaded through the Django REST API.
    '''
    content = {}
    
    # Open each file in read mode and read all lines into a list.
    with open(os.path.join(dir, file), 'r') as txtfile:
        for index, line in enumerate(txtfile):
            line = line.strip() # Remove leading/trailing whitespace
            content[format[index]] = line # Add line to dictionary

    print(content)
    
    '''
    Use the Python requests module to post the dictionary to the company's website. 
    Use the request.post() method to make a POST request to http://<corpweb-external-IP>/feedback. 
    Replace <corpweb-external-IP> with corpweb's external IP address.
    '''
    response = requests.post("http://34.73.151.136/feedback/",json = content)

    '''
    You can print the status_code and text of the response objects to check out what's going on. 
    You can also use the response status_code 201 for created success status response code that indicates the request has succeeded.
    '''
    # Check the response status code
    if response.status_code == 201:
        print(f"Feedback successfully posted: {content['title']}")
    else:
        print(f"Failed to post feedback: {content['title']}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")