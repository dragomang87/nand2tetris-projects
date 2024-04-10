
// VM push constant 17
@17
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 17
@17
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM ge
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
D = M - D
M = 1
@ CMP.1
D; JGE
@SP
A = M - 1
M = 0
(CMP.1)
@SP
// VM push constant 17
@17
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 16
@16
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM ge
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
D = M - D
M = 1
@ CMP.2
D; JGE
@SP
A = M - 1
M = 0
(CMP.2)
@SP
// VM push constant 16
@16
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 17
@17
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM ge
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
D = M - D
M = 1
@ CMP.3
D; JGE
@SP
A = M - 1
M = 0
(CMP.3)
@SP
// VM push constant 892
@892
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 891
@891
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM ge
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
D = M - D
M = 1
@ CMP.4
D; JGE
@SP
A = M - 1
M = 0
(CMP.4)
@SP
// VM push constant 891
@891
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 892
@892
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM ge
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
D = M - D
M = 1
@ CMP.5
D; JGE
@SP
A = M - 1
M = 0
(CMP.5)
@SP
// VM push constant 891
@891
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 891
@891
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM ge
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
D = M - D
M = 1
@ CMP.6
D; JGE
@SP
A = M - 1
M = 0
(CMP.6)
@SP
// VM push constant 32767
@32767
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 32766
@32766
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM ge
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
D = M - D
M = 1
@ CMP.7
D; JGE
@SP
A = M - 1
M = 0
(CMP.7)
@SP
// VM push constant 32766
@32766
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 32767
@32767
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM ge
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
D = M - D
M = 1
@ CMP.8
D; JGE
@SP
A = M - 1
M = 0
(CMP.8)
@SP
// VM push constant 32766
@32766
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 32766
@32766
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM ge
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
D = M - D
M = 1
@ CMP.9
D; JGE
@SP
A = M - 1
M = 0
(CMP.9)
@SP
// VM push constant 57
@57
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 31
@31
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 53
@53
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM add
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
M = M + D
D = 0
// VM push constant 112
@112
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM sub
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
M = M - D
D = 0
// VM neg
@SP
A = M - 1
M = -M
// VM and
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
M = M & D
D = 0
// VM push constant 82
@82
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM or
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
M = M | D
D = 0
// VM not
@SP
A = M - 1
M = !M