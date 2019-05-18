import socket

PORT = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('0.0.0.0', PORT))

print('Bind UDP on %s...' % PORT)

while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('From %s, received: %s' % (addr, data.decode('utf-8')))
    s.sendto(b'Hello, %s!' % data, addr)
