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
Other tools : Postman

## Implementation
### Step 1 : Extract the data 
The data was extracted from CA driver's handbook and converted to txt file
### Step 2 : Clean and normalize the data
Using Regex the data was cleaned and removed all the non alpha numeric charcters along with white spaces and empty lines
### Step 3 : Process the data
Once the data is ready its saved as manual.txt on EC2 instance the referrence manual.txt is uploaded here
then using the text splitter.py script the data is processed in chunks and the output is saved under training_txt folder
###  Step 4: Backend API Implementation
Django code sets up an API endpoint for a chatbot that is trained to respond to questions related to the California drivers manual. The model is trained using the langchain library, which utilizes OpenAI embeddings and a vector store. The training text documents are loaded from a specified directory and split into chunks for processing. The trained model, VectorDBQA, is created with the OpenAI language model and the vector store. When a POST request is made to the API endpoint with a question in the request body, the question is passed to the model, and the model generates a response. The response is returned as a JSON object from the API endpoint.<br>
Spinned up a EC2 instance created a virtual environment  and installed all the required dependecies for the as listed in requirements.txt and created a django project
Model is trained under the code in views.py and response is rendered using API endpoint `api/endpoint`. Replace the API Key with your own API key to make this project work.
### Step 5 : FrontEnd Implementation
Android chat application allows users to ask questions related to the California drivers manual. It sends the user's question to a backend API endpoint, which runs a model trained specifically to answer questions related to the manual. If the question is related to the manual, the chatbot will provide a response. However, if the question is unrelated or unknown, the chatbot will respond with "I don't know."

### Instructions to run the app: 
* Generate your openAI keys from https://platform.openai.com/account/api-keys
* Clone the repo 
* Clean , Extract, proocess and clean the data that you want to train using the steps given in Implementation 
* Spin up a EC2 instance and move the Backend code to EC2 . create a Virtual environment install the required dependencies. Replace API keys with the key you have generated in step 1
* Run the server and Test the reponse using API endpoint 
* Now run the app code in android studio to get the response.


### Architecture Diagram :

### API Response Screenshots:

Question related to CA driver's Manual:

![image](https://user-images.githubusercontent.com/85700971/236658300-324bd9ae-2220-4021-b73b-ff7dd0cc32f6.png)

Question that is not related to CA driver's Manual:

<img width="910" alt="image" src="https://user-images.githubusercontent.com/85700971/236658380-74741e4c-6b69-432f-a952-e250cb109e6b.png">


### App Screenshots:

![image](https://user-images.githubusercontent.com/85700971/236658458-17ff3725-a766-4838-9534-df2eab398527.png)

![image](https://user-images.githubusercontent.com/85700971/236658466-c02e9cc3-d6f4-43c7-afd4-5a359521501c.png)

![image](https://user-images.githubusercontent.com/85700971/236658469-321082a6-4bd3-4592-9e4a-e8fff171c15b.png)

![image](https://user-images.githubusercontent.com/85700971/236658473-159b69b1-4c49-463a-b9c4-f05efa15569e.png)














