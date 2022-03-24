import java.sql.SQLOutput;
import java.util.*;
import java.io.*;

class Main {

    public static String QuestionsMarks(String str) {
        // code goes here
        int length= str.length();
        //System.out.println(length);
        int sum=0,q=0;
        String res="false";
        boolean mode = false;
        for (int i=0; i<length; i++){
            //System.out.println(i);
            if ( Character.isDigit( str.charAt(i) ) || mode ){
                mode=true;
                if (Character.isDigit(str.charAt(i))) {
                    sum += (int)str.charAt(i)-48;
                    //System.out.println((int)str.charAt(i) + "i is " + i + " and sum is " + sum);
                    i++;
                }
                while(!Character.isDigit(str.charAt(i)) ){
                    if(str.charAt(i)=='?'){
                        q++;
                    }
                    i++;
                    //System.out.println(i);
                    if( i >= length)
                        return res;
                }
                sum+=(int)str.charAt(i)-48;
                if(sum==10) {
                    if (q==3) {
                        res = "true";
                        //System.out.println(i);
                        //System.out.println(res);
                    }
                    else
                        return "false";
                }
                sum = (int)str.charAt(i)-48;
                q=0;
            }
        }
        return res;
    }

    public static void main (String[] args) {
        // keep this function call here
        Scanner s = new Scanner(System.in);
        System.out.print(QuestionsMarks("mbbv???????????4??????ddsdsdcc9?"));
    }

}
