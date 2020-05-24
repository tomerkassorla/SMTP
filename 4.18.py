import socket

IP = '54.213.229.251'
PORT = 587


def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, PORT))
    mail = raw_input("enter mail")
    password = raw_input("enter pass")
    print my_socket.recv(1024)
    my_socket.send("EHLO\r\n")
    print my_socket.recv(1024)
    x = "\x00" + mail + "\x00Password" + password + "!"
    new_str1 = x.encode('base64')
    my_socket.send("AUTH PLAIN " + new_str1 + "\r\n")
    print my_socket.recv(1024)
    y = mail.split("@")
    my_socket.send("MAIL FROM: < " + y[0] + "@" + y[1] + " >\r\n")
    print my_socket.recv(1024)
    my_socket.send('RCPT TO:resha@bads.com\r\n')
    print my_socket.recv(1024)
    my_socket.send('DATA\r\n')
    print my_socket.recv(1024)
    my_socket.send('Subject: hi!\r\n\r\ntomer\r\n.\r\n')
    print my_socket.recv(1024)
    my_socket.send('QUIT\r\n')
    print my_socket.recv(1024)


if __name__ == "__main__":
    main()
