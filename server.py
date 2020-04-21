import socket
import os
def find_files(filename, search_path):
    result = []
    if os.path.exists(search_path+filename):
        for root, dir, files in os.walk(search_path):
              if filename in files:
                result.append(os.path.join(root, filename))

    else:
        print("file is not exit")

    return result



def renamefile(src,des):
    if os.path.exists(src):
        os.rename(src,des)
        print("done")
    else:
        print("file is not exit")



def removeFile(src):
    if os.path.exists(src):
        os.remove(src)
        print("done")
    else:
        print("file is not exit")



def display(src):
    if os.path.exists(src):
        file = open(src, "r")
        for line in file:
            word = line.strip()
            print(word)
    else:
        print("file is not exit")


def create(src):
    if os.path.exists(src):
        print("file is exit")
    else:
        print("file is not exit")
        file = open(src, "w")
        print("Done")




def server_program():
    host = socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if data[:6] == "search":
            filename = data[7:]
            print(find_files(filename, "C:/Users/moham/Desktop/"))
        if data[:2] == "rm":
            filename = data[3:].split(",")
            renamefile("C:/Users/moham/Desktop/"+filename[0],"C:/Users/moham/Desktop/"+filename[1])
        if data[:7] =="display":
            msf=data[8:]
            display("C:/Users/moham/Desktop/"+msf)
        if data[:5] == "touch":
            msf2 = data[6:]
            create("C:/Users/moham/Desktop/"+msf2)
        if data[:2] == "rv":
            msf4=data[3:]
            removeFile("C:/Users/moham/Desktop/"+msf4)
        data = input(' -> ')
        conn.send(data.encode())
    conn.close()

if __name__ == '__main__':
    server_program()
