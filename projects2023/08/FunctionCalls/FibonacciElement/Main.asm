
// VM function Main.fibonacci 0
// CANNOT assume LCL is zero!!!
(function_define_label|Main.fibonacci)
@SP
 M  = M - 1
@0
  D = A
(function_clean_locals_label|Main.fibonacci)
@SP
AM  = M + 1
 M  = 0
  D = D - 1
@function_clean_locals_label|Main.fibonacci
 D; JGE
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
// VM push constant 2
// ASM['push value'](2)
@2
  D = A
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM lt (x lt y?)
// pop y and compute x-y (SP points to y)
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = A - 1
  D = M - D
// Comparison x = True = -1 = 0xFFFF
 M  = -1
@compare_label_lt|Main.vm|instance_label_1
D; JLT
// Comparison x = False = 0
// (SP points to y)
@SP
A   = M - 1
 M  = 0
(compare_label_lt|Main.vm|instance_label_1)
// VM if-goto N_LT_2
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@vm_label|N_LT_2|N_LT_2
D; JNE
// VM goto N_GE_2
@vm_label|N_GE_2|N_GE_2
0; JMP
// VM label N_LT_2
(vm_label|N_LT_2|N_LT_2)
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
(asm_delete_stack_label|Main.vm|instance_label_2|local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Main.vm|instance_label_2|local   // loop jump
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
(asm_delete_stack_label|Main.vm|instance_label_2|argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Main.vm|instance_label_2|argument   // loop jump
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
// VM label N_GE_2
(vm_label|N_GE_2|N_GE_2)
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
// VM push constant 2
// ASM['push value'](2)
@2
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
// VM call Main.fibonacci 1
// Save current frame
// ASM['push value'](return_label|Main.vm|Main.fibonacci|instance_label_3)
@return_label|Main.vm|Main.fibonacci|instance_label_3
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
(return_label|Main.vm|Main.fibonacci|instance_label_3)
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
// VM call Main.fibonacci 1
// Save current frame
// ASM['push value'](return_label|Main.vm|Main.fibonacci|instance_label_4)
@return_label|Main.vm|Main.fibonacci|instance_label_4
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
(return_label|Main.vm|Main.fibonacci|instance_label_4)
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
(asm_delete_stack_label|Main.vm|instance_label_5|local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Main.vm|instance_label_5|local   // loop jump
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
(asm_delete_stack_label|Main.vm|instance_label_5|argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Main.vm|instance_label_5|argument   // loop jump
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