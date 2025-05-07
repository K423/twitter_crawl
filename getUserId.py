import requests
from loguru import logger
import os
import random
import time


def get_htmlInfo(_account_name):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://x.com",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }
    url = f"https://x.com/{_account_name}/"
    response = requests.get(url, headers=headers)
    return response.text


def parse_cookie(_html):
    import re
    # 使用正则表达式匹配 document.cookie="xxx"
    _gt = ''
    cookie_pattern = r'document\.cookie\s*=\s*"([^"]+)"'
    matches = re.findall(cookie_pattern, _html)
    if matches:
        for match in matches:
            logger.info(f"Cookie: {match}")
            if 'gt=' in match:
                _gt = match.split('gt=')[1].split(';')[0]
    else:
        logger.info("No cookie found.")
    return _gt


def get_user_id(_ac, _gt):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "origin": "https://x.com",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://x.com/",
        "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Google Chrome\";v=\"134\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
        "x-client-transaction-id": "Os7a6RTuRN8qd551UcCISYc9Wg633DGC2yJ5qhHIuSudLFQRaLVsSez9GHgTAjpQdCRkrjl2l/IqJoOBAN0fQ6UUpu7mOQ",
        # "x-guest-token": "1904820053817909356",
        "x-guest-token": _gt,
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": "zh-cn"
    }

    url = "https://api.x.com/graphql/32pL5BWe9WKeSK1MoPvFQQ/UserByScreenName"
    params = {
        "variables": f"{{\"screen_name\":\"{_ac}\"}}",
        "features": "{\"hidden_profile_subscriptions_enabled\":true,\"profile_label_improvements_pcf_label_in_post_enabled\":true,\"rweb_tipjar_consumption_enabled\":true,\"responsive_web_graphql_exclude_directive_enabled\":true,\"verified_phone_label_enabled\":false,\"subscriptions_verification_info_is_identity_verified_enabled\":true,\"subscriptions_verification_info_verified_since_enabled\":true,\"highlights_tweets_tab_ui_enabled\":true,\"responsive_web_twitter_article_notes_tab_enabled\":true,\"subscriptions_feature_can_gift_premium\":true,\"creator_subscriptions_tweet_preview_api_enabled\":true,\"responsive_web_graphql_skip_user_profile_image_extensions_enabled\":false,\"responsive_web_graphql_timeline_navigation_enabled\":true}",
        "fieldToggles": "{\"withAuxiliaryUserLabels\":false}"
    }
    response = requests.get(url, headers=headers, params=params)
    logger.info(f"User ID: {response.json()['data']['user']['result']['rest_id']}")
    return response.json()['data']['user']['result']['rest_id']


if __name__ == '__main__':
    os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
    os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'

    userName = "houkaistarrail"  # 请求用户的昵称
    html = get_htmlInfo(userName)
    gt = parse_cookie(html)
    time.sleep(random.randint(2, 3))
    userId = get_user_id(userName, gt)
