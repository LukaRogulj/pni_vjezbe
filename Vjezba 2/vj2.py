import socket
import re

visitedPages = []

def scraper(link):
    
    if(len(visitedPages) >= 50):
        return
    
    if(link in visitedPages):
        return

    source = getSource(link)
    visitedPages.append(link)
    unopendLinks = getLink(source)
    
    for pageLink in unopendLinks:
        scraper(pageLink)

    

def getSource(link):
    print(link)
    HOST = 'www.sheldonbrown.com'
    PORT = 80 

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddress = (HOST, PORT)
    clientSocket.connect(serverAddress)

    request_header = b'GET / HTTP/1.0\r\nHost: www.sheldonbrown.com\r\n\r\n'
    clientSocket.sendall(request_header)

    response = ''
    while True:
        recv = clientSocket.recv(1024)
        if not recv:
            break
        response += str(recv)
        
    return response


def getLink(source):

    return re.findall('http://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', source)



#print(socket.gethostbyname_ex('https://www.sheldonbrown.com/')
scraper("www.watchthatpage.com")
print(visitedPages)