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
    
    public LinkedList(){
        
    }
    
    public void unorderedInsert(int[] initialValues){   //Will insert into list in the order the numbers appear in the array
        for(int i = 0; i < initialValues.length; i++) {
            Node newNode = new Node(null, null, initialValues[i]);
            if(head == null && tail == null){
                head = newNode;
                tail = newNode;
            }else{
                newNode.prev = tail;
                tail.next = newNode ;
                tail = newNode;
            }
        }
    }
    
    public void orderedInsert(int[] initialValues){ //Will insert into linked list from largest to smallest
        for(int i = 0; i < initialValues.length; i++){
            Node newNode = new Node(null, null, initialValues[i]);
            Node currentNode = head;
            if(head == null){
                head = newNode;
            }else if(initialValues[i] < head.value){
                newNode.next = currentNode;
                head = newNode;
            }else{
                while(currentNode.next != null && currentNode.next.value < initialValues[i] && currentNode.value < initialValues[i]){
                    currentNode = currentNode.next;
                }
                System.out.println("Adding: " + initialValues[i] + ", " + currentNode.value);
                currentNode.next = newNode;
                newNode.prev = currentNode;
            }
            
            printList();
            System.out.println("");
        }
    }
    
    public void printList(){    //Print the linked list
        Node currentNode = head;
        while (currentNode != null){            
            System.out.print(currentNode.value + ",");
            currentNode = currentNode.next;
        }
        System.out.print("\n");
    }
}
