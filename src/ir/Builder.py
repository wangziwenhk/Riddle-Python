import Type
from llvmlite import ir


class Builder:
    def __init__(self, module: ir.Module):
        self.module = module
        self.context = module.context
        self.builder = None

    def getModule(self) -> ir.Module:
        return self.module

    def getContext(self) -> ir.Context:
        return self.context

    def CreateFunction(self, name: str, return_type: ir.types, args=None):
        if args is None:
            args = []

        # Create
        func_type = ir.FunctionType(return_type, args)
        function = ir.Function(self.module, func_type, name)

        block = function.append_basic_block('entry')
        self.builder = ir.IRBuilder(block)

    def CreateAdd(self, x: ir.Value, y: ir.Value) -> ir.Value:
        return self.builder.CreateAdd(x, y)
