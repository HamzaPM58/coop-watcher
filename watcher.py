import requests

# list of companies we're going to be looking at
COMPANIES = [
    "magnetforensics", "achievers", "evr",
    "kepler", "waabi", "eqbank", "acceldata", "fullscript", "shyftlabs", "gomaterials",
    "kabam", "pointclickcare", "telesat", "syntronic", "osedea", "altaml",
    "promiserobotics", "blackbirdinteractive",
]

# initilize a list with terms for summer coops
SUMMER_TERMS = ["may 2027", "summer 2027"]

# terms that mark a student role in the commitment field
COMMITMENT_TERMS = ["co-op", "coop", "intern", "student"]

# terms safe to match in the title ("intern" would also match "internal")
TITLE_TERMS = ["co-op", "coop"]

# create a list for coops that don't match out search criteria
other_coops = []

# create a list for summer coops
summer_coops = []

# create a list for terms we don't need
OTHER_TERMS = ["winter 2027", "january 2027", "fall 2026"]

# loop through the companies
for company in COMPANIES:
    url = f"https://api.lever.co/v0/postings/{company}?mode=json"
    # Timeout stops the script from hanging forever if Lever doesn't respond.
    try:
        response = requests.get(url, timeout=20)
    except requests.exceptions.RequestException as error:
        print(f"Skipping {company}: {error}")
        continue  # jump to the next company

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

        description = posting.get("descriptionPlain") or ""
        description_lower = description.lower()

        # .get() returns None instead of crashing if a posting has no location.
        location = posting["categories"].get("location")

        commitment = posting["categories"].get("commitment") or ""
        commitment_lower = commitment.lower()

        is_coop = False

        link = posting["hostedUrl"]

        # check the commitment for any student term
        for term in COMMITMENT_TERMS:
            if term in commitment_lower:
                is_coop = True
                break

        if not is_coop:
            # check the title for co-op (catches postings with an empty commitment)
            for term in TITLE_TERMS:
                if term in title_lower:
                    is_coop = True
                    break

        # check if the posting is for a co-op
        if is_coop:
            is_summer = False
            for term in SUMMER_TERMS:
                if term in title_lower or term in description_lower:
                    is_summer = True
                    break

            if is_summer:
                summer_coops.append(f"{company} | {title} | {location} | {commitment} | {link}")
            else:
                # skip co-ops whose title names a known non-summer term
                is_other_term = False
                for term in OTHER_TERMS:
                    if term in title_lower:
                        is_other_term = True
                        break

                if not is_other_term:
                    other_coops.append(f"{company} | {title} | {location} | {commitment} | {link}")


print(f"{len(summer_coops)} Summer 2027 co-op postings") # print how many coop postings were found
for coop in summer_coops:
    print(coop)

print(f"{len(other_coops)} co-ops with no clear term (check by hand):")

# loop through coops
for coop in other_coops:
    print(coop)