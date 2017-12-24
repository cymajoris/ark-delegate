#!/usr/bin/python3
# Python auto payment script for ARK voters
# by majoris

from pythark import *

# Class inits
acc = Account()
d   = Delegate()

# Constants
own_addr = 'APi28EMFUBEfgVwXr6rWLNqY2ra2R7eJSa'
own_nick = 'majoris'
own_key  = '02e732cfe59f6c6c5d7401aa9afd78197d1fef14ffd86ee6eb1693be01a4900082'

# Variables
voters   = []

def get_balance(address):
    balance = acc.get_balance(address)
    ret = int(balance['balance']) / (10**8)
    return ret

def delegate_info(nickname):
    info = d.search_delegates(nickname)
    return info

def pick_element(nickname, element):
    info = delegate_info(nickname)
    ret = info['delegates'][0][element]
    return ret

def get_voters(nickname):
    pubkey = pick_element(nickname, 'publicKey')
    voters = d.get_voters(pubkey)
    return voters

brut_voters = get_voters('goose')['accounts']
for info_block in brut_voters:
    voters.append(info_block['address'])

for voter in voters:
    print(voter)

