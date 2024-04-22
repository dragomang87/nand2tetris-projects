
// VM function Main.fibonacci 0
(function_label.08_FunctionCalls_FibonacciElement_Main.vm.Main.fibonacci)
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
// VM push constant 2
// ASM['push value'](2)
@2
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM lt
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
 D  = M - D
  M = -1
@compare_label.08_FunctionCalls_FibonacciElement_Main.vm.lt.instance_label_{ASM['instance_label_index']}
D; JLT
@SP
A   = M - 1
  M = 0
(compare_label.08_FunctionCalls_FibonacciElement_Main.vm.lt.instance_label_{ASM['instance_label_index']})
// VM goto N_LT_2
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@vm_label.08_FunctionCalls_FibonacciElement_Main.vm.N_LT_2
D; JMP
// VM goto N_GE_2
@vm_label.08_FunctionCalls_FibonacciElement_Main.vm.N_GE_2
JMP
// VM label N_LT_2
(vm_label.08_FunctionCalls_FibonacciElement_Main.vm.N_LT_2)
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
(asm_delete_stack_label.08_FunctionCalls_FibonacciElement_Main.vm.instance_label_{ASM['instance_label_index']}.local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_FibonacciElement_Main.vm.instance_label_{ASM['instance_label_index']}.local      // point to clearing
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
(asm_delete_stack_label.08_FunctionCalls_FibonacciElement_Main.vm.instance_label_{ASM['instance_label_index']}.argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_FibonacciElement_Main.vm.instance_label_{ASM['instance_label_index']}.argument      // point to clearing
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
// VM label N_GE_2
(vm_label.08_FunctionCalls_FibonacciElement_Main.vm.N_GE_2)
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
// VM push constant 2
// ASM['push value'](2)
@2
 D  = A
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
// VM call Main.fibonacci 1
// ASM['push value'](return_label.08_FunctionCalls_FibonacciElement_Main.vm.Main.fibonacci.instance_label_{ASM['instance_label_index']})
@return_label.08_FunctionCalls_FibonacciElement_Main.vm.Main.fibonacci.instance_label_{ASM['instance_label_index']}
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
@function_label.08_FunctionCalls_FibonacciElement_Main.vm.Main.fibonacci
JMP
(return_label.08_FunctionCalls_FibonacciElement_Main.vm.Main.fibonacci.instance_label_{ASM['instance_label_index']})
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
// VM push constant 1
// ASM['push value'](1)
@1
 D  = A
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
// VM call Main.fibonacci 1
// ASM['push value'](return_label.08_FunctionCalls_FibonacciElement_Main.vm.Main.fibonacci.instance_label_{ASM['instance_label_index']})
@return_label.08_FunctionCalls_FibonacciElement_Main.vm.Main.fibonacci.instance_label_{ASM['instance_label_index']}
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
@function_label.08_FunctionCalls_FibonacciElement_Main.vm.Main.fibonacci
JMP
(return_label.08_FunctionCalls_FibonacciElement_Main.vm.Main.fibonacci.instance_label_{ASM['instance_label_index']})
// VM add
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
  M = M + D
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
(asm_delete_stack_label.08_FunctionCalls_FibonacciElement_Main.vm.instance_label_{ASM['instance_label_index']}.local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_FibonacciElement_Main.vm.instance_label_{ASM['instance_label_index']}.local      // point to clearing
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
(asm_delete_stack_label.08_FunctionCalls_FibonacciElement_Main.vm.instance_label_{ASM['instance_label_index']}.argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_FibonacciElement_Main.vm.instance_label_{ASM['instance_label_index']}.argument      // point to clearing
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