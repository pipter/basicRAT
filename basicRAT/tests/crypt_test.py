#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# lame testing of pseduo testing of crypto from client to server
#


import os

from core.crypto import encrypt, decrypt
from core.transport import json2dict, dict2json, server_to_client, client_to_server


KEY = os.urandom(16)
CMD = "cat"
ACT = "/etc/resolv.conf"


def main():
    # prep data to send to server
    data = server_to_client(CMD, ACT)
    data = dict2json(data)
    enc_data = encrypt(data, KEY)

    # data sent to client
    dec_data = decrypt(enc_data, KEY)
    dec_data = json2dict(dec_data)
    dec_cmd, dec_act = dec_data['command'], dec_data['action']

    # things are working so far :)
    if (CMD == dec_cmd) and (ACT == dec_act):
        print('working!')
    results = os.popen('%s %s' % (CMD, ACT)).read()

    # prep data to send to client
    data = client_to_server(results)
    data = dict2json(data)
    enc_data = encrypt(data, KEY)

    # data sent to server
    dec_data = decrypt(enc_data, KEY)
    dec_data = json2dict(dec_data)
    dec_results = dec_data['results']

    print(dec_results)


if __name__ == '__main__':
    main()
