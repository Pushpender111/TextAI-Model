# # import nlpcloud
# import paralleldots
# # client = nlpcloud.Client("finetuned-llama-3-70b", "bdfe31ddbddd89ea8175c46eeb4e2fcf56901ea9", gpu=True)


# paralleldots.set_api_key('IH4OCcC3pwUFU6jRcoyzug4ShpopFEtpLFigQEZImmk')

# def ner(para,entity=None):
#     # response = client.entities(para,searched_entity=entity)
#     # return response
#     try:
#         response = paralleldots.ner(para)
#         print("Raw response:", response)   # Debugging
#         return response
#     except Exception as e:
#         return e
from dotenv import load_dotenv
load_dotenv()  
import requests
import os
DANDELION_API_TOKEN = os.getenv("API_KEY")

def ner(text):
    url = "https://api.dandelion.eu/datatxt/nex/v1"
    params = {
        "text": text,
        "lang": "en",
        "token": DANDELION_API_TOKEN
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def sentiment_analysis(para,lang="en"):
    url="https://api.dandelion.eu/datatxt/sent/v1"
    params = {
        "text": para,
        "lang": lang,
        "token": DANDELION_API_TOKEN
    }
    try:
        response=requests.get(url,params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error : " , str(e)}