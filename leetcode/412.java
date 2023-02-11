class Solution {

    public List<String> fizzBuzz(int n) {
       List <String> temp = new ArrayList<>();
       for( int i = 1 ; i<=n ; i++){
           if(i % 3  == 0  && i % 5 == 0 ){
               temp.add("FizzBuzz");
           }

           else if(i % 3 == 0){
               temp.add("Fizz");
           }

           else if(i % 5 == 0 ){
               temp.add("Buzz");
           }

           else {
               temp.add(String.valueOf(i));
           }
       }
       return temp;
    }
}