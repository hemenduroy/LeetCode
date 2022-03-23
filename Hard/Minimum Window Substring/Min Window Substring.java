import java.util.*; 
import java.io.*;
//Coderbyte
class Main {

  public static String MinWindowSubstring(String[] strArr) {
    // code goes here
    int need[]= new int[26];
    int missing = strArr[1].length();
    for(int i=0;i<missing;i++){
      need[(int)strArr[1].charAt(i)-97]+=1;
    }//end for
    int i=0,I=0,J=0;
    for(int j=0;j<strArr[0].length();j++){
      if(need[strArr[0].charAt(j)-97] > 0)
        missing-=1;//end if
      need[strArr[0].charAt(j)-97]-=1;

      if (missing==0){
        while(i<j+1 && need[strArr[0].charAt(i)-97]<0){
          need[strArr[0].charAt(i)-97]+=1;
          i+=1;
        }//end while
        if (J==0 || j+1-i <= J-I){
          I=i;
          J=j+1;
        }//end if
      }//end if
    }//end for
    return strArr[0].substring(I,J);
  }//end func


  public static void main (String[] args) {  
    // keep this function call here     
    Scanner s = new Scanner(System.in);
    System.out.print(MinWindowSubstring(s.nextLine())); 
  }

}
