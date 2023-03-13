from tabulate import tabulate
from termcolor import colored
from itertools import zip_longest

from enum import Enum

class Color_by_difficulty(Enum):
    easy = 'green'
    medium = 'blue'
    hard = 'yellow'
    insane = 'red'

def format_title(title, color=None, status=None):
    if status == 'PWND':
        title = '\u0336'.join(title) + '\u0336'
    return colored(title, color.value) if color else title


def format_data(data, colorize=False):
    headers = [str.upper(difficulty.name) for difficulty in Color_by_difficulty]
    if colorize:
        headers = [colored(header, Color_by_difficulty[header.lower()].value) for header in headers]

    table_data = []
    for items in zip_longest(*[sorted(data[difficulty.name], key=lambda x: x['title']) for difficulty in Color_by_difficulty]):
        row_data = []
        for item, difficulty in zip(items, Color_by_difficulty):
            title = item.get('title', '') if item else ''
            status = item.get('status') if item else ''
            color = difficulty if colorize else None
            row_data.append(format_title(title, color=color, status=status))
        table_data.append(row_data)
    
    tablefmt = 'fancy_grid' if colorize else 'github'
    table = tabulate(table_data, headers=headers, tablefmt=tablefmt, stralign='center')
    
    return table
