
// VM push constant 111
@111
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 333
@333
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 888
@888
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop  static (static.07_MemoryAccess_StaticTest_StaticTest.vm) 8
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@static.07_MemoryAccess_StaticTest_StaticTest.vm.8
  M = D
 D  = 0             // optional safety feature
// VM pop  static (static.07_MemoryAccess_StaticTest_StaticTest.vm) 3
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@static.07_MemoryAccess_StaticTest_StaticTest.vm.3
  M = D
 D  = 0             // optional safety feature
// VM pop  static (static.07_MemoryAccess_StaticTest_StaticTest.vm) 1
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@static.07_MemoryAccess_StaticTest_StaticTest.vm.1
  M = D
 D  = 0             // optional safety feature
// VM push static (static.07_MemoryAccess_StaticTest_StaticTest.vm) 3
@static.07_MemoryAccess_StaticTest_StaticTest.vm.3
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push static (static.07_MemoryAccess_StaticTest_StaticTest.vm) 1
@static.07_MemoryAccess_StaticTest_StaticTest.vm.1
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM sub
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
  M = M - D
 D  = 0             // optional safety feature
// VM push static (static.07_MemoryAccess_StaticTest_StaticTest.vm) 8
@static.07_MemoryAccess_StaticTest_StaticTest.vm.8
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM add
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
  M = M + D
 D  = 0             // optional safety feature