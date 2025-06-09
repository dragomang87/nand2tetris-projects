
// VM function Sys.init 0
// CANNOT assume LCL is zero!!!
(function_define_label|Sys.init)
@SP
 M  = M - 1
@0
  D = A
(function_clean_locals_label|Sys.init)
@SP
AM  = M + 1
 M  = 0
  D = D - 1
@function_clean_locals_label|Sys.init
 D; JGE
// VM push constant 4
// ASM['push value'](4)
@4
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM call Main.fibonacci 1
// Save current frame
// ASM['push value'](return_label|Sys.vm|Main.fibonacci|instance_label_6)
@return_label|Sys.vm|Main.fibonacci|instance_label_6
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// ASM['push ram'](LCL)
@LCL
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// ASM['push ram'](ARG)
@ARG
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// ASM['push ram'](THIS)
@THIS
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// ASM['push ram'](THAT)
@THAT
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// Set call function LCL
// (LCL = SP = A + 1)
// (A = SP - 1 after 'push ram')
  D = A + 1
@LCL
 M  = D
// Set call function ARG
// (ARG = SP - n_frame - n_arguments)
// (n_frame = 5)
@5
  D = D - A
@1
  D = D - A
@ARG
 M  = D
// Jump to function and set RETURN label
@function_define_label|Main.fibonacci
0; JMP
(return_label|Sys.vm|Main.fibonacci|instance_label_6)
// VM label END
(vm_label|END|END)
// VM goto END
@vm_label|END|END
0; JMP