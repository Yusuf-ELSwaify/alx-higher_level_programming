#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int i = 0, size = Py_SIZE(p);
	PyObject *obj;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
	while (i < size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}
}
