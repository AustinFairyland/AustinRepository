# coding: utf8
""" 
@File: _main.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2024-02-24
"""
from __future__ import annotations

import os
import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import requests
from Crypto.Cipher import AES
import m3u8


class AuraVideo:

    @staticmethod
    def download():
        url = "https://vod.cn-shanghai.aliyuncs.com"
        parameters = {
            "AccessKeyId": "STS.NU1vgKKhhgU9rwsyDNBbiqFRJ",
            "Action": "GetPlayInfo",
            "AuthInfo": {
                "CI": "0iDJM19uxyq8oioheE3mXeVUgI0xeyHSaSKkbpIb31E+e7xrOyG8ZwuUB+gwMwRn4ay2Z2p4fQMNJWv20Je3Va/v3wL6/MithxEqnj6iXF0=",
                "Caller": "sjrgQnWv0gwn+A6TfHLwXPwTBD3xXRPoGgEPD7MxYWY=",
                "ExpireTime": "2024-02-24T11:38:44Z",
                "MediaId": "9882bf28ec7f4bbdb7d82296249b815a",
                "PlayDomain": "mv.aura-el.com",
                "Signature": "UV4abSM8eLDOwoJF9okXjyS1BIw=",
            },
            "AuthTimeout": 7200,
            "Channel": "HTML5",
            "Definition": "",
            "Format": "JSON",
            "Formats": "",
            "PlayConfig": {},
            "PlayerVersion": "2.8.2",
            "Rand": "HlbsCu9U1RoCAyYE0MMYWF7G2fzbqTj4OCy3daD4gCbHEPg7VN+MVXoxwUtYkkJNjf8kX/u7wwN4iQxrus40Zg==",
            "ReAuthInfo": {},
            "SecurityToken": "CAIShwN1q6Ft5B2yfSjIr5aEPd3/prdJ0JfScFHCnUQbTu1FnoP5qDz2IHpKeXduAeAXs/o0mmhZ7/YYlrMqEMAYHRWfMpsrssgOrV36JpLFst2J6r8JjsV9hsgsvkepsvXJasDVEfl2E5XEMiIR/00e6L/+cirYpTXHVbSClZ9gaPkOQwC8dkAoLdxKJwxk2t14UmXWOaSCPwLShmPBLUxmvWgGl2Rzu4uy3vOd5hfZp1r8xO4axeL0PoP2V81lLZplesqp3I4Sc7baghZU4glr8qlx7spB5SyVktyWGUhJ/zaLIoit7NpjfiB0eoQAPopFp/X6jvAawPLUm9bYxgphB8R+Xj7DZYaux7GzeoWTO80+aKzwNlnUz9mLLeOViQ4/Zm8BPw44ELhIaF0IUExzEW+FevL/pgmQPl/+FJLoiv9mjcBHqHzz5sePKlS1RLGU7D0VIJdUbTlzbUBLgzK5Iv5bLVcSKwI+V+yPMax3bQFDr53vsTbbXzZb0mptuPnzdwJ4TWbrgkeUGoABIVO1NMayMRQbKyc+RP0tImUdYJEN/KFIHI29Faazynp0On0IU5b4LVQr58ewtzXET9oOfynSxoayl4XPg6OfOHcs2IcRGpicFprRf8o3Mca0WlNVVqAkIQR1X5KRTRQmInZs6aUqjwC4UuyB7FB9uzS/h72zAUAXHWc8hUKRc5kgAA==",
            "SignatureMethod": "HMAC-SHA1",
            "SignatureNonce": "8bce3231-436b-4f7f-9990-c0e73ac0fada",
            "SignatureVersion": 1,
            "StreamType": "video",
            "Version": "2017-03-21",
            "VideoId": "9882bf28ec7f4bbdb7d82296249b815a",
            "Signature": "hOlI2GlLzPEsrNkKUnHxvGRTb9g=",
        }
        request_headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip,deflate,br,zstd",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "vod.cn-shanghai.aliyuncs.com",
            "Origin": "https://yun.aura.cn",
            "Pragma": "no-cache",
            "Referer": "https://yun.aura.cn/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/120.0.0.0Safari/537.36",
            "sec-ch-ua": '"Not_ABrand";v="8","Chromium";v="120","GoogleChrome";v="120"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
        }
        response_headers = {
            "Date": "Sat,24Feb202410:48:50GMT",
            "Content-Type": "application/json;charset=utf-8",
            "Connection": "keep-alive",
            "Keep-Alive": "timeout=25",
            "Vary": "Accept-Encoding",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Expose-Headers": "*",
            "x-acs-request-id": "980FBE39-D01C-5C50-BB27-4C71AA79FE15",
            "x-acs-trace-id": "c0fada5ce5c44f0bf3ac35d92693ddf1",
            "Content-Encoding": "gzip",
            "Transfer-Encoding": "chunked",
        }
        response = requests.get(url=url, params=parameters, headers=request_headers)
        results = response.status_code, response.text
        print(results)

    @staticmethod
    def decryptor(key):
        return AES.new(key, AES.MODE_CBC, IV=b"0000000000000000")

    @staticmethod
    def decryption(file):
        m3u8_obj = m3u8.load(uri=file)
        key: str = m3u8_obj.files[0]
        key: str = "xxxxxxxxxxxxxxxx"
        segment_urls = [segment.uri for segment in m3u8_obj.segments]
        return key, segment_urls

    @classmethod
    def download_ts(cls):
        url = "https://mv.aura-el.com/"
        key, segment_urls = cls.decryption(file="./data/example.m3u8")
        for segment in segment_urls:
            fullurl = f"{url}{segment}"
            # TODO(下载ts加密文件)
            fullurl = "./data/suchkey.ts"
            cls.decryption_ts(fullurl, key.encode())
            break

    @classmethod
    def decryption_ts(cls, file, key):
        with open(file, mode="rb") as encrypted_file:
            encrypted_data = encrypted_file.read()
            decrypted_data = cls.decryptor(key).decrypt(encrypted_data)
        with open("./data/decrypted.ts", "wb") as decrypted_file:
            decrypted_file.write(decrypted_data)


class Main:

    @staticmethod
    def run():
        AuraVideo.download_ts()


if __name__ == "__main__":
    Main.run()
