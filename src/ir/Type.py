import enum

class Type:
    class TypeID(enum.Enum):
        Variable = 1

    def __init__(self, typeid: TypeID):
        self.type = typeid

    def getType(self) -> TypeID:
        return self.type
