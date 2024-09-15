from llvmlite import ir

from src.ir.builders import Builder
from src.ir.types import Class
from src.parser.RiddleParser import RiddleParser as Parser, RiddleParser
from src.parser.RiddleParserVisitor import RiddleParserVisitor


class GenVisitor(RiddleParserVisitor):
    def __init__(self, name: str = ''):
        self.module: ir.Module = ir.Module(name)
        self.builder: Builder = Builder(self.module)

    def visitProgram(self, ctx: Parser.ProgramContext):
        self.builder.push()
        self.visitChildren(ctx)
        self.builder.pop()

    def visitFuncDefine(self, ctx: RiddleParser.FuncDefineContext):
        func_name: str = ctx.funcName.text
        func_args: dict[str:str] = self.visit(ctx.args)
        if ctx.returnType is None:
            return_type = ir.VoidType()
        else:
            return_type = self.visitTypeName(ctx.returnType)

        self.builder.create_function(func_name, return_type, func_args)
        self.visit(ctx.body)

    def visitDefineArgs(self, ctx: RiddleParser.DefineArgsContext) -> dict[str:str]:
        args: dict[str:str] = {}
        temp_name: str = ""
        temp_type: str = ""
        if ctx.children is None:
            return args
        for i in ctx.children:
            # 参数名称
            if isinstance(i, RiddleParser.Identifier):
                temp_name = i.getText()

            # 参数类型
            if isinstance(i, RiddleParser.TypeNameContext):
                temp_type = i.getText()

            # 压入参数
            if temp_name != "" and temp_type != "":
                args[temp_name] = temp_type

        return args

    def visitTypeName(self, ctx: RiddleParser.TypeNameContext) -> ir.Type:
        name = ctx.getText()
        return self.builder.getType(name)

    def visitInteger(self, ctx: RiddleParser.IntegerContext) -> int:
        return ctx.value

    def visitFloat(self, ctx: RiddleParser.FloatContext) -> float:
        return ctx.value

    def visitBoolean(self, ctx: RiddleParser.BooleanContext) -> bool:
        return ctx.value
