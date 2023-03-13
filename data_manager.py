import csv

def generate_csv(data, filename='CTF_Challenges.csv'):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['title', 'status', 'difficulty']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for difficulty, challenges in data.items():
            for challenge in challenges:
                writer.writerow({'title': challenge['title'], 'status': challenge['status'], 'difficulty': difficulty})

def read_csv():
    with open('CTF_Challenges.csv', mode='r') as file:
        csvFile = csv.reader(file)
        data = {}
        next(csvFile)
        for row in csvFile:
            difficulty = row[2]
            if difficulty not in data:
                data[difficulty] = []
            data[difficulty].append({'title': row[0], 'status': row[1]})
        return data

def update_csv(fetched_data,data):
    # Loop over the fetched_data object
    for category in fetched_data:
        for ctf in fetched_data[category]:
            # Check if the ctf is already in the data object
            if ctf['title'] not in [item['title'] for item in data[category]]:
                # If not, add the new entry to the appropriate list
                data[category].append(ctf)
    return data

def edit_csv(ctf_title,new_status='PWND',csv_file_path='CTF_Challenges.csv'):
    # Read data from CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    # Update status of specified CTF
    for row in data:
        if row['title'].lower() == ctf_title.lower():
            row['status'] = new_status
            break  # Stop iterating once CTF is found and updated

    # Write updated data back to CSV file
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'status', 'difficulty'])
        writer.writeheader()
        writer.writerows(data)