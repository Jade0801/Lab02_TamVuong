#TV Maze Show 
A Python commnand-line utility that fetches television show data from the TV Maze API, processes and gaggregates records, and output a structured JSON summary to help analyze genre distribution, top highlights.
## Data source
-**URL**: `https://api.tvmaze.com/shows?page=0`
-**Record descriptions**: Each record represents a single television show entry containing metadata such as showw game, operational status, and user ratings.
-**Record count**: 240 records

## Setup
python -m venv .venv
source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt

## Run
python records.py

## Example output
{
  "source_url": "https://api.tvmaze.com/shows?page=0",
  "total_records_processed": 240,
  "shows_per_genre": {
    "Drama": 154,
    "Science-Fiction": 39,
    "Thriller": 41,
    "Action": 55,
    "Crime": 57,
    "Horror": 21,
    "Romance": 32,
    "Adventure": 23,
    "Espionage": 2,
    "Music": 3,
    "Mystery": 15,
    "Supernatural": 18,
    "Fantasy": 13,
    "Family": 21,
    "Anime": 4,
    "Comedy": 66,
    "History": 4,
    "Medical": 6,
    "Legal": 6,
    "Western": 3,
    "War": 4,
    "Sports": 2
  },
  "top_genre": {
    "genre": "Drama",
    "count": 154
  }
}
This summary tells us the exact distriution of television genres across the fetched dataset, alongside the single most prominent genre

## Data quirks
- Missing or Empty Genres: some shows don't have a defined genre list in the API payload => The program handles this by using .get("genres", []) and checking if the list is populated before counting.
- Ratings are nested inside a dictionary structure; the script safely checks for rating existence and falls back gracefully if rating data is absent.

## Desgin choices
- List: for storing the raw API response (records) because it preserves the sequential order of elements and allow efficient iteration over all download entries.
- Dict: used for frequency aggregations (genre_count) and constructing the final output schema
- Tuple: used to group few fixed values together (lie the top genre name and its count) and return them from a function all at one. Because it's read - only so it keeps data safe.