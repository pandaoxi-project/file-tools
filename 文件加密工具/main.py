from sys import exit # line:0
from tkinter import Tk  # line:1
from tkinter.filedialog import askopenfilename  # line:2
from easygui import buttonbox, msgbox, passwordbox  # line:3
from tkinter.messagebox import showinfo, showwarning, showerror  # line:4
from os import name, environ  # line:5
from hashlib import md5  # line:6
from random import shuffle  # line:7
from base64 import (
    a85encode,
    a85decode,
    b64encode,
    b64decode,
    b32encode,
    b32decode,
    b16encode,
    b16decode,
)  # line:8


def shuffle_str(O000000O0000000O0):  # line:9
    OO00O0O0OOOO0OO0O = list(O000000O0000000O0)  # line:10
    shuffle(OO00O0O0OOOO0OO0O)  # line:11
    return "".join(OO00O0O0OOOO0OO0O)  # line:12


def create_md5(O00OOO00O0O0O0OO0):  # line:13
    O000O0O00OOO0OOO0 = md5(O00OOO00O0O0O0OO0.encode()).hexdigest()  # line:14
    return O000O0O00OOO0OOO0  # line:15


dx1marks = {}  # line:16
dx1dict = "0123456789AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz`~@#$%^&*()_+{}|\/{}[]<>?:;\"'=+-.,! "  # line:17
title = "文件通文件加解密工具"  # line:18
ec = "UTF-8"  # line:19
button = "确定"  # line:20
userprofile = environ["Userprofile"].replace("\\", "/")  # line:21
states = "RUNNING"  # line:22
hide = Tk()  # line:23
hide.withdraw()  # line:24
for i in range(0, len(dx1dict)):  # line:25
    if i <= 9:  # line:26
        dx1marks["0" + str(i)] = dx1dict[i]  # line:27
    else:  # line:28
        dx1marks[str(i)] = dx1dict[i]  # line:29


class Dx1:  # line:30
    def __init__(O0000O0O0OO0OO0OO):  # line:31
        O0000O0O0OO0OO0OO.content = (
            "DaoXi 1.0/2.0 Encrypt Decrypt Algorithm Library"  # line:32
        )
        O0000O0O0OO0OO0OO.interval_mark = "-"  # line:33
        O0000O0O0OO0OO0OO.ec = "UTF-8"  # line:34
        O0000O0O0OO0OO0OO.dx1dx1marks = dx1marks  # line:35

    def encrypt(OO00O0O00OOO0O000):  # line:36
        OO00OO0OO00O000OO = a85encode(
            OO00O0O00OOO0O000.content.encode(OO00O0O00OOO0O000.ec)
        ).decode(
            OO00O0O00OOO0O000.ec
        )  # line:37
        OOOOO00OO00O0O00O = []  # line:38
        for O0O0000O0000OO0O0 in OO00OO0OO00O000OO:  # line:39
            OOOOO00OO00O0O00O.append(
                list(dx1marks.keys())[list(dx1marks.values()).index(O0O0000O0000OO0O0)]
            )  # line:40
        return [
            "OKAY",
            OO00O0O00OOO0O000.interval_mark.join(OOOOO00OO00O0O00O),
        ]  # line:41

    def decrypt(O0O0O0O0OOO0OO000):  # line:42
        try:  # line:43
            O0O0O0O0OOO0O000O = O0O0O0O0OOO0OO000.content.split(
                O0O0O0O0OOO0OO000.interval_mark
            )  # line:44
            O00OOOOO00OO0OO0O = []  # line:45
            for O00O0OOOOOOO0OOOO in O0O0O0O0OOO0O000O:  # line:46
                O00OOOOO00OO0OO0O.append(dx1marks[O00O0OOOOOOO0OOOO])  # line:47
            OO0O00OO0OO00OO00 = "".join(O00OOOOO00OO0OO0O)  # line:48
            return [
                "OKAY",
                a85decode(OO0O00OO0OO00OO00.encode(O0O0O0O0OOO0OO000.ec)).decode(
                    O0O0O0O0OOO0OO000.ec
                ),
            ]  # line:49
        except Exception as OOOO00O0OO000OO0O:  # line:50
            return ["ERROR", OOOO00O0OO000OO0O]  # line:51


