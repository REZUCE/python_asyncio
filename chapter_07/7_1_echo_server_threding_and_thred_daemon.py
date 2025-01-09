from threading import Thread
import socket


def echo(client: socket):
    while True:
        data = client.recv(2048)
        print(f'Received {data}, sending!')
        client.sendall(data) # send message client connect. sent what I received


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8000))
    server.listen()
    while True:
        connection, _ = server.accept()  # A - waiting for connect client - which will end with Ctrl + C = KeyboardInterrupt
        thread = Thread(target=echo, args=(connection,))  # B - it turns out = echo(connection)
        # thread.daemon = True # This IS HOW IT WILL WORK thread daemon, which will end with Ctrl + C without error.
        thread.start()  # C - start after connect

    """
    telnet localhost 8000 in Linux use for test.
    This project have to problem:
    1. Когда используем Ctrl + C и у нас не отключаются потоки. Решение использовать thread.daemon = True, перед thread.start()
    2. Мы хотим уведомление о завершении thread клиенту и чисто завершить установку. Решение в 7_2.
    """
 