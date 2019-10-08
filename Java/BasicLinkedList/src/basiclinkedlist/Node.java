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
public class Node {
    
    public Node next;
    public Node prev;
    public int value;  

    public Node(Node next, Node prev, int value) {  //Constructor
        this.next = next;
        this.prev = prev;
        this.value = value;
    }
    
    public Node getNext(){
        return next;    //Get the next element in the list
    }
    
    public Node getPrev() {
        return prev;    //Get the previous element in the list
    }
    
    public int getValue(){
        return value;
    }
    
    public void setNext(Node nextNode){
        next = nextNode;
    }
    
    public void setPrev(Node prevNode){
        prev = prevNode;
    }
}
