import enum

from llvmlite import ir


class TypeID(enum.Enum):
    VariableType = 1


class BaseType:
    def __init__(self, typeid: TypeID):
        self.type = typeid

    def getType(self) -> TypeID:
        return self.type


class Variable(BaseType):
    def __init__(self, name: str, value: ir.Value):
        super().__init__(TypeID.VariableType)
        self.name: str = name
        self.value: ir.Value = value

    def getName(self) -> str:
        return self.name

    def getValue(self) -> ir.Value:
        return self.value

    def setValue(self, value: ir.Value):
        self.value = value
