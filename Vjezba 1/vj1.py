# -*- coding: utf-8 -*-
import socket
import time
import threading
import sys

recvMsg = ""
sentMsg = ""
inputMsg = ""
sendingMsg = False

def startServer():
    global recvMsg
    global sentMsg
    
    HOST = socket.gethostname()
    PORT = int(sys.argv[1])
        
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(3)
        while True:
            conn, addr = s.accept()
            #print('Started server on:', addr)
            
            with conn:
                recvMsg = (conn.recv(1024)).decode()
                #if (sentMsg != recvMsg and recvMsg != inputMsg):
                    #print(recvMsg)

                
def connectToServer():
    global recvMsg
    global sentMsg 
    global sendingMsg
    global inputMsg
    
    try:
        HOST = socket.gethostname()
        PORT = int(sys.argv[2])
        
        while True:
            time.sleep(1)
           
            if(sentMsg != recvMsg and recvMsg != inputMsg):
                print(inputMsg)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((HOST, PORT))
                    s.send(recvMsg.encode())
                    sentMsg = recvMsg
                    
            if (sendingMsg == True):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((HOST, PORT))
                    s.send(inputMsg.encode())
                    sendingMsg = False
                    sentMsg = inputMsg
                    
    except Exception as e:
        connectToServer()
        
def inputMessage():
    while True:
        global inputMsg
        global sendingMsg
        
        inputMsg = input("Unesite poruku: ")
        sendingMsg = True
        


threading._start_new_thread(startServer,())
threading._start_new_thread(inputMessage,())
connectToServer()