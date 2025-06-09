// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen
// by writing 'black' in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen by writing
// 'white' in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Algorithm:
// (LOOP) reading KBD, if change jump to (BLACK) or (WHITE)
// implement black and whit
// at the end of either black and white jump to lopp
//
// Pseudo code
// R1 = (BLACK)
// R0 = (WHITE)
// R2 = key state (0 or not)
// R3 = current color
// for ever
//   state = (key == 0)
//   if (state != previous state)
//      R2 = state
//      @R2
//      A = M
//      0; JMP
//   else
//      @LOOP
//      0; JMP
//
//(BLACK) and (WHITE) *single* for loop on SCREEN registers
//  because all the registers are already in sequence
//  number of registers = 131072


// default no key press
@oldkey     // Register 16
M = 0
// default no key press
@newkey
M = 0       // Register 17
// default white color
@color      // Register 18
M = 0
// default null pixel pointer
@pixel      // Register 19
M = 0

// select implementation to use
(INPUT)
    @INPUTDUMB
    @INPUTDIFF
    0; JMP

// Dumb implementation: draw every time
(INPUTDUMB)
    @KBD
    D = M

    // Draw black or white depending on D
    @BLACK
    D; JNE
    @WHITE
    0; JMP


// Smart implementation: draw only if change
(INPUTDIFF)
    @KBD
    D = M
    @KEYpressed
    D; JNE
    @KEYreleased
    0; JMP

(KEYpressed)
    @newkey
    M = 1
    @KEYchanged
    0; JMP
(KEYreleased)
    @newkey
    M = 0
    @KEYchanged
    0; JMP

(KEYchanged)
    @oldkey
    D = M
    @newkey
    D = D - M
    @oldkey
    M = D
    @CHOOSE_COLOR
    D; JNE
    @INPUT
    0; JMP

(CHOOSE_COLOR)
    // save new key state first
    @newkey
    D = M
    @oldkey
    M = D
    // Draw black or white depending on D
    @BLACK
    D; JNE
    @WHITE
    0; JMP



(WHITE)
    @color
    M = 0
    @SCREEN
    D = A
    @pixel
    M = D
    @DRAW
    0; JMP

(BLACK)
    @color
    M = -1
    @SCREEN
    D = A
    @pixel
    M = D
    @DRAW
    0; JMP

(DRAW)
    // Load the pixel address RAM[pixel] in D
    @pixel
    D = M
    // if maximum reached back to waiting
    // SCREEN = 2^14 = 16384
    // screen size = (512/16)*256 = 2^13 = 8192
    // register after last pixel = 16384 + 8192 = 24576
    @24576
    D = D - A
    @INPUT
    D; JEQ
    // if not load the current color
    @color
    D = M
    // set the pixel color RAM[RAM[pixel]] to the color stored in D
    @pixel
    A = M
    M = D
    // go to next pixel: RAM[pixel]++
    @pixel
    M = M + 1
    // repeat
    @DRAW
    0; JMP

//(EXIT)
//    @EXIT
//    0; JMP
