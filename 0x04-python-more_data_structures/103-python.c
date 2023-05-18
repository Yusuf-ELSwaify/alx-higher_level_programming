#include <Python.h>
/**
 * print_python_list - prints some basic info about Python lists
 * @p: A PyObject list.
 */
void print_python_list(PyObject *p)
{
	int i = 0, size = Py_SIZE(p);
	PyObject *obj;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	while (i < size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
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
	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);
	size = size > 10 ? 10 : size + 1;
	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i != size - 1)
			printf(" ");
	}
	printf("\n");
}
