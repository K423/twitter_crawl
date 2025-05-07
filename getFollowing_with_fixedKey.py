# -*- coding: UTF-8 -*- #
"""
@fileName: getFollowing_with_fixedKey
@author: Lzhuan
@time: 2025-05-06 14:05
@Product: PyCharm
"""
import hashlib
import random
import time
import math
import struct
import base64
from loguru import logger
import requests


def get_dynamic_e():
    """
    获取动态时间差

    该函数计算当前时间与一个预设时间的差值，并将差值转换为距离1970年1月1日00:00:00 UTC的秒数（不包含毫秒）
    返回值为整数，表示秒数

    Returns:
        int: 当前时间与预设时间的差值，单位为秒
    """
    # 获取当前时间的毫秒数
    now_time = int(time.time() * 1000)
    # now_time = 1723779373708  # 测试用
    # 预设时间的毫秒数，这里使用了一个特定的时间戳（1682924400秒）转换为毫秒
    key = 1682924400 * 1000
    # 计算当前时间与预设时间的差值，结果为毫秒数
    now_time_key = now_time - key
    # 将毫秒数转换为秒，并保留小数点后两位
    result_e = round(now_time_key / 1000, 2)
    # 返回转换后的秒数，向下取整
    return math.floor(result_e)


def convert_int32_to_bytes(dynamic_e):
    # 将32位整数转换为4个8位整数
    # 'I' 表示无符号整数（32位），'BBBB' 表示四个无符号字节（8位）
    values = struct.pack('I', dynamic_e)

    # 提取四个8位整数
    byte_values = struct.unpack('BBBB', values)

    return byte_values


def base64_decode(n):
    # 解码 base64 字符串
    decoded_bytes = base64.b64decode(n)

    # 将解码后的字节转换为整数列表
    int_list = [byte for byte in decoded_bytes]

    return int_list  # 返回整数列表，Python 中没有 Uint8Array，这里使用 list 表示


def get_dynamic_f():
    """
    暂时固定从网页获取的key值与path数组, 进行测试
    """
    get_f = "eb39640e3d70a3d70a3d8075c28f5c28f5c4075c28f5c28f5c40e3d70a3d70a3d800"
    return get_f


def contact_arrays(arr1, arr2, arr3):
    t = random.random() * 256
    t_int = [(int(t))]
    return t_int + arr1 + arr2 + arr3 + [3]


def obtain_transaction_id(_api):
    e = get_dynamic_e()
    logger.info(f"Dynamic e: {e}")
    result_bytes = convert_int32_to_bytes(e)
    logger.info(f"result_bytes: {result_bytes}")
    base64_key = "hw0U/CXr08osoLZsc0qMHijq6zIHT/4oNX+p9gHwb2K10/C7rA2thzmOg1Oavzsa"  # 固定 从网页<meta name="tw..">标签的content属性获取
    base64_decode_result = base64_decode(base64_key)
    logger.info(f"base64_decode_result: {base64_decode_result}")
    get_f = get_dynamic_f()
    logger.info(f"get_f: {get_f}")

    enc_api = _api + "!" + str(e) + "obfiowerehiring" + get_f
    logger.info(f"enc_api: {enc_api}")
    encode_list = list(enc_api.encode('utf-8'))
    logger.info(f"encode_list: {encode_list}")
    # sha256加密, 输出加密后的数组形式
    digest_arr = hashlib.sha256(enc_api.encode('utf-8')).digest()
    logger.info(f"digest_arr: {digest_arr}")
    digest_hex = hashlib.sha256(enc_api.encode('utf-8')).hexdigest()
    logger.info(f"digest_hex: {digest_hex}")
    temp = ['\r', '\n']
    digest_arr = list(digest_arr) + temp
    logger.info(f"digest_arr: {digest_arr}")
    # 取前16位
    digest_arr_slice = digest_arr[:16]
    logger.info(f"digest_arr_slice: {digest_arr_slice}")

    # 拼接数组
    contact_arrays_result = contact_arrays(base64_decode_result, list(result_bytes), digest_arr_slice)
    logger.info(f"contact_arrays_result: {contact_arrays_result}")
    logger.info(f"len(contact_arrays_result): {len(contact_arrays_result)}")

    # map处理
    base = contact_arrays_result[0]
    xor_arr = []
    for i in range(len(contact_arrays_result)):
        if i:
            xor_arr.append(contact_arrays_result[i] ^ base)
        else:
            xor_arr.append(contact_arrays_result[i])
    logger.info(f"xor_arr: {xor_arr}")
    logger.info(f"len(xor_arr): {len(xor_arr)}")

    # Sting.fromCharCode(...xor_arr)
    bytes_arr = bytes(xor_arr)
    # 使用 base64.b64encode 编码为 Base64
    base64_bytes = base64.b64encode(bytes_arr)
    # 将 Base64 编码的字节对象解码为字符串
    base64_string = base64_bytes.decode('utf-8')
    # 替换"="
    base64_string = base64_string.replace('=', '')
    logger.info(f"base64_string: {base64_string}")
    return base64_string


