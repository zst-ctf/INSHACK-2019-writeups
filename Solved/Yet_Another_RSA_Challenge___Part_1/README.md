# Yet Another RSA Challenge - Part 1
Crypto

## Challenge 

Buy an encrypted flag, get a (almost intact) prime factor for free !

You can find a harder version of this challenge in the Programming category.

## Solution

We are given the following:

	print N
	print '0x'+p.replace('9F','FC')
	print pow(flag,65537,N)

We have N, e, c, and also p with a replacement.

We can do a permutation replacement of 'FC' to '9F' and then check if we get a proper prime of q.

Doing so, we can decrypt and get the flag.

## Flag

	INSA{I_w1ll_us3_OTp_n3xT_T1M3}
