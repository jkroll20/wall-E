import socket

s = None

def init():
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("172.22.99.6", 1338))

def pixel(x, y, color="ff0000"):
	s.send("02%02x%02x%s\r\n" % (x + 1, y + 1 , color)) # fixed wrong direction

def frame(buf):
	s.send("03%s\r\n" % buf)

def send(buf):
	s.send(buf + "\r\n")

def clear(): frame("0" * 6 * 15 * 16)

