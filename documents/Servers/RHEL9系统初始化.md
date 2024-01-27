[toc]

# RHEL9系统初始化

> @File: RHEL9系统初始化.md
>
> @Editor: PyCharm
>
> @Author: [Austin (From Chengdu.China)](https://fairy.host)
>
> @HomePage: [AustinFairyland](https://github.com/AustinFairyland)
>
> @OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
>
> @CreatedTime: 2024-01-27

[![Author](https://img.shields.io/badge/Author-Austin-orange)](https://t.me/FairyLtd) [![github](https://img.shields.io/badge/Github-Austin.D-green)](https://github.com/AustinFairyland) [![GitBook](https://img.shields.io/badge/GitBook-Austin.D-green)](https://interestingbooks.gitbook.io/) [![Editor](https://img.shields.io/badge/Editor-PyCharm-yellow)](https://github.com/AustinFairyland) [![Language](https://img.shields.io/badge/Language-Markdown-orange)](https://github.com/AustinFairyland) [![Version](https://img.shields.io/badge/Version-Release-blue)](https://github.com/AustinFairyland) [![Docs](https://img.shields.io/badge/Docs-Passing-brightgreen)](https://github.com/AustinFairyland) [![Type](https://img.shields.io/badge/Type-Documents-blue)](https://github.com/AustinFairyland) [![Wakatime](https://wakatime.com/badge/user/fa851759-c657-4b1e-8bcb-3ec3a693a2cd.svg)](https://wakatime.com/@fa851759-c657-4b1e-8bcb-3ec3a693a2cd) [![Sign](https://img.shields.io/badge/%E7%AD%89%E6%88%91%E4%BB%A3%E7%A0%81%E7%BC%96%E6%88%90-%E5%A8%B6%E4%BD%A0%E4%B8%BA%E5%A6%BB%E5%8F%AF%E5%A5%BD-red)](https://github.com/AustinFairyland)

---

## 添加 yum 源

### EPEL(epel-release)

```Shell
subscription-manager repos --enable codeready-builder-for-rhel-9-$(arch)-rpms
dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
```

## 关闭 selinux

```Shell
# 临时禁用
setenforce 0
# 永久禁用(需重启)
sudo sed -i 's/^SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
sudo sed -i 's/^SELINUX=permissive/SELINUX=disabled/' /etc/selinux/config
```

## 安装 Docker

卸载 Podman 和相关工具

```Shell
sudo dnf remove podman buildah
```
   
安装 Docker CE

```Shell
sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# 如果有依赖冲突
sudo yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin --nobest
```

