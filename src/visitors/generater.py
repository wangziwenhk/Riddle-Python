from llvmlite.ir import Module

from src.ir.builders import Builder
from src.parser.RiddleParser import RiddleParser as Parser, RiddleParser
from src.parser.RiddleParserVisitor import RiddleParserVisitor


class GenVisitor(RiddleParserVisitor):
    def __init__(self, name: str = ''):
        self.module: Module = Module(name)
        self.builder: Builder = Builder(self.module)

    def visitProgram(self, ctx: Parser.ProgramContext):
        self.builder.push()
        self.visitChildren(ctx)
        self.builder.pop()

    def visitFuncDefine(self, ctx:RiddleParser.FuncDefineContext):
        func_name = ctx.funcName

