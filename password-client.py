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
    PORT = 6666        # Port ID number used by the server
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Kombucha!')
        data = s.recv(1024)

    print('Received', repr(data))

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))