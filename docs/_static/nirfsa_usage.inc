Usage
------

The following is a basic example of using the **nirfsa** module to open a session to an RF Signal Analyzer and perform a spectrum acquisition.

.. code-block:: python

    import nirfsa

    # Configure the session
    with nirfsa.Session(resource_name=resource_name, id_query=False, reset_device=False, options=options) as rfsa_session:
        rfsa_session.acquisition_type = nirfsa.AcquisitionType.IQ

        rfsa_session.reference_level = -10
        rfsa_session.iq_carrier_frequency = 1e9
        rfsa_session.number_of_samples = 1024
        rfsa_session.iq_rate = 1e6

        iq_data_array = np.zeros(number_of_samples, dtype=np.complex128)

        wfm_info = rfsa_session.read_iq_single_record_into(iq_data_array)
        # Perform measurements...

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nirfsa/examples>`_
