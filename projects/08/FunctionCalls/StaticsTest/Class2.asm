
// VM function Class2.set 0
// CANNOT assume LCL is zero!!!
(function_define_label|Class2.set)
@SP
 M  = M - 1
@0
  D = A
(function_clean_locals_label|Class2.set)
@SP
AM  = M + 1
 M  = 0
  D = D - 1
@function_clean_locals_label|Class2.set
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
// VM pop  static 0
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@Class2.0
 M  = D
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
// VM pop  static 1
// ASM['pop stack'] (to D)
@SP
AM  = M - 1
  D = M
 M  = 0             // optional safety feature
@Class2.1
 M  = D
  D = 0             // optional safety feature
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
(asm_delete_stack_label|Class2.vm|instance_label_3|local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Class2.vm|instance_label_3|local   // loop jump
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
(asm_delete_stack_label|Class2.vm|instance_label_3|argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Class2.vm|instance_label_3|argument   // loop jump
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
// VM function Class2.get 0
// CANNOT assume LCL is zero!!!
(function_define_label|Class2.get)
@SP
 M  = M - 1
@0
  D = A
(function_clean_locals_label|Class2.get)
@SP
AM  = M + 1
 M  = 0
  D = D - 1
@function_clean_locals_label|Class2.get
 D; JGE
// VM push static 0
// ASM['push ram'](Class2.0)
@Class2.0
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM push static 1
// ASM['push ram'](Class2.1)
@Class2.1
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
(asm_delete_stack_label|Class2.vm|instance_label_4|local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Class2.vm|instance_label_4|local   // loop jump
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
(asm_delete_stack_label|Class2.vm|instance_label_4|argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Class2.vm|instance_label_4|argument   // loop jump
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