import requests

# 判断网络状态 get请求223.6.6.6,返回404为连通,校园网未登录状态因ip劫持将返回200
def whatstatus():
    networkstatus = True

    url = 'http://223.5.5.5'
    try:
        resp = requests.get(url, timeout=2)
        # print(resp.status_code)
        if resp.status_code == 404:
            networkstatus = True
        else:
            networkstatus = False
    except requests.exceptions.Timeout:
        networkstatus = False
    
    return networkstatus