def dx1encrypt(O0000O000O00O000O, interval="-"):  # line:52
    OO000OO0O0O0O00OO = Dx1()  # line:53
    OO000OO0O0O0O00OO.content = O0000O000O00O000O  # line:54
    OO000OO0O0O0O00OO.interval_mark = interval  # line:55
    OO00000O0000000O0 = OO000OO0O0O0O00OO.encrypt()  # line:56
    if OO00000O0000000O0[0] == "OKAY":  # line:57
        return OO00000O0000000O0[1]  # line:58
    else:  # line:59
        return "Error! " + OO00000O0000000O0[1]  # line:60


def dx1decrypt(OO0000O0OOOO0OOOO):  # line:61
    O00OO0OO0O0O000O0 = Dx1()  # line:62
    O00OO0OO0O0O000O0.content = OO0000O0OOOO0OOOO  # line:63
    O000OO0OOOOO00O0O = O00OO0OO0O0O000O0.decrypt()  # line:64
    if O000OO0OOOOO00O0O[0] == "OKAY":  # line:65
        return O000OO0OOOOO00O0O[1]  # line:66
    else:  # line:67
        return "Error! " + str(O000OO0OOOOO00O0O[1])  # line:68


class Dx2:  # line:69
    def __init__(OOO0OO000O00OO0OO):  # line:70
        OOO0OO000O00OO0OO.content = (
            "DaoXi 1.0/2.0 Encrypt Decrypt Algorithm Library"  # line:71
        )
        OOO0OO000O00OO0OO.interval_mark = "-"  # line:72
        OOO0OO000O00OO0OO.password = "default"  # line:73
        OOO0OO000O00OO0OO.__OO00OO000O0OO0000 = {}  # line:74
        OOO0OO000O00OO0OO.__O00O0O00O00O0OO0O = {}  # line:75
        OOO0OO000O00OO0OO.__OOO00000OO000OO00 = shuffle_str(dx1dict)  # line:76
        for OOO0O00OO0O0OO000 in range(
            0, len(OOO0OO000O00OO0OO.__OOO00000OO000OO00)
        ):  # line:77
            if OOO0O00OO0O0OO000 <= 9:  # line:78
                OOO0OO000O00OO0OO.__OO00OO000O0OO0000[
                    "0" + str(OOO0O00OO0O0OO000)
                ] = OOO0OO000O00OO0OO.__OOO00000OO000OO00[
                    OOO0O00OO0O0OO000
                ]  # line:79
            else:  # line:80
                OOO0OO000O00OO0OO.__OO00OO000O0OO0000[
                    str(OOO0O00OO0O0OO000)
                ] = OOO0OO000O00OO0OO.__OOO00000OO000OO00[
                    OOO0O00OO0O0OO000
                ]  # line:81

    def encrypt(O0O0O0O000OOO00O0):  # line:82
        try:  # line:83
            O0OOOO00O0O0O00OO = O0O0O0O000OOO00O0.content  # line:84
            O000000O0O0O0OOOO = b32encode(
                create_md5(O0O0O0O000OOO00O0.password).encode()
            ).decode()  # line:85
            OO0OOO00OO0OOOOO0 = b32encode(
                b64encode(
                    a85encode(str(O0O0O0O000OOO00O0.__OO00OO000O0OO0000).encode())
                )
            ).decode()  # line:86
            OO0O00O0OOOO0OO00 = []  # line:87
            for O00O0OO00OO0O0O00 in O0OOOO00O0O0O00OO:  # line:88
                OO0O00O0OOOO0OO00.append(
                    list(O0O0O0O000OOO00O0.__OO00OO000O0OO0000.keys())[
                        list(O0O0O0O000OOO00O0.__OO00OO000O0OO0000.values()).index(
                            O00O0OO00OO0O0O00
                        )
                    ]
                )  # line:89
            OOOO000OO0000OO00 = O0O0O0O000OOO00O0.interval_mark.join(
                OO0O00O0OOOO0OO00
            )  # line:90
            OO00OO00OO00O00O0 = "%s(dx2)%s(dx2)%s(dx2)" % (
                OOOO000OO0000OO00,
                O000000O0O0O0OOOO,
                OO0OOO00OO0OOOOO0,
            )  # line:91
            O0OO00OOOOOO000O0 = dx1encrypt(OO00OO00OO00O00O0)  # line:92
            return ["OKAY", O0OO00OOOOOO000O0]  # line:93
        except Exception as O00OO00OO0OOO0OO0:  # line:94
            return ["ERROR", O00OO00OO0OOO0OO0]  # line:95

    def decrypt(O0OO0OO0O0O00OOO0):  # line:96
        try:  # line:97
            OOO0O000O00O0O00O = dx1decrypt(O0OO0OO0O0O00OOO0.content).split(
                "(dx2)"
            )  # line:98
            OOO0O000O00O0O00O.pop(3)  # line:99
            OO0OOO0O0O00O00O0 = b32decode(OOO0O000O00O0O00O[1]).decode()  # line:100
            OOO00OO000OOO0O0O = create_md5(O0OO0OO0O0O00OOO0.password)  # line:101
            if OO0OOO0O0O00O00O0 == OOO00OO000OOO0O0O:  # line:102
                O0O0O0OO000OO000O = a85decode(
                    b64decode(b32decode(OOO0O000O00O0O00O[2]))
                ).decode()  # line:103
                O00OO00O0OOOOO00O = eval(O0O0O0OO000OO000O)  # line:104
                O0OO0OO0O0O00OOO0.__O00O0O00O00O0OO0O = O00OO00O0OOOOO00O  # line:105
                O00000OOO00000O0O = []  # line:106
                OO00O0OOOOO0000O0 = OOO0O000O00O0O00O[0].split(
                    O0OO0OO0O0O00OOO0.interval_mark
                )  # line:107
                for O0OO0OOOO0000OOO0 in OO00O0OOOOO0000O0:  # line:108
                    if O00OO00O0OOOOO00O[O0OO0OOOO0000OOO0]:  # line:109
                        O00000OOO00000O0O.append(
                            O00OO00O0OOOOO00O[O0OO0OOOO0000OOO0]
                        )  # line:110
                OOO00O00O0OO0O0OO = "".join(O00000OOO00000O0O)  # line:111
                return ["OKAY", OOO00O00O0OO0O0OO]  # line:112
            else:  # line:113
                return ["ERROR", "The password is incorrect"]  # line:114
        except Exception as O0OO0OO0OOO000000:  # line:115
            return ["ERROR", O0OO0OO0OOO000000]  # line:116


