import requests

response = requests.get(
    url=f"https://api.agify.io/",
    params={"name": "Rune"}
)
if response.status_code == 200:
    activity_data = response.json()
    activity = activity_data['age']

    print("Activiteit: ", activity)
else:
    print(f"Fout: {response.status_code} - {response.text}")