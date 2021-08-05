## Usage ##

This repo contains several scripts for creating random sets with binary colorings with discrepancy bounded by 2n + 1, where n is the number of objects. You can run

    python3 beckfiala.py
    
to generate a the set/coloring pair. The script will output the given discrepancy. 

In the standard beck fiala algorithm we always pick the direction that corresponds rounding "positively".
There is also a randomized version that rounds negatively such that if we consider the current discrepancy as a random variable, the expected value of stays the same
This version can be run with

    python3 beckfiala.py random
    
## References ##

Matousek, Jiri (Ed.), Geometric Discrepancy Theory, Springer 1999
