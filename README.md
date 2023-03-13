# THM CTF Manager
A command-line tool for managing TryHackMe CTFs. The tool allows you to fetch CTF data from the TryHackMe, view the list of available CTFs displaying if PWND or not and edit the status of a CTF.

### Usage:
    thm_ctf_manager.py -h | --help
    thm_ctf_manager.py -s | --show
    thm_ctf_manager.py -u | --update
    thm_ctf_manager.py -e | --edit <ctf_name> 
    thm_ctf_manager.py -i | --info <status>

### Options:
    -h, --help                      Show this help message and exit
    -s, --show                      Print all available CTFs
    -u, --update                    Fetch THM CTFs into local file
    -e, --edit <ctf_name>           Select a CTF to change its status
    -i, --info <status>             Set the status of a CTF <unresolved,PWND>

### Examples:
    thm_ctf_manager.py --show
    thm_ctf_manager.py --update
    thm_ctf_manager.py --edit "CTF Name"
    thm_ctf_manager.py --edit "CTF Name" --info "PWND"

##### Check reports here: [Reports](https://h4ck3df1sh.github.io/index-en.html#portfolio)

[TryHackMe PWND machines!](./THM_CTFs.md#CTFs)