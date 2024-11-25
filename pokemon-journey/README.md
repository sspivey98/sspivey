# Overall Idea
This an example problem of a heap overflow where you have poke around the heap
instead of the stack because the variables are allocated using `malloc()`.
The goal is to understand better how the heap allocates and how to overflow. 

Also, I would rather start my pokemon journey with mewtwo...

# Solution Approach

(See the `solution.py` file attached)

1. Run the program in `gdb` and break right before pikachu

2. Look at the address allocations using `info proc map`

3. `telescope` at the start address of the heap 
(add `-l 200` to find the fp)

4. See where your input is overwritting and count the difference between 
the overflow and the fp

5. Replace fp with `&mewtwo`

# Building

This should be ready for cmgr. Extract the `sspivey.tar.gz` to `cmgr/challanges/`
and it should be all ready to deploy.

If you choose to deploy with docker, you'll need to include ARG when building.