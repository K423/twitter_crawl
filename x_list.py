# -*- coding: UTF-8 -*- #
"""
@fileName: x_list
@author: Lzhuan
@time: 2025-03-26 16:01
@Product: PyCharm
"""
import random
import time

import os

os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
import requests
from loguru import logger


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


def get_user_list(_userId, _gt):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        # 校验 authorization  目前是固定的,可以直接从js中获取
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
        # 可有可无 x-client-trace-id
        "x-client-transaction-id": "Cx8e78pPXb86JKKEjvyViuBpWRsGcf4YfZ+piqnlNt/SC526PIAlvMCdPMBWjGHJsoUgnwge8jXYjUFUfg1ZX0CihBvDCA",
        # 校验 x-guest-token  直接从网页中获取, 有时效性
        # "x-guest-token": "1904800925094732277",
        "x-guest-token": _gt,
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": "zh-cn"
    }

    _url = "https://api.x.com/graphql/oEZZ1LnECXaSquxLjQd_bw/UserTweets"
    _params = {
        "variables": f"{{\"userId\":\"{_userId}\",\"count\":20,\"includePromotedContent\":true,\"withQuickPromoteEligibilityTweetFields\":true,\"withVoice\":true,\"withV2Timeline\":true}}",
        "features": "{\"rweb_video_screen_enabled\":false,\"profile_label_improvements_pcf_label_in_post_enabled\":true,\"rweb_tipjar_consumption_enabled\":true,\"responsive_web_graphql_exclude_directive_enabled\":true,\"verified_phone_label_enabled\":false,\"creator_subscriptions_tweet_preview_api_enabled\":true,\"responsive_web_graphql_timeline_navigation_enabled\":true,\"responsive_web_graphql_skip_user_profile_image_extensions_enabled\":false,\"premium_content_api_read_enabled\":false,\"communities_web_enable_tweet_community_results_fetch\":true,\"c9s_tweet_anatomy_moderator_badge_enabled\":true,\"responsive_web_grok_analyze_button_fetch_trends_enabled\":false,\"responsive_web_grok_analyze_post_followups_enabled\":false,\"responsive_web_jetfuel_frame\":false,\"responsive_web_grok_share_attachment_enabled\":true,\"articles_preview_enabled\":true,\"responsive_web_edit_tweet_api_enabled\":true,\"graphql_is_translatable_rweb_tweet_is_translatable_enabled\":true,\"view_counts_everywhere_api_enabled\":true,\"longform_notetweets_consumption_enabled\":true,\"responsive_web_twitter_article_tweet_consumption_enabled\":true,\"tweet_awards_web_tipping_enabled\":false,\"responsive_web_grok_analysis_button_from_backend\":true,\"creator_subscriptions_quote_tweet_preview_enabled\":false,\"freedom_of_speech_not_reach_fetch_enabled\":true,\"standardized_nudges_misinfo\":true,\"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled\":true,\"rweb_video_timestamps_enabled\":true,\"longform_notetweets_rich_text_read_enabled\":true,\"longform_notetweets_inline_media_enabled\":true,\"responsive_web_grok_image_annotation_enabled\":true,\"responsive_web_enhance_cards_enabled\":false}",
        "fieldToggles": "{\"withArticlePlainText\":false}"
    }
    # 未登录状态下, 只能获取到20条数据, 后续需要登录获取更多
    _response = requests.get(_url, headers=headers, params=_params)
    return _response.json()


def get_user_list_with_cookie(_userId, _gt):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        # 校验 authorization  目前是固定的,可以直接从js中获取
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
        # 可有可无 x-client-trace-id
        # "x-client-transaction-id": "Cx8e78pPXb86JKKEjvyViuBpWRsGcf4YfZ+piqnlNt/SC526PIAlvMCdPMBWjGHJsoUgnwge8jXYjUFUfg1ZX0CihBvDCA",
        # 校验 x-guest-token  直接从网页中获取, 有时效性
        # "x-guest-token": "1904800925094732277",
        "x-guest-token": _gt,
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": "zh-cn",
        # 登陆状态下的 x-csrf-token
        "x-csrf-token": "xxx",
    }

    _url = "https://api.x.com/graphql/oEZZ1LnECXaSquxLjQd_bw/UserTweets"
    _params = {
        "variables": "{\"userId\":\"1412998764701249542\",\"count\":20,\"cursor\":\"DAABCgABGm9Mzgy__-oKAAIaX4LMppYA4QgAAwAAAAIAAA\",\"includePromotedContent\":true,\"withQuickPromoteEligibilityTweetFields\":true,\"withVoice\":true,\"withV2Timeline\":true}",
        "features": "{\"rweb_video_screen_enabled\":false,\"profile_label_improvements_pcf_label_in_post_enabled\":true,\"rweb_tipjar_consumption_enabled\":true,\"responsive_web_graphql_exclude_directive_enabled\":true,\"verified_phone_label_enabled\":false,\"creator_subscriptions_tweet_preview_api_enabled\":true,\"responsive_web_graphql_timeline_navigation_enabled\":true,\"responsive_web_graphql_skip_user_profile_image_extensions_enabled\":false,\"premium_content_api_read_enabled\":false,\"communities_web_enable_tweet_community_results_fetch\":true,\"c9s_tweet_anatomy_moderator_badge_enabled\":true,\"responsive_web_grok_analyze_button_fetch_trends_enabled\":false,\"responsive_web_grok_analyze_post_followups_enabled\":true,\"responsive_web_jetfuel_frame\":false,\"responsive_web_grok_share_attachment_enabled\":true,\"articles_preview_enabled\":true,\"responsive_web_edit_tweet_api_enabled\":true,\"graphql_is_translatable_rweb_tweet_is_translatable_enabled\":true,\"view_counts_everywhere_api_enabled\":true,\"longform_notetweets_consumption_enabled\":true,\"responsive_web_twitter_article_tweet_consumption_enabled\":true,\"tweet_awards_web_tipping_enabled\":false,\"responsive_web_grok_analysis_button_from_backend\":true,\"creator_subscriptions_quote_tweet_preview_enabled\":false,\"freedom_of_speech_not_reach_fetch_enabled\":true,\"standardized_nudges_misinfo\":true,\"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled\":true,\"rweb_video_timestamps_enabled\":true,\"longform_notetweets_rich_text_read_enabled\":true,\"longform_notetweets_inline_media_enabled\":true,\"responsive_web_grok_image_annotation_enabled\":true,\"responsive_web_enhance_cards_enabled\":false}",
        "fieldToggles": "{\"withArticlePlainText\":false}"
    }
    cookies = {
        "auth_token": "xx",
        "ct0": "xx",
    }
    _response = requests.get(_url, headers=headers, params=_params, cookies=cookies)
    return _response.json()


if __name__ == '__main__':
    account_name = "honkaistarrail"
    html = get_htmlInfo(account_name)
    gt = parse_cookie(html)
    time.sleep(random.randint(2, 3))
    user_id = get_user_id(account_name, gt)
    time.sleep(random.randint(2, 3))
    user_list = get_user_list(user_id, gt)
    logger.info(user_list)
    # 登陆状态下获取更多数据
    # user_list_with_cookie = get_user_list_with_cookie(user_id, gt)
    # logger.info(user_list_with_cookie)
