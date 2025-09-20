import requests
import pandas as pd
from time import sleep

API_KEY = "3a2e04976f2148a9b2222c71f1dff77b"
BASE_URL = "https://api.football-data.org/v4"
COMPETITION = "PL"
headers = {"X-Auth-Token": API_KEY}

seasons = range(2023, 2026)  
all_matches = []

for season in seasons:
    url = f"{BASE_URL}/competitions/{COMPETITION}/matches?season={season}"
    response = requests.get(url, headers=headers)
    
    # Rate limit protection: free tier = 10 requests/minute
    sleep(6)  # 6 seconds between requests is safe
    
    if response.status_code != 200:
        print(f"Skipping season {season}: Error {response.status_code}")
        continue
    
    data = response.json()
    
    for match in data.get("matches", []):
        home = match["homeTeam"]["name"]
        away = match["awayTeam"]["name"]
        score = match.get("score", {}).get("fullTime", {})
        home_goals = score.get("home")
        away_goals = score.get("away")
        if home_goals is None or away_goals is None:
            result = None
        elif home_goals > away_goals:
            result = "H"
        elif home_goals < away_goals:
            result = "A"
        else:
            result = "D"
        
        all_matches.append({
            "home_team": home,
            "away_team": away,
            "home_goals": home_goals,
            "away_goals": away_goals,
            "result": result,
            "season": f"{season}/{season+1}"
        })

# Create DataFrame
df = pd.DataFrame(all_matches)
df.to_csv("premier_league_2023_2025.csv", index=False)
print(f"Saved {len(df)} matches from 2015–2025")
