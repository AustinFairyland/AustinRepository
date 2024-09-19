# Docker容器IP端口映射关系

> @software: PyCharm  
> @author: [Lionel Johnson](https://fairy.host)  
> @contact: [Blog](https://blog.fairy.host/) | [Github](https://github.com/PrettiestFairy) | [Telegram](https://t.me/FairylandFuture)  
> @organization: [Github·FairylandFuture](https://github.com/FairylandFuture)  
> @datetime: 2024-07-05 14:28:52 UTC+08:00

[![Author](https://img.shields.io/badge/Author-Lionel_Johnson-orange)](https://t.me/FairylandFuture) [![github](https://img.shields.io/badge/Github-PrettiestFairy-green)](https://github.com/PrettiestFairy) [![GitBook](https://img.shields.io/badge/Gitbook-Interesting_book-green)](https://interestingbooks.gitbook.io/) [![Editor](https://img.shields.io/badge/Editor-Jetbrains_PyCharm-yellow)](https://www.jetbrains.com/pycharm) [![Language](https://img.shields.io/badge/Language-Markdown-orange)](https://en.wikipedia.org/wiki/Markdown) [![Version](https://img.shields.io/badge/Version-Release-blue)]() [![Docs](https://img.shields.io/badge/Docs-Passing-brightgreen)]() [![Type](https://img.shields.io/badge/Type-Document-blue)]() [![Wakatime](https://wakatime.com/badge/user/fa851759-c657-4b1e-8bcb-3ec3a693a2cd.svg)](https://wakatime.com/@fa851759-c657-4b1e-8bcb-3ec3a693a2cd) [![Sign](https://img.shields.io/badge/%E7%AD%89%E6%88%91%E4%BB%A3%E7%A0%81%E7%BC%96%E6%88%90-%E5%A8%B6%E4%BD%A0%E4%B8%BA%E5%A6%BB%E5%8F%AF%E5%A5%BD-red)](https://fairy.host)

---

## 自定义子网

桥接模式 子网IP范围: 173.1.0.0 掩码 16 (173.1.0.1~173.1.255.254),

随机IP范围:  173.1.0.1~173.1.0.254

## 映射表

| 服务       | 容器IP     | 端口映射(宿主机:) |
| ---------- | ---------- | ----------------- |
| MySQL      | 173.1.10.1 | 51001:3306        |
| PostgreSQL | 173.1.10.2 | 51002:5432        |
| Redis      | 173.0.10.3 | 51003:6379        |
| Picsur     | 173.0.10.3 | 51004:8080        |
