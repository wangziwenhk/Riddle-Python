import Type
from llvmlite import ir

class Builder:
    def __init__(self,module:ir.Module):
        self.module = module
        self.context = module.context

    def getModule(self):
        return self.module
