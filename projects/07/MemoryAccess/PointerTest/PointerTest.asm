
// VM push constant 3030
@3030
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop pointer 0
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THIS
  M = D
 D  = 0             // optional safety feature
// VM push constant 3040
@3040
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop pointer 1
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THAT
  M = D
 D  = 0             // optional safety feature
// VM push constant 32
@32
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop this 2
// D = this + 2 = destination
@THIS
 D  = M
@2
 D  = D + A
// A = stack, M = value
@SP
A M = M - 1
// D = destination + value
 D  = D + M
// A = destination, M = ?
A   = D - M
// A = destination, M = value
  M = D - A
 D  = 0         // optional safety feature
@SP             // optional safety feature
A   = M         // optional safety feature
  M = 0         // optional safety feature
// VM push constant 46
@46
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop that 6
// D = that + 6 = destination
@THAT
 D  = M
@6
 D  = D + A
// A = stack, M = value
@SP
A M = M - 1
// D = destination + value
 D  = D + M
// A = destination, M = ?
A   = D - M
// A = destination, M = value
  M = D - A
 D  = 0         // optional safety feature
@SP             // optional safety feature
A   = M         // optional safety feature
  M = 0         // optional safety feature
// VM push pointer 0
@THIS
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push pointer 1
@THAT
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
// VM push this 2
// A = this + 2 = source
@THIS
 D  = M
@2
A   = D + A
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
// VM push that 6
// A = that + 6 = source
@THAT
 D  = M
@6
A   = D + A
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