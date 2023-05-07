# Mobile ChatGPT - California Driver’s Handbook & Aid

**Student Name:** Bhavya Hegde <br>
**Student ID:** 016605029 <br>
**Course:** Smartphone Application Development <br>
## Learning Objective

Integration of ChatGPT trained models on the Android Mobile Application!
It's a synonym in today's enterprise web technologies the use of ChatGPT with customer satisfaction and customer aid. The purpose of the assignment is to create a ChatGPT model that trains driving rule book from California Driver’s Handbook, 2023.  <br>


## Tools and Technologies used
Frontend: Java based Android app<br/>
Backend API : Python Django framework<br/>
AWS component: EC2

## Implementation
### Step 1 : Extract the data 
The data was extracted from CA driver's handbook and converted to txt file
### Step 2 : Clean and normalize the data
Using Regex the data was cleaned and removed all the non alpha numeric charcters along with white spaces and empty lines
### Step 3 : Process the data
Once the data is ready its saved as manual.txt on EC2 instance the referrence manual.txt is uploaded here
then using the text splitter.py script the data is processed in chunks and the output is saved under training_txt folder
###  Step 4: Backend API Implementation
This project is a Django-based API endpoint for question-answering using language embeddings and vector stores.This API endpoint allows users to send a question as a POST request and receive a JSON response with the answer. The question is processed using language embeddings and a vector store, which enables accurate question-answering.
Spinned up a EC2 instance created a virtual environment  and installed all the required dependecies for the as listed in requirements.txt and created a django project
Model is trained under the code in views.py and response is rendered using API endpoint `api/endpoint`. Replace the API Key with your own API key to make this project work.
### Step 5 : FrontEnd Implementation
Android chat application allows users to ask questions related to the California drivers manual. It sends the user's question to a backend API endpoint, which runs a model trained specifically to answer questions related to the manual. If the question is related to the manual, the chatbot will provide a response. However, if the question is unrelated or unknown, the chatbot will respond with "I don't know."







