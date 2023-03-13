import requests
import json
import threading

def fetch_ctfs(max_pages=20):
    # Define how data is getting stored
    table_data = {'easy': [], 'medium': [], 'hard': [], 'insane': []}

    # Define a function to fetch data for a particular difficulty and page number
    def fetch_data(difficulty, page_number):
        # Define the URL to fetch data from
        url = f'https://tryhackme.com/api/hacktivities?page={page_number}&free=all&order=most-popular&difficulty={difficulty}&type=challenge'

        # Send a GET request to the URL and load the JSON response into a dictionary
        response = requests.get(url)

        data = json.loads(response.text)

        # Extract the title of each CTF from the response and add it to the corresponding difficulty level
        for CTF in data['rooms']:
            table_data[difficulty].append({'title':CTF['title'],'status':'unresolved'})

    # Create a list to store all the threads
    threads = []

    # Fetch data for each difficulty and page number using a separate thread for each combination
    for difficulty in ['easy', 'medium', 'hard', 'insane']:
        for page_number in range(1,max_pages):
            t = threading.Thread(target=fetch_data, args=(difficulty, page_number))
            threads.append(t)
            t.start()

    # Wait for all threads to complete before proceeding
    for t in threads:
        t.join()

    return table_data
