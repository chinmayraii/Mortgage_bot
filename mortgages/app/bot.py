import csv
import random
import openai
import os

# Load your OpenAI API credentials
openai.api_key = os.getenv('OPENAI_API_KEY')

# Load mortgage data from CSV file
def load_data():
    data = []
    with open('app\mort.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            data.append(row)
    return data

# Generate a mixed response using OpenAI and CSV data
def generate_response(input_text, csv_data):
    csv_response = None

    # Check if user input matches any data in the CSV file
    for row in csv_data:
        if input_text.lower() in row[0].lower():
            csv_response = row[1]
            break

    # Generate a response using OpenAI
    openai_response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        temperature=0.7,
        max_tokens=50,
        n=1,
        stop=None,
    )
    openai_response = openai_response.choices[0].text.strip()

    # Mix the CSV response and OpenAI response
    responses = [csv_response, openai_response]
    mixed_response = random.choice(responses)

    return mixed_response

# Main loop
def chat():
    print("Mortgage Chatbot: Welcome! How can I assist you today?")
    data = load_data()

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = generate_response(user_input, data)
        print(f"Mortgage Chatbot: {response}")

chat()
