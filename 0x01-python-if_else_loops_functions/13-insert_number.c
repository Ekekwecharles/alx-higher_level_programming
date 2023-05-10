#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - adds a number to a sorted array
 * @head: head of node
 * @number: number to add
 * Return: addressof the added node
 *	otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new, *prev = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	while (node)
	{
		if (number > node->n)
		{
			prev = node;
			node = node->next;
			continue;
		}
		else if (!prev)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			new->next = prev->next;
			prev->next = new;
		}
		return (new);
	}

	if (!prev)
		*head = new;
	else
		prev->next = new;

	return (new);
}
