#!/usr/bin/env python3

import xml.dom.minidom
import urllib.request

from collections import OrderedDict

opcode_xml = urllib.request.urlopen('https://github.com/Maratyszcza/Opcodes/raw/master/opcodes/x86_64.xml')
domtree = xml.dom.minidom.parse(opcode_xml)
instructions = domtree.documentElement.getElementsByTagName('Instruction')

out = """# Generated by the tools/gen_goopcode.py. DO NOT EDIT!
# This conversion list acquired from https://github.com/Maratyszcza/Opcodes/raw/master/opcodes/x86_64.xml

class go(object):
    symbols = [
        {
            'word': 'FP',
            'abbr': 'FP',
            'kind': 'Frame pointer: arguments and locals.',
            'info': 'FP Frame pointer: arguments and locals.',
            'dup': 1
        },
        {
            'word': 'PC',
            'abbr': 'PC',
            'kind': 'Program counter: jumps and branches.',
            'info': 'PC Program counter: jumps and branches.',
            'dup': 1
        },
        {
            'word': 'SB',
            'abbr': 'SB',
            'kind': 'Static base pointer: global symbols.',
            'info': 'SB Static base pointer: global symbols.',
            'dup': 1
        },
        {
            'word': 'SP',
            'abbr': 'SP',
            'kind': 'Stack pointer: top of stack.',
            'info': 'SP Stack pointer: top of stack.',
            'dup': 1
        },
        {
            'word': 'DATA',
            'abbr': 'DATA',
            # TODO(zchee):
            # 'kind': ,
            # 'info': ,
            'dup': 1
        },
        {
            'word': 'GLOBL',
            'abbr': 'GLOBL',
            # TODO(zchee):
            # 'kind': ,
            # 'info': ,
            'dup': 1
        },
        {
            'word': 'FUNCDATA',
            'abbr': 'FUNCDATA',
            # TODO(zchee):
            # 'kind': ,
            # 'info': ,
            'dup': 1
        },
        {
            'word': 'PCDATA',
            'abbr': 'PCDATA',
            # TODO(zchee):
            # 'kind': ,
            # 'info': ,
            'dup': 1
        },
        {
            'word': 'TEXT',
            'abbr': 'TEXT',
            # TODO(zchee):
            # 'kind': ,
            # 'info': ,
            'dup': 1
        },
    ]

    mnemonics = dict({
"""
d = OrderedDict()
for instruction in instructions:
    instruction_form = instruction.getElementsByTagName('InstructionForm')
    for ins in instruction_form:
        go = ins.getAttribute('go-name')
        if go and not d.get(go):
            gas = ins.getAttribute('gas-name')
            d[go] = gas

for go, gas in d.items():
    out += "        '{}': '{}',\n".format(gas, go)

out += '    })'
print(out)
