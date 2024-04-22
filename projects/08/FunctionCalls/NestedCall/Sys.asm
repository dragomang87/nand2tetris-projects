
// VM function Sys.init 0
(function_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.init)
@0
 D  = A
@SP
  M = M + D
// VM push constant 4000
// ASM['push value'](4000)
@4000
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop pointer 0
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THIS
  M = D
 D  = 0             // optional safety feature
// VM push constant 5000
// ASM['push value'](5000)
@5000
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop pointer 1
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THAT
  M = D
 D  = 0             // optional safety feature
// VM call Sys.main 0
@SP
  M = M + 1
// ASM['push value'](return_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.main.instance_label_{ASM['instance_label_index']})
@return_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.main.instance_label_{ASM['instance_label_index']}
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
@function_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.main
JMP
(return_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.main.instance_label_{ASM['instance_label_index']})
// VM pop temp 1
// D = temp + 1 = destination
@5   
 D  = A
@1
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
// VM label LOOP
(vm_label.08_FunctionCalls_NestedCall_Sys.vm.LOOP)
// VM goto LOOP
@vm_label.08_FunctionCalls_NestedCall_Sys.vm.LOOP
JMP
// VM function Sys.main 5
(function_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.main)
@5
 D  = A
@SP
  M = M + D
// VM push constant 4001
// ASM['push value'](4001)
@4001
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop pointer 0
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THIS
  M = D
 D  = 0             // optional safety feature
// VM push constant 5001
// ASM['push value'](5001)
@5001
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop pointer 1
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THAT
  M = D
 D  = 0             // optional safety feature
// VM push constant 200
// ASM['push value'](200)
@200
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop local 1
// D = local + 1 = destination
@LCL 
 D  = M
@1
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
// VM push constant 40
// ASM['push value'](40)
@40
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop local 2
// D = local + 2 = destination
@LCL 
 D  = M
@2
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
// VM pop local 3
// D = local + 3 = destination
@LCL 
 D  = M
@3
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
// VM push constant 123
// ASM['push value'](123)
@123
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM call Sys.add12 1
// ASM['push value'](return_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.add12.instance_label_{ASM['instance_label_index']})
@return_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.add12.instance_label_{ASM['instance_label_index']}
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
@function_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.add12
JMP
(return_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.add12.instance_label_{ASM['instance_label_index']})
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
// VM push local 0
// A = local + 0 = source
@LCL 
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
// VM push local 1
// A = local + 1 = source
@LCL 
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
// VM push local 2
// A = local + 2 = source
@LCL 
 D  = M
@2
A   = D + A
 D  = M
 M  = 0         // optional safety feature
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push local 3
// A = local + 3 = source
@LCL 
 D  = M
@3
A   = D + A
 D  = M
 M  = 0         // optional safety feature
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push local 4
// A = local + 4 = source
@LCL 
 D  = M
@4
A   = D + A
 D  = M
 M  = 0         // optional safety feature
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM add
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
  M = M + D
 D  = 0             // optional safety feature
// VM add
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
  M = M + D
 D  = 0             // optional safety feature
// VM add
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
  M = M + D
 D  = 0             // optional safety feature
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
(asm_delete_stack_label.08_FunctionCalls_NestedCall_Sys.vm.instance_label_{ASM['instance_label_index']}.local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_NestedCall_Sys.vm.instance_label_{ASM['instance_label_index']}.local      // point to clearing
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
(asm_delete_stack_label.08_FunctionCalls_NestedCall_Sys.vm.instance_label_{ASM['instance_label_index']}.argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_NestedCall_Sys.vm.instance_label_{ASM['instance_label_index']}.argument      // point to clearing
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
// VM function Sys.add12 0
(function_label.08_FunctionCalls_NestedCall_Sys.vm.Sys.add12)
@0
 D  = A
@SP
  M = M + D
// VM push constant 4002
// ASM['push value'](4002)
@4002
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop pointer 0
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THIS
  M = D
 D  = 0             // optional safety feature
// VM push constant 5002
// ASM['push value'](5002)
@5002
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM pop pointer 1
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
@THAT
  M = D
 D  = 0             // optional safety feature
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
// VM push constant 12
// ASM['push value'](12)
@12
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
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
(asm_delete_stack_label.08_FunctionCalls_NestedCall_Sys.vm.instance_label_{ASM['instance_label_index']}.local)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_NestedCall_Sys.vm.instance_label_{ASM['instance_label_index']}.local      // point to clearing
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
(asm_delete_stack_label.08_FunctionCalls_NestedCall_Sys.vm.instance_label_{ASM['instance_label_index']}.argument)  // loop start
// ASM['delete stack']
@SP                 // optional safety feature
A M = M - 1         // optional safety feature
  M = 0             // optional safety feature
 D  = D - 1         // decrement counter
@asm_delete_stack_label.08_FunctionCalls_NestedCall_Sys.vm.instance_label_{ASM['instance_label_index']}.argument      // point to clearing
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