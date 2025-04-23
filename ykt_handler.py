import requests

# TODO: Define the request route
def get_room_bill(room = "417"):
    """
    Args:
        room: str, the code like 417 room address

    Return:
        room: str
        current_price: str
        current_time: str
    """
    url = "https://ykt.ujs.edu.cn/charge/feeitem/getThirdData"

    headers = {
        "Host": "ykt.ujs.edu.cn",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "synjones-auth": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiIxIiwiZmxhZyI6IjAwMDAwIiwidXNlcl9uYW1lIjoiakpOUCUyQm9leVMySGVPQmVHcjZhYklNYjBtUURUdEtVemNOdG9OJTJCJTJCVUVlRSUzRCIsIm1vYmlsZSI6IiIsImxvZ2luRnJvbSI6IndlY2hhdC1tcCIsInV1aWQiOiIwMTRmNDc2OWZlMWM5OWY1NTYxZmY3OWFiZWVmMWNmMiIsImNsaWVudF9pZCI6Im1vYmlsZV9zZXJ2aWNlX3BsYXRmb3JtIiwiaXNfcGFzc3dvcmRfZXhwaXJlZCI6ZmFsc2UsImlzX2ZpcnN0X2xvZ2luIjpmYWxzZSwic25vIjoiMzIzMDYxMTA4MSIsInNjb3BlIjpbImFsbCJdLCJsb2dpbnR5cGUiOiJzc28iLCJuYW1lIjoi55ub5a2Q5ra1IiwiaWQiOjE5NTExLCJleHAiOjE3NTEzODI3NTksImp0aSI6ImYwOWQ0OGEyLTk2OWMtNGU5MS04ZDg4LTkxNGQ4Mjg4NWQ5NyJ9.BexIcf6vSWblqRjE5GSN2TCpr-J2Hb3CKkFHREIkNng",
        "Authorization": "Basic Y2hhcmdlOmNoYXJnZV9zZWNyZXQ=",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x63090c33) XWEB/13487 Flue",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://ykt.ujs.edu.cn",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://ykt.ujs.edu.cn/charge-app/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": 'iPlanetDirectoryPro=200QmSYAlNcqNcLGXR12KP; JSESSIONID=jIL0h-40BnIfsw80qhrqbGbmgjo91FHKZF3GKtBx; TGC="third_login:TGT-6c0b9ffe7e7643e7bd5d501ee08ffe40"; error_times=0; locSession=ce20154f303d0b46762febe458889352'
    }

    data = {
        "feeitemid": "408",
        "type": "IEC",
        "level": "4",
        "campus": "校本部",
        "building": "F区",
        "floor": "7",
        "room": f"7-4-{room}"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        res_json = response.json()
        try:
            show_data = res_json["map"]["showData"]
            room_address = show_data["房间信息"]
            current_time = show_data["查询时间"]
            current_price = show_data["当前剩余"]
            return (room_address, current_price, current_time)
        except (KeyError, TypeError):
            print("数据格式错误或缺失字段")
            return None
    else:
        print(f"请求失败，状态码：{response.status_code}")
        return None


if __name__ == "__main__":
    info = get_room_bill()
    if info:
        print(info)
