# -*- coding: UTF-8 -*- #
"""
@fileName: search_with_fixedKey
@author: Lzhuan
@time: 2025-05-06 10:51
@Product: PyCharm
"""
import hashlib
import random
import time
import math
import struct
import base64
from urllib.parse import quote
import requests
from loguru import logger
import os


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
    # base64_key = "hw0U/CXr08osoLZsc0qMHijq6zIHT/4oNX+p9gHwb2K10/C7rA2thzmOg1Oavzsa"  # 动态获取 从网页<meta name="tw..">标签的content属性获取
    # # base64_key = get_twitter_site_verification_key_and_nodes()  # 动态获取 从网页<meta name="tw..">标签的content属性获取
    # base64_decode_result = base64_decode(base64_key)
    # print("base64_decode_result: ", base64_decode_result)
    # print("len(base64_decode_result): ", len(base64_decode_result))
    # # 计算并打印结果
    # result_x, result_w = calculate_X_w(base64_decode_result)
    # print("result_x: ", result_x)
    # print("result_w: ", result_w)
    # # get_d = get_dynamic_d('path.txt', base64_decode_result)
    # get_arr = [[239, 189, 146, 144, 157, 195, 199, 90, 255, 89, 182], [114, 255, 152, 205, 210, 116, 17, 34, 209, 255, 218],
    #  [72, 118, 250, 126, 143, 135, 31, 235, 67, 239, 76], [31, 134, 3, 80, 137, 11, 162, 128, 79, 18, 109],
    #  [212, 116, 21, 211, 130, 207, 17, 193, 140, 53, 146], [124, 131, 106, 37, 142, 253, 64, 68, 120, 188, 201],
    #  [155, 43, 191, 107, 169, 199, 17, 82, 210, 243, 198], [234, 201, 152, 153, 205, 254, 20, 37, 166, 158, 238],
    #  [115, 175, 105, 25, 231, 169, 121, 119, 110, 35, 121], [129, 98, 128, 115, 45, 89, 242, 197, 34, 251, 174],
    #  [54, 159, 68, 246, 220, 205, 179, 114, 3, 226, 25], [201, 155, 71, 34, 140, 229, 189, 32, 123, 123, 133],
    #  [69, 119, 112, 194, 170, 38, 229, 84, 25, 23, 173], [105, 177, 115, 80, 80, 11, 223, 45, 251, 233, 109],
    #  [144, 239, 143, 214, 5, 161, 164, 225, 73, 229, 77], [116, 251, 12, 34, 99, 114, 31, 141, 191, 107, 68]]
    # print("get_arr: ", get_arr)
    # get_f = function_f(get_arr, result_x)

    """
    暂时固定从网页获取的key值与path数组, 进行测试
    """
    get_f = "eb39640e3d70a3d70a3d8075c28f5c28f5c4075c28f5c28f5c40e3d70a3d70a3d800"
    return get_f


def contact_arrays(arr1, arr2, arr3):
    t = random.random() * 256
    t_int = [(int(t))]
    # t_int = [207]
    return t_int + arr1 + arr2 + arr3 + [3]


def obtain_transaction_id(_api):
    e = get_dynamic_e()
    logger.info("e: {}".format(e))
    result_bytes = convert_int32_to_bytes(e)
    logger.info("result_bytes: {}".format(result_bytes))
    base64_key = "hw0U/CXr08osoLZsc0qMHijq6zIHT/4oNX+p9gHwb2K10/C7rA2thzmOg1Oavzsa"  # 固定 从网页<meta name="tw..">标签的content属性获取
    base64_decode_result = base64_decode(base64_key)
    logger.info("base64_decode_result: {}".format(base64_decode_result))
    get_f = get_dynamic_f()
    logger.info("get_f: {}".format(get_f))

    enc_api = _api + "!" + str(e) + "obfiowerehiring" + get_f
    logger.info("enc_api: {}".format(enc_api))
    encode_list = list(enc_api.encode('utf-8'))
    logger.info("encode_list: {}".format(encode_list))
    # sha256加密, 输出加密后的数组形式
    digest_arr = hashlib.sha256(enc_api.encode('utf-8')).digest()
    logger.info("digest_arr: {}".format(digest_arr))
    digest_ss = hashlib.sha256(enc_api.encode('utf-8')).hexdigest()
    logger.info("digest_ss: {}".format(digest_ss))
    temp = ['\r', '\n']
    digest_arr = list(digest_arr) + temp
    logger.info("digest_arr: {}".format(digest_arr))
    # 取前16位
    digest_arr_slice = digest_arr[:16]
    logger.info("digest_arr_slice: {}".format(digest_arr_slice))

    # 继续拼接数组
    contact_arrays_result = contact_arrays(base64_decode_result, list(result_bytes), digest_arr_slice)
    logger.info("contact_arrays_result: {}".format(contact_arrays_result))
    logger.info("len(contact_arrays_result): {}".format(len(contact_arrays_result)))

    # map处理
    base = contact_arrays_result[0]
    xor_arr = []
    for i in range(len(contact_arrays_result)):
        if i:
            xor_arr.append(contact_arrays_result[i] ^ base)
        else:
            xor_arr.append(contact_arrays_result[i])
    logger.info("xor_arr: {}".format(xor_arr))
    logger.info("len(xor_arr): {}".format(len(xor_arr)))

    # Sting.fromCharCode(...xor_arr)
    bytes_arr = bytes(xor_arr)
    # 使用 base64.b64encode 编码为 Base64
    base64_bytes = base64.b64encode(bytes_arr)
    # 将 Base64 编码的字节对象解码为字符串
    base64_string = base64_bytes.decode('utf-8')
    # 替换"="
    base64_string = base64_string.replace('=', '')
    logger.info("base64_string: {}".format(base64_string))
    return base64_string


