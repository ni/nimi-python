<%page args="function, config, method_template, indent"/>\
.. function:: get_cal_date_and_time(cal_type)

    Returns the date and time of the last calibration performed.

    

    .. note:: The NI 4050 and NI 4060 are not supported.



    :param cal_type:


        Specifies the type of calibration performed (external or
        self-calibration).

        +--------------------------------------+---+----------------------+
        | NIDMM\_VAL\_INTERNAL\_AREA (default) | 0 | Self-Calibration     |
        +--------------------------------------+---+----------------------+
        | NIDMM\_VAL\_EXTERNAL\_AREA           | 1 | External Calibration |
        +--------------------------------------+---+----------------------+

        .. note:: The NI 4065 does not support self-calibration.


    :type cal_type: int

    :rtype: datetime

        datetime object representing the date and time of the last calibration of the given type


