import requests

# list of companies we're going to be looking at
COMPANIES = ["magnetforensics", "achievers", "evr"]

# initilize a list with terms for summer coops
SUMMER_TERMS = ["may 2027", "summer 2027"]

# initialize a variable for the number of coop postings for summer
summer_count = 0

# loop through the companies
for company in COMPANIES:
    url = f"https://api.lever.co/v0/postings/{company}?mode=json"
    # Timeout stops the script from hanging forever if Lever doesn't respond.
    response = requests.get(url, timeout=10)

    # 200 means success. Anything else means the company wasn't found or Lever had a problem.
    if response.status_code != 200:
        print(f"Skipping {company}: status {response.status_code}")
        continue  # jump to the next company

    # Converts the JSON text into Python objects we can work with.
    postings = response.json()
    # print how many postings were found
    print(f"Found {len(postings)} postings at {company}")

    # loop through the postings
    for posting in postings:
        title = posting["text"] # Lever calls the job title "text"
        title_lower = title.lower()
        # .get() returns None instead of crashing if a posting has no location.
        location = posting["categories"].get("location")
        commitment = posting["categories"].get("commitment", "").lower()
        # check if the posting is for a co-op
        if "co-op" in commitment or "coop" in commitment:
            is_summer = False
            for term in SUMMER_TERMS:
                if term in title_lower:
                    is_summer = True
                    break

            if is_summer:
                print(f"{title} | {location} | {commitment}") # print job info
                summer_count += 1 # increment the number of coops found

print(f"{summer_count} Summer 2027 co-op postings") # print how many coop postings were found