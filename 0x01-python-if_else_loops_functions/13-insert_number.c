#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a new node at its position in sorted list
 * @head: pointer to the address of the head node in list
 * @number: the value of the new node
 * Return: pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp = *head;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!new_node || temp->n >= number)
	{
		new_node->next = temp;
		*head = new_node;
		return (new_node);
	}
	while (temp && temp->next && temp->next->n < number)
		temp = temp->next;
	new_node->next = temp->next;
	temp->next = new_node;
	return (new_node);
}
