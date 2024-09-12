from src.ir.Builder import Builder
from llvmlite import ir

module = ir.Module("main")
a = Builder(module)
a.CreateFunction("af",ir.IntType(32))
a.CreateAllocate('b','b')
