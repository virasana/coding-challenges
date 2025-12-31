import requests
import logging
import time
from collections import defaultdict
import pandas

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logging.getLogger('urllib3').setLevel('INFO')

API_URL = 'https://jsonplaceholder.typicode.com/posts'
API_MAX_TRIES = 3
API_DELAY=5

def get_posts(api_url, api_max_tries, api_delay):
    for attempt in range(1, api_max_tries + 1):
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            result = response.json()
            return result
        except Exception as e:
            if attempt < api_max_tries:
                logger.debug(f'Attempt {attempt} failed.  Trying again in {api_delay} seconds. {e}')
                time.sleep(api_delay)
            else:
                logger.debug(f'Final attempt {attempt} failed. {e}')
      
def create_report_pandas(posts_json):
    if data is None:
        return []

    df = pandas.DataFrame(posts_json)

    df['title_length'] = df['title'].str.len()

    df_sorted = df.sort_values(
        by = ['userId', 'title_length'],
        ascending=[True, False]
    )

    result_df = (
        df_sorted
        .groupby('userId', as_index=False)
        .agg(
            postCount=('id', 'count'),
            longestTitle=('title', 'first'),
            longestTitleLength=('title_length', 'first')
        )
    )

    return result_df.to_dict(orient='records')

def create_report(posts_json):
    if data is None:
        return []

    user_stats = defaultdict(lambda: {
            'postCount': 0,
            'longestTitle': '',
            'longestTitleLength': 0
        })
    
    for post in posts_json:
        user_id = post['userId']
        title = post['title']
        title_length = len(title)

        user_stats[user_id]['postCount'] += 1
        if(title_length > user_stats[user_id]['longestTitleLength']):
            user_stats[user_id]['longestTitle'] = title
            user_stats[user_id]['longestTitleLength'] = title_length
    result = [
        {"userId": user_id, **stats} 
        for user_id, stats in sorted(user_stats.items(), key=lambda x: x[1]['longestTitleLength'], reverse=True)
    ]
    return result

if __name__ == '__main__':
    data=get_posts(API_URL, API_MAX_TRIES, API_DELAY)
    summary=create_report_pandas(data)
    logger.info(summary)
        
