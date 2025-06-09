
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
// VM push constant 4000
// ASM['push value'](4000)
@4000
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM pop pointer 0
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THIS
 M  = D
  D = 0             // optional safety feature
// VM push constant 5000
// ASM['push value'](5000)
@5000
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM pop pointer 1
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THAT
 M  = D
  D = 0             // optional safety feature
// VM call Sys.main 0
// Add one argument for the return value
@SP
 M  = M + 1
// Save current frame
// ASM['push value'](return_label|Sys.vm|Sys.main|instance_label_1)
@return_label|Sys.vm|Sys.main|instance_label_1
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
@function_define_label|Sys.main
0; JMP
(return_label|Sys.vm|Sys.main|instance_label_1)
// VM pop temp 1
// D = temp + 1 = destination
@5   
  D = A
@1
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
// VM goto LOOP
@vm_label|LOOP|LOOP
0; JMP
// VM function Sys.main 5
// CANNOT assume LCL is zero!!!
(function_define_label|Sys.main)
@SP
 M  = M - 1
@5
  D = A
(function_clean_locals_label|Sys.main)
@SP
AM  = M + 1
 M  = 0
  D = D - 1
@function_clean_locals_label|Sys.main
 D; JGE
// VM push constant 4001
// ASM['push value'](4001)
@4001
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM pop pointer 0
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THIS
 M  = D
  D = 0             // optional safety feature
// VM push constant 5001
// ASM['push value'](5001)
@5001
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM pop pointer 1
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THAT
 M  = D
  D = 0             // optional safety feature
// VM push constant 200
// ASM['push value'](200)
@200
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM pop local 1
// D = local + 1 = destination
@LCL 
  D = M
@1
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
// VM push constant 40
// ASM['push value'](40)
@40
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM pop local 2
// D = local + 2 = destination
@LCL 
  D = M
@2
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
// VM pop local 3
// D = local + 3 = destination
@LCL 
  D = M
@3
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
// VM push constant 123
// ASM['push value'](123)
@123
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM call Sys.add12 1
// Save current frame
// ASM['push value'](return_label|Sys.vm|Sys.add12|instance_label_2)
@return_label|Sys.vm|Sys.add12|instance_label_2
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
@function_define_label|Sys.add12
0; JMP
(return_label|Sys.vm|Sys.add12|instance_label_2)
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
// VM push local 1
// A = local + 1 = source
@LCL 
  D = M
@1
A   = D + A
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM push local 2
// A = local + 2 = source
@LCL 
  D = M
@2
A   = D + A
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM push local 3
// A = local + 3 = source
@LCL 
  D = M
@3
A   = D + A
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM push local 4
// A = local + 4 = source
@LCL 
  D = M
@4
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
// VM add
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = A - 1
 M  = M + D
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
// VM add
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = A - 1
 M  = M + D
  D = 0             // optional safety feature
// VM return START
// Result to ARG[0]
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@ARG
A   = M
  M = D
// Delete the stack until LCL[0]
@LCL
  D = M
// ASM['delete stack - if repeat'] (until address D)
// (zero above the stack and until address D included)
// START optional safety feature
@SP                 // go to stack pointer
 M  = M + 1         // SP++, SP is always deleted
  D = M - D         // D = how many
(asm_delete_stack_label|Sys.vm|instance_label_3|local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Sys.vm|instance_label_3|local   // loop jump
D; JGT              // loop jump if counter >= 1
// END   optional safety feature
//@SP               // Alternative discard code
//  M = D           // Alternative discard code
// Recover THAT
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THAT
 M  = D
// Recover THIS
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THIS
 M  = D
// Recover LCL
@SP
 M  = M - 1
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@LCL
 M  = D
// Put RETURN in ARG[1]
@SP
A   = M - 1
  D = M
 M  = 0             // optional safety feature
@ARG
AM  = M + 1
 M  = D
// Recover ARG
@SP
A   = M + 1
  D = M
 M  = 0             // optional safety feature
@ARG
  D = D + M
 M  = D - M
// Point to old ARG
A   = D - M
// Delete the stack until ARG[2]
  D = A + 1
// ASM['delete stack - if repeat'] (until address D)
// (zero above the stack and until address D included)
// START optional safety feature
@SP                 // go to stack pointer
 M  = M + 1         // SP++, SP is always deleted
  D = M - D         // D = how many
(asm_delete_stack_label|Sys.vm|instance_label_3|argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Sys.vm|instance_label_3|argument   // loop jump
D; JGT              // loop jump if counter >= 1
// END   optional safety feature
//@SP               // Alternative discard code
//  M = D           // Alternative discard code
// Recover RETURN and jump
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = D
0; JMP
// VM return END
// VM function Sys.add12 0
// CANNOT assume LCL is zero!!!
(function_define_label|Sys.add12)
@SP
 M  = M - 1
@0
  D = A
(function_clean_locals_label|Sys.add12)
@SP
AM  = M + 1
 M  = 0
  D = D - 1
@function_clean_locals_label|Sys.add12
 D; JGE
// VM push constant 4002
// ASM['push value'](4002)
@4002
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM pop pointer 0
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THIS
 M  = D
  D = 0             // optional safety feature
// VM push constant 5002
// ASM['push value'](5002)
@5002
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM pop pointer 1
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THAT
 M  = D
  D = 0             // optional safety feature
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
// VM push constant 12
// ASM['push value'](12)
@12
  D = A
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
// VM return START
// Result to ARG[0]
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@ARG
A   = M
  M = D
// Delete the stack until LCL[0]
@LCL
  D = M
// ASM['delete stack - if repeat'] (until address D)
// (zero above the stack and until address D included)
// START optional safety feature
@SP                 // go to stack pointer
 M  = M + 1         // SP++, SP is always deleted
  D = M - D         // D = how many
(asm_delete_stack_label|Sys.vm|instance_label_4|local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Sys.vm|instance_label_4|local   // loop jump
D; JGT              // loop jump if counter >= 1
// END   optional safety feature
//@SP               // Alternative discard code
//  M = D           // Alternative discard code
// Recover THAT
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THAT
 M  = D
// Recover THIS
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@THIS
 M  = D
// Recover LCL
@SP
 M  = M - 1
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@LCL
 M  = D
// Put RETURN in ARG[1]
@SP
A   = M - 1
  D = M
 M  = 0             // optional safety feature
@ARG
AM  = M + 1
 M  = D
// Recover ARG
@SP
A   = M + 1
  D = M
 M  = 0             // optional safety feature
@ARG
  D = D + M
 M  = D - M
// Point to old ARG
A   = D - M
// Delete the stack until ARG[2]
  D = A + 1
// ASM['delete stack - if repeat'] (until address D)
// (zero above the stack and until address D included)
// START optional safety feature
@SP                 // go to stack pointer
 M  = M + 1         // SP++, SP is always deleted
  D = M - D         // D = how many
(asm_delete_stack_label|Sys.vm|instance_label_4|argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Sys.vm|instance_label_4|argument   // loop jump
D; JGT              // loop jump if counter >= 1
// END   optional safety feature
//@SP               // Alternative discard code
//  M = D           // Alternative discard code
// Recover RETURN and jump
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = D
0; JMP
// VM return END