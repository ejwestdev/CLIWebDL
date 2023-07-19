import argparse
import requests
def get_json(url, file):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(file_name, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded {url} to {file_name} successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except IOError as e:
        print(f"Error writing to file {file_name}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI program to parse HTML requests")
    parser.add_argument("-j", "--get_json", required=False, type=str, help="The URL of the file to download.")
    parser.add_argument("file_name", help="The name of the file to save.")
    args = parser.parse_args()
    get_json(args.get_json, args.file_name)