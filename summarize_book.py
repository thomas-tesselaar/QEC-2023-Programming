#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 11:13:43 2023

summarizes text for some

@author: thomastesselaar
"""


import openai

def read_book(filename: str) -> str:
    """

    Parameters
    ----------
    filename : str
        location of the text file.

    Returns
    -------
    str
        A string of all the text ing the file.

    """
    
    # Open text file in read mode
    try:
        text_file = open(filename, "r")
    except:
        raise Exception('Invalid file name')
    
    # Read whole file to a string
    data = text_file.read()
    
    # Close file
    text_file.close()
    
    return data


def summarize_book(text:str, l: int) -> str:
    """
    
    Parameters
    ----------
    text : str
        The contents/text of the book to summarize.
    l : int
        The length of the summary.
        This is given as an input 0-4  where each input maps to a given user 
        selected length in minutes

    Returns
    -------
    str
        The summary of the book.

    """
    
    # Setting api keys to use the openai api
    api_key = "API_KEY"
    openai.api_key = api_key
    
    
    # Length in minutes of desired summary
    lengths = [5, 15, 30, 60, 120]
    minute_length = lengths[l]
    
    # Assuming a reading rate of 200 wpm. This would in the future be adjusted 
    # to individual users based on their reading speed
    reading_rate = 200
    desired_words = minute_length * reading_rate
    
    
# =============================================================================
#     # Commenting out because below code is unused with the openai model
#     # We initally took the title as an input parametre to the function
#
#     # Here, the code would have to query an SQL database 
#     # I used a dict to represent looking up the title in the data base
#     # SQL query would be along the lines of:
#     # SELECT word_count FROM Books WHERE title = ttl
#     
#     database = {"Alice in Wonderland":29610, "To Kill a Mockingbird":100388, 
#                 "Les Misrable":568751}
#     
#     word_count = database[ttl]
#
# =============================================================================
    
    
    # Use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"summarize this text: {text}"),
        temperature=0.5,
        max_tokens=desired_words,
        
    )
    
    # Returns the summarized text
    return response["choices"][0]["text"]

def summarize_to_sentence(text:str) -> str:
    """
    
    Parameters
    ----------
    text : str
        The contents/text of the book to summarize.
    Returns
    -------
    str
        The summary of the book.

    """
    
    # Setting api keys to use the openai api
    api_key = "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"
    openai.api_key = api_key
    
    
    # use the OpenAI API to summarize the text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=(f"summarize this text in a sentence: {text}"),
        temperature=0.5,
        max_tokens=12,
        
    )
    
    # Returns the summarized text
    return response["choices"][0]["text"]



