import requests
# A module in pytohn that helps us to communicate with servers
# Docs: https://docs.python-requests.org/en/master/
response = requests.get("https://randomfox.ca/floof")

# Status Codes
# 200 - Means "OK"
print("----CODE----")
print(response.status_code)
print("\n")
print("----TEXT----")
print(response.text)
print("\n")
print("----JSON----")
print(response.json())
print("----IMAGE KEY----")
print("response.json()[image]",response.json()['image'])
print("response.json()[link]",response.json()['link'])
print("\n")
