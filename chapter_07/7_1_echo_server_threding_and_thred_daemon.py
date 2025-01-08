from threading import Thread
import socket


def echo(client: socket):
    while True:
        data = client.recv(2048)
        print(f'Received {data}, sending!')
        client.sendall(data) # send message client connect


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 8000))
    server.listen()
    while True:
        connection, _ = server.accept()  # A - waiting for connect client 
        thread = Thread(target=echo, args=(connection,))  # B
        # thread.daemon = True Так будут работать потоки демоны, которые буду завершаться с Ctrl + C без ошибок.
        thread.start()  # C - start after connect
