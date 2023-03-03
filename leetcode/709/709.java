class Solution {
    public String toLowerCase(String s) {
        String result = "";
        for(char c : s.toCharArray()){
            if(Character.isUpperCase(c)){
               result += (char)(c + 32);
            }

            else {
                result+=c;
            }
        }

        return result;
    }
}
