from llvmlite import ir


class Builder:
    def __init__(self, module: ir.Module):
        self.module = module
        self.context = module.context
        self.builder: ir.IRBuilder

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
        if self.builder is None:
            raise RuntimeError("Cannot create statement outside the allowed scope")
        return self.builder.add(x, y)

    def CreateSub(self, x: ir.Value, y: ir.Value) -> ir.Value:
        if self.builder is None:
            raise RuntimeError("Cannot create statement outside the allowed scope")
        return self.builder.sub(x, y)

    def CreateMul(self, x: ir.Value, y: ir.Value) -> ir.Value:
        if self.builder is None:
            raise RuntimeError("Cannot create statement outside the allowed scope")
        return self.builder.mul(x, y)

    def CreateStore(self, value: ir.Value, ptr: ir.Value) -> ir.Value:
        if self.builder is None:
            raise RuntimeError("Cannot create statement outside the allowed scope")
        return self.builder.store(value, ptr)

    def CreateLoad(self, ptr: ir.Value, name: ir.Value) -> ir.Value:
        if self.builder is None:
            raise RuntimeError("Cannot create statement outside the allowed scope")
        return self.builder.load(ptr, name)

    def CreateAllocate(self, typ: ir.Type, name: str = '') -> ir.Value:
        if self.builder is None:
            raise RuntimeError("Cannot create statement outside the allowed scope")
        return self.builder.alloca(typ, name=name)
