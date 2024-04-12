
// VM push constant 111
@111
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM push constant 333
@333
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM push constant 888
@888
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM pop  static (static.MemoryAccess/StaticTest/StaticTest.vm) 8
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
@static.MemoryAccess/StaticTest/StaticTest.vm.8
M = D
D = 0 // optional safety feature
// VM pop  static (static.MemoryAccess/StaticTest/StaticTest.vm) 3
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
@static.MemoryAccess/StaticTest/StaticTest.vm.3
M = D
D = 0 // optional safety feature
// VM pop  static (static.MemoryAccess/StaticTest/StaticTest.vm) 1
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
@static.MemoryAccess/StaticTest/StaticTest.vm.1
M = D
D = 0 // optional safety feature
// VM push static (static.MemoryAccess/StaticTest/StaticTest.vm) 3
@static.MemoryAccess/StaticTest/StaticTest.vm.3
D = M
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM push static (static.MemoryAccess/StaticTest/StaticTest.vm) 1
@static.MemoryAccess/StaticTest/StaticTest.vm.1
D = M
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM sub
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
A = A - 1
M = M - D
D = 0 // optional safety feature
// VM push static (static.MemoryAccess/StaticTest/StaticTest.vm) 8
@static.MemoryAccess/StaticTest/StaticTest.vm.8
D = M
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM add
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
A = A - 1
M = M + D
D = 0 // optional safety feature