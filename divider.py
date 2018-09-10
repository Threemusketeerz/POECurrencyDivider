import os
import json
import requests


def find_tab():
    account = "sporring2"
    stash_tab = "FoundMapping"

    api_url = "http://api.pathofexile.com/public-stash-tabs/"
    id_count = 0
    id = 0

    found = False


    # with open("data.json", "w") as outfile:
    #     json.dump(response_json, outfile)


    # Look for stash with account name, else keep requesting stashes to look in
    while not found:

        # Check whether we've visted an ID we need to continue from
        if (os.path.exists("last_visited_id.txt")) and id is 0:
            with open("last_visited_id.txt", "r") as infile:
                id = infile.readline()

        id_url = f"?id={id}"
        print(f"Requesting url: {api_url}{id_url}")
        response = requests.get(api_url + id_url)
        print(f"Status: {response.status_code}")

        # If response is OK
        # Else it should keep trying
        if response.status_code is 200:
            # Write last visited ID to a file
            with open("last_visited_id.txt", "w") as out:
                out.write(f"{id}")

            response_json = response.json()

            stashes = response_json.get("stashes")

            if stashes:
                for stash in stashes:
                    account_name = stash.get("accountName")
                    items = stash.get("items")
                    if account_name:
                        print(f"Looking in: {account_name}")
                    if (account_name == account):
                        print("FOUND sporring2")

                        with open("found_at_id.txt", "w") as out:
                            print("Writing location to a file")
                            out.write(f"{id}")

                        found = True

            if not found:
                id = response_json.get("next_change_id")
                # print(f"Didn't find {account}")
    # Did we succeed
    print(f"Response: {response.status_code}")



    return "Done."

def divide_currency(tab, amount_of_people, dest):
    return

if __name__ == "__main__":
    print(find_tab())
