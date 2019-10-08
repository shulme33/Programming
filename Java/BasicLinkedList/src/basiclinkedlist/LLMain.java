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
        LinkedList list1 = new LinkedList();
        list1.unorderedInsert(new int[] {2,4,6,8,10});
        list1.printList();
        
        LinkedList list2 = new LinkedList();
        list2.orderedInsert(new int[] {2,5,6,1,3,0,7,8,-1,10});
        list2.printList();
    }
    
    
    
}
