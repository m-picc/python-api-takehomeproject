from fastapi import FastAPI, HTTPException
from getAuthors import build_authors_dictionary
import certifi
import requests
import random

# create FastAPI instance
app = FastAPI()

authors_dictionary = build_authors_dictionary()

@app.get("/")
def read_root():
    return {"message": "Its ALIVE!"}

@app.get("/{letter_value}")
def get_poet_from_letter(letter_value: str):
    """
    Endpoint for providing a poet's name, whos first name matches the received letter.
    Argument: a single english letter.
    Returns: A random name from the child list that matches the received letter.
    """
    # verify input value is actually a letter
    if not letter_value.isalpha() or len(letter_value) != 1:
        raise HTTPException(status_code=400, detail=letter_value + " is not a single english letter :(, Try again.",)

    # make input letter value upper case
    letter_value = letter_value.upper()

    # get the list of poets from the backend API
    matching_poets = authors_dictionary.get(letter_value, [])

    if not matching_poets:
        raise HTTPException(status_code=404,
        detail="Poet Not found with first name starting with the letter " + letter_value + ".")
    
    # Choose one of the poets from the matching sublist of names
    poet = random.choice(matching_poets)

    return {poet}
