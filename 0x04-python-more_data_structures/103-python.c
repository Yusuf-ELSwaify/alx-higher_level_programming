#include <Python.h>
/**
 * print_python_bytes - Prints info about Python byte objects
 * @p: A PyObject list
 */
void print_python_bytes(PyObject *p)
{
	int size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = ((PyVarObject *)p)->ob_size;
	printf("  size: %d\n", size);
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", str);

	size = size > 10 ? 10 : size + 1;
	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", str[i]);
		if (i != size - 1)
			printf(" ");
	}
	printf("\n");
}
/**
 * print_python_list - prints some basic info about Python lists
 * @p: A PyObject list.
 */
void print_python_list(PyObject *p)
{
	int i = 0, size = ((PyVarObject *)p)->ob_size;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %zd\n", list->allocated);
	while (i < size)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		i++;
	}
}
