
// VM push constant 3030
@3030
 D  = A
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM pop pointer 0
// ASM pop stack
@SP
A M = M - 1
 D  = M
  M = 0 // optional safety feature
@THIS
  M = D
 D  = 0 // optional safety feature
// VM push constant 3040
@3040
 D  = A
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM pop pointer 1
// ASM pop stack
@SP
A M = M - 1
 D  = M
  M = 0 // optional safety feature
@THAT
  M = D
 D  = 0 // optional safety feature
// VM push constant 32
@32
 D  = A
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM pop temp 2
// ASM D = temp + 2
@temp
 D  = M
@2
D = D + A
@SP
A M = M - 1
 D  = D + M
A   = D - M
  M = D - A
 D  = 0     // optional safety feature
@SP       // optional safety feature
A   = M + 1 // optional safety feature
  M = 0     // optional safety feature
// VM push constant 46
@46
 D  = A
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM pop temp 6
// ASM D = temp + 6
@temp
 D  = M
@6
D = D + A
@SP
A M = M - 1
 D  = D + M
A   = D - M
  M = D - A
 D  = 0     // optional safety feature
@SP       // optional safety feature
A   = M + 1 // optional safety feature
  M = 0     // optional safety feature
// VM push pointer 0
@THIS
 D  = M
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM push pointer 1
@THAT
 D  = M
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM add
// ASM pop stack
@SP
A M = M - 1
 D  = M
  M = 0 // optional safety feature
A   = A - 1
  M = M + D
 D  = 0 // optional safety feature
// VM push temp 2
// ASM A = temp + 2
@temp
 D  = M
@2
A = D + A
 D  = M
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM sub
// ASM pop stack
@SP
A M = M - 1
 D  = M
  M = 0 // optional safety feature
A   = A - 1
  M = M - D
 D  = 0 // optional safety feature
// VM push temp 6
// ASM A = temp + 6
@temp
 D  = M
@6
A = D + A
 D  = M
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM add
// ASM pop stack
@SP
A M = M - 1
 D  = M
  M = 0 // optional safety feature
A   = A - 1
  M = M + D
 D  = 0 // optional safety feature