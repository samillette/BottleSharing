#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  echo-server.py
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
	
	Socket program for my kombucha bottle sharing server hosted on a raspberry pi 4
"""

import socket

def main(args):
    HOST = '10.0.0.61'    # Host IP address (pi bishop IP)
    PORT = 4321        # Port ID number used by the server

    # initializes socket object as s
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        # connects to the server socket
        s.connect((HOST, PORT))
        print("connection to" + HOST + " over confirmed")

        # sends introductory 'password'
        s.send(b'Kombucha!')

        # receives yes confirmation (if it was a no the socket would close anyways
        if s.recv(1) == b'Y':
            print("connection confirmed")

            #TODO: QR code in order to read and load bottle ID number

            # sends bottle number (placeholder for now)
            s.sendall(b"99")

            # receive state of the bottle leading to different layout on the app
            bottle_state = s.recv(1)

            #TODO: find interface between python and Android to make layout change conditional to bottle state
        print(bottle_state.decode('UTF-8'))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
