#include "lists.h"
/**
 * check_cycle - checks for loop in a list
 * @list: list to check
 * Return: 0 if no cycle and 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list->next;
	/* if tortoise == to hare */
	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}


