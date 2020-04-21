import socket

def parse():
    print("[+] search on File")
    print("[+] rename a File")
    print("[+] remove a File")
    print("[+] display content of File")
    print("[+] create a File")


def client_program():
    parse()
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = input(" Enter seach file name-> ")
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)
        message = input(" -> ")
    client_socket.close()

if __name__ == '__main__':
    client_program()
