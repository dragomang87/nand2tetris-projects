
// VM push constant 7
@7
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 8
@8
 D  = A
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