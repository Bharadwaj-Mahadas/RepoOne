import requests

get_response = requests.get("https://www.geeksforgeeks.org/python-requests-tutorial/")

print(get_response.status_code)