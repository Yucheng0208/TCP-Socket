import socket

from datetime import datetime


def server(host='0.0.0.0', port=2000):
    # create socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        # sock.setblocking(False)
        print("[+] Listening on {0}:{1}".format(host, port))
        sock.listen(5)
        # permit to access
        connect, addr = sock.accept()

        with connect as conn:
            # display the current time
            time = datetime.now().ctime()
            print("[+] Connecting by {0}:{1} ({2})".format(
                addr[0], addr[1], time))

            while True:
                request = conn.recv(4096)
                print("[+] Received", repr(request.decode('utf-8')))
                response = input("[+] Enter string : ")
                conn.sendall(response.encode('utf-8'))
                print("[+] Sending to {0}:{1}".format(addr[0], addr[1]))

                if not request:
                    print("[-] Not Received")
                    break


if __name__ == "__main__":
    server()
