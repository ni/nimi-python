# Different documentation snippets we add to the generated documentation

rep_cap_method_desc = '''
This method requires repeated capabilities (usually channels). If called directly on the
{0}.Session object, then the method will use all repeated capabilities in the session.
You can specify a subset of repeated capabilities using the Python index notation on an
{0}.Session instance, and calling this method on the result.:
'''
rep_cap_method_desc_rst = rep_cap_method_desc + '''
.. code:: python

    session['0,1'].{1}({2})
'''

rep_cap_method_desc_docstring = rep_cap_method_desc + '''
    session['0,1'].{1}({2})
'''

func_note_text = '''
One or more of the referenced functions are not in the Python API for this driver.
'''

attr_note_text = '''
One or more of the referenced attributes are not in the Python API for this driver.
'''

enum_note_text = '''
One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
'''





