
import requests

BASE_URL = None

def send_request(method:str,endpoint:str,base_url:str):
    url = base_url + endpoint
    try:
        return requests.request(method, url)
    except requests.RequestException as exc:
        raise RuntimeError(f"HTTP request Failed: {exc}")





def login_and_get_token(base_url:str, email:str, password: str) -> str:
    url = f"{base_url}/api/login"

    payload = {"email":email,
                "password":password}
    
    try:
        response = requests.post(url=url,json=payload)
    except requests.RequestException as exc:
        raise RuntimeError(f"Login request failed: {exc}")

    if response.status_code != 200:
        raise RuntimeError (f"Login failed with status code {response.text}")
    
    try:
        token = response.json().get("token")
    except ValueError:
        raise RuntimeError("Login Response is not valid json")
    

    if not token:
        raise RuntimeError("token not found in login response")
    

    return token