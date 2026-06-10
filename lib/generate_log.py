from datetime import datetime
import os


def generate_log(data):
    """Write a list of log entries to a dated file and return the filename.

    Args:
        data (list): List of string log entries.

    Returns:
        str: The filename that was written.

    Raises:
        ValueError: If `data` is not a list.
    """
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch a sample post from jsonplaceholder.typicode.com using requests.

    Imports `requests` inside the function so the module is only required when
    the integration is used (keeps the function import-light for tests).
    """
    try:
        import requests

        resp = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        return {}

    return {}


if __name__ == "__main__":
    sample = ["User logged in", "User updated profile", "Report exported"]
    filename = generate_log(sample)

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
