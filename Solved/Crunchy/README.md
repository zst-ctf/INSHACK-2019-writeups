# Crunchy
Programming

## Challenge 

Trade 500 billion years of CPU time and 50 exabytes of RAM for a shiny flag : [crunchy](https://static.ctf.insecurity-insa.fr/d099bd3ce0d20ce8aaff41451a6adcda4184fc4f.tar.gz)

## Solution


We have a crunchy formula where `C(n) = 6*C(n-1) + C(n-2)`

	crunchy(0) 0 0
	crunchy(1) 1 1
	crunchy(2) 6 6
	crunchy(3) 37 37
	crunchy(4) 228 228
	crunchy(5) 1405 1405
	crunchy(6) 8658 8658
	crunchy(7) 53353 53353
	crunchy(8) 328776 328776
	crunchy(9) 2026009 2026009
	crunchy(10) 12484830 12484830
	crunchy(11) 76934989 76934989
	crunchy(12) 474094764 74094736
	crunchy(13) 2921503573 21503370
	crunchy(14) 18003116202 3114942
	crunchy(15) 110940200785 40193022
	crunchy(16) 683644320912 44273060
	crunchy(17) 4212806126257 5831361

It works nicely under modulo

	>>> 76934989 + 474094764*6  ## C(11) + 6*C(12)
	2921503573  ## C(13)
	>>> (76934989 + 74094736*6)%100000007  ## ditto with modulo
	21503370
	
This is similar to the fibbonacci series.

If the modulo is small enough, we will easily get a repeating pattern as seen in the Pisano period

- https://en.wikipedia.org/wiki/Pisano_period#Definition

Trying it out, it did not work because the modulo we have (100000007) is huge. 

Another method is to use matrix multiplication.

- https://medium.com/competitive/huge-fibonacci-number-modulo-m-6b4926a5c836
- https://www.quora.com/Whats-a-fast-algorithm-to-find-the-remainder-of-the-division-of-a-huge-Fibonacci-number-by-some-big-integer/answer/Michal-Forišek

Modify the identity matrix A

	$ python3 solve.py 
	crunchy(0) 0
	crunchy(1) 1
	crunchy(2) 6
	crunchy(3) 37
	crunchy(4) 228
	crunchy(5) 1405
	crunchy(6) 8658
	crunchy(7) 53353
	crunchy(8) 328776
	crunchy(9) 2026009
	Your flag is: INSA{41322239}

## Flag

	INSA{41322239}
