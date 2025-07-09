import httpx

r = httpx.post("http://127.0.0.1:8000/hi",json={"who": "Fine"})
print(r.json())