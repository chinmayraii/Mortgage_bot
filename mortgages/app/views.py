# from django.shortcuts import render
# import openai
# import pandas as pd
# import os
# from . models import Mortgage
# from django.views.decorators.csrf import csrf_exempt
# import csv
# from django.http import JsonResponse


# openai.api_key = os.getenv('OPENAI_API_KEY')


# # Load mortgage data from CSV file
# mortgage_data = []
# with open('app\mort.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         mortgage_data.append(row)


# def index(request):
#     return render(request,'index.html')



# # Function to handle user requests
# def mortgage_chatbot(request):
#     # Get user input from the request
#     user_input = request.GET.get('input')

#     # Use OpenAI to generate a response
#     response = openai.Completion.create(
#         engine="text-davinci-003", 
#         prompt=user_input,
#         temperature=0.5,
#         max_tokens=100,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#     )

#     # Extract relevant data from mortgage_data based on the chatbot response
#     if "interest rate" in response.choices[0].text:
#         data = mortgage_data[0]
#     elif "monthly payment" in response.choices[0].text:
#         data = mortgage_data[1] 
#     elif "company" in response.choices[0].text:
#         data = mortgage_data[2]        
#     else:
#         data = {}

#     # Incorporate mortgage data into the chatbot response
#     response_text = response.choices[0].text
#     for key in data:
#         response_text = response_text.replace(key, data[key])

#     # Return the response as a JSON object
#     return JsonResponse({"response": response_text})



# import csv
# import random
# import openai
# import os

# # Load your OpenAI API credentials
# openai.api_key = os.getenv('OPENAI_API_KEY')

# # Load mortgage data from CSV file
# def load_data():
#     data = []
#     with open('app\mort.csv', 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip header row
#         for row in reader:
#             data.append(row)
#     return data

# # Generate a mixed response using OpenAI
# def generate_response(input_text):
#     response = openai.Completion.create(
#         engine='text-davinci-003',
#         prompt=input_text,
#         temperature=0.7,
#         max_tokens=50,
#         n=1,

#     )
#     return response.choices[0].text.strip()

# # Main loop
# def chat():
#     print("Mortgage Chatbot: Welcome! How can I assist you today?")
#     data = load_data()

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'exit':
#             break

#         # Check if user input matches any data in the CSV file
#         for row in data:
#             if user_input.lower() in row[0].lower():
#                 print(f"Mortgage Chatbot: {row[1]}")
#                 break
#         else:
#             # If no matching data, generate a mixed response
#             response = generate_response(user_input)
#             print(f"Mortgage Chatbot: {response}")

# chat()

from langchain.agents import create_csv_agent

from langchain.llms import OpenAI

import os

os.environ["OPENAI_API_KEY"] 

llm = OpenAI(openai_api_key="OPENAI_API_KEY")


agent = create_csv_agent(OpenAI(temperature=0), 'app\data.csv', verbose=True)

question=input("Enter your question : ")

agent.run(question)



