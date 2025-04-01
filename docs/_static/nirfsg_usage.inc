Usage
------

The following is a basic example of using the **nirfsg** module to open a session to a Function Generator and generate a sine wave for 5 seconds.

.. code-block:: python

    import nirfsg
    with nirfsg.Session('SwitchExecutiveExample') as session:
        session.connect('DIOToUUT')

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nirfsg/examples>`_

