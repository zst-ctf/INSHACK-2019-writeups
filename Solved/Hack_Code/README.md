# Hack Code
Programming

## Challenge 

We have a little budgeting issue with our latest red team campaign. Please help us figure it out :

https://hack-code.ctf.insecurity-insa.fr

This challenge has 4 different flags, better solutions will grant you more flags.

### Problem
	
This file contains 10 000 network routes. We want to have at least one network tap on each route. Find a list of routers to intercept, and keep the number of taps low ! You will get the first flag for any solution with at most 150 taps.

### Example

If we have the following routes :

	c,b,a
	d,a,g
	b,c,e
	f,d,g
	            
One solution could be :

	g
	b

## Solution

My initial solution managed to get 128 taps.

1. Scan through all routes and find the ID which intersects the most number of routes.
2. Choose that ID and then delete all routes containing that ID.
3. We are now left with remaining routes.
4. Repeat Step 1 and 2 for the remaining routes. Do so until all routes are done.

This gave me 3 flags.

	The first flag is INSA{N0t_bad_f0r_a_start}. The next flag will be awarded at <= 135.
	INSA{135_is_pretty_g0Od_but_how_l0w_c4n_u_gO}. Get your next flag at <= 128
	INSA{Getting_cl0ser}. The last flag is waiting for you at 126 !


This is a minimul Hitting set problem

- http://theory.stanford.edu/~virgi/cs267/lecture5.pdf
- https://cs.nyu.edu/shasha/papers/glife/algorithm.html

## Flag

Solved 3 of 4 parts

	INSA{N0t_bad_f0r_a_start}
	INSA{135_is_pretty_g0Od_but_how_l0w_c4n_u_gO}
	INSA{Getting_cl0ser}
