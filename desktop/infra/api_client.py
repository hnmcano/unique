import requests

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.token = None

        print("base_url:", self.base_url, "token:", self.token)

    def set_token(self, token: str):
        self.token = token

    def headers(self):
        headers = {
            "Content-Type": "application/json"
        }

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        return headers

    def get(self, endpoint: str):
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers())
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, data: dict):
        response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers=self.headers())
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint: str, data: dict):
        response = requests.put(f"{self.base_url}/{endpoint}", json=data, headers=self.headers())
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint: str, data: dict):
        response = requests.delete(f"{self.base_url}/{endpoint}", json=data, headers=self.headers())
        response.raise_for_status()
        return response.json()
    
    def patch(self, endpoint: str, data: dict):
        response = requests.patch(f"{self.base_url}/{endpoint}", json=data, headers=self.headers())
        response.raise_for_status()
        return response.json()

    def options(self, endpoint: str):
        response = requests.options(f"{self.base_url}/{endpoint}", headers=self.headers())
        response.raise_for_status()
        return response.json()

    def head(self, endpoint: str):
        response = requests.head(f"{self.base_url}/{endpoint}", headers=self.headers())
        response.raise_for_status()
        return response.json()
    