
// VM push constant 3030
@3030
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM pop pointer 0
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
@THIS
M = D
D = 0 // optional safety feature
// VM push constant 3040
@3040
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM pop pointer 1
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
@THAT
M = D
D = 0 // optional safety feature
// VM push constant 32
@32
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM pop that 2
// ASM address(THAT,2)
@THAT
D = M
@2
D = D + A
@address
M = D
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
// ASM push address
@address
A = M
M = D
D = 0 // optional safety feature
@address // optional safety feature
M = 0 // optional safety feature
// VM push constant 46
@46
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM pop that 6
// ASM address(THAT,6)
@THAT
D = M
@6
D = D + A
@address
M = D
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
// ASM push address
@address
A = M
M = D
D = 0 // optional safety feature
@address // optional safety feature
M = 0 // optional safety feature
// VM push pointer 0
@THIS
D = M
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM push pointer 1
@THAT
D = M
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM add
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
A = A - 1
M = M + D
D = 0 // optional safety feature
// VM push that 2
// ASM A(THAT,2)
@THAT
D = M
@2
A = D + A
D = M
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM sub
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
A = A - 1
M = M - D
D = 0 // optional safety feature
// VM push that 6
// ASM A(THAT,6)
@THAT
D = M
@6
A = D + A
D = M
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0 // optional safety feature
// VM add
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0 // optional safety feature
A = A - 1
M = M + D
D = 0 // optional safety feature