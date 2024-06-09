import os


def register():
    """
    函数功能：注册新用户，将用户名和密码写入本地文件

    Args:
        无参数

    Returns:
        无返回值
    """
    username = input("请输入用户名：")
    password = input("请输入密码：")
    # 将用户名和密码写入本地文件
    with open(
        "login.txt", "w"
    ) as file:
        file.write(
            "%s,%s"
            % (username, password)
        )


def login():
    # 读取本地用户名密码
    """
    从本地文件 login.txt 中读取用户名和密码，并与用户输入的用户名和密码进行校验。

    Args:
        无参数。

    Returns:
        无返回值。

    """
    with open(
        "login.txt", "r"
    ) as file:
        (
            username,
            password,
        ) = file.read().split(",")
    # 校验用户名密码
    input_username = input(
        "请输入用户名："
    )
    input_password = input(
        "请输入密码："
    )
    if (
        username == input_username
        and password
        == input_password
    ):
        print("登录成功！")
    else:
        print("登录失败！")


def logout():
    # 删除本地的用户名和密码
    """
    从本地删除登录信息文件并输出注销成功的提示信息

    Args:
        无参数

    Returns:
        无返回值，仅输出注销成功的提示信息
    """
    os.remove("login.txt")
    print("注销成功！")


if os.path.exists("login.txt"):
    print("登录成功！")
else:
    print("没有登录，进入登录。")
    register()

import time
import pyautogui
import pyperclip

print("30%")
import turtle

print("50%")
import pyttsx3

print("60%")
# 初始化
print("70%")
print("80%")
print("90%")
print(
    "[1]超级AI/[2]夸克（未去广告）/[3]百度/[4]谷歌/[5]书签/[6]bibi搜索/搜狐搜索[7]/[8]应用商店/[9]退出/[10]西瓜视频搜/[11]搜狗搜索/[12]头条搜索",
    end="",
)
print(
    "/[13]百科搜索/[14]网盘搜索/[15]翻译/[16]作文/[xsh]/[17]音乐搜"
)
q = input("")
if q == "5":
    e = input(
        "看剧[1]/摸鱼[2]/deer考试[3]/[4]搜狐/[5]map/[6]西瓜视频/[yx]/[7]黑客地球/[8]音乐/[9]黑客浏览器"
    )
    if e == "1":
        os.system(
            "start https://www.bilibili.com/"
        )
    if e == "2":
        os.system(
            "start https://haiyong.site/moyu/"
        )
    if e == "3":
        os.system(
            "start https://deer.zuoyebang.com/static/hy/contest-pc/index.html"
        )
    if e == "4":
        os.system(
            "start https://tv.sohu.com/"
        )
    if e == "5":
        os.system(
            "start https://map.qq.com/?type="
        )
    if e == "6":
        os.system(
            "start https://www.ixigua.com/"
        )
    if e == "7":
        os.system(
            "start https://cybermap.kaspersky.com/cn"
        )
    if e == "yx":
        os.system("start poki.cn")
    if e == "8":
        os.system(
            "start https://tool.liumingye.cn/music/#/ https://streetvoice.cn/"
        )
    if e == "9":
        pyperclip.copy(
            "user login -u 仙王吖py -p wrt090706"
        )
        print(
            "user login -u 仙王吖py -p wrt090706 (clrl+V)"
        )
        os.system(
            "start http://yuindex.yupi.icu/#/"
        )
        print(
            "user login -u 仙王吖py -p wrt090706 (clrl+V)"
        )
        pyautogui.hotkey(
            "ctrl", "v"
        )
        # 粘贴
        pyautogui.typewrite("\n")
if q == "1":
    os.system(
        "start https://search.tiangong.cn/"
    )
elif q == "2":
    w = input(
        "使用intitle:关键字检索[1](效果不大）"
    )
    a = input("搜：")
    if w == "1":
        a = "intitle:" + a
    os.system(
        "start https://quark.sm.cn/s?q="
        + a
    )
elif q == "3":
    w = input(
        "使用intitle:关键字检索[1](效果超大）"
    )
    a = input("搜：")
    if w == "1":
        a = "intitle:" + a
    os.system(
        "start https://www.baidu.com/s?wd="
        + a
    )
elif q == "4":
    a = input("搜：")
    os.system(
        "start https://www.google.com/search?q="
        + a +"&lr=lang_zh-CN%7Clang_zh-TW" # 中文搜索
    )
elif q == "6":
    a = input("搜：")
    os.system(
        "start https://search.bilibili.com/all?keyword="
        + a
    )
elif q == "7":
    a = input("搜：")
    os.system(
        "start https://so.tv.sohu.com/mts?wd="
        + a
    )
elif q == "8":
    a = input("搜：")
    os.system(
        "start https://pc.qq.com/search.html#!keyword="
        + a
    )
elif q == "10":
    a = input("搜：")
    os.system(
        "start https://www.ixigua.com/search/"
        + a
    )
elif q == "11":
    a = input("搜：")
    os.system(
        "start https://www.sogou.com/sogou?query="
        + a
    )
elif q == "12":
    a = input("搜：")
    os.system(
        "start https://www.baike.com/search?keyword="
        + a
    )

elif q == "13":
    a = input("搜：")
    os.system(
        "start  https://baike.baidu.com/search?word="
        + a
    )
elif q == "14":
    a = input("搜：")
    os.system(
        "start  https://www.alipansou.com/search?k="
        + a
    )
    os.system(
        "start https://www.yunpanziyuan.com/fontsearch.htm?fontname="
        + a
    )
elif q == "15":
    a = input("搜：")
    os.system(
        '"start  https://fanyi.baidu.com/?aldtype=23#en/zh/'
        + a
    )
elif q == "16":
    a = input("搜：")
    os.system(
        "start https://easylearn.baidu.com/edu-page/tiangong/composition/list?query="
        + a
    )
elif q == "xsh":
    a = input("搜：")
    os.system(
        "start https://www.qidian.com/soushu/"
        + a
    )
elif q == "17":
    a = input("搜：")
    os.system(
        "start https://www.yeyulingfeng.com/tools/music/?name="
        + a
    )
else:
    if q != "5":
        os.system(
            "start https://quark.sm.cn/s?q="
            + q
        )
