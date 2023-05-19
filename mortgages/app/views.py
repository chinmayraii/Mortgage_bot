from django.shortcuts import render
import openai
import pandas as pd
import os

from django.views.decorators.csrf import csrf_exempt
import csv
from django.http import JsonResponse
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.agents import initialize_agent
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd




def index(request):
    return render(request,'index.html')

# os.environ["OPENAI_API_KEY"] 

# llm = OpenAI(openai_api_key="OPENAI_API_KEY")

# model=OpenAI(temperature=0.9,)

# agent = create_csv_agent(model, 'app\mortgages.csv', verbose=True)


# question=input("Enter your question : ")
# agent.run(question)

df = pd.read_csv('app\mortgages.csv')

def generate_response(question):
    agent = create_pandas_dataframe_agent(
        OpenAI(temperature=0),
        df,
        verbose=True
    )
    return agent.run(question)

@csrf_exempt
def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']
        response=generate_response(user_input)
        return render (request,'index.html',{"response":response})























# from langchain.agents.agent_toolkits import ZapierToolkit
# from langchain.utilities.zapier import ZapierNLAWrapper



# llm = OpenAI(temperature=0)
# zapier = ZapierNLAWrapper()
# toolkit = ZapierToolkit.from_zapier_nla_wrapper(zapier)
# csv_file = create_csv_agent(OpenAI(temperature=0.9), 'app\mortgages.csv', verbose=True)
# agent = initialize_agent(toolkit.get_tools(), llm,csv_file, agent="zero-shot-react-description", verbose=True)

# question=input("Enter your question : ")

# agent.run(question)












