import concurrent.futures
import threading
import requests
import time

thread_local = threading.local()

def get_session():
    if not getattr(thread_local,"session", None):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = ["https://www.google.com", "https://www.facebook.com"] * 50
    start_time = time.time()
    download_all(sites)
    duration = time.time() - start_time
    print(f"\nDownloaded {len(sites)} in {format(duration,'.2f')} seconds!")
    print(f"\nAverage of {format(len(sites)/duration,'.2f')} sites per second!")


