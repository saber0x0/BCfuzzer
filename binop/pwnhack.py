# encoding = utf-8
import os
import sys
import time
import struct
from importlib import reload
import requests
import re
import random
from pwn import *
from LibcSearcher import *
from cmd import Cmd
from rich.console import Console
import binop
from subprocess import *


console = Console()


class Client(Cmd):
    prompt = time.strftime('\033[1;31mhuahua>\033[32m')  # 自定义交互式提示字符串
    intro = time.strftime('\033[1;35mBCfuzzer!\033[36m')

    def __init(self):
        reload(sys)
        Cmd.__init__(self)

    def do_ls(self, arg):
        if not arg:
            print("\t".join(os.listdir("./")))
            # self.help_ls()
        elif os.path.exists(arg):
            print("\t".join(os.listdir(arg)))
        else:
            print("No such pathexists.")

    def do_readelf(self, arg):
        if not arg:
            print("no args")
        elif os.path.exists(arg):
            binop.main(arg)
        else:
            print("No such file.")

    def do_objdump(self, arg):
        if not arg:
            print("no args")
        elif os.path.exists(arg):
            os.system("objdump -M intel -d " + arg)
        else:
            print("No such file.")

    def do_clear(self, arg):
        # call("cls||clear")
        os.system('cls||clear')
        pass
        # sys.stdout.flush()

    def emptyline(self):  # 当输入空行的时候
        pass

    def do_hello(self, arg):
        print('hello', arg)

    def do_quit(self, arg):
        print('Bye!')
        return True  # 返回True，直接输入exit命令将会退出




class COMMON(object):
    context.log_level = "debug"


if __name__ == '__main__':
    client = Client()
    client.cmdloop()

"""
context.log_level = "debug"
context.os = 'linux'
context.arch = 'amd64'

binary = ""
libcelf = ""
ip = ""
port = ""
local = 1
arm = 0
mips = 0
riscv = 0
core = 64

s = lambda data: p.send(str(data))
sa = lambda delim, data: p.sendafter(str(delim), str(data))
sl = lambda data: p.sendline(str(data))
sla = lambda delim, data: p.sendlineafter(str(delim), str(data))
r = lambda num=4096: p.recv(num)
ru = lambda delims, drop=True: p.recvuntil(delims, drop)
itr = lambda: p.interactive()
uu32 = lambda data: u32(data.ljust(4, 'x00'))
uu64 = lambda data: u64(data.ljust(8, 'x00'))
leak = lambda name, addr: log.success('{} = {:#x}'.format(name, addr))

if local == 1:
    if arm == 1:
        if core == 64:
            p = process(["qemu-arm", "-g", "1212", "-L", "/usr/arm-linux-gnueabi", binary])
        if core == 32:
            p = process(["qemu-aarch64", "-g", "1212", "-L", "/usr/aarch64-linux-gnu/", binary])
    # mips/riscv
    else:
        p = process(binary)
else:
    p = remote(ip, port)

elf = ELF(binary)
libc = ELF(libcelf)


def pwn():
    pass


if __name__ == '__main__':
    pwn()
"""
