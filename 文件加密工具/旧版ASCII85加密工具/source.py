from tkinter import Tk #line:2
from tkinter .filedialog import askopenfilename #line:3
from easygui import buttonbox ,msgbox #line:4
from tkinter .messagebox import showinfo ,showwarning ,showerror #line:5
from base64 import a85encode ,a85decode #line:6
from os import name ,environ #line:7
title ="文件通"#line:10
ec ="UTF-8"#line:11
button ="确定"#line:12
userprofile =environ ["Userprofile"].replace ("\\","/")#line:13
hide =Tk ()#line:16
hide .withdraw ()#line:17
def encodef ():#line:21
    O0OOOOO0O00OO000O =askopenfilename (title =title ,initialdir =userprofile ,filetypes =[("All Files","*.*")])#line:25
    with open (O0OOOOO0O00OO000O ,"rb")as OO000OOO0000OO00O :#line:27
        O00OOO0O0O0OO0OO0 =OO000OOO0000OO00O .read ()#line:28
    O0OOO0O00OOOOOOO0 =a85encode (O00OOO0O0O0OO0OO0 )#line:30
    OOO00O00O0O00OOO0 =O0OOOOO0O00OO000O .split ("/")#line:32
    OO0OO0O0OO00O0OOO =OOO00O00O0O00OOO0 [len (OOO00O00O0O00OOO0 )-1 ]#line:33
    O0O0O00OOOOOOOOOO ="/".join (OOO00O00O0O00OOO0 ).replace (OO0OO0O0OO00O0OOO ,"(encode)"+OO0OO0O0OO00O0OOO )#line:34
    with open (O0O0O00OOOOOOOOOO ,"wb")as OOO0O0OOO00O0O0O0 :#line:36
        OOO0O0OOO00O0O0O0 .write (O0OOO0O00OOOOOOO0 )#line:37
    msgbox ("加密成功！",title ,button )#line:39
def decodef ():#line:43
    OOO00OOO000OO00O0 =askopenfilename (title =title ,initialdir =userprofile ,filetypes =[("All Files","*.*")])#line:47
    with open (OOO00OOO000OO00O0 ,"r",encoding =ec )as OO0OO00O000000000 :#line:49
        O0O0000O0OOOOO0O0 =bytes (a85decode (OO0OO00O000000000 .read ()))#line:50
    O0000OOO00O0OO0OO =O0O0000O0OOOOO0O0 #line:52
    OOO0000OOO0OOOO00 =OOO00OOO000OO00O0 .split ("/")#line:54
    OOO0O0O0000O000O0 =OOO0000OOO0OOOO00 [len (OOO0000OOO0OOOO00 )-1 ]#line:55
    OOO00OOO000OO0000 ="/".join (OOO0000OOO0OOOO00 ).replace (OOO0O0O0000O000O0 ,"(decode)"+OOO0O0O0000O000O0 )#line:56
    with open ("%s"%(OOO00OOO000OO0000 ),"wb")as OO00OO0O0OOOO0OOO :#line:59
        OO00OO0O0OOOO0OOO .write (O0000OOO00O0OO0OO )#line:60
    msgbox ("解密成功！",title ,button )#line:62
def help ():#line:66
    O000O0000OOO0OOOO ="""欢迎使用此软件，此软件可以加密或解密各种文件，以免被盗窃。
    开发者：潘道熹
    开发时间：2020年1月
    联系邮箱：qingfengstudio@yeah.net
    客服QQ：3377063617
    代码语言：Python 3.6
    
    如果您在使用中出现了问题，请联系客服解决。
    """#line:75
    msgbox (O000O0000OOO0OOOO ,title ,button )#line:76
if __name__ =="__main__"and name =="nt":#line:79
    choose =buttonbox ("欢迎使用%s！\n请选择您需要的服务："%title ,title ,("加密文件","解密文件","关于我们"))#line:80
    if choose =="关于我们":#line:81
        help ()#line:82
    elif choose =="加密文件":#line:83
        encodef ()#line:84
    elif choose =="解密文件":#line:85
        decodef ()#line:86
else :#line:87
    showerror (title ,"请使用Windows系统运行此程序！\n请自主运行此程序，不能使用模块进行导入。")#line:88
hide .mainloop ()#line:89
