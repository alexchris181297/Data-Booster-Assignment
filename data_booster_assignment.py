import requests

def get_flag(url, headers):
    cursor = None  # Start without a cursor
    while True:
        data = {"cursor": cursor} if cursor else {}  # Send the cursor if it exists
        response = requests.post(url, json=data, headers=headers)
        result = response.json()
        
        print(result)  # Print the response to track progress
        
        if 'error' in result:
            print("Error:", result['error'])
            break
        
        if 'nextCursor' in result:
            cursor = result['nextCursor']  # Update the cursor for the next request
        else:
            print("No more cursors. Challenge complete or error occurred.")
            break

url = "https://flag-gilt.vercel.app/api/challenge"
headers = {
    "Authorization": "Bearer uM0M7uypyeeHZ741XIrs9KsFOUEhxUdtXJA="
}

get_flag(url, headers)