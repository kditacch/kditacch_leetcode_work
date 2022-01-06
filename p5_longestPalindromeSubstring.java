/*
  # 5. Longest Palindrome Substring

  Given a string s, return the longest palindromic substring in s.

*/

class Solution {

    public String longestPalindrome(String s) {
        if (s == null || s == ""){return "";}
        if (s.length() == 1){return s;}
        String maxpal = "";
        for (int i = 0; i < s.length(); i++){
            maxpal = validPalindrome(s, maxpal, i, i);
            maxpal = validPalindrome(s, maxpal, i, i+1);
        }
        return maxpal;
    }

    public String validPalindrome(String s, String curr_max, int l_i, int r_i){
        int buff = 0;
        String sub = "";
        while ((r_i + buff) < s.length() && (l_i - buff) >= 0 && s.charAt(r_i + buff) == s.charAt(l_i - buff)){
            if (r_i + buff == l_i - buff){
                sub = sub + s.charAt(r_i + buff);
            } else {
                sub = s.charAt(l_i - buff) + sub + s.charAt(r_i + buff);
            }
           buff++;
        }

        if (sub.length() > curr_max.length()){return sub;}
        return curr_max;
    }
}
