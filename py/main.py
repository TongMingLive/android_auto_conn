from easygui import *
import sys
import os

f = open('../file/conn_url.txt')
f_dic = f.read()
if f_dic == '':
    dic = {'url':'','android':''}
else:
    dic = eval(f_dic)


def save(name,ent):
    if str(ent) != dic.get(name) and ent != None:
        f = open('../file/conn_url.txt', 'w')
        dic[name] = str(ent)
        f.write(str(dic))


ent = enterbox('请输入您的adb.exe可执行文件路径：',default=dic.get('url'))
save('url',ent)
ent = enterbox('请输入安卓调试地址：',default=dic.get('android'))
save('android',ent)

cmd = str(dic.get('url'))+' connect '+str(dic.get('android'))

print('adb执行目录：',dic.get('url'))
print('ipv4地址：','暂无')
print('安卓调试地址：',dic.get('android'))
print('cmd拼接',cmd)

r = os.popen(cmd)
info = r.readlines()

ip = os.popen('ipconfig/all')
ipv = ip.readlines()
ipv4 = ''
for ip in ipv:
    if str(ip).find('IPv4 地址') > 0 :
        ipv4 = str(ip)
        print(str(ip))

msgbox(msg=str(info),title='执行结果：',ok_button='确定')
msgbox(msg=str(ipv4),title='您的ipv4地址为：',ok_button='确定')
