
// VM push constant 10
@10
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM pop that 0
// ASM address(THAT,0)
@THAT
D = M
@0
D = D + A
@address
M = D
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
// ASM push address
@address
A = M
M = D
D = 0
@address
M = 0
// VM push constant 21
@21
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 22
@22
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
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
M = 0
// ASM push address
@address
A = M
M = D
D = 0
@address
M = 0
// VM pop that 1
// ASM address(THAT,1)
@THAT
D = M
@1
D = D + A
@address
M = D
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
// ASM push address
@address
A = M
M = D
D = 0
@address
M = 0
// VM push constant 36
@36
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
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
M = 0
// ASM push address
@address
A = M
M = D
D = 0
@address
M = 0
// VM push constant 42
@42
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push constant 45
@45
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM pop that 5
// ASM address(THAT,5)
@THAT
D = M
@5
D = D + A
@address
M = D
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
// ASM push address
@address
A = M
M = D
D = 0
@address
M = 0
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
M = 0
// ASM push address
@address
A = M
M = D
D = 0
@address
M = 0
// VM push constant 510
@510
D = A
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM pop temp 6
@5
D = A
@6
D = D + A
@address
M = D
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
// ASM push address
@address
A = M
M = D
D = 0
@address
M = 0
// VM push that 0
// ASM A(THAT,0)
@THAT
D = M
@0
A = D + A
D = M
// ASM push stack
@SP
A = M
M = D
@SP
M = M + 1
D = 0
// VM push that 5
// ASM A(THAT,5)
@THAT
D = M
@5
A = D + A
D = M
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
// VM push that 1
// ASM A(THAT,1)
@THAT
D = M
@1
A = D + A
D = M
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
D = 0
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
// VM sub
// ASM pop stack
@SP
AM = M - 1
D = M
M = 0
A = A - 1
M = M - D
D = 0 
// VM push temp 6
@5
D = A
@6
A = D + A
D = M
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