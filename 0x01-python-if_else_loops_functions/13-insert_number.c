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
#if 0
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new_node, *prev = NULL;

	if (!head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	temp = *head;
	while (temp && new_node->n > temp->n)
	{
		prev = temp;
		temp = temp->next;
	}
	/* for duplicate node values */
	if (temp && new_node->n == temp->n)
	{
		new_node->next = temp;
		prev->next = new_node;
	}
	/* when new_node value is lower than value at first node */
	else if (!prev)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = prev->next;
		prev->next = new_node;
	}

	return (new_node);
}
#endif
