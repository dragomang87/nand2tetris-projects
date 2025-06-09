// Multiplication algorithm

//
// R2 = R0 * R1
// R0 and R1 are not changed
//
// Pseudo code smart
//   go thorugh the bits of R1
//   R1 & 2^i with i = 0..15
//   compute the multiples by {2^i} by taking the sum with itself
//   sum this multiple if the corresponding bit of R1 is 1
//
// Pseudo code dumb
//   sum R0 to the result R1 times with a counter from R1 to zero

// set up a temporary variable to store the product
@product
M = 0

///////////////////////////////////////
// ZERO MULTIPLICATION
///////////////////////////////////////

@R0
D = M
@SAVE
D; JEQ
@R1
D = M
@SAVE
D; JEQ


///////////////////////////////////////
// NON-ZERO MULTIPLICATION
///////////////////////////////////////

// Choose Implementation
@OBVIOUS
@SMART
0; JMP

///////////////////////////////////////
// DUMB MULTIPLICATION
///////////////////////////////////////

// Sum R0 to itself R1 number of times

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

// Sum the power-of-2 multiples of R0
// when the non-zero bits of R1 are encountered
// Remove the multiples as they are used to stop early for small numbers

(SMART)
    // Set up the bit selector at the first bit
    @bit_selector
    M = 1
    // store the first multiple equal to R0
    @R0
    D = M
    @R0_multiple
    M = D
    // set up the counter at R1
    @R1
    D = M
    @R1_counter
    M = D

(SMART_LOOP)
    // check if the selected bit is equal to 1
    @bit_selector
    D = M
    @R1_counter
    D = M & D
    // If zero skip the sum
    @SKIP_SUM
    D; JEQ
        // If non zero, add the multiple to product
        @R0_multiple
        D = M
        @product
        M = M + D
        // Remove the selected bit from the counter
        @bit_selector
        D = M
        @R1_counter
        MD = M - D        
        // Done if this was the last bit of R1_counter
        // Thus save if R1_counter is now zero
        @SAVE
        D; JEQ
    (SKIP_SUM)
    // If we are here then R1_counter is still not zero
    // Double the multiple variable
    @R0_multiple
    D = M
    M = M + D
    // Doube the bit selector (shift up)
    @bit_selector
    D = M
    M = M + D
    // repeat
    @SMART_LOOP
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



