# -*- coding: UTF-8 -*- #
"""
@fileName: get_gt_cookie.py
@author: Lzhuan
@time: 2025-03-26 14:18
@Product: PyCharm
"""
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


# OWNiZWJhYWEtNjY3Ni00M2ZkLThlOWUtMDAyOTcwZWY2ZjEz

def parse_cookie(_html):
    import re
    # 使用正则表达式匹配 document.cookie="xxx"
    gt = ''
    cookie_pattern = r'document\.cookie\s*=\s*"([^"]+)"'
    matches = re.findall(cookie_pattern, _html)
    if matches:
        for match in matches:
            logger.info(f"Cookie: {match}")
            if 'gt=' in match:
                gt = match.split('gt=')[1].split(';')[0]
    else:
        logger.info("No cookie found.")
    return gt


if __name__ == '__main__':
    ac = 'elonmusk'
    html = get_htmlInfo(ac)
    gt_cookie = parse_cookie(html)
    logger.info(f"GT Cookie: {gt_cookie}")
