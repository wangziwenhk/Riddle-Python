from venv import create

from dill.pointers import children
from llvmlite import ir
from src.ir.managers import VarManager


class Builder:
    def __init__(self, module: ir.Module):
        self.module = module
        self.context = module.context
        self.llvm_builder = None
        self.llvm_builder: ir.IRBuilder
        self.var_manager = VarManager()

    def get_module(self) -> ir.Module:
        return self.module

    def get_context(self) -> ir.Context:
        return self.context

    def create_function(self, name: str, return_type: ir.types = ir.VoidType(), args: dict[str:str] = None):
        if args is None:
            args = []

        # 创建函数
        func_type = ir.FunctionType(return_type, args)
        function = ir.Function(self.module, func_type, name)

        # 进入函数代码块
        block = function.append_basic_block('entry')
        self.llvm_builder = ir.IRBuilder(block)

    def create_add(self, x: ir.Value, y: ir.Value) -> ir.Value:
        if self.llvm_builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.llvm_builder.add(x, y)

    def create_sub(self, x: ir.Value, y: ir.Value) -> ir.Value:
        if self.llvm_builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.llvm_builder.sub(x, y)

    # 创建一个乘法
    def create_mul(self, x: ir.Value, y: ir.Value) -> ir.Value:
        if self.llvm_builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.llvm_builder.mul(x, y)

    # 创建一个赋值指令
    def create_store(self, value: ir.Value, ptr: ir.Value) -> ir.Value:
        if self.llvm_builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.llvm_builder.store(value, ptr)

    # 创建一个 load 指令
    def create_load(self, ptr: ir.Value, name: ir.Value) -> ir.Value:
        if self.llvm_builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.llvm_builder.load(ptr, name)

    # 创建一个局部变量
    def create_allocate(self, typ: ir.Type, name: str = '') -> ir.Value:
        if self.llvm_builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')
        return self.llvm_builder.alloca(typ, name=name)

    # 创建一个通用变量
    def create_variable(self, typ: ir.Type, name: str = '', value: ir.Value = None, is_const: bool = False) -> ir.Value:
        if self.llvm_builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')

        if self.var_manager.deep() == 1:
            return self.create_variable(typ, name, value, is_const)
        else:
            return self.llvm_builder.alloca(typ, name=name, is_const=is_const)

    # 创建一个全局变量
    def create_global_var(self, typ: ir.Type, name: str, value: ir.Value = None, is_const: bool = False) -> ir.Value:
        global_var = ir.GlobalVariable(self.module, typ, name)
        # 初始化
        global_var.initializer(value)
        # 是否可变
        global_var.global_constant = is_const
        return global_var

    # 创建一个返回语句
    def create_return(self, value: ir.Value = None) -> ir.Value:
        if self.llvm_builder is None:
            raise RuntimeError('Cannot create statement outside the allowed scope')

        if value is None:
            return self.llvm_builder.ret_void()

        return self.llvm_builder.ret(value)

    def push(self):
        self.var_manager.push()

    def pop(self):
        self.var_manager.pop()
