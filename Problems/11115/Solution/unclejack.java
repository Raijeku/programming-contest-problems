/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package semillero.programacion.competitiva;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 *
 * @author Davquiroga
 */
public class unclejack {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] a = new int[2];
        int n = scanner.nextInt();
        int d = scanner.nextInt();
        List<Integer> results = new ArrayList<>();
        while (n!=0 || d!=0) {
            results.add((int)Math.pow(n, d));
            n = scanner.nextInt();
            d = scanner.nextInt();
        }
        for(int i : results){
            System.out.println(i);
        }
    }
    
}
