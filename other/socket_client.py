import socket

# 1.创建socket
socket = socket.socket()

# 2. 连接服务器
socket.connect(('192.168.124.11', 8000))
socket.send(b'connect')

# 3.接收数据
msg = socket.recv(4096) # 阻塞方法
print('Server:', msg.decode('utf-8'))

# 4.向服务端发送数据
socket.send('您好，我想听首张学友的歌'.encode('utf-8'))

# 关闭
socket.close()


