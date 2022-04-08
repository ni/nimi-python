Usage
------

The following is a basic example of using the **nise** module to open a session to a Switch Executive Virtual Device and connect a routegroup.

.. code-block:: python

    import nise
    with nise.Session('SwitchExecutiveExample') as session:
        session.connect('DIOToUUT')

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nise/examples>`_

