class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int[] arras = new int[128];
        int length = s.length();
        int index = 0;
        int temp = 0;
        for (int i = 0; i < length; i++) {
            temp = Math.max(temp, arras[s.charAt(i)]);
            index = Math.max(index, i + 1 - temp);
            arras[s.charAt(i)] = i + 1;
        }
        return index;
        
    }
}