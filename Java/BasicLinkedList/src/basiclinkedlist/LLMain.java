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
        LinkedList list1 = new LinkedList(new int[] {2,4,6,8,10});
        list1.printList();
        
        LinkedList list2 = new LinkedList(new int[] {1,2,3,4,5});
        list2.printList();
    }
    
    
    
}
