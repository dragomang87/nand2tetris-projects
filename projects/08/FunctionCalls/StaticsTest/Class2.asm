
// VM function Class2.set 0
(function_label.08_FunctionCalls_StaticsTest_Class2.vm.Class2.set)
@0
 D  = A
@SP
  M = M + D
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
// VM pop  static (static.08_FunctionCalls_StaticsTest_Class2.vm) 0
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@static.08_FunctionCalls_StaticsTest_Class2.vm.0
  M = D
 D  = 0             // optional safety feature
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
// VM pop  static (static.08_FunctionCalls_StaticsTest_Class2.vm) 1
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@static.08_FunctionCalls_StaticsTest_Class2.vm.1
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
// VM return START
// Save the return value to argument[0],
// which is the top of the stack after return
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
// Clear the stack until LCL[0]
@LCL
 D  = M
// ASM['delete stack to D'] (until address D)
// (clear to zero until address D included)
// START optional safety feature
@SP                 // go to stack pointer
  M = M + 1         // add one entry to SP, one is always deleted
 D  = M - D         // turn D into a counter of entries to clear
(asm_delete_stack_label.08_FunctionCalls_StaticsTest_Class2.vm.instance_label_{ASM['instance_label_index']}.local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_StaticsTest_Class2.vm.instance_label_{ASM['instance_label_index']}.local      // point to clearing
D; JGT              // loop jump if counter >= 1
// END   optional safety feature
//@SP               // Alternative unsafe code
//  M = D + 1       // Alternative unsafe code
// Skip the saved frame and clear until and point to ARG[1]
@5
 D  = A
@SP
  M = M - D
@ARG
 D  = M + 1
// ASM['delete stack to D'] (until address D)
// (clear to zero until address D included)
// START optional safety feature
@SP                 // go to stack pointer
  M = M + 1         // add one entry to SP, one is always deleted
 D  = M - D         // turn D into a counter of entries to clear
(asm_delete_stack_label.08_FunctionCalls_StaticsTest_Class2.vm.instance_label_{ASM['instance_label_index']}.argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_StaticsTest_Class2.vm.instance_label_{ASM['instance_label_index']}.argument      // point to clearing
D; JGT              // loop jump if counter >= 1
// END   optional safety feature
//@SP               // Alternative unsafe code
//  M = D + 1       // Alternative unsafe code
// Return to saved frame and recover THAT
@LCL
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THAT
  M = D
// Return to saved frame and recover THIS
@LCL
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THIS
  M = D
// Return to saved frame and recover ARG
@LCL
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@ARG
  M = D
// Return to saved frame and recover LCL
// keep the sum of both LCL in D to return to frame
@LCL
ADM = M - 1
 D  = M + D
@LCL
  M = D - M
// Return to saved frame and delete callerLCL
A   = D - M
  M = 0             // optional safety feature
// Recover caller's return address and jump
A   = A - 1
 D  = M
  M = 0             // optional safety feature
A   = D
JMP
// VM return END
// VM function Class2.get 0
(function_label.08_FunctionCalls_StaticsTest_Class2.vm.Class2.get)
@0
 D  = A
@SP
  M = M + D
// VM push static (static.08_FunctionCalls_StaticsTest_Class2.vm) 0
// ASM['push ram']({static}.{i})
@{static}.{i}
 D  = M
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push static (static.08_FunctionCalls_StaticsTest_Class2.vm) 1
// ASM['push ram']({static}.{i})
@{static}.{i}
 D  = M
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
// VM return START
// Save the return value to argument[0],
// which is the top of the stack after return
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
// Clear the stack until LCL[0]
@LCL
 D  = M
// ASM['delete stack to D'] (until address D)
// (clear to zero until address D included)
// START optional safety feature
@SP                 // go to stack pointer
  M = M + 1         // add one entry to SP, one is always deleted
 D  = M - D         // turn D into a counter of entries to clear
(asm_delete_stack_label.08_FunctionCalls_StaticsTest_Class2.vm.instance_label_{ASM['instance_label_index']}.local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_StaticsTest_Class2.vm.instance_label_{ASM['instance_label_index']}.local      // point to clearing
D; JGT              // loop jump if counter >= 1
// END   optional safety feature
//@SP               // Alternative unsafe code
//  M = D + 1       // Alternative unsafe code
// Skip the saved frame and clear until and point to ARG[1]
@5
 D  = A
@SP
  M = M - D
@ARG
 D  = M + 1
// ASM['delete stack to D'] (until address D)
// (clear to zero until address D included)
// START optional safety feature
@SP                 // go to stack pointer
  M = M + 1         // add one entry to SP, one is always deleted
 D  = M - D         // turn D into a counter of entries to clear
(asm_delete_stack_label.08_FunctionCalls_StaticsTest_Class2.vm.instance_label_{ASM['instance_label_index']}.argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_StaticsTest_Class2.vm.instance_label_{ASM['instance_label_index']}.argument      // point to clearing
D; JGT              // loop jump if counter >= 1
// END   optional safety feature
//@SP               // Alternative unsafe code
//  M = D + 1       // Alternative unsafe code
// Return to saved frame and recover THAT
@LCL
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THAT
  M = D
// Return to saved frame and recover THIS
@LCL
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THIS
  M = D
// Return to saved frame and recover ARG
@LCL
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@ARG
  M = D
// Return to saved frame and recover LCL
// keep the sum of both LCL in D to return to frame
@LCL
ADM = M - 1
 D  = M + D
@LCL
  M = D - M
// Return to saved frame and delete callerLCL
A   = D - M
  M = 0             // optional safety feature
// Recover caller's return address and jump
A   = A - 1
 D  = M
  M = 0             // optional safety feature
A   = D
JMP
// VM return END