def dx2encrypt(O0O0OOOO0OOO0OOOO, OOOOOOOO0OO00000O):  # line:117
    OO00OO0OOOO0O0OOO = Dx2()  # line:118
    OO00OO0OOOO0O0OOO.content = O0O0OOOO0OOO0OOOO  # line:119
    OO00OO0OOOO0O0OOO.password = OOOOOOOO0OO00000O  # line:120
    O00OOO0O0O00O00O0 = OO00OO0OOOO0O0OOO.encrypt()  # line:121
    if O00OOO0O0O00O00O0[0] == "OKAY":  # line:122
        return O00OOO0O0O00O00O0[1]  # line:123
    else:  # line:124
        return O00OOO0O0O00O00O0[0]  # line:125


def dx2decrypt(OO000O0OO00O0OOOO, OO0OO0OO0O00OOOO0):  # line:126
    OO000O000O0O0OOOO = Dx2()  # line:127
    OO000O000O0O0OOOO.content = OO000O0OO00O0OOOO  # line:128
    OO000O000O0O0OOOO.password = OO0OO0OO0O00OOOO0  # line:129
    OO0OOOO0OO00OO000 = OO000O000O0O0OOOO.decrypt()  # line:130
    if OO0OOOO0OO00OO000[0] == "OKAY":  # line:131
        return OO0OOOO0OO00OO000  # line:132
    else:  # line:133
        return OO0OOOO0OO00OO000  # line:134


