Usage
------

The following is a basic example of using the **nimodinst** module to retrieve information on all High Speed Digitizers currently in the system.

.. code-block:: python

    import nimodinst
    with nimodinst.Session("niscope") as session:
        for device in session:
            print("{: >20} {: >15} {: >10}".format(device.device_name, device.device_model, device.serial_number))

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nimodinst/examples>`_

