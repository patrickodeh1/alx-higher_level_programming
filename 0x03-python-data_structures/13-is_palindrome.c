#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (head != NULL)
	{
		next = head->next;
		head->next = prev;
		prev = head;
		head = next;
	}

	return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to a pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *second_half, *first_half;
	if (*head == NULL || (*head)->next == NULL)
		return (1);

	slow = *head;
	fast = *head;

	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	second_half = reverse_list(slow->next);

	first_half = *head;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return (1);
}
