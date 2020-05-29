import requests

headers = {
    'authority': 'www.vivino.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'pl-PL,pl;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cookie': 'recently_viewed=b1ptSHNWQlZYVW85L05QSUtGYUc0Zz09LS12VU9CcGpYVG1ybVN5UUlDK0hJcHlBPT0%3D--3440aa9660ee7eb906651e29c15d21aab2a098e9; client_cache_key=Z0ZsVDVZZXNOZTByVHJlSHQ0eHllR3NyRjlTdzZsOVBJV0VsNlMzbHVwZz0tLVN2b3ZMVy8rYXVQbmhtMXpDQ1ZrSHc9PQ%3D%3D--fed390240b8140debda8e4dd253688b612d7eaac; _ga=GA1.2.78399984.1590586099; _gid=GA1.2.771466013.1590586099; __auc=e93306b41725651c3780f3ea090; _hjid=7c24bc4e-3a06-48a2-8c3a-332d39c96a52; _hp2_ses_props.3503103446=%7B%22r%22%3A%22https%3A%2F%2Fwww.vivino.com%2F%22%2C%22ts%22%3A1590591401632%2C%22d%22%3A%22www.vivino.com%22%2C%22h%22%3A%22%2Fsearch%2Fwines%22%2C%22q%22%3A%22%3Fq%3Dfoo%2Bbar%22%7D; __asc=1e1e641717256a2befd4f9616dc; _ruby-web_session=YVBPSDFOSndCQmpwRkprVlFxNDVTK09yK3V6a09sN3hPQzkvUjRrWkszZU0zKzdpMk5ZV0ZZTmpFNUtocWRVcGh5ZzNJYmkvQitrN2lmaE9pa0wrRWZUKyt4VmpnNTE3eFppN1gyYVlIdW12T2ZPMXM2USs3enQyemVmdlpQYXJ4ek5LS3VVQnhRclJSQ05LUUVVWDRsUEUrUWVteGpKZWhXSGV1K0wxbEM3V0owT3ZJZzI1SXowbDM5RHdJMnNDS09IL2ZPTVNsMVBWTFVZeG44Wmk4d28xZktYWi9rb3l5UjhXQTJJdXdndWN5TnBaUm96NWN0UmpHSHZpaThVNnQ4NjdLNk5lWXdOSEFkZ1g5SW1vQ3c9PS0tYUJsOC9CNnAwbEQ4SVR4ZUtkODhiUT09--1565c8788df45dec18a68166f62a161125f9c921; _hp2_id.3503103446=%7B%22userId%22%3A%223595900987555922%22%2C%22pageviewId%22%3A%228652455435654195%22%2C%22sessionId%22%3A%22820078683572922%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    'if-none-match': 'W/"0995ca344ee52db4047c29cdbaa9628f"',
}


def bar(wine):
    params = (
        ('q', wine),
    )
    response = requests.get('https://www.vivino.com/search/wines', headers=headers, params=params)
    return response

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('https://www.vivino.com/search/wines?q=Baron+De+Ley+Finca+Monasterio+Rioja', headers=headers)
