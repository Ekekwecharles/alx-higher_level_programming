#include "lists.h"

/**
 * get_nodeint_at_index - Locates a given node of
 *                        a listint_t linked list.
 * @head: A pointer to the head of the listint_t list.
 * @index: The index of the node to locate - index start at 0.
 *
 * Return: If the node doesn't exist - NULL.
 *         Otherwise - node found at index
 */

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int i;

	for (i = 0; i < index; i++)
	{
		if (head == NULL)
			return (NULL);
		head = head->next;
	}
	return (head);
}

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: address of the head node
 * Return: 1 if a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	int list_len = 0, half_len, i = 0, j = 0;
	listint_t *node = *head;

	/* Empty list or single node list is cnsiderted a palindrome */
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (node != NULL)
	{
		list_len++;
		node = node->next;
	}
	/* Use ceiling division for odd lengths */
	half_len = (list_len + 1) / 2;
	j = list_len - 1;
	while (i < half_len)
	{
		if (get_nodeint_at_index(*head, i)->n != get_nodeint_at_index(*head, j)->n)
			return (0);
		i++;
		j--;
	}
	return (1);
}

