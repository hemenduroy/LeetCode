import java.util.*; 
import java.io.*;

class Main {

  public static String BracketMatcher(String str) {
    // code goes here  
    int open=0;
    for (int i=0;i<str.length();i++){
      if(str.charAt(i)=='(')
        open+=1;
      if(str.charAt(i)==')'){
        open-=1;
      }
      if(open<0)
        return "0";
    }
    if (open!=0)
      return "0";
    else
      return "1";
  }

  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    System.out.print(BracketMatcher(s.nextLine())); 
  }

}
