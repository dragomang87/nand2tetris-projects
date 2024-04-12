
// VM push constant 10
@10
 D  = A
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM pop temp 0
// ASM D = temp + 0
@temp
 D  = M
@0
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
// VM push constant 21
@21
 D  = A
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM push constant 22
@22
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
// VM pop temp 1
// ASM D = temp + 1
@temp
 D  = M
@1
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
// VM push constant 36
@36
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
// VM push constant 42
@42
 D  = A
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM push constant 45
@45
 D  = A
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM pop temp 5
// ASM D = temp + 5
@temp
 D  = M
@5
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
// VM push constant 510
@510
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
// VM push temp 0
// ASM A = temp + 0
@temp
 D  = M
@0
A = D + A
 D  = M
// ASM push stack
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0 // optional safety feature
// VM push temp 5
// ASM A = temp + 5
@temp
 D  = M
@5
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
// VM push temp 1
// ASM A = temp + 1
@temp
 D  = M
@1
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