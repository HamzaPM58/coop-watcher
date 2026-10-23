import requests

# Lever's public API returns a company's open jobs as JSON.
URL = "https://api.lever.co/v0/postings/magnetforensics?mode=json"

# Timeout stops the script from hanging forever if Lever doesn't respond.
response = requests.get(URL, timeout=10)

# Converts the JSON text into Python objects we can work with.
postings = response.json()

# print how many postings were found
print(f"Found {len(postings)} postings")

# initialize a variable for the number of coop postings
coop_count = 0

# loop through the postings
for posting in postings:
    title = posting["text"] # Lever calls the job title "text"
    # .get() returns None instead of crashing if a posting has no location.
    location = posting["categories"].get("location")
    commitment = posting["categories"].get("commitment", "")
    # check if the posting is for a co-op
    if "co-op" in commitment.lower():
        print(f"{title} | {location} | {commitment}") # print job info
        coop_count += 1 # increment the number of coops found

print(f"{coop_count} co-op postings") # print how many coop postings were found