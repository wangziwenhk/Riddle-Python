from src.ir.types import Variable


class VarManager:
    def __init__(self):
        self.vars: dict[str, list] = {}
        self.defined: list[list] = []

    def get(self, item: str):
        # 该变量不存在
        if item not in self.vars:
            raise KeyError('The variable does not exist')
        return self.vars[item][-1]

    def set(self, key: str, value: Variable):
        self.vars[key].append(value)

    # 进入下一个作用域
    def push(self):
        self.defined.append([])

    # 退出当前作用域
    def pop(self):
        # 销毁当前作用域中声明和定义的变量
        for i in self.defined[-1]:
            self.vars[i].pop()
            # 如果一个名称没有对应的变量，则删除这个 map
            if len(self.vars[i]) == 0:
                self.vars.pop(i)

        self.defined.pop()

    def deep(self) -> int:
        return len(self.defined)
