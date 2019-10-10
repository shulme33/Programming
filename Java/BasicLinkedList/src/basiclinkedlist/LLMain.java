/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package basiclinkedlist;

/**
 *
 * @author Sam
 */
public class LLMain {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        System.out.println("Creating Linked List...");
        
        //Initialize the linked list
//        LinkedList list1 = new LinkedList();
//        System.out.println("\nUn-Ordered:");
//        list1.createListUnordered(new int[] {2,4,6,8,10});
//        list1.printList();
        
        LinkedList list2 = new LinkedList();
        System.out.println("\nOrdered Improved:");
        int[] array2 = new int[100000];
        list2.randomPopulateArray(array2);
        System.out.println("Array Created.");
        list2.createListOrdered(array2, 2);
        System.out.println("Test was successful: " + list2.testSort());
        
//        LinkedList list3 = new LinkedList();
//        System.out.println("\nOrdered 2:");
//        list3.createListOrdered(new int[] {2,5,6,13,5,40,7,1,-5,-10,1,3,0,0,0,7,8,-1,10}, 2);
//        list3.printList();
    }
    
    
    
}
