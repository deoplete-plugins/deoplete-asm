#!/usr/bin/env python3

import xml.dom.minidom
import urllib.request

opcode_xml = urllib.request.urlopen('https://github.com/Maratyszcza/Opcodes/raw/master/opcodes/x86_64.xml')
domtree = xml.dom.minidom.parse(opcode_xml)
instructions = domtree.documentElement.getElementsByTagName('Instruction')

out = 'class go(object):\n    mnemonics = dict({\n'
for instruction in instructions:
    instruction_form = instruction.getElementsByTagName('InstructionForm')
    for ins in instruction_form:
        go = ins.getAttribute('go-name')
        if go:
            gas = ins.getAttribute('gas-name')
            out += "        '{}': '{}',\n".format(gas, go)
out += '    })'
print(out)
