#include "list.h"
/**
*Description:function in C that checks if a singly linked list has a cycle in it.
*Return:0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list) {

list_t *head *current
if (!list || !list ->next)

return 0;

head = list;
current = list;

while (currenrt != NULL && head != NULL && head -> list != NULL)
current = current -> next;
head = head -> next;
if (cirrent = head) {

return 1;
}

return 0;
}

