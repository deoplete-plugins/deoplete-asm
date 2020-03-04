import os
import re

from typing import List, Any

from .base import Base
from deoplete.util import error, load_external_module
from deoplete.util import Nvim, UserContext, Candidates

load_external_module(__file__, "")
from exegesis.proto.pdf.x86 import intel_sdm_pb2 as intel_sdm  # noqa: E261


class Source(Base):
    def __init__(self, vim: Nvim) -> None:
        super(Source, self).__init__(vim)

        self.name = "asm"
        self.mark = "[asm]"
        self.rank = 500
        self.filetypes = [
            "goasm",
            "gas",
            "asm",
            "anm68k",
            "asmh8300",
            "ia64",
            "masm",
            "nasm",
            "tasm",
        ]
        self.input_pattern = "[^.'\" \t0-9]\\.\\w*"

        self.instructions: Any = intel_sdm.SdmDocument()
        self.result: List = []  # for cache

    def on_init(self, context: UserContext) -> None:
        vars = context["vars"]
        self.go_mode = vars.get("deoplete#sources#asm#go_mode", False)

        pb = "{}/pb/instructions.sdm.pb".format(os.path.dirname(__file__))
        try:
            f = open(pb, "rb")  # binary mode for predump protobuf data
            self.instructions.ParseFromString(f.read())
            f.close()
        except IOError:
            error(self.vim, "could not open {}".format(pb))

    def get_complete_position(self, context: UserContext) -> int:
        m = re.search(r"\w*$", context["input"])
        return m.start() if m else -1

    def gather_candidates(self, context: UserContext) -> Candidates:
        if not self.result:
            if self.go_mode:
                from sources.opcode import go

                self.result += go.symbols

            for section in self.instructions.instruction_sections:
                for instructions in section.instruction_table.instructions:
                    kind = instructions.description

                    vendor_syntax = instructions.vendor_syntax
                    mnemonic = str(vendor_syntax.mnemonic).lower()
                    if self.go_mode:
                        try:
                            kind = "({}) {}".format(mnemonic, kind)
                            mnemonic = go.mnemonics[mnemonic]
                        except Exception:
                            continue

                    operand = ""
                    for i, op in enumerate(vendor_syntax.operands):
                        operand += op.name
                        if i < len(vendor_syntax.operands) - 1:
                            operand += ", "
                    abbr = "{} {}".format(mnemonic, operand)

                    if instructions.feature_name:
                        abbr += " ({})".format(instructions.feature_name)

                    self.result.append(
                        dict(word=mnemonic, abbr=abbr, kind=kind, info=abbr, dup=1)
                    )

        return self.result
