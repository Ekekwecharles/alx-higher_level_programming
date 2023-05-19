#include <stdio.h>
#include "Python.h"

void print_python_bytes(PyObject *p);
/**
 * print_python_list - prints info about a python list
 * @p: list object
 */
void print_python_list(PyObject *p)
{
	int i;
	PyListObject *pp;

	pp = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", pp->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", pp->allocated);

	for (i = 0; i < pp->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
		if (strcmp(pp->ob_item[i]->ob_type->tp_name, "bytes") == 0)
			print_python_bytes(pp->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints info about a python byte
 * @p: bytes object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char j, size;
	PyBytesObject *pp;

	pp = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", pp->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", size);
	for (j = 0; j < size; j++)
	{
		printf("%02hhx", pp->ob_sval[j]);
		if (j == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}
