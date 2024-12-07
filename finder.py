#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:22:02 2024

@author: adiyogi
"""
import requests as req
import json


def title(key: bool, api: str) -> str:
    if key:
        title = input("Enter Title of Movie/ Series/ Episode : ")
        fullReq = f'{api}t={title}'
        print(fullReq)
        resp = req.get(fullReq)
        respDict = json.loads(resp.text)
        if respDict["Response"].lower() == "true":
            print(f"{respDict['Type'].capitalize()} name : {respDict['Title']}")
            print(f"Type : {respDict['Type']}")
            #tt9813792
            print(f"Ratings : {respDict['Ratings'][0]['Value']}")
            print(f"IMDb Rating : {respDict['imdbRating']}")
            print(f"IMDb Votes : {respDict['imdbVotes']}")
            print(f"Release Date : {respDict['Released']}")
            print(f"Content Type : {respDict['Rated']}")
            print(f"Awards : {respDict['Awards']}")
            print(f"Plot : {respDict['Plot']}")
            print(f"Actors : {respDict['Actors']}")
            print(f"Runtime : {respDict['Runtime'] if respDict['Type'] == 'movie' else None}")
            print(f"Genre : {respDict['Genre']}")
            print(f"Director : {respDict['Director']}")
            print(f"Writer : {respDict['Writer']}")
            print(f"Language : {respDict['Language']}")
            print(f"Country : {respDict['Country']}")
        else:
            print("Sorry, requested Title doesn\'t exist")
            resumer()


def imdb(key: bool, api: str) -> str:
    if key:
        imdbID = input("Enter IMDb ID : ")
        fullReq = f'{api}i={imdbID}'
        print(fullReq)
        resp = req.get(fullReq)
        respDict = json.loads(resp.text)
        if respDict["Response"].lower() == "true":
            print(f"{respDict['Type'].capitalize()} name : {respDict['Title']}")
            print(f"Type : {respDict['Type']}")
            #tt9813792
            print(f"Ratings : {respDict['Ratings'][0]['Value']}")
            print(f"IMDb Rating : {respDict['imdbRating']}")
            print(f"IMDb Votes : {respDict['imdbVotes']}")
            print(f"Release Date : {respDict['Released']}")
            print(f"Content Type : {respDict['Rated']}")
            print(f"Awards : {respDict['Awards']}")
            print(f"Plot : {respDict['Plot']}")
            print(f"Actors : {respDict['Actors']}")
            print(f"Runtime : {respDict['Runtime'] if respDict['Type'] == 'movie' else None}")
            print(f"Genre : {respDict['Genre']}")
            print(f"Director : {respDict['Director']}")
            print(f"Writer : {respDict['Writer']}")
            print(f"Language : {respDict['Language']}")
            print(f"Country : {respDict['Country']}")
        else:
            print("Sorry, requested IMDb ID doesn\'t exist")
            resumer()


def apiGetter(key: bool) -> str:
    apiKey = input("Enter your Open Movie Data Base (OMDb) API KEY : ")
    if json.loads(req.get(f"https://www.omdbapi.com/?apikey={apiKey}&i=tt9813792").text)["Response"].lower() == "false":
        print("Invalid API Key. Try again")
        apiGetter(True)
    else:
        return apiKey


def valGetter(key: bool) -> int:
    titleOrId = input("How do you want to search Movie/Series : [1:Title (Default), 2:IMDb ID] : ").lower()
    if titleOrId == str(2):
        return 2
    else:
        return 1

def main(keySet):
    rec =  valGetter(True)
    if 2 == rec:
        imdb(True, keySet)
    elif 1 == rec:
        title(True, keySet)
    resumer()

def resumer():
    resume = input("Wanna search more [y/N] : ").lower()
    if resume == "y":
        main(keySet)
    elif resume == "n":
        print("Thank you for using Movie Finder\n@Rockin Buddha")
    else:
        print("Invalid Input!\nTry Again")
        resumer()

keySet = f"https://www.omdbapi.com/?apikey={apiGetter(True)}&"
main(keySet)
