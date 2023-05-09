#include "lists.h"
#include <stdlib.h>

/**
 * insert - adds a number to a sorted array
 * @head: head of node
 * @number: number to add
 * Return: addressof the added node
 *	otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new, *next;

	if (!head || !*head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	while (node)
	{
		if (node->n < number && node->next->n > number)
		{
			next = node->next;
			node->next = new;
			new->n = number;
			new->next = next;
		}
		node = node->next;
	}

	return (new);
}

