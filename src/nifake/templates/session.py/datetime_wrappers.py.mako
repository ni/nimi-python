<%page args="f, config"/>\
    def read(self, maximum_time):
        '''read

        Acquires a single measurement and returns the measured value.

        Args:
            maximum_time (int or timedelta): Specifies the **maximum_time** allowed in years.

        Returns:
            reading (float): The measured value.
        '''
        if str(type(maximum_time)).find("'datetime.timedelta'") != -1:
            years = int(maximum_time.days / 365)
        else:
            years = maximum_time

        return self._read(years)

    def get_cal_date_and_time(self, cal_type):
        '''get_cal_date_and_time

        Returns the date and time of the last calibration performed.

        Note: The NI 4050 and NI 4060 are not supported.

        Args:
            cal_type (int): Specifies the type of calibration performed (external or self-calibration).

                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_INTERNAL_AREA (default) | 0 | Self-Calibration     |
                +-----------------------------------+---+----------------------+
                | NIDMM_VAL_EXTERNAL_AREA           | 1 | External Calibration |
                +-----------------------------------+---+----------------------+

                Note: The NI 4065 does not support self-calibration.

        Returns:
            datetime object representing the date and time of the last calibration
        '''
        import datetime

        month, day, year, hour, minute = self._get_cal_date_and_time(cal_type)
        return datetime.datetime(year, month, day, hour, minute)

