class Solution:
    def addBinary(self, a: str, b: str) -> str:

        res = ""
        carry =0

        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i< len(a)  else 0
            digitB = int(b[i]) if i< len(b)  else 0
            
            total = digitA + digitB + carry
            digit = str(total % 2)
            carry = total//2
            res = digit + res 

        if carry == 1:
            res ="1" + res

        return res