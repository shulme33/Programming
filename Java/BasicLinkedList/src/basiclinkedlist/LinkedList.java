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
    
    public void createListUnordered(int[] initialValues){
        for(int i = 0; i < initialValues.length; i++) {
            unorderedInsert(initialValues[i]);
        }
    }
    
    public void createListOrdered(int[] initialValues, int orderFunction){
        for(int i = 0; i < initialValues.length; i++) {
            switch(orderFunction){
                case 1:
                    orderedInsert1(initialValues[i]);
                    break;
                case 2:
                    orderedInsert2(initialValues[i]);
                    break;
            }
        }
    }
    
    public void unorderedInsert(int value){   //Will insert into list in the order the numbers appear in the array
        Node newNode = new Node(null, null, value);
        if(head == null && tail == null){
            head = newNode;
            tail = newNode;
        }else{
            newNode.prev = tail;
            tail.next = newNode ;
            tail = newNode;
        }
    }
    
    public void orderedInsert1(int value){ //Will insert into linked list from largest to smallest
        Node newNode = new Node(null, null, value);
        Node current = head;
        if(current == null){   //First node in the list'
            head = newNode;
            tail = newNode;
        }else{
            boolean valueAdded = false;
            while (!valueAdded){
                if(newNode.value < current.value && head == current){ //Adding at beginning
                    newNode.next = current;
                    current.prev = newNode;
                    head = newNode;
                    valueAdded = true;
                }else if(newNode.value >= current.value && tail == current){ //Adding to the end
                    current.next = newNode;
                    newNode.prev = current;
                    tail = newNode;
                    valueAdded = true;
                }else if(newNode.value < current.value){ //Adding in the middle
                    newNode.next = current;
                    current.prev.next = newNode;
                    newNode.prev = current.prev;
                    current.prev = newNode;
                    valueAdded = true;
                }else{  //Nothing to do, move to the next one
                    current = current.next;
                }
            }
        }
    }
    
    public void orderedInsert2(int value){ //Will insert into linked list from largest to smallest
        Node newNode = new Node(null, null, value);
        Node current = head;
        if(current == null){   //First node in the list'
            head = newNode;
            tail = newNode;
            return;
        }
        while (newNode.next == null && newNode.prev == null){
            if(newNode.value < current.value && head == current){ //Adding at beginning
                newNode.next = current;
                current.prev = newNode;
                head = newNode;
            }else if(newNode.value >= current.value && tail == current){ //Adding to the end
                current.next = newNode;
                newNode.prev = current;
                tail = newNode;
            }else if(newNode.value < current.value){ //Adding in the middle
                newNode.next = current;
                current.prev.next = newNode;
                newNode.prev = current.prev;
                current.prev = newNode;
            }else{  //Nothing to do, move to the next one
                current = current.next;
            }
        }
    }
    
    public void randomPopulateArray(int[] array){
        for(int i = 0; i < array.length; i++){
            array[i] = (int)(Math.random()*array.length*2) - array.length;   //Random #'s between -5000 and 5000
        }
    }
    
    public boolean testSort(){
        Node current = head;
        
        while(current.next != null){
            if(current.value > current.next.value){
                return false;
            }
            current = current.next;
        }
        return true;
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
