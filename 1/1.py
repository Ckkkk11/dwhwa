import requests
import gzip
import json

url = "https://jw1.hustwenhua.net/jwglxt/kbcx/xskbcx_cxXsgrkb.html?gnmkdm=N2151"

headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://jw1.hustwenhua.net",
    "Referer": "https://jw1.hustwenhua.net/jwglxt/kbcx/xskbcx_cxXskbcxIndex.html?gnmkdm=N2151&layout=default",
    "X-Requested-With": "XMLHttpRequest"
}

cookies = {
    "JSESSIONID": "67CBD6939B8B4EC01C141D132E27C5B2",
    "route": "cf268aa417e3b0063890a14afc24f195"
}

# 替换成抓包拿到的 payload
payload = "xnm=xxx&xqm=xxx&..."

resp = requests.post(url, headers=headers, cookies=cookies, data=payload, timeout=15)

# gzip 解压
if resp.headers.get("Content-Encoding") == "gzip":
    data = gzip.decompress(resp.content).decode("utf-8")
else:
    data = resp.text

print("状态码：", resp.status_code)
try:
    js = json.loads(data)
    print(json.dumps(js, ensure_ascii=False, indent=2))
except Exception:
    print("原始返回：", data)
