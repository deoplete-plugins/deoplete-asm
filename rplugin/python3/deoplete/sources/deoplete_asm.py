import re
import os

from .base import Base
from deoplete.util import error, load_external_module

load_external_module(__file__, '')
from exegesis.proto.pdf.x86 import intel_sdm_pb2 as intel_sdm  # noqa: E261


class Source(Base):

    def __init__(self, vim):
        super(Source, self).__init__(vim)

        self.name = 'asm'
        self.mark = '[asm]'
        self.rank = 500
        self.filetypes = ['gas', 'masm']

        self.instructions = intel_sdm.SdmDocument()
        self.result = []  # for cache

    def on_init(self, context):
        pb = '{}/pb/instructions.sdm.pb'.format(os.path.dirname(__file__))
        try:
            f = open(pb, "rb")  # binary mode for predump protobuf data
            self.instructions.ParseFromString(f.read())
            f.close()
        except IOError:
            error(self.vim, 'could not open {}'.format(pb))

    def get_complete_position(self, context):
        m = re.search(r'\w*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        if not self.result:
            for section in self.instructions.instruction_sections:
                for instructions in section.instruction_table.instructions:
                    vendor_syntax = instructions.vendor_syntax
                    mnemonic = str(vendor_syntax.mnemonic).lower()
                    operand = ''
                    for i, op in enumerate(vendor_syntax.operands):
                        operand += op.name
                        if i < len(vendor_syntax.operands)-1:
                            operand += ', '
                    abbr = '{} {}'.format(mnemonic, operand)
                    self.result.append(
                        dict(
                            word=mnemonic,
                            abbr=abbr,
                            kind=instructions.description,
                            info=abbr,
                            dup=1)
                    )

        return self.result
