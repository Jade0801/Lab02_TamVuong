import json
from pathlib import Path
import requests
SOURCE_URL = "https://api.tvmaze.com/shows?page=0"
OUTPUT_PATH = Path("summary.json")
def fetch_records(url):
    """Download the TV shows records and return them as Python objects."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

def count_shows_per_genre(records):
    genre_count = {}
    for show in records:
        genres = show.get("genres", [])
        if genres:
            for genre in genres:
                if genre in genre_count:
                    genre_count[genre] += 1
                else:
                    genre_count[genre] = 1
    return genre_count

def get_top_genre(genre_count):
    if not genre_count:
        return ("",0)
    top_genre = max(genre_count, key=genre_count.get)
    top_count = genre_count[top_genre]
    return (top_genre, top_count)


def main():
    print("Fetching TV shows records...")
    records = fetch_records(SOURCE_URL)
    print("Processing data...")
    genre_count = count_shows_per_genre(records)
    top_genre = get_top_genre(genre_count)
    summary = {
        "source_url": SOURCE_URL,
        "total_records_processed": len(records),
        "shows_per_genre": genre_count,
        "top_genre": {
            "genre": top_genre[0],
            "count": top_genre[1]
        }

    }
    OUTPUT_PATH.write_text(json.dumps(summary,indent=2), encoding="utf-8")
    print(f'Successfully wrote summary to {OUTPUT_PATH.resolve()}')

if __name__ == "__main__":
    main()