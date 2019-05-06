# xHell
Reverse

## Challenge 

[This](https://static.ctf.insecurity-insa.fr/e2ccb4917c2c8305d2fda31133b3d37af880e7fb.tar.gz) is what happens when you let a manager create challenges for INS'hAck.

If you don't have Microsoft Excel, this challenge also works in Google Sheets.

IMPORTANT: there are two valid inputs, only one of them is the flag. The input that will give you the flag is the one with the highest sum of the two.

## Solution

From the Excel sheet, we see a cell G2 with a formula which will output the flag. 

	=IF(AND(E82=1,B1>1,B1<=256,C1>1,C1<=256,D1>1,D1<=256,E1>1,E1<=256,B1-C1=46,E1-D1=119),"Congrats! Here is yout flag: INSA{"&TEXT(B1,"0")&"-"&TEXT(C1,"0")&"-"&TEXT(D1,"0")&"-"&TEXT(E1,"0")&"}","Wrong input")

It takes 4 inputs from B1, C1, D1, E1.

If we see the conditions, we need to fulfil this
    
    AND(
        E82=1,
        B1>1,B1<=256,
        C1>1,C1<=256,
        D1>1,D1<=256,
        E1>1,E1<=256,
        B1-C1=46,
        E1-D1=119
    ),

Firstly, we see that B1 through E1 needs to be within 8 bits `1 < X <= 256`.

Next, we see some relations. I will set the formula of 2 cells, E1 and B1.

    E1 == 119 + D1
    B1 == 46 + C1

This leaves us with C1 and D1 as unknown.

We merely need to bruteforce D1 and C1.

    D1 where 0 < D1 < (256-119)
    D1 where 0 < D1 < 137

    C1 where 0 < C1 < (256-46)
    C1 where 0 < C1 < 210

Using visual basic script macros, I created a simple for-loop bruteforce

    Sub RangeObjects()
        Dim i As Integer, j As Integer
        For i = 1 To 256
            Cells(1, "C").Value = i
            
            For j = 1 To 256
                Cells(1, "D").Value = j
                
                If InStr(1, (Range("G2").Value), "flag") > 0 Then
                    Debug.Print (Range("G2").Value)
                End If

            Next j

        Next i
    End Sub

And we can open the intermediate window and see the printed results

    Congrats! Here is yout flag: INSA{75-29-13-132}
    Congrats! Here is yout flag: INSA{203-157-13-132}

## Flag

	INSA{203-157-13-132}
