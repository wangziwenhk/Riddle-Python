from llvmlite import ir


class Builder:
    def __init__(self, module: ir.Module):
        self.module = module
        self.context = module.context
        self.builder = None
        self.builder: ir.IRBuilder

    def get_module(self) -> ir.Module:
        return self.module

    def get_context(self) -> ir.Context:
        return self.context

    def create_function(self, name: str, return_type: ir.types, args=None):
        if args is None:
            args = []

        # Create
        func_type = ir.FunctionType(return_type, args)
        function = ir.Function(self.module, func_type, name)

        block = function.append_basic_block('entry')
        self.builder = ir.IRBuilder(block)

    def create_add(self, x: ir.Value, y: ir.Value) -> ir.Value:
        if self.builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.builder.add(x, y)

    def create_sub(self, x: ir.Value, y: ir.Value) -> ir.Value:
        if self.builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.builder.sub(x, y)

    def create_mul(self, x: ir.Value, y: ir.Value) -> ir.Value:
        if self.builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.builder.mul(x, y)

    def create_store(self, value: ir.Value, ptr: ir.Value) -> ir.Value:
        if self.builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.builder.store(value, ptr)

    def create_load(self, ptr: ir.Value, name: ir.Value) -> ir.Value:
        if self.builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.builder.load(ptr, name)

    def create_allocate(self, typ: ir.Type, name: str = '') -> ir.Value:
        if self.builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.builder.alloca(typ, name=name)

    def create_return(self, value: ir.Value = None) -> ir.Value:
        if self.builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')

        if value is None:
            return self.builder.ret_void()

        return self.builder.ret(value)