# To implement on the stack

# STACK
# StackPointer = SP = RAM[0]
# Stack Base address = 256
# SP always points to the next where to push
# (the next "free" address)


# ARITHMETICS (Module II.1)
# pop y, pop x (y is on top of the stack)
# add: x + y
# sub: x - y
# neg: -y
# eq : x == 0 (I think here it's y)
# gt : x > y
# lt : x < y
# and: x and y
# or : x or y
# not: not y

# MEMORY SEGMENTS (Module II.1)
#
# Operations:
# pop  segment i: pop from the stack into segment[i]
# push segment i: push the value of segment[i] into the stack
# Exception: "pop  const i" not allowed
#
# Segments:
#   essentially predefined arrays
#   with predefined locations
#   for the pointer to the base address
#   location of the base address decided at compilation
# local   :
#   poiter LCL = 1
#   base address RAM[LCL]
#   local[i] = RAM[LCL + i]
# argument:
#   poiter ARG = 2
#   base address RAM[ARG]
#   arguments[i] = RAM[ARG + i]
# this    :
#   poiter THIS = 3
#   base address RAM[THIS]
#   this[i] = RAM[THIS + i]
# that    :
#   poiter THAT = 4
#   base address RAM[THAT]
#   that[i] = RAM[THAT + i]
# constant:
#       const[i] = i (no need to actually store it)
# static  :
#   will be shared by all instances of the same objects
#   it is compiled differently
#   static[i] becomes an assembly variable, eg, static.i
#   automatically stored by the compiler in RAM[16] and onwards
#   might need to take care to never exceed RAM[255] for static
# temp    :
#   dedicated RAM locations 5 to 12
#   i = 0..7
#   temp[i] = RAM[5+i]
#   fixed size to 8 values
# pointer :
#   another fixed memory segment of size 2
#   pointer[0] = RAM[THIS]
#   pointer[1] = RAM[THAT]

# Other mentioned ommands
# D = *p with p a RAM address => D = RAM[p]
# *p = value => RAM[p] = value
# x++
# x--


{
'and':
'or' :
