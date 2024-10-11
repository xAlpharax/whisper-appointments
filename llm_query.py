#!/usr/bin/env python3

##############################################################################

from dotenv import load_dotenv
import os

load_dotenv()
PREDICTION_API_URL = str(os.getenv("PREDICTION_API_URL"))

import requests

def query(payload):

    response = requests.post(PREDICTION_API_URL, json=payload).json()
    print(response)

    return response

##############################################################################

if __name__ == "__main__":
    output = query({
        "question": "Hello there! How are you doing today?",
    })
