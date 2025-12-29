import requests
import logging
import time
from collections import defaultdict

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

API_URL = 'https://jsonplaceholder.typicode.com/posts'
API_MAX_RETRIES = 3
API_RETRY_DELAY_SECONDS = 2
API_API_TIMEOUT_SECONDS = 5

def fetch_data(api_url, max_retries, retry_delay_seconds, api_timeout_seconds):
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(api_url, timeout=api_timeout_seconds)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.debug(f'Attempt failed to fetch from {API_URL}, current try number {attempt}')
            if attempt < max_retries:
                time.sleep(retry_delay_seconds)
            else:
                logger.error(f'Failed to fetch from {API_URL}, current try number {attempt}.  Max retries {max_retries} exceeded,')
                return []

def get_summary_report_without_pandas(data):
    if not data:
        return []
    
    user_stats = defaultdict(lambda: {
        'postCount': 0,
        'longestTitle': '', 
        'longestTitleLength': 0
    })

    for post in data:
        user_id = post['userId']
        title = post['title']
        title_length = len(title)

        user_stats[user_id]['postCount'] += 1

        if title_length > user_stats[user_id]['longestTitleLength']:
            user_stats[user_id]['longestTitle'] = title
            user_stats[user_id]['longestTitleLength'] = title_length

    result = [
        { "userId": user_id, **stats }
        # for user_id, stats in sorted(user_stats.items(), key=lambda x:x[1]['longestTitleLength'], reverse=True)
        for user_id, stats in sorted(user_stats.items(), reverse=True) # by default it sorts by userId as this is the key
    ]

    return result

if __name__ == "__main__":
    data = fetch_data(API_URL, API_MAX_RETRIES, API_RETRY_DELAY_SECONDS, API_API_TIMEOUT_SECONDS)
    results = get_summary_report_without_pandas(data)
    logger.info(results)