import sys
import requests


def check_for_website(in_url):
    try:
        response = requests.get(in_url)
        response.raise_for_status()

        if 200 <= response.status_code < 400:
            print(f"The website at {in_url} is accessible.")
        else:
            print(f"The website at {in_url} returned an unexpected status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error accessing the website at {in_url}: {e}")


if len(sys.argv) != 2:
    print("Usage: python script_name.py <url>")
else:
    url = sys.argv[1]
    check_for_website(url)

