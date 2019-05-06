# signed or not signed
Pwn

## Challenge 

## Hint

## Solution

Decompile

	int main(int arg0, int arg1) {
	    printf("Please give me a number:");
	    fflush(0x0);
	    if (__isoc99_scanf("%d", &var_8, &var_8) != 0x1) {
	            puts("I expect a number.");
	            fflush(0x0);
	            rax = exit(0x1);
	    } else {
	            if (var_8 > 0xa) {
	                    puts("Bro, it's really too big.");
	            }else {
	                    vuln(var_8 & 0xffff);
	            }
	    }
	}

	int vuln(int arg0) {
	    if (arg0 == 0xfd66) {
	            rax = gimmeFlagPliz();
	    }
	    else {
	            puts("You are not going to have the flag.");
	            rax = fflush(0x0);
	    }
	    return rax;
	}

From the title, we are hinted that we need to put in a negative number.

And from the source code, the number & 0xffff == 0xfd66...

Pass in a negative number like 0xfffffd66 which is -666.

## Flag

	INSA{Th3_qU3sTi0n_1s_S1gN3d_0r_x90}
