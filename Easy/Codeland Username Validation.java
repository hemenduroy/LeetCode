import java.util.*; 
import java.io.*;

class Main {

  public static String CodelandUsernameValidation(String str) {
    // code goes here
    int strlength=str.length();
    if(strlength<4 || strlength>25)
      return "false";
    else if (!Character.isLetter(str.charAt(0)))
      return "false";
    else if (str.charAt(strlength-1) == '_')
      return "false";
    
    for (int i=0; i<strlength;i++){
      if (!(Character.isLetter(str.charAt(i)) || Character.isDigit(str.charAt(i)) ||  str.charAt(i)=='_'))
        return "false";
    }
    return "true";
  }

  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    System.out.print(CodelandUsernameValidation(s.nextLine())); 
  }

}
