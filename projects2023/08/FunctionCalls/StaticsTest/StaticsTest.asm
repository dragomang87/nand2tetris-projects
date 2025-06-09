
// Bootloader
// Sys.init ARG = bootloader SP = 256
// Sys.init has 0 arguments and ARG WILL BE EMPTY!! not like other functions
// Sys.init return: at 256
@return_label.bootloader.shutdown
  D = A
@256
 M  = D
// Bootloader frame: LCL, ARG, THIS, THAT
//  - CANNOT assume that they are zero
@LCL
  D = M
@257
 M  = D
@ARG
  D = M
@258
 M  = D
@THIS
  D = M
@259
 M  = D
@THAT
  D = M
@260
 M  = D
// Sys.init frame:
//  - LCL = SP = 261
//  - ARG = 256
@261
  D = A
@SP
 M  = D
@LCL
 M  = D
@256
  D = A
@ARG
 M  = D
// Call Sys.init
@function_define_label|Sys.init
0; JMP
// Sys.init return label
(return_label.bootloader.shutdown)
// Bootloader loop forever
0; JMP
// VM function Class1.set 0
// CANNOT assume LCL is zero!!!
(function_define_label|Class1.set)
@SP
 M  = M - 1
@0
  D = A
(function_clean_locals_label|Class1.set)
@SP
AM  = M + 1
 M  = 0
  D = D - 1
@function_clean_locals_label|Class1.set
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
@Class1.0
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
@Class1.1
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
(asm_delete_stack_label|Class1.vm|instance_label_1|local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Class1.vm|instance_label_1|local   // loop jump
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
(asm_delete_stack_label|Class1.vm|instance_label_1|argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Class1.vm|instance_label_1|argument   // loop jump
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
// VM function Class1.get 0
// CANNOT assume LCL is zero!!!
(function_define_label|Class1.get)
@SP
 M  = M - 1
@0
  D = A
(function_clean_locals_label|Class1.get)
@SP
AM  = M + 1
 M  = 0
  D = D - 1
@function_clean_locals_label|Class1.get
 D; JGE
// VM push static 0
// ASM['push ram'](Class1.0)
@Class1.0
  D = M
// ASM['push stack'] (from D)
@SP
AM  = M + 1
A   = A - 1
 M  = D
  D = 0             // optional safety feature
// VM push static 1
// ASM['push ram'](Class1.1)
@Class1.1
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
(asm_delete_stack_label|Class1.vm|instance_label_2|local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Class1.vm|instance_label_2|local   // loop jump
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
(asm_delete_stack_label|Class1.vm|instance_label_2|argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
AM  = M - 1         // optional safety feature
 M  = 0             // optional safety feature
  D = D - 1         // decrement counter
@asm_delete_stack_label|Class1.vm|instance_label_2|argument   // loop jump
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