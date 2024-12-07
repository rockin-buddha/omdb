Movie Finder Script

This is a Python command-line application that allows users to search for movies, series, or episodes using the OMDb API. Users can search by movie title or IMDb ID and retrieve detailed information about the movie/series, including ratings, plot, release date, cast, director, and more.
Features

    Search for movies and series by title or IMDb ID.
    Retrieve detailed information about the movie or series, including:
        Title
        Type (movie/series/episode)
        IMDb ratings and votes
        Release date
        Plot
        Actors, director, writer
        Genre, runtime, language, and country
        Awards won
    Simple and user-friendly command-line interface.
    Option to continue searching after each query.

Requirements

    Python 3.x
    requests library (for making API calls)

You can install the required dependencies using the following command:

    pip install requests

Setup

    Get OMDb API Key:
        To use this script, you need an API key from OMDb.
        Go to OMDb API and create an account to obtain your API key.

    Run the Script:
        Clone or download the repository.
        Navigate to the directory containing the script.
        Run the script using the following command:

        python finder.py

    Provide Your API Key:
        When prompted, enter your OMDb API key.

    Search for Movies or Series:
        You will be prompted to search by either title or IMDb ID. Select your preferred search method by entering 1 (Title) or 2 (IMDb ID).
        If you choose the title, enter the name of the movie/series you wish to search for.
        If you choose IMDb ID, enter the IMDb ID (e.g., tt0133093 for The Matrix).

    View the Results:
        The script will display detailed information about the movie or series you searched for.
        You can choose to search for another movie or exit the program.

Usage

Here’s how the script interacts with the user:

    Prompt for API Key: The script asks for your OMDb API key.
    Search Option: Choose whether you want to search by:
        Title (default option)
        IMDb ID
    Movie/Series Details: After the search, the script displays detailed information such as:
        Title, Type (movie/series), IMDb Rating, Release Date, Plot, Actors, Director, etc.
    Continue Searching: After viewing the results, you can choose to search for more movies/series or exit.

Example search:

    Enter Title of Movie/ Series/ Episode : Inception
    Movie name : Inception
    Type : movie
    Ratings : 8.8/10
    IMDb Rating : 8.8
    IMDb Votes : 2000000
    Release Date : 16 Jul 2010
    Content Type : PG-13
    Awards : 4 wins & 148 nominations
    Plot : A thief who steals corporate secrets through the use of dream-sharing technology...
    Actors : Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page
    Runtime : 148 min
    Genre : Action, Adventure, Sci-Fi
    Director : Christopher Nolan
    Writer : Christopher Nolan
    Language : English, Japanese, French
    Country : USA, UK

Functions

    title(key: bool, api: str): Searches for a movie/series by title.
    imdb(key: bool, api: str): Searches for a movie/series by IMDb ID.
    apiGetter(key: bool): Prompts for the OMDb API key and checks if it's valid.
    valGetter(key: bool): Asks how the user wants to search (by title or IMDb ID).
    main(keySet): Drives the main program flow based on user input.
    resumer(): Prompts the user if they want to continue searching.

Example Run

    Enter your Open Movie Data Base (OMDb) API KEY : <Your API Key>
    How do you want to search Movie/Series : [1:Title (Default), 2:IMDb ID] : 1
    Enter Title of Movie/ Series/ Episode : Inception
    Movie name : Inception
    Type : movie
    Ratings : 8.8/10
    IMDb Rating : 8.8
    IMDb Votes : 2000000
    Release Date : 16 Jul 2010
    Content Type : PG-13
    Awards : 4 wins & 148 nominations
    Plot : A thief who steals corporate secrets through the use of dream-sharing technology...
    Actors : Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page
    Runtime : 148 min
    Genre : Action, Adventure, Sci-Fi
    Director : Christopher Nolan
    Writer : Christopher Nolan
    Language : English, Japanese, French
    Country : USA, UK
    Wanna search more [y/N] : y

Error Handling

    Invalid API Key: If the provided API key is invalid, the script will prompt the user to re-enter a valid key.
    Movie/Series Not Found: If the title or IMDb ID does not match any movie or series, the script will notify the user and allow them to try again.

Contribution

Feel free to contribute to this project by creating issues or submitting pull requests. Any improvements, bug fixes, or suggestions are welcome!
License

This project is open source and available under the MIT License.
