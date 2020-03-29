/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semillero.programacion.competitiva;

import java.util.Scanner;

/**
 *
 * @author Davquiroga
 */
class elections {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] v = new int[n];
        double[] p = new double[n];
        int t = 0;
        boolean firstRound = false;
        int highestVotes = 0;
        int amountValid = 0;
        int highestIndex = -1;
        for (int i = 0; i<n; i++){
            v[i] = scanner.nextInt();
            t += v[i];
        }
        for (int i = 0; i < n; i++) {
            if (v[i]>highestVotes) {
                highestVotes=v[i];
                highestIndex=i;
            }
        }
        for (int i = 0; i<n; i++){
            p[i] = (double)v[i]/(double)t;
        }
        if (p[highestIndex]>=0.45) {
                firstRound = true;
        }
        if (!firstRound) {
            if (p[highestIndex]>=0.40)
            {
                for (int j = 0; j < n; j++) {
                    if (j!=highestIndex && p[highestIndex]>=(p[j]+0.10)) {
                        amountValid++;
                    }
                }
                if(amountValid==n-1){
                    firstRound = true;
                }
            }
            amountValid=0;
            
        }
        if (firstRound) {
            System.out.println("1");
        } else {
            System.out.println("2");
        }
        
    }
}
