"""
THM CTF Manager

A command-line tool for managing TryHackMe CTFs. The tool allows you to fetch CTF data from the TryHackMe, view the list of available CTFs displaying if PWND or not and edit the status of a CTF.
Usage:
    thm_ctf_manager.py -h | --help
    thm_ctf_manager.py -s | --show
    thm_ctf_manager.py -u | --update
    thm_ctf_manager.py -e | --edit <ctf_name> <status>

Options:
    -h, --help                      Show this help message and exit
    -s, --show                      Print all available CTFs
    -u, --update                    Fetch THM CTFs into local file
    -e, --edit <ctf_name> <status>  Set the status of a CTF <unresolved,PWND>

Examples:
    thm_ctf_manager.py --show
    thm_ctf_manager.py --update
    thm_ctf_manager.py --edit "CTF Name" "PWND"
"""

import argparse
from colorama import Fore

from data_fetcher import fetch_ctfs
from data_formatter import format_data
from data_manager import *
from cursor_manager import show_cursor, hide_cursor
from readme_manager import manage_readme


def show_ctfs():
    try:
        data = read_csv()
        print(format_data(data, colorize=True))
    except Exception as e:
        print(f"\n{Fore.RED}[!] No data found on system{Fore.RESET}\n")
        print(
            f"{Fore.YELLOW}[»] Use the --update option to fetch data into local file{Fore.RESET}\n")


def update_ctfs():
    print(
        f"\n{Fore.GREEN}[+] Fetching THM CTFs into local file{Fore.RESET}")

    fetched_data = fetch_ctfs()

    try:
        data = read_csv()
        print(
            f"\n{Fore.YELLOW}[»] Data found on system. Checking for updates...{Fore.RESET}\n")
        data = update_csv(fetched_data, data)
    except Exception as e:
        print(
            f"\n{Fore.YELLOW}[»] No data found on system. Generating data...{Fore.RESET}\n")
        data = fetched_data

    generate_csv(data)
    print(f"{Fore.GREEN}[+] Fetching completed!{Fore.RESET}\n")
    edit_md(data)


def edit_ctf(args):
    try:
        edit_csv(args.edit[0], args.info)
        print(
            f"\n{Fore.GREEN}[+] Status for CTF: {args.edit[0].capitalize()} changed!{Fore.RESET}\n")
        edit_md()
    except Exception as e:
        print(e)
        print(f"\n{Fore.RED}[!] No data found on system{Fore.RESET}\n")
        print(
            f"{Fore.YELLOW}[»] Use the --update option to fetch data into local file{Fore.RESET}\n")


def edit_md(data=None):
    data = read_csv() if data is None else data
    manage_readme(format_data(data))


def main():

    # Create argument parser
    parser = argparse.ArgumentParser(description='THM CTF manager')

    # Add arguments
    parser.add_argument('-s', '--show', action='store_true',
                        help='Show all CTFs')
    parser.add_argument('-u', '--update', action='store_true',
                        help='Fetch THM CTFs into local file')
    parser.add_argument('-e', '--edit', metavar='[]', type=str, nargs=1,
                        help='Set a CTF status')
    parser.add_argument('-i', '--info', metavar='', type=str, nargs='?',
                        const='unresolved', default='PWND',
                        help='Set PWND or unresolved')

    # Parse arguments
    args = parser.parse_args()

    hide_cursor()

    # Handle arguments
    if args.show:
        show_ctfs()
    elif args.update:
        update_ctfs()
    elif args.edit:
        edit_ctf(args)
    else:
        # Print help if no arguments are provided
        parser.print_help()
    show_cursor()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(
            f"\n{Fore.RED}[!] Keyboard interrupt received. Exiting...{Fore.RESET}\n")

        show_cursor()
    except Exception as e:
        show_cursor()
        pass
