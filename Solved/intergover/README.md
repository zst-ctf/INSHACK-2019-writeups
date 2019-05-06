# intergover
Pwn

## Challenge 

I hope you know how integers are stored.

`ssh -i <your_keyfile> -p 2223 user@intergover.ctf.insecurity-insa.fr`
To find your keyfile, look into your profile on this website.

[Binary](https://static.ctf.insecurity-insa.fr/b9ae1bb499daefff8aac28c936dc0cef1071d7ed.tar.gz)

[`https://www.youtube.com/watch?v=_BgblvF90UE`](https://www.youtube.com/watch?v=_BgblvF90UE)

## Solution

Decompile in hopper

	int main(int arg0, int arg1) {
	    printf("Give me one param: ");
	    fflush(0x0);
	    if (__isoc99_scanf(0x400869, &var_14) != 0x1) {
	            puts("I expect a number.");
	            fflush(0x0);
	    }
	    var_15 = 0x0;
	    for (var_10 = 0x0; var_10 < var_14; var_10 = var_10 + 0x1) {
	            var_15 = (var_15 & 0xff) + 0x1;
	    }
	    if (var_15 == 0xf2) {
	            gimmeFlagPliz();
	    }
	    ...
	}

Put 0xf2 or 242 into the server

	$ ssh -i ../priv_key -p 2223 user@intergover.ctf.insecurity-insa.fr
	Give me one param: 242
	INSA{B3_v3rY_c4r3fUL_w1tH_uR_1nt3g3r_bR0}

## Flag

	INSA{B3_v3rY_c4r3fUL_w1tH_uR_1nt3g3r_bR0}
