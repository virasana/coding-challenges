import requests
import logging
import time
from retry import retry
from collections import defaultdict
from pandas import DataFrame

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('__name__')

logging.getLogger('urllib3').setLevel(logging.WARNING)

API_URL='https://jsonplaceholder.typicode.com/posts'
API_MAX_RETRIES=5
API_RETRY_DELAY_SECONDS=1
API_RETRY_BACKOFF_SECONDS=1

@retry(tries=API_MAX_RETRIES, delay=API_RETRY_DELAY_SECONDS, backoff=API_RETRY_BACKOFF_SECONDS, logger=logger)
def fetch_data(api_url, api_max_retries, api_retry_delay_seconds):
    response = requests.get(api_url)
    response.raise_for_status()
    result = response.json()
    return result 

def get_summary_report(data):
    if data is None:
        return data
    
    user_stats = defaultdict(lambda: 
        {
            'postCount': 0,
            'longestTitle': '',
            'longestTitleLength': 0
        }
    )
    
    for post in data:
        user_id = post['userId']
        title = post['title']
        titleLength = len(title)
        user_stats[user_id]['postCount'] += 1
        
        if titleLength > user_stats[user_id]['longestTitleLength']:
            user_stats[user_id]['longestTitle'] = title
            user_stats[user_id]['longestTitleLength'] = titleLength
    
    result = [
        { 'userId': user_id, **user_stats } 
        for user_id, user_stats 
        in sorted(
            user_stats.items(), key=lambda x: x[1]['longestTitleLength'], reverse=True
        )
    ]
    return result

def get_summary_report_pandas(data):
    if data is None:
        return []
    df = DataFrame(data)

    df['titleLength'] = df['title'].str.len()

    df_sorted = df.sort_values(
        by=['titleLength', 'userId'], 
        ascending=[False, True]
    )

    result_df = (
        df_sorted
        .groupby('userId', as_index=False)
        .agg(
            postCount=('id', 'count'),
            longestTitle=('title', 'first'),
            longestTitleLength=('titleLength', 'first')
        )
    )

    return result_df.to_dict(orient='records')



if __name__ == '__main__':
    data=fetch_data(API_URL, API_MAX_RETRIES, API_RETRY_DELAY_SECONDS)
    # report = get_summary_report(data)
    report = get_summary_report_pandas(data)
    logger.info(report)








# import requests
# import time
# import json
# from collections import defaultdict
# # Optional: only needed if you enable the Pandas approach
# import pandas as pd


# API_URL = "https://jsonplaceholder.typicode.com/posts"
# MAX_RETRIES = 3
# RETRY_DELAY = 2  # seconds


# def fetch_api_data(url, retries=MAX_RETRIES, delay=RETRY_DELAY):
#     """
#     Fetch JSON data from the API with retry logic.
#     Returns a list of dicts or an empty list on failure.
#     """
#     for attempt in range(1, retries + 1):
#         try:
#             response = requests.get(url, timeout=5)
#             response.raise_for_status()
#             return response.json()
#         except requests.exceptions.RequestException as e:
#             print(f"Attempt {attempt} failed: {e}")
#             if attempt < retries:
#                 time.sleep(delay)
#             else:
#                 print("Failed to fetch data after maximum retries.")
#                 return []


# def process_with_pandas(data):
#     """
#     Process posts using Pandas DataFrames.
#     """
#     if not data:
#         return []

#     df = pd.DataFrame(data)

#     # Derive title length
#     df["title_length"] = df["title"].str.len()

#     # Sort so longest title per user is first
#     df_sorted = df.sort_values(
#         by=["userId", "title_length"],
#         ascending=[True, False]
#     )

#     # Aggregate per user
#     result_df = (
#         df_sorted
#         .groupby("userId", as_index=False)
#         .agg(
#             postCount=("id", "count"),
#             longestTitle=("title", "first"),
#             longestTitleLength=("title_length", "first")
#         )
#     )

#     return result_df.to_dict(orient="records")


# def process_without_pandas(data):
#     """
#     Process posts using plain Python (no Pandas).
#     """
#     if not data:
#         return []

#     user_stats = defaultdict(lambda: {
#         "postCount": 0,
#         "longestTitle": "",
#         "longestTitleLength": 0
#     })

#     for post in data:
#         user_id = post["userId"]
#         title = post["title"]
#         title_length = len(title)

#         user_stats[user_id]["postCount"] += 1

#         if title_length > user_stats[user_id]["longestTitleLength"]:
#             user_stats[user_id]["longestTitle"] = title
#             user_stats[user_id]["longestTitleLength"] = title_length

#     # Convert to sorted list
#     result = [
#         {"userId": user_id, **stats}
#         for user_id, stats in sorted(user_stats.items())
#     ]

#     return result


# def main():
#     data = fetch_api_data(API_URL)

#     # ---- Choose ONE approach ----

#     result = process_with_pandas(data)
#     # result = process_without_pandas(data)

#     # --------------------------------

#     print(json.dumps(result, indent=2))


# if __name__ == "__main__":
#     main()
