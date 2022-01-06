/*

# 7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers
(signed or unsigned).

*/

class Solution {
    public int reverse(int x) {
        String ret = "";
        int test = 0;
        boolean signed = (x < 0) ? true : false;
        if (signed) {x*=-1;}
        while (x != 0){
            int digit = x % 10;
            x /= 10;
            ret = ((ret == "") && signed) ? ("-" + ret + digit) : (ret + digit);
            try{
                test = Integer.parseInt(ret);
            } catch (Exception e){
                return 0;
            }

        }
        return test;
    }
}
