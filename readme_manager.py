import sys
import fileinput

def manage_readme(data):
    # Open a file for writing
    with open('THM_CTFs.md', 'w') as f:
        # Redirect stdout to the file
        sys.stdout = f
        
        # Your code here
        print('# CTFs')
        print(data)
        
        # Restore stdout
        sys.stdout = sys.__stdout__
    for line in fileinput.input('THM_CTFs.md', inplace=True):
        line = line.replace("|-", "|:-").replace("-|", "-:|")
        print(line, end='')