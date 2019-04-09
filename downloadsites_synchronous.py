import time
import requests

def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = ["https://www.google.com", "https://www.facebook.com"] * 50
    start_time = time.time()
    download_all(sites)
    duration = time.time() - start_time
    print(f"\nDownloaded {len(sites)} in {format(duration,'.2f')} seconds!")
    print(f"\nAverage of {format(len(sites)/duration,'.2f')} sites per second!")

"""
Using the Session object, instead of simple using get() from requests, because it runs faster by doing some *network magic*
"""