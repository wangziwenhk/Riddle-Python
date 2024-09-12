from src.ir.Builder import Builder
from llvmlite import ir

module = ir.Module('main')
a = Builder(module)
a.CreateFunction('main',ir.IntType(32))
v1 = a.CreateAllocate(ir.IntType(32),'a')
v2 = a.CreateAllocate(ir.IntType(32),'b')
a.CreateStore(ir.Constant(ir.IntType(32), 1),v1)
a.CreateStore(ir.Constant(ir.IntType(32), 1),v2)
v1 = a.CreateAdd(v1,v2)
print(module)
