import argparse
import os
import requests

def txt_file(filename):
    if not filename.endswith(".txt"):
        raise argparse.ArgumentTypeError(f"{filename} is not a .txt file")
    if not os.path.isfile(filename):
        raise argparse.ArgumentTypeError(f"{filename} does not exist")
    return filename

def process_file(filename):
    word_list = []
    with open(filename, 'r') as file:
        for line in file:
            processed_line = line.strip()
            word_list.append(processed_line)
    return word_list

def recieve_status_codes(url, endpoints):
    working_endpoints = []
    if not url.endswith("/"):
        url += "/"
    for word in endpoints:
        urlwithendpoint = url+word
        response = requests.get(urlwithendpoint)
        print(f"{urlwithendpoint} and {response.status_code}")
        if response.status_code in [200, 301, 302, 403, 401, 405]:
            working_endpoints.append((urlwithendpoint, response.status_code))
    print(f"Working Endpoints are#######{working_endpoints}")
        

def main():
    endpoints = []

    parser = argparse.ArgumentParser(description="A dirb clone")
    parser.add_argument("--url", type=str, required=True, help="PLease give the base url that you want to scan")
    parser.add_argument("--file", type=txt_file, default="./wordlists/common.txt",help="Please give the path to the txt file")
    args = parser.parse_args()
    print(f"the file is {args.file} and the url is {args.url}")
    endpoints = process_file(args.file)
    recieve_status_codes(args.url, endpoints)


main()

