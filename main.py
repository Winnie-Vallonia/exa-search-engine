from exa_py import Exa
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Exa with the API key from the environment variable
exa = Exa(os.getenv("EXA_API_KEY"))

# Searching: query holds the response to the input of what we want to search
query = input("Search here: ")

response = exa.search(
    query,
    num_results=5,
    type='keyword',
    include_domains=['https://www.tiktok.com']
)

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()
