#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  password-server.py
#  
#  Copyright 2020  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
"""
    Samuel Millette
    7.2.2020
    With the help of RealPython's Socket Programming tutorial

    Socket program mfor my kombucha bottle sharing server hosted on a raspberry pi 4
"""

import socket


def main(args):
    HOST = '10.0.0.61'# Host IP address (pi bishop IP)
    PORT = 4321# Port ID number used by the server
    
    #creates listening socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        
        #binds socket
        s.bind((HOST, PORT))
        
        #sets socket to listen
        s.listen(0)
        
        #on connection, creates a new socket object 'conn' and address of client socket
        conn, addr = s.accept()
        print(f"Connection from {addr} has been established, verifying client ID")
        
        #selects 'conn' socket object for action
        with conn:
            
            #saves initial data for checking
            data = conn.recv(9)
            print(data.decode('UTF-8'))
            
            #simple check to see if opening communication is from a wanted source
            if data != b'Kombucha!':
                print("Connection from {addr} not accepted")
                
                #closes the 'conn' socket object
                #conn.close()
                #'with' statement automatically closes 'conn' at end of statement
            
            #if the opening communication is from a wanted source
            else:
                
                #sends affirmative to client
                conn.send(b'Y')
                print("connection accepted")
                
                #starts the send / receive loop
                
                    #receives data on bottle ID
                    bottleID = conn.recv(2)
                    
                    #TODO add in mySQl data grabber
                    #three paths: bottle found and checked in (I), found and checked out (O), not found (F)
                    
                    #sends state of bottle
                    conn.sendall(b'I')
                    
                    #TODO, code dummy paths with user input to simulate different states, figure out
                    # how to automate this program to run after closure
                    
                    #checks if there is any data received at all
                    if not data:
                        print("Connection from {addr} no longer receiving data")
                        break
                    else:
                        
            print("closing socket")
            conn.sendall(data)
            conn.close()
    s.close()


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
