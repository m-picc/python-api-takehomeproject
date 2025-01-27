# Obtain the list of authors from the api URL
# Build a dictionary from the list of authors
#   Use the appropriate first name in the dictionary in case a Title is included in the name.

import certifi
import requests

titles = {"Lord", "Lady", "Major", "Sir"}
poetry_api_url = "https://poetrydb.org/author"


def build_authors_dictionary():
    response = requests.get(poetry_api_url, verify=certifi.where())

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from poetry authors db API: {response.status_code}")

    authors_data = response.json()
    authors_list = authors_data.get("authors", [])
    authors_dictionary = {}

    for author in authors_list:
        name_parts = author.split()
        # Check if first part of the name is a title
        if name_parts[0] in titles and len(name_parts) > 1:
            first_letter = name_parts[1][0].upper()  # Use the second word's first letter
        else:
            first_letter = name_parts[0][0].upper()  # Use the first word's first letter

        authors_dictionary.setdefault(first_letter, []).append(author)

    return authors_dictionary
