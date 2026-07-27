import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

print(response.status_code)

data = response.json()

print(type(data))
print(data.keys())
print(data["status"])
print(data["meta"])

print(data["meta"]["scheme_name"])

print(type(data["data"]))
print(data["data"][0])

df=pd.DataFrame(data["data"])

print("\nfirst 5 nav record")
print(df.head())

df.to_csv("data/raw/live_nav_125497.csv", index=False)

scheme_codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response=requests.get(url)
    print(f"Scheme Code: {code} | Status: {response.status_code}")
