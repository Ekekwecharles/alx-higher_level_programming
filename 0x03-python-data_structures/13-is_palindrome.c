#include "lists.h"

/**reverse_list - reverses the list
 * @head: list to reverse
 * Return: reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}


/**
 * is_palindrome - checks if a list is a palindrome
 * @head: address of the head node
 * Return: 1 if a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev_slow = *head;
	listint_t *mid_node = NULL;
	listint_t *second_half = NULL;
	int result = 1;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	second_half = reverse_list(slow);
	prev_slow->next = NULL;

	listint_t *temp1 = *head;
	listint_t *temp2 = second_half;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n != temp2->n)
		{
			result = 0;
			break;
		}
		temp1 = temp1->next;
		temp2 = temp2->next;
	}

	second_half = reverse_list(second_half);
	prev_slow->next = second_half;

	if (mid_node != NULL)
	{
		prev_slow->next = mid_node;
		mid_node->next = second_half;
	}
	return result;
}