def get_following_with_fixedKey(_userNickname, _userId, _tid, _cookies):
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": f"https://x.com/{_userNickname}/following",
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "x-client-transaction-id": _tid,
        "x-client-uuid": "b939b973-06c1-4f30-93e7-469f84ffe9c6",
        "x-csrf-token": _cookies['ct0'],
        "x-twitter-active-user": "yes",
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-client-language": "en"
    }

    url = "https://x.com/i/api/graphql/zx6e-TLzRkeDO_a7p4b3JQ/Following"
    params = {
        'variables': f'{{"userId":"{_userId}","count":20,"includePromotedContent":false}}',
        'features': '{"rweb_video_screen_enabled":false,"profile_label_improvements_pcf_label_in_post_enabled":true,"rweb_tipjar_consumption_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":false,"responsive_web_grok_analyze_post_followups_enabled":true,"responsive_web_jetfuel_frame":false,"responsive_web_grok_share_attachment_enabled":true,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"responsive_web_grok_show_grok_translated_post":false,"responsive_web_grok_analysis_button_from_backend":true,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_grok_image_annotation_enabled":true,"responsive_web_enhance_cards_enabled":false}'
    }
    params_fy = {  # 翻页
        'variables': f'{{"userId":"{_userId}","count":20,"cursor":"","includePromotedContent":false}}',
        'features': '{"rweb_video_screen_enabled":false,"profile_label_improvements_pcf_label_in_post_enabled":true,"rweb_tipjar_consumption_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":false,"responsive_web_grok_analyze_post_followups_enabled":true,"responsive_web_jetfuel_frame":false,"responsive_web_grok_share_attachment_enabled":true,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"responsive_web_grok_show_grok_translated_post":false,"responsive_web_grok_analysis_button_from_backend":true,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_grok_image_annotation_enabled":true,"responsive_web_enhance_cards_enabled":false}'
    }
    response = requests.get(url, headers=headers, cookies=_cookies, params=params)

    try:
        logger.info(f"response.status_code: {response.status_code}")
        logger.info(f"response.text: {response.json()}")
    except Exception as e:
        logger.error(f"Error: {e}")


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

    proxies = {
        "http": "http://127.0.0.1:10809",
        "https": "http://127.0.0.1:10809",
    }

    userName = "houkaistarrail"  # 请求用户的昵称
    html = get_htmlInfo(userName)
    gt = parse_cookie(html)
    time.sleep(random.randint(2, 3))
    userId = get_user_id(userName, gt)
    time.sleep(random.randint(2, 3))

    cookies = {
    }

    api = "GET!/i/api/graphql/zx6e-TLzRkeDO_a7p4b3JQ/Following"  # 关注接口
    tid = obtain_transaction_id(api)
    logger.info(f"Transaction ID: {tid}")

    get_following_with_fixedKey(userName, userId, tid, cookies)