def encodef():  # line:135
    global states  # line:136
    O0OO00O0OOOO0O0O0 = askopenfilename(
        title=title, initialdir=userprofile, filetypes=[("All Files", "*.*")]
    )  # line:137
    with open(O0OO00O0OOOO0O0O0, "rb") as OO0OOO0000O0OO0O0:  # line:138
        OOOO0O0O00OOO0OO0 = OO0OOO0000O0OO0O0.read()  # line:139
    O0OO000OO0O00O00O = passwordbox("请输入加密密码（请妥善保存）：", title)  # line:140
    OOOOOOOO000O00O00 = dx2encrypt(
        a85encode(OOOO0O0O00OOO0OO0).decode(), O0OO000OO0O00O00O
    ).encode()  # line:141
    O0O00O00000O00OOO = O0OO00O0OOOO0O0O0.split("/")  # line:142
    O00OOO0O0O0O0O0OO = O0O00O00000O00OOO[len(O0O00O00000O00OOO) - 1]  # line:143
    O0O0O00O0O000000O = "/".join(O0O00O00000O00OOO).replace(
        O00OOO0O0O0O0O0OO, "(encode)" + O00OOO0O0O0O0O0OO
    )  # line:144
    with open(O0O0O00O0O000000O, "wb") as O000O0O00OOO0O000:  # line:145
        O000O0O00OOO0O000.write(OOOOOOOO000O00O00)  # line:146
    msgbox("加密成功！", title, button)  # line:147
    states = "OVER"  # line:148


def decodef():  # line:149
    global states  # line:150
    OO0000OOOOOO0000O = askopenfilename(
        title=title, initialdir=userprofile, filetypes=[("All Files", "*.*")]
    )  # line:151
    OO0OOOOOO0O0O0O0O = passwordbox("请输入加密密码以解密文件：", title)  # line:152
    O00O0000O0O00OOOO = False  # line:153
    with open(OO0000OOOOOO0000O, "r", encoding=ec) as O0OO0000O0000O0O0:  # line:154
        OOOOO000OO0000000 = dx2decrypt(
            O0OO0000O0000O0O0.read(), OO0OOOOOO0O0O0O0O
        )  # line:155
        if not OOOOO000OO0000000[1] == "The password is incorrect":  # line:156
            O000OO0O0O00OOO0O = OOOOO000OO0000000[1].encode()  # line:157
            O000OO0O0O00OOO0O = a85decode(O000OO0O0O00OOO0O)  # line:158
            O00O0000O0O00OOOO = True  # line:159
        else:  # line:160
            showerror(title, "密码有误！")  # line:161
            O000OO0O0O00OOO0O = "The password is incorrect"  # line:162
    OO00O0OO00000OO0O = O000OO0O0O00OOO0O  # line:163
    O0OO000OO00O0000O = OO0000OOOOOO0000O.split("/")  # line:164
    O0O00OO00O0O0OOO0 = O0OO000OO00O0000O[len(O0OO000OO00O0000O) - 1]  # line:165
    O000O0000O0OO00O0 = "/".join(O0OO000OO00O0000O).replace(
        O0O00OO00O0O0OOO0, "(decode)" + O0O00OO00O0O0OOO0
    )  # line:166
    with open("%s" % (O000O0000O0OO00O0), "wb") as OOO0O0O0O0OO000OO:  # line:167
        OOO0O0O0O0OO000OO.write(OO00O0OO00000OO0O)  # line:168
    if O00O0000O0O00OOOO == True:  # line:169
        msgbox("解密成功！", title, button)  # line:170
    else:  # line:171
        exit()  # line:172
    states = "OVER"  # line:173


def help():  # line:174
    OOO0OO0OOO0O00OO0 = """欢迎使用此软件，此软件可以加密或解密各种文件，以免被盗窃。
    开发者：潘道熹
    版本：2.0
    开发时间：2021年8月
    联系邮箱：qingfengstudio@yeah.net
    客服QQ：3377063617
    代码语言：Python 3.6
    官方博客：https://blog.csdn.net/pandaoxi2020
    
    如果您在使用中出现了问题，请联系客服解决。
    """  # line:185
    msgbox(OOO0OO0OOO0O00OO0, title, button)  # line:186


try:  # line:187
    while states == "RUNNING":  # line:188
        if __name__ == "__main__" and name == "nt":  # line:189
            choose = buttonbox(
                "欢迎使用%s！\n请选择您需要的服务：" % title, title, ("加密文件", "解密文件", "关于我们")
            )  # line:190
            if choose == "关于我们":  # line:191
                help()  # line:192
            elif choose == "加密文件":  # line:193
                encodef()  # line:194
            elif choose == "解密文件":  # line:195
                decodef()  # line:196
            else:  # line:197
                exit()  # line:198
        else:  # line:199
            showerror(title, "请使用Windows系统运行此程序！\n请自主运行此程序，不能使用模块进行导入。")  # line:200
            exit()  # line:201
except Exception as e:  # line:202
    showwarning(title, "错误：%s" % e)  # line:203
hide.mainloop()  # line:204
