import csv
import re

import requests

# The "process"...

# 1. Fetch from sheets through csv-export download URL.
# 2. Process CSV, get usernames, do some conversions and general clean-up.
# 3. Output new CSV-file importable in Mastodon.
# (4. Push repository to Github.)
# (5. Run the job every 24 hours.)


GOOGLE_INFOSEC_URL = "https://docs.google.com/spreadsheets/d/1t13k5_cNhP9_TgoUmqDZk2ROkWkF6Bg3O5269vKIqWw/export?format=csv&id=1t13k5_cNhP9_TgoUmqDZk2ROkWkF6Bg3O5269vKIqWw"

INFOSEC_MASTODON_CSV = "mastodon_infosec_import.csv"

def fetch_infosec_sheet() -> str:

    response = requests.get(GOOGLE_INFOSEC_URL)

    if response.status_code == 200:
        return response.text

    return ""

def extract_infosec_usernames(sheet: str = "") -> list:

    usernames = []
    csv_data = sheet.split('\n')
    reader = csv.reader(csv_data, delimiter=',')
    _ = next(reader) # Skip first line of the sheet.

    for row in reader:
        username = ""

        # Match against pattern @username@instance, and https://instance/@username
        # ... otherwise no match.
        
        match = re.search("^[@\w]{1,}@[\w\.]{2,}", row[3])
        if match:
            if match.string[0] == '@':
                username = match.string[1:]
            else:
                username = match.string

        match = re.search("^https", row[3])
        if match:
            li = row[3].split('/')
            username = f"{li[3][1:]}@{li[2]}"

        if username:
            usernames.append(username)

    return usernames

def infosec_generate_mastondon_import_csv(usernames:list,
                                          show_boosts:bool = True,
                                          notify_on_posts:bool = False,
                                          languages:str = "") -> None:
    # Accept a list of Mastodon usernames, create and save an importable
    # Mastodon CSV-file.
    with open(INFOSEC_MASTODON_CSV, 'w') as fd:
        fd.write(f"Account address,Show boosts,Notify on new posts,Languages\n")
        for username in usernames:
            fd.write(f"{username},{show_boosts},{notify_on_posts},{languages}\n")

if __name__ == "__main__":

    # 1. Fetch the sheet (Keep writing shit! :-)
    infosec_sheet = fetch_infosec_sheet()
    
    # 2. Extract usernames, and some conversions and cleanup
    usernames = extract_infosec_usernames(infosec_sheet)

    # 3. Generate an Importable Mastodon CSV-file.
    infosec_generate_mastondon_import_csv(usernames)
    
    # 4. Tooooot tooot.
    
