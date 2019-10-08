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
public class LinkedList {
    
    public Node head;
    public Node tail;
    
    public LinkedList(int[] initialValues){
        for(int i = 0; i < initialValues.length; i++) {
            Node newNode = new Node(null, null, initialValues[i]);
            if(head == null && tail == null){
                head = newNode;
                tail = newNode;
            }else{
                newNode.setPrev(tail);
                tail.setNext(newNode);
                tail = newNode;
            }
        }
    }
    
    public void printList(){
        //Print the linked list
        Node currentNode = head;
        while (currentNode != null){            
            System.out.println(currentNode.getValue());
            currentNode = currentNode.next;
        }
    }
}
