# -*- coding: UTF-8 -*-
import getopt
import json


def getargs(argv:list):
    username = None
    password = None
    ispcode = None

    try:
        opts, args = getopt.getopt(argv, "u:p:i:c:vh", ["username=","isp=","password=","config=","version","help"])
    except getopt.GetoptError:
        print("参数错误。请输入\033[32m-h/--help\033[0m查看具体用法")
        return
 
    for opt, arg in opts:
        if opt in ['-u', '--username']:
            username = arg
        elif opt in ['-i', '--isp']:
            ispdict = {"jzg":"@jzg", "dx":"@aust", "lt":"@unicom", "yd":"@cmcc"}
            try:
                ispcode = ispdict[arg]
            except:
                print("参数\033[32m-i/--isp\033[0m错误。请输入\033[32m-h/--help\033[0m查看具体用法")
                return
        elif opt in ['-p', '--password']:
            password = arg
        elif opt in ['-c', '--config']:
            try:
                with open(arg) as cfgfile:
                    cfg = json.load(cfgfile)
                ispdict = {"jzg":"@jzg", "dx":"@aust", "lt":"@unicom", "yd":"@cmcc"}
                cfg["isp"] = ispdict[cfg["isp"]]
                return cfg
            except:
                print("参数配置文件路径错误。请检查配置文件路径是否正确。")
                return
        elif opt in ['-v', '--version']:
            print("\033[33maustlogin v1.0\033[0m (c) 2022 by 心海")
            print("\033[4;36mhttps://gitee.com/xinhai1/austLogin\033[0m")
            return
        elif opt in ['-h', '--help']:
            print(
'''
{:*^50}
{:25} 后跟学号工号
{:25} 后跟运营商代号: 电信为dx|移动为yd|联通为lt|教职工为jzg|校内留空
{:25} 后跟密码
{:25} 后跟配置文件的路径  配置文件为json形式
    配置文件样本: {}
{:25} 查看版本
{:25} 查看帮助
{:*^50}
例子1: austlogin \033[32m-u\033[0m 2019000000 \033[32m-p\033[0m 123456 \033[32m-i\033[0m dx
例子2: austlogin \033[32m-c\033[0m .\myconfig.json
'''.format( 
    "\033[4;33m参数说明\033[0m",
    "  \033[32m-u--username\033[0m", 
    "  \033[32m-i/-isp\033[0m", 
    "  \033[32m-p/--password\033[0m", 
    "  \033[32m-c/--config\033[0m", 
    '{"username":"2019000000","password":"123456","isp":"dx"}',
    "  \033[32m-v/--version\033[0m", 
    "  \033[32m-h/--help\033[0m",
    "\033[4;33m使用说明\033[0m"
)
            )
            return

    if username == None or password == None:
        print("必要参数缺失。请输入\033[32m-h/--help\033[0m查看具体用法")
        return
    else:
        cfg = {"username":username,"password":password,"isp":ispcode}
    
    return cfg