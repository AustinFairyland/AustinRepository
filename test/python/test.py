# coding: utf-8
"""
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-07-25 18:58:33 UTC+08:00
"""

import socket
import ssl
import hashlib
import sys
import os
import re
import json
import time
from datetime import datetime

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad

HOST = '192.168.2.40'
PORT = 18809

# 服务器的CA证书
CA_CERTFILE = '/home/test/server_cert.pem'

# 要发送的文件
# FILE_TO_SEND = '/home/master/test/1.txt'
KEY = b'72e31155c616484bbef40651'


def create_client_socket(host, port, ca_certfile):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket = ssl.wrap_socket(client_socket, ca_certs=ca_certfile,
                                    cert_reqs=ssl.CERT_REQUIRED,
                                    ssl_version=ssl.PROTOCOL_TLSv1)
    client_socket.connect((host, port))
    return client_socket


def send_file_info(client_socket, filename):
    # 计算文件的MD5值
    with open(filename, 'rb') as f:
        file_data = f.read()
        file_md5 = hashlib.md5(file_data).hexdigest()
        # 发送文件名和MD5值
        client_socket.sendall(os.path.basename(filename).encode() + b'\0')  # 文件名后跟一个空字符作为分隔符
        client_socket.sendall(file_md5.encode() + b'\0')  # MD5值后跟一个空字符


def encrypt_data(plaintext, key):
    # 3DES加密
    cipher = DES3.new(key, DES3.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))  # 加密
    return ciphertext


def send_file_data(client_socket, filename, key):
    try:
        with open(filename, 'rb') as f:
            file_data = f.read()
            encrypted_data = encrypt_data(file_data, key)
            print(9999, len(encrypted_data))
            client_socket.sendall(encrypted_data)
            print("发送成功")
    except Exception as e:
        print(8888, str(e))


def analysis_json(file_path):
    file_list = []
    now_time = int(time.time())
    start_time = now_time - 300
    with open(file_path, "r") as file:
        for line in file:
            if "md5" in line and "path" in line:
                log_date = line.split(" ", )[0]
                log_time = line.split(" ", )[1]
                log_date_time = " ".join([log_date, log_time])
                dt_object = datetime.strptime(log_date_time, "%Y-%m-%d %H:%M:%S")
                timestamp = int(time.mktime(dt_object.timetuple()))
                if now_time > timestamp > start_time:
                    start_index = line.find('{')
                    end_index = line.rfind('}')
                    json_data_str = line[start_index:end_index + 1]
                    json_dict = json.loads(json_data_str)

                    if json_dict.get("process") == "/usr/local/go-fastdfs/fileserver":
                        base_path = "/opt/fsti/fsti-lydsj-prod/middleware/go-fastdfs/files/"
                        filename = json_dict.get("filename")
                        prefix = filename.split("/")[-2][:2]
                        new_path = os.path.join(base_path, prefix, filename.split("/")[-1])
                        json_dict["path"] = new_path
                        file_list.append(new_path)

                    if json_dict.get("md5") and json_dict.get("path"):
                        file_list.append(json_dict.get("path"))
                        print(json_dict.get("md5"), json_dict.get("path"))
        print(len(file_list))
        return file_list


def find_files_by_paths(path):
    if os.path.exists(path):
        print(path)
        return path
    else:
        print(f"Path does not exist: {path}")
        return ""


def send_file():
    file_path_list = analysis_json('/usr/local/nsfagent/nsfagent.log')
    for file_path in file_path_list:
        absolute_path = find_files_by_paths(file_path)
        if absolute_path:
            try:
                client_socket = create_client_socket(HOST, PORT, CA_CERTFILE)
                send_file_info(client_socket, absolute_path)
                send_file_data(client_socket, absolute_path, KEY)
                client_socket.close()
                print(f"文件 {file_path} 发送成功")
            except Exception as e:
                print(f"文件 {file_path} 发送失败: {e}")
        else:
            print(f"找不到文件 {file_path}")


if __name__ == "__main__":
    send_file()
