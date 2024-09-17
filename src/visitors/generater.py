from antlr4.tree.Tree import TerminalNodeImpl
from llvmlite import ir

from src.ir.builders import Builder
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
        if ctx.funcName is None:
            raise RuntimeError("FuncName is None")
        func_name: str = ctx.funcName.text
        func_args: dict[str, ir.Type] = self.visit(ctx.args)
        if ctx.returnType is None:
            return_type = ir.VoidType()
        else:
            return_type = self.visitTypeName(ctx.returnType)

        self.builder.create_function(func_name, return_type, func_args)
        self.builder.push()
        self.visit(ctx.body)
        self.builder.pop()

    def visitDefineArgs(self, ctx: RiddleParser.DefineArgsContext) -> dict[str, ir.Type]:
        args: dict[str, ir.types] = {}
        temp_name: str = ""
        temp_type: str = ""
        if ctx.children is None:
            return args
        for i in ctx.children:
            # 参数名称
            if isinstance(i, TerminalNodeImpl):
                if i.getSymbol().type == RiddleParser.Identifier:
                    temp_name = i.getText()

            # 参数类型
            if isinstance(i, RiddleParser.TypeNameContext):
                temp_type = i.getText()

            # 压入参数
            if temp_name != "" and temp_type != "":
                args[temp_name] = self.builder.get_type(temp_type)
                temp_name = ""
                temp_type = ""

        return args

    def visitVarDefineStatement(self, ctx: RiddleParser.VarDefineStatementContext):
        if ctx.name is None:
            raise RuntimeError("name is None")
        name: str = ctx.name.text
        value = self.visit(ctx.value) if ctx.value is not None else None
        typ: ir.Type
        if ctx.type_ is not None:
            typ = self.visit(ctx.type_)
        elif value is not None:
            typ = value.type
        else:
            typ = ir.VoidType()
        self.builder.create_variable(typ, name,value)

    def visitReturnStatement(self, ctx: RiddleParser.ReturnStatementContext):
        self.builder.create_return(self.visit(ctx.result))

    def visitTypeName(self, ctx: RiddleParser.TypeNameContext) -> ir.Type:
        name = ctx.getText()
        return self.builder.get_type(name)

    def visitInteger(self, ctx: RiddleParser.IntegerContext) -> ir.Value:
        if ctx.value is None:
            raise RuntimeError("Value is None")
        return self.builder.get_int(ctx.value)

    def visitFloat(self, ctx: RiddleParser.FloatContext) -> ir.Value:
        if ctx.value is None:
            raise RuntimeError("Value is None")
        return self.builder.get_float(ctx.value)

    def visitBoolean(self, ctx: RiddleParser.BooleanContext) -> ir.Value:
        if ctx.value is None:
            raise RuntimeError("Value is None")
        return self.builder.get_bool(ctx.value)

    def visitString(self, ctx: RiddleParser.StringContext) -> str:
        return eval(ctx.getText())

    def visitStatement_ed(self, ctx: RiddleParser.Statement_edContext):
        return self.visit(ctx.children[0])
