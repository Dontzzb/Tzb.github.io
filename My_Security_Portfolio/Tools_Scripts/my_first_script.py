#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 我的第一个安全相关脚本：网络连通性简易检查

import os
import sys

def ping_host(hostname):
    """
    尝试ping一个主机，用于检查基础网络连通性。
    这是渗透测试中信息收集的第一步。
    """
    response = os.system(f"ping -c 2 {hostname} > /dev/null 2>&1") # Linux/Mac命令
    # 如果在Windows上，请将上面的命令改为：response = os.system(f"ping -n 2 {hostname}")
    if response == 0:
        print(f"[+] 主机 {hostname} 可达！")
        return True
    else:
        print(f"[-] 主机 {hostname} 不可达。")
        return False

if __name__ == "__main__":
    print("=== 简易网络检查工具 ===")
    target = input("请输入要检查的主机名或IP（例如：google.com）: ").strip()
    ping_host(target)
    print("检查完毕。")