# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging

def main(text:str) -> list: #run mapper on line of text
    words = text.lower().split()  #split lines into words
    mpp =  [(word, 1) for word in words] #save as tubles
    return mpp