if __name__ == '__main__':
    # 示例调用
    api = "GET!/i/api/graphql/VhUd6vHVmLBcw0uX-6jMLA/SearchTimeline"  # 搜获接口
    tid = obtain_transaction_id(api)
    logger.info("tid: {}".format(tid))

    os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
    os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:10809'

    # 替换为用户登录后的cookies
    cookies = {
        "guest_id_marketing": "v1%3A174600079905711698",
        "guest_id_ads": "v1%3A174600079905711698",
        "guest_id": "v1%3A174600079905711698",
        "personalization_id": "\"v1_D12j4LJOaBchjRqRIcRnzg==\"",
        "kdt": "zJ3LyRfC2RA9QBKeuLfwEXxtbXRip1ixfuj9QzEP",
        "auth_token": "2febe5874adae57abb5f0d7c7f0cf3d6a674bac2",
        "ct0": "7016be3227d88d612701073c787c3bdabb859a4032366cebef505f4f28ed03570ba808a9994a88963e3ad5cbdec74a6c557833fda1023ac448272b7c6d50f215c1c18930a987b1b4c4cfe90f7a52dca5",
        "lang": "en",
        "twid": "u%3D1831257378882461696"
    }
    # 替换为要搜索的关键词
    search_keyword = "原神"
    # 如果search_keyword为汉字，需要先进行urlencode编码
    search_keyword = quote(search_keyword)
    logger.info("search_keyword: {}".format(search_keyword))

    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": f"https://x.com/search?q={search_keyword}&src=typed_query",
        "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        # "x-client-transaction-id": "z0jC2zPqJBwF4295o7yFQ9HnJST9yIAx5/qwZjnOP6Ctehw/dGPCYkj2QUycVXD01ajHBczXUild8tNizryiSoNUsDNjzA",
        "x-client-transaction-id": tid,
        # "x-csrf-token": "7016be3227d88d612701073c787c3bdabb859a4032366cebef505f4f28ed03570ba808a9994a88963e3ad5cbdec74a6c557833fda1023ac448272b7c6d50f215c1c18930a987b1b4c4cfe90f7a52dca5",
        "x-csrf-token": cookies['ct0'],  # 用户登录后获取的csrf_token
        "x-twitter-active-user": "yes",
        "x-twitter-auth-type": "OAuth2Session",
        "x-twitter-client-language": "en"
    }

    url = "https://x.com/i/api/graphql/VhUd6vHVmLBcw0uX-6jMLA/SearchTimeline"

    params = {
        "variables": f'{{"rawQuery":"{search_keyword}","count":20,"querySource":"typed_query","product":"Top"}}',
        "features": '{"rweb_video_screen_enabled":false,"profile_label_improvements_pcf_label_in_post_enabled":true,"rweb_tipjar_consumption_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":false,"responsive_web_grok_analyze_post_followups_enabled":true,"responsive_web_jetfuel_frame":false,"responsive_web_grok_share_attachment_enabled":true,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"responsive_web_grok_show_grok_translated_post":false,"responsive_web_grok_analysis_button_from_backend":true,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_grok_image_annotation_enabled":true,"responsive_web_enhance_cards_enabled":false}'
    }
    # 翻页参数, cursor: 翻页标识符, 从上一次请求的结果中获取
    params_fy = {
        'variables': f'{{"rawQuery":"{search_keyword}","count":20,"cursor":"DAACCgACGqPFSHfAJxAKAAMao8VId7_Y8AgABAAAAAILAAUAAAD8RW1QQzZ3QUFBZlEvZ0dKTjB2R3AvQUFBQUJVYUpNVnVQVm9CNmhwMHJEVlZHc0NlR3BnOUdoTGEwV3dhb0tZNVJadHhpaG9aZkVKeTJpRjJHcDIzWXExYmdFZ2FreFBZdVJyaEFocGdBVm9pR3BCckdwVGptVTZiWVlBYW9iUVIxeFloZHhxZ2NycEIydkNKR29mVHNiNGEwWUVhZEhHdmdWc3d6aHFlUVNDdUZ0QnBHcUI3c3JOYW9CRWFsd2xlL0JvQnVocHZvbUxWMjNJQUdwOVhtZUNXWWE0YW9IelBWcGRnNlJwMGR3RHRtNkYyR3FPM0YrdmFJSWs9CAAGAAAAAAgABwAAAAAMAAgKAAEaGXxCctohdgAAAA","querySource":"typed_query","product":"Top"}}',
        'features': '{"rweb_video_screen_enabled":false,"profile_label_improvements_pcf_label_in_post_enabled":true,"rweb_tipjar_consumption_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"premium_content_api_read_enabled":false,"communities_web_enable_tweet_community_results_fetch":true,"c9s_tweet_anatomy_moderator_badge_enabled":true,"responsive_web_grok_analyze_button_fetch_trends_enabled":false,"responsive_web_grok_analyze_post_followups_enabled":true,"responsive_web_jetfuel_frame":false,"responsive_web_grok_share_attachment_enabled":true,"articles_preview_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"responsive_web_grok_show_grok_translated_post":false,"responsive_web_grok_analysis_button_from_backend":true,"creator_subscriptions_quote_tweet_preview_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_grok_image_annotation_enabled":true,"responsive_web_enhance_cards_enabled":false}'
    }

    response = requests.get(url, headers=headers, cookies=cookies, params=params)
    try:
        logger.info("response.status_code: {}".format(response.status_code))
        logger.info("response.text: {}".format(response.json()))
        # 解析json数据
    except Exception as e1:
        logger.error("解析json数据失败: {}".format(e1))
