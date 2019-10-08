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

    public Node(Node prev, Node next, int value) {  //Constructor
        this.next = next;
        this.prev = prev;
        this.value = value;
    }
}
