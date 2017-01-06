#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import os, signal, subprocess

def scanQR():
    # mit display und 640x480 Auflösung
    #zbarcam=subprocess.Popen("zbarcam --raw --prescale=640x480 /dev/video0", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    # mit Display und max. Auflösung
    #zbarcam=subprocess.Popen("zbarcam --raw /dev/video0", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    # ohne Display und max. Auflösung
    qrcam=subprocess.Popen("zbarcam --raw --nodisplay /dev/video0", stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
    print 'QR-Code wird gescannt'
    while True:
        plaintext=qrcam.stdout.readline()
        if plaintext!='':
            print 'QR scannen erfolgreich!'
            break
    os.killpg(qrcam.pid, signal.SIGTERM)  # Prozess stoppen
    print 'QR-scan beendet'
    return plaintext