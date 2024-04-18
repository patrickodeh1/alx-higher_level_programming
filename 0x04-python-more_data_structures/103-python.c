#include <Python.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *element;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "[*] Python list info\n");
        fprintf(stderr, "  [ERROR] Invalid Python List\n");
        return;
    }

    size = PyObject_Size(p);
    fprintf(stderr, "[*] Python list info\n");
    fprintf(stderr, "[*] Size of the Python List = %ld\n", size);
    fprintf(stderr, "[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        element = PyList_GetItem(p, i);
        fprintf(stderr, "Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    unsigned char *buffer;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[.] bytes object info\n");
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyObject_Size(p);
    fprintf(stderr, "[.] bytes object info\n");
    fprintf(stderr, "  size: %ld\n", size);
    fprintf(stderr, "  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
    fprintf(stderr, "  first 10 bytes: ");

    buffer = (unsigned char *)((PyBytesObject *)p)->ob_sval;
    for (i = 0; i < size && i < 10; i++)
    {
        fprintf(stderr, "%02x ", buffer[i]);
    }
    fprintf(stderr, "\n");
}