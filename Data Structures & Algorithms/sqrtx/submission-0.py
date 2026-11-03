class Solution:
    def mySqrt(self, x: int) -> int:

        i = 0 
        j = x

        res = 0

        while i <= j:

            m = (i + j) //2

            if m * m == x :

                return m

            elif m*m < x:

                res = m 

                i = m+1
            else :

                j = m-1

        return res
        