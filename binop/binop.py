# coding=utf-8
# 解析 elf 文件需要导入的依赖库
# 安装 pyelftools 库成功 , 安装 elftools 库会报错
from elftools.elf.elffile import ELFFile
# 导入 Capstone 反汇编框架 , 用于解析 ELF 文件
from capstone import *
from elftools import *


def main(arg):

    # 要解析的动态库路径
    elf_path = arg
    # 打开 elf 文件
    file = open(elf_path, 'rb')
    # 创建 ELFFile 对象 , 该对象是核心对象
    elf_file = ELFFile(file)

    # 打印 elf 文件头
    print(elf_file.header)
    # 打印 程序头入口 个数
    print(elf_file.num_segments())
    # 打印 节区头入口 个数
    print(elf_file.num_sections())

    # 遍历打印 程序头入口
    for segment in elf_file.iter_segments():
        print(segment.header)

    # 遍历打印 节区头入口
    for section in elf_file.iter_sections():
        print('name:', section.name)
        print('header', section.header)

        # 使用 Capstone 反汇编框架
        # 节区入口名称是 .text , 表示该节区数据是代码数据
        if section.name == '.text':
            # 获取节区地址
            file.seek(section.header['sh_addr'])
            # 获取节区大小
            sh_size = section.header['sh_size']
            # 读取 节区 二进制数据
            #   这是需要反汇编的机器码数据
            raw = file.read(sh_size)
            # 创建 Capstone 实例对象
            capstone = Cs(CS_ARCH_X86, CS_MODE_32)
            # 此处设置为 true , 表示需要显示细节 , 打开后 , 会标明每条汇编代码中对寄存器的影响
            #   如 : 本条汇编代码中 , 会读写哪些寄存器
            capstone.detail = True
            # 向汇编解析器中传入 节区数据 对应的 二进制数据 , 这些二进制数据都是机器码数据
            #   即 , 需要反汇编这些二进制数据为 汇编 代码
            # 第一个参数设置二进制数据
            # 第二个参数指的是读取 raw 二进制数据的起始地址 , 一般设置 0 即可
            # 得到的是反汇编后的汇编代码列表 , 如果反汇编失败 , 此处为空
            disasm = capstone.disasm(raw, 0)
            # 遍历反汇编代码列表
            for line in disasm:
                # 打印每行汇编代码的 地址 , 指令 , 操作对象
                text = '%08X: %s %s ' % (line.address, line.mnemonic, line.op_str)
                # 统计汇编代码行的字符串个数 , 保证在第 55 字节处打印寄存器读写信息
                # 00000000: push ebx                                     ; 读寄存器:esp 写寄存器:esp ; 机器码 :53
                length = len(text)
                if length < 55:
                    text += ' ' * (55 - length)
                text += ';'
                # 读取操作影响到的寄存器
                if hasattr(line, 'regs_read') and len(line.regs_read) > 0:
                    text += ' 读寄存器:'
                    for j, r in enumerate(line.regs_read):
                        if j > 0:
                            text += ','
                        text += '%s' % line.reg_name(r)
                # 写出操作影响到的寄存器
                if hasattr(line, 'regs_write') and len(line.regs_write) > 0:
                    text += ' 写寄存器:'
                    for j, r in enumerate(line.regs_write):
                        if j > 0:
                            text += ','
                        text += '%s' % line.reg_name(r)
                text += ' ; 机器码 :'
                # 打印 本条汇编代码对应的 机器码
                for i in range(line.size):
                    text += '%02X ' % line.bytes[i]
                # 打印最终数据
                print(text)
            pass
    # 关闭文件
    file.close()
    pass


class ELFop(object):
    def __init__(self):
        self.status = None


if __name__ == '__main__':
    main()
