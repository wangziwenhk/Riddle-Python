from src.ir.builders import Builder
from llvmlite import ir

module = ir.Module('main')
a = Builder(module)
a.create_function('main',ir.IntType(32))
v1 = a.create_allocate(ir.IntType(32),'a')
v2 = a.create_allocate(ir.IntType(32),'b')
a.create_store(ir.Constant(ir.IntType(32), 1),v1)
a.create_store(ir.Constant(ir.IntType(32), 1),v2)
v1 = a.create_add(v1,v2)
print(module)
