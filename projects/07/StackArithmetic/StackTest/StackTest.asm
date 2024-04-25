
// VM push constant 17
// ASM['push value'](17)
@17
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 17
// ASM['push value'](17)
@17
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM eq
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
 D  = M - D
  M = -1
@compare_label.07_StackArithmetic_StackTest_StackTest.vm.eq.instance_label_1
D; JEQ
@SP
A   = M - 1
  M = 0
(compare_label.07_StackArithmetic_StackTest_StackTest.vm.eq.instance_label_1)
// VM push constant 17
// ASM['push value'](17)
@17
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 16
// ASM['push value'](16)
@16
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM eq
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
 D  = M - D
  M = -1
@compare_label.07_StackArithmetic_StackTest_StackTest.vm.eq.instance_label_2
D; JEQ
@SP
A   = M - 1
  M = 0
(compare_label.07_StackArithmetic_StackTest_StackTest.vm.eq.instance_label_2)
// VM push constant 16
// ASM['push value'](16)
@16
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 17
// ASM['push value'](17)
@17
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM eq
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
 D  = M - D
  M = -1
@compare_label.07_StackArithmetic_StackTest_StackTest.vm.eq.instance_label_3
D; JEQ
@SP
A   = M - 1
  M = 0
(compare_label.07_StackArithmetic_StackTest_StackTest.vm.eq.instance_label_3)
// VM push constant 892
// ASM['push value'](892)
@892
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 891
// ASM['push value'](891)
@891
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
@compare_label.07_StackArithmetic_StackTest_StackTest.vm.lt.instance_label_4
D; JLT
@SP
A   = M - 1
  M = 0
(compare_label.07_StackArithmetic_StackTest_StackTest.vm.lt.instance_label_4)
// VM push constant 891
// ASM['push value'](891)
@891
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 892
// ASM['push value'](892)
@892
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
@compare_label.07_StackArithmetic_StackTest_StackTest.vm.lt.instance_label_5
D; JLT
@SP
A   = M - 1
  M = 0
(compare_label.07_StackArithmetic_StackTest_StackTest.vm.lt.instance_label_5)
// VM push constant 891
// ASM['push value'](891)
@891
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 891
// ASM['push value'](891)
@891
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
@compare_label.07_StackArithmetic_StackTest_StackTest.vm.lt.instance_label_6
D; JLT
@SP
A   = M - 1
  M = 0
(compare_label.07_StackArithmetic_StackTest_StackTest.vm.lt.instance_label_6)
// VM push constant 32767
// ASM['push value'](32767)
@32767
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 32766
// ASM['push value'](32766)
@32766
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM gt
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
 D  = M - D
  M = -1
@compare_label.07_StackArithmetic_StackTest_StackTest.vm.gt.instance_label_7
D; JGT
@SP
A   = M - 1
  M = 0
(compare_label.07_StackArithmetic_StackTest_StackTest.vm.gt.instance_label_7)
// VM push constant 32766
// ASM['push value'](32766)
@32766
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 32767
// ASM['push value'](32767)
@32767
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM gt
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
 D  = M - D
  M = -1
@compare_label.07_StackArithmetic_StackTest_StackTest.vm.gt.instance_label_8
D; JGT
@SP
A   = M - 1
  M = 0
(compare_label.07_StackArithmetic_StackTest_StackTest.vm.gt.instance_label_8)
// VM push constant 32766
// ASM['push value'](32766)
@32766
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 32766
// ASM['push value'](32766)
@32766
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM gt
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
 D  = M - D
  M = -1
@compare_label.07_StackArithmetic_StackTest_StackTest.vm.gt.instance_label_9
D; JGT
@SP
A   = M - 1
  M = 0
(compare_label.07_StackArithmetic_StackTest_StackTest.vm.gt.instance_label_9)
// VM push constant 57
// ASM['push value'](57)
@57
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 31
// ASM['push value'](31)
@31
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM push constant 53
// ASM['push value'](53)
@53
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
// VM push constant 112
// ASM['push value'](112)
@112
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
// VM neg
@SP
A   = M - 1
  M = -M
// VM and
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
  M = M & D
 D  = 0             // optional safety feature
// VM push constant 82
// ASM['push value'](82)
@82
 D  = A
// ASM['push stack'] (from D)
@SP
A M = M + 1
A   = A - 1
  M = D
 D  = 0             // optional safety feature
// VM or
// ASM['pop stack'] (to D)
@SP
A M = M - 1
 D  = M
  M = 0             // optional safety feature
A   = A - 1
  M = M | D
 D  = 0             // optional safety feature
// VM not
@SP
A   = M - 1
  M = !M