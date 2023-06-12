#include <Python.h>
/**
 * print_python_list_info - Set to print basic info about Python lists.
 * @p: PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, s;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (s = 0; s < size; s++)
	{
		printf("Element %d: ", s);

		obj = PyList_GetItem(p, s);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
