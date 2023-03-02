/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        
        ListNode l3 = new ListNode(-1);
        ListNode node3 = l3;
        int ex = 0;

        while (l1 != null || l2 != null){
            ListNode nodeNext = new ListNode(-1);
            node3.next = nodeNext;
            int a = 0;
            if (l1 != null) a = l1.val;
            int b = 0;
            if (l2 != null) b = l2.val;
            int c = a + b + ex;
            if (c < 10 )  ex = 0;
            if (c >= 10){
                c =  c - 10;
                ex = 1;
            }
            nodeNext.val = c;
            node3 = node3.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        if (ex == 1){
            ListNode cur = new ListNode(1);
            node3.next = cur;
        }

        return l3.next;  
    }
}