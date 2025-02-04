"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self. next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:  # type: ignore
        """Returns data attribute for the first element in the linked list."""
        if self.data == 0:
            return self.data
    
    def tail(self) -> Node | None:
        """Returns inked list of every element minus head."""
        if self.next is None:
            return None
        else:
            return self.next
    
    def last(self) -> int:
        """Returns data of last element in linked list."""
        if self.next is None:
            return self.data
        else:
            return self.next.data