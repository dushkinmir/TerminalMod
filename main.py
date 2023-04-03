from base.module import BaseModule

# Extensions
from .extensions.eval import EvalCmd
from .extensions.term import TermCmd

class TerminalMod(BaseModule):
    @property
    def module_extensions(self):
        return [
            TermCmd,
            EvalCmd
        ]