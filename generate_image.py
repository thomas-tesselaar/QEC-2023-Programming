#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 13:10:13 2023

@author: thomastesselaar
"""

import openai


# Returns a url to view the image, could also be switched to put image directly
# on your device
def generate_image(prompt: str, title: str):
    openai.api_key = "API_KEY"
    
    # use the OpenAI API to generate the image
    response = openai.Image.create(
        prompt=prompt,
        model="image-alpha-001",
    )
    
    # save the image
    # with open(title + ".jpg", "wb") as f:
    #     f.write(response["data"][0]["url"])
    
    # print("Image saved as image.jpg")
    
    return response["data"][0]["url"]
