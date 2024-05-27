import requests
def internet_check():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            print("\033[92m" + "✓ Found active connection!" + "\033[0m")
            return "iok"
    except:
        print("\033[91m" + "Something went wrong with internet connection! Please check..." + "\033[0m")
