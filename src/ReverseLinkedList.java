public class ReverseLinkedList {

    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    class Solution {
        public ListNode reverseList(ListNode head) {
            ListNode prev = null, curr = head;
            while (curr != null) {
                ListNode next = curr.next;
                curr.next = prev;
                prev = curr;
                curr = next;
            }
            return prev;
        }
    }
}
