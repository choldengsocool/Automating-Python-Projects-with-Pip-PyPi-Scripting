from lib.generate_log import generate_log, fetch_data


if __name__ == "__main__":
    sample = ["User logged in", "User updated profile", "Report exported"]
    filename = generate_log(sample)
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))
