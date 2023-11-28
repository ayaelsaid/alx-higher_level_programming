#include "lists.h"
#include <stdio.h>
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *faster = list;

	while (slow && faster & faster->next)
	{
		slow = slow->next;
		faster = faster->next->next;
		if (slow == faster)
			return (1);
	}
	return (0);
}
