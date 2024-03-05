import socket


def client(host='127.0.0.1', port=2000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))

        while True:
            data = input("[+] Enter string : ")
            sock.sendall(data.encode('utf-8'))
            print("[+] Sending to {}:{}".format(host, port))
            response = sock.recv(4096)
            print("[+] Received", repr(response.decode('utf-8')))

            if not response:
                print("[-] Not Received")
                break


if __name__ == "__main__":
    client()
