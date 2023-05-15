#include "lists.h"

/**
 * reverse_list - reverses the list
 * @head: list to reverse
 * Return: reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}


/**
 * is_palindrome - checks if a list is a palindrome
 * @head: address of the head node
 * Return: 1 if a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = NULL;
	listint_t *mid_node = NULL;
	listint_t *rev_list = NULL;
	int len_list = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		len_list++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (len_list / 2) - 1; i++)
		temp = temp->next;

	if ((len_list % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev_list = reverse_list(&temp);
	mid_node = rev_list;

	temp = *head;
	while (rev_list)
	{
		if (temp->n != rev_list->n)
			return (0);
		temp = temp->next;
		rev_list = rev_list->next;
	}
	reverse_list(&mid_node);

	return (1);
}
