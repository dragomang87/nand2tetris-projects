
// VM function Sys.init 0
(function_label.08_FunctionCalls_FibonacciElement_Sys.vm.Sys.init)
@0
 D  = A
@SP
  M = M + D
// VM push constant 4
// ASM['push value'](4)
@4
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM call Main.fibonacci 1
// ASM['push value'](return_label.08_FunctionCalls_FibonacciElement_Sys.vm.Main.fibonacci.instance_label_{ASM['instance_label_index']})
@return_label.08_FunctionCalls_FibonacciElement_Sys.vm.Main.fibonacci.instance_label_{ASM['instance_label_index']}
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// ASM['push ram'](LCL)
@LCL
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// ASM['push ram'](ARG)
@ARG
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// ASM['push ram'](THIS)
@THIS
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// ASM['push ram'](THAT)
@THAT
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// function LCL = SP
 D  = M
@LCL
  M = D
// function ARG = SP - n_frame - n_arguments = SP - 5 - 1
@5
 D  = D - A
@1
 D  = D - A
@ARG
  M = D
 D  = 0             // optional safety feature
@function_label.08_FunctionCalls_FibonacciElement_Sys.vm.Main.fibonacci
JMP
(return_label.08_FunctionCalls_FibonacciElement_Sys.vm.Main.fibonacci.instance_label_{ASM['instance_label_index']})
// VM label END
(vm_label.08_FunctionCalls_FibonacciElement_Sys.vm.END)
// VM goto END
@vm_label.08_FunctionCalls_FibonacciElement_Sys.vm.END
JMP