import requests

# Lever's public API returns a company's open jobs as JSON.
URL = "https://api.lever.co/v0/postings/magnetforensics?mode=json"

# Timeout stops the script from hanging forever if Lever doesn't respond.
response = requests.get(URL, timeout=10)

# Converts the JSON text into Python objects we can work with.
postings = response.json()

# print how many postings were found
print(f"Found {len(postings)} postings")

# loop through the postings
for posting in postings:
    title = posting["text"] # Lever calls the job title "text"
    # .get() returns None instead of crashing if a posting has no location.
    location = posting["categories"].get("location")
    print(f"{title} | {location}") # print job title and location