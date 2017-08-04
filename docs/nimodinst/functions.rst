NI-ModInst Functions
====================

.. py:currentmodule:: nimodinst


.. function:: _close_installed_devices_session(handle)

    :param handle: 
    :type handle: ViSession


.. function:: get_extended_error_info(error_info_buffer_size, error_info)

    :param error_info_buffer_size: 
    :type error_info_buffer_size: ViInt32

    :rtype: ViChar


.. function:: _get_installed_device_attribute_vi_int32(handle, index, attribute_id, attribute_value)

    :param handle: 
    :type handle: ViSession
    :param index: 
    :type index: ViInt32
    :param attribute_id: 
    :type attribute_id: ViInt32

    :rtype: ViInt32


.. function:: _get_installed_device_attribute_vi_string(handle, index, attribute_id, attribute_value_buffer_size, attribute_value)

    :param handle: 
    :type handle: ViSession
    :param index: 
    :type index: ViInt32
    :param attribute_id: 
    :type attribute_id: ViInt32
    :param attribute_value_buffer_size: 
    :type attribute_value_buffer_size: ViInt32

    :rtype: ViChar


.. function:: _open_installed_devices_session(driver, handle, item_count)

    :param driver: 
    :type driver: ViConstString

    :rtype: tuple (handle, item_count)
        WHERE
        handle (ViSession): 
        item_count (ViInt32): 


