
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
// VM push constant 6
// ASM['push value'](6)
@6
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM push constant 8
// ASM['push value'](8)
@8
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM call Class1.set 2
// Save current frame
// ASM['push value'](return_label|Sys.vm|Class1.set|instance_label_5)
@return_label|Sys.vm|Class1.set|instance_label_5
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
@2
  D = D - A
@ARG
 M  = D
// Jump to function and set RETURN label
@function_define_label|Class1.set
0; JMP
(return_label|Sys.vm|Class1.set|instance_label_5)
// VM pop temp 0
// D = temp + 0 = destination
@5   
  D = A
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
// VM push constant 23
// ASM['push value'](23)
@23
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM push constant 15
// ASM['push value'](15)
@15
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM call Class2.set 2
// Save current frame
// ASM['push value'](return_label|Sys.vm|Class2.set|instance_label_6)
@return_label|Sys.vm|Class2.set|instance_label_6
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
@2
  D = D - A
@ARG
 M  = D
// Jump to function and set RETURN label
@function_define_label|Class2.set
0; JMP
(return_label|Sys.vm|Class2.set|instance_label_6)
// VM pop temp 0
// D = temp + 0 = destination
@5   
  D = A
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
// VM call Class1.get 0
// Add one argument for the return value
@SP
 M  = M + 1
// Save current frame
// ASM['push value'](return_label|Sys.vm|Class1.get|instance_label_7)
@return_label|Sys.vm|Class1.get|instance_label_7
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
@function_define_label|Class1.get
0; JMP
(return_label|Sys.vm|Class1.get|instance_label_7)
// VM call Class2.get 0
// Add one argument for the return value
@SP
 M  = M + 1
// Save current frame
// ASM['push value'](return_label|Sys.vm|Class2.get|instance_label_8)
@return_label|Sys.vm|Class2.get|instance_label_8
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
@function_define_label|Class2.get
0; JMP
(return_label|Sys.vm|Class2.get|instance_label_8)
// VM label END
(vm_label|END|END)
// VM goto END
@vm_label|END|END
0; JMP