
// VM push argument 1
// A = argument + 1 = source
@ARG 
 D  = M
@1
A   = D + A
 D  = M
 M  = 0         // optional safety feature
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
// VM push constant 0
// ASM['push value'](0)
@0
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop that 0
// D = that + 0 = destination
@THAT
 D  = M
@0
 D  = D + A
// ASM['move stack']
// D = destination
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
// VM push constant 1
// ASM['push value'](1)
@1
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop that 1
// D = that + 1 = destination
@THAT
 D  = M
@1
 D  = D + A
// ASM['move stack']
// D = destination
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
// VM push argument 0
// A = argument + 0 = source
@ARG 
 D  = M
@0
A   = D + A
 D  = M
 M  = 0         // optional safety feature
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 2
// ASM['push value'](2)
@2
 D  = A
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
// VM pop argument 0
// D = argument + 0 = destination
@ARG 
 D  = M
@0
 D  = D + A
// ASM['move stack']
// D = destination
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
// VM label LOOP
(vm_label.08_ProgramFlow_FibonacciSeries_FibonacciSeries.vm.LOOP)
// VM push argument 0
// A = argument + 0 = source
@ARG 
 D  = M
@0
A   = D + A
 D  = M
 M  = 0         // optional safety feature
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM goto COMPUTE_ELEMENT
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@vm_label.08_ProgramFlow_FibonacciSeries_FibonacciSeries.vm.COMPUTE_ELEMENT
D; JMP
// VM goto END
@vm_label.08_ProgramFlow_FibonacciSeries_FibonacciSeries.vm.END
JMP
// VM label COMPUTE_ELEMENT
(vm_label.08_ProgramFlow_FibonacciSeries_FibonacciSeries.vm.COMPUTE_ELEMENT)
// VM push that 0
// A = that + 0 = source
@THAT
 D  = M
@0
A   = D + A
 D  = M
 M  = 0         // optional safety feature
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push that 1
// A = that + 1 = source
@THAT
 D  = M
@1
A   = D + A
 D  = M
 M  = 0         // optional safety feature
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
// VM pop that 2
// D = that + 2 = destination
@THAT
 D  = M
@2
 D  = D + A
// ASM['move stack']
// D = destination
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
// VM push pointer 1
// ASM['push ram'](THAT)
@THAT
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 1
// ASM['push value'](1)
@1
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
// VM pop pointer 1
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THAT
  M = D
 D  = 0             // optional safety feature
// VM push argument 0
// A = argument + 0 = source
@ARG 
 D  = M
@0
A   = D + A
 D  = M
 M  = 0         // optional safety feature
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 1
// ASM['push value'](1)
@1
 D  = A
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
// VM pop argument 0
// D = argument + 0 = destination
@ARG 
 D  = M
@0
 D  = D + A
// ASM['move stack']
// D = destination
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
// VM goto LOOP
@vm_label.08_ProgramFlow_FibonacciSeries_FibonacciSeries.vm.LOOP
JMP
// VM label END
(vm_label.08_ProgramFlow_FibonacciSeries_FibonacciSeries.vm.END)