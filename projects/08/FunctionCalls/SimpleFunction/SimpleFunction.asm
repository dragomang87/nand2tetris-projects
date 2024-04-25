
// VM function SimpleFunction.test 2
// CANNOT assume LCL is zero!!!
(function_define_label|SimpleFunction.test)
@SP
 M  = M - 1
@2
  D = A
(function_clean_locals_label|SimpleFunction.test)
@SP
AM  = M + 1
 M  = 0
  D = D - 1
@function_clean_locals_label|SimpleFunction.test
 D; JGE
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
// VM add
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = A - 1
 M  = M + D
  D = 0             // optional safety feature
// VM not
@SP
A   = M - 1
 M  = !M
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
// VM add
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = A - 1
 M  = M + D
  D = 0             // optional safety feature
// VM push argument 1
// A = argument + 1 = source
@ARG 
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
// VM sub
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
A   = A - 1
 M  = M - D
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
(asm_delete_stack_label|SimpleFunction.vm|instance_label_1|local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|SimpleFunction.vm|instance_label_1|local   // loop jump
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
(asm_delete_stack_label|SimpleFunction.vm|instance_label_1|argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|SimpleFunction.vm|instance_label_1|argument   // loop jump
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