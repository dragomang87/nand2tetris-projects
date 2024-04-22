
// VM function Sys.init 0
(function_label.08_FunctionCalls_StaticsTest_Sys.vm.Sys.init)
@0
 D  = A
@SP
  M = M + D
// VM push constant 6
// ASM['push value'](6)
@6
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 8
// ASM['push value'](8)
@8
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM call Class1.set 2
// ASM['push value'](return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class1.set.instance_label_{ASM['instance_label_index']})
@return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class1.set.instance_label_{ASM['instance_label_index']}
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
// function ARG = SP - n_frame - n_arguments = SP - 5 - 2
@5
 D  = D - A
@1
 D  = D - A
@ARG
  M = D
 D  = 0             // optional safety feature
@function_label.08_FunctionCalls_StaticsTest_Sys.vm.Class1.set
JMP
(return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class1.set.instance_label_{ASM['instance_label_index']})
// VM pop temp 0
// D = temp + 0 = destination
@5   
 D  = A
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
// VM push constant 23
// ASM['push value'](23)
@23
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 15
// ASM['push value'](15)
@15
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM call Class2.set 2
// ASM['push value'](return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class2.set.instance_label_{ASM['instance_label_index']})
@return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class2.set.instance_label_{ASM['instance_label_index']}
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
// function ARG = SP - n_frame - n_arguments = SP - 5 - 2
@5
 D  = D - A
@1
 D  = D - A
@ARG
  M = D
 D  = 0             // optional safety feature
@function_label.08_FunctionCalls_StaticsTest_Sys.vm.Class2.set
JMP
(return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class2.set.instance_label_{ASM['instance_label_index']})
// VM pop temp 0
// D = temp + 0 = destination
@5   
 D  = A
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
// VM call Class1.get 0
@SP
  M = M + 1
// ASM['push value'](return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class1.get.instance_label_{ASM['instance_label_index']})
@return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class1.get.instance_label_{ASM['instance_label_index']}
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
// function ARG = SP - n_frame - n_arguments = SP - 5 - 0
@5
 D  = D - A
@0
 D  = D - A
@ARG
  M = D
 D  = 0             // optional safety feature
@function_label.08_FunctionCalls_StaticsTest_Sys.vm.Class1.get
JMP
(return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class1.get.instance_label_{ASM['instance_label_index']})
// VM call Class2.get 0
@SP
  M = M + 1
// ASM['push value'](return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class2.get.instance_label_{ASM['instance_label_index']})
@return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class2.get.instance_label_{ASM['instance_label_index']}
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
// function ARG = SP - n_frame - n_arguments = SP - 5 - 0
@5
 D  = D - A
@0
 D  = D - A
@ARG
  M = D
 D  = 0             // optional safety feature
@function_label.08_FunctionCalls_StaticsTest_Sys.vm.Class2.get
JMP
(return_label.08_FunctionCalls_StaticsTest_Sys.vm.Class2.get.instance_label_{ASM['instance_label_index']})
// VM label END
(vm_label.08_FunctionCalls_StaticsTest_Sys.vm.END)
// VM goto END
@vm_label.08_FunctionCalls_StaticsTest_Sys.vm.END
JMP