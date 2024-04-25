
// VM push constant 0
// ASM['push value'](0)
@0
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM pop local 0
// D = local + 0 = destination
@LCL 
  D = M
@0
  D = D + A
// ASM['move stack']
// D = destination
@SP
AM  = M - 1
  D = D + M
// A = stack, M = value
// D = destination + value
// A = destination, M = ?
A   = D - M
// A = destination, M = value
 M  = D - A
  D = 0             // optional safety feature
@SP                 // optional safety feature
A   = M             // optional safety feature
 M  = 0             // optional safety feature
// VM label LOOP
(vm_label|LOOP|LOOP)
// VM push argument 0
// A = argument + 0 = source
@ARG 
  D = M
@0
A   = D + A
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM push local 0
// A = local + 0 = source
@LCL 
  D = M
@0
A   = D + A
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM add
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = A - 1
 M  = M + D
  D = 0             // optional safety feature
// VM pop local 0
// D = local + 0 = destination
@LCL 
  D = M
@0
  D = D + A
// ASM['move stack']
// D = destination
@SP
AM  = M - 1
  D = D + M
// A = stack, M = value
// D = destination + value
// A = destination, M = ?
A   = D - M
// A = destination, M = value
 M  = D - A
  D = 0             // optional safety feature
@SP                 // optional safety feature
A   = M             // optional safety feature
 M  = 0             // optional safety feature
// VM push argument 0
// A = argument + 0 = source
@ARG 
  D = M
@0
A   = D + A
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM push constant 1
// ASM['push value'](1)
@1
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM sub
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = A - 1
 M  = M - D
  D = 0             // optional safety feature
// VM pop argument 0
// D = argument + 0 = destination
@ARG 
  D = M
@0
  D = D + A
// ASM['move stack']
// D = destination
@SP
AM  = M - 1
  D = D + M
// A = stack, M = value
// D = destination + value
// A = destination, M = ?
A   = D - M
// A = destination, M = value
 M  = D - A
  D = 0             // optional safety feature
@SP                 // optional safety feature
A   = M             // optional safety feature
 M  = 0             // optional safety feature
// VM push argument 0
// A = argument + 0 = source
@ARG 
  D = M
@0
A   = D + A
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM if-goto LOOP
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@vm_label|LOOP|LOOP
D; JNE
// VM push local 0
// A = local + 0 = source
@LCL 
  D = M
@0
A   = D + A
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature