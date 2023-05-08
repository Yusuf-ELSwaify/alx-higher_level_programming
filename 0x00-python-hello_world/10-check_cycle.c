#include "lists.h"
/**
 * check_cycle - finds the loop in a linked list
 * @head: pointer to the first node in list
 * Return: 0 (no loops) otherwise 1
 */
int check_cycle(listint_t *head)
{
	listint_t *fast, *slow;

	if (!head || !head->next)
		return (0);
	fast = (head->next)->next;
	slow =  head->next;
	while (fast && fast->next && slow)
	{
		if (fast == slow)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
