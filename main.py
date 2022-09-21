# express 示例流程
import json
import requests

BASE_URL = 'http://express-api.fw-blog.com/api'
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9leHByZXNzLWFwaS5mdy1ibG9nLmNvbVwvYXBpXC90b2tlbiIsImlhdCI6MTY2MzY2NzA5NywiZXhwIjoxNjYzNzUzNDk3LCJuYmYiOjE2NjM2NjcwOTcsImp0aSI6IjQzdnU2Y0hFbmZ1REJ6dG8iLCJzdWIiOjIsInBydiI6IjU4OGQ1YjMyNTBhMzE1MTFiNmU5YTViYzExNTkzYTZmM2MwYTVlYWUifQ.OlV7-kGmJ-En80CQFTRgTBDg0e3y6CHmKsC4Yp1h1K8"


def get_token():
    """
    获取登录token
    :return:
    """
    if TOKEN != "":
        return TOKEN
    content = get_content('response/login.json')
    header = {
        'Content-Type': 'application/json',
    }
    response = requests.post("{}/token".format(BASE_URL), data=content, headers=header)
    res = json.loads(response.content)
    # 将返回的token填写到TOKEN中
    print(res)


def get_rate():
    """
    获取价格费率
    :return:
    """
    content = get_content('response/rate.json')
    response = requests.post("{}/order-evaluate".format(BASE_URL), data=content, headers=get_headers())
    res = json.loads(response.content)
    print(res)


def waybill_add():
    """
    创建运单
    :return:
    """
    content = get_content('response/waybill_add.json')
    response = requests.post("{}/order".format(BASE_URL), data=content, headers=get_headers())
    res = json.loads(response.content)
    print(res)


def waybill_edit():
    """
    运单更新
    :return:
    """
    content = get_content('response/waybill_edit.json')
    response = requests.post("{}/order-edit".format(BASE_URL), data=content, headers=get_headers())
    res = json.loads(response.content)
    print(res)


def waybill_confirm():
    """
    运单确认
    :return:
    """
    content = {
        "sn": "SN071008230000000108"
    }
    response = requests.post("{}/order-confirm".format(BASE_URL), data=content, headers=get_headers())
    res = json.loads(response.content)
    print(res)


def waybill_cancel():
    """
    取消运单
    :return:
    """
    content = {
        "sn": "SN071008230000000108"
    }
    response = requests.post("{}/order-cancel".format(BASE_URL), data=content, headers=get_headers())
    res = json.loads(response.content)
    print(res)


def get_label():
    """
    获取label
    :return:
    """
    content = {
        "sn": [
            "SN0000000052",
            "SN0000000053",
            "SN0000000054"
        ]
    }
    response = requests.post("{}/order-label".format(BASE_URL), data=content, headers=get_headers())
    res = json.loads(response.content)
    print(res)


def get_content(file_url):
    """
    获取json文件内容
    :param file_url:
    :return:
    """
    file = open(file_url, encoding='utf-8')
    paramJson = file.read()
    data = json.loads(paramJson)
    return json.dumps(data)


def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(TOKEN)
    }


if __name__ == '__main__':
    # get_token()
    get_label()
