/*

# 6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern
on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion
given a number of rows:

string convert(string s, int numRows);

*/

class Solution {
    public String convert(String s, int numRows) {
        int j = 0;
        int slen = s.length();
        if (slen == numRows || numRows == 1){return s;}
        String converted = "";
        for (int i = numRows; i > 0;  i--){
            int k = j;
            while (k < slen){
                converted = converted + s.charAt(k);
                if (i != numRows && j != (numRows-1)){
                    int twn = k + 2 * (i - 1);
                    if (twn < slen)
                    converted += s.charAt(twn);
                }
                k = k + 2 * (numRows-1);
            }
            j++;
        }
        return converted;
    }
}
