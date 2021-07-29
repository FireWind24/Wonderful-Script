import sys
import webbrowser
import time
import random
while True:
    sites = random.choice(['google.com', 'youtube.com', 'facebook.com', 'weather.gov', 'amazon.com', 'reddit.com', 'wikipedia.org', 'netflix.com'])
    visit = "https://{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(1, 3)
    time.sleep(seconds)

