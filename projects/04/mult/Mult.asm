// Multiplication algorithm

//
// R2 = R0 * R1
// R0 and R1 are not changed
//
// Pseudo code smart
//   go thorugh the bits of R1
//   R1 & 2^i with i = 0..15
//   compute the powers to the ^{2^i} by taking the product with itself
//   sum this power if the corresponding bit of R1 is 1
//
// Pseudo code dumb
//   sum R0 to the result R1 times with a counter from R1 to zero


// Choose Implementation
@OBVIOUS
@SMART
0; JMP




///////////////////////////////////////
// DUMB MULTIPLICATION
///////////////////////////////////////


(OBVIOUS)
    // Make a copy of R1 that will count how many times we summed R0
    @R1
    D = M
    @counter
    M = D
    // Set the variable to store the product
    @product
    M = 0

(OBVIOUS_LOOP)
    // sum R0 to the current product
    @R0
    D = M
    @product
    M = M + D
    // decrease the numer of sums to do
    @counter
    M = M - 1
    // if non zero repeat, otherwise exit
    D = M
    @OBVIOUS_LOOP
    D; JNE
    @SAVE
    0; JMP



///////////////////////////////////////
// SMART MULTIPLICATION
///////////////////////////////////////

(SMART)
    // set up a temporary variable to store the product
    @product
    M = 0
    // set up the counter at 1 and the bitstring with first bit 1
    @i_counter
    M = 1
    @i_bit
    M = 1
    // store the first power equal to R0
    @R0
    D = M
    @power
    M = D

(SMART_LOOP)
    // check if the selected i-th bit is equal to 1
    @i_bit
    D = M
    @R1
    D = M & D
    // If zero skip the sum
    @SKIP_SUM
    D; JEQ
        // If non zero, add the power to product
        @power
        D = M
        @product
        M = M + D
    (SKIP_SUM)
    // double the power variable
    @power
    D = M
    M = M + D
    // shift the bit up
    @i_bit
    D = M
    M = M + D
    // increase the counter
    @i_counter
    M = M + 1
    // if counter is not 16 then repeat
    D = M
    @16
    D = D - A
    // repeat if not 16th bit
    @SMART_LOOP
    D; JNE
    @SAVE
    0; JMP



///////////////////////////////////////
// Finish operations
///////////////////////////////////////

(SAVE)
    @product
    D = M
    @R2
    M = D

(EXIT)
    @EXIT
    0; JMP



