<%page args="f, config"/>\
    def read_from_channel(self, maximum_time):
        '''read_from_channel

        Acquires a single measurement and returns the measured value.

        Tip:
        This method requires repeated capabilities (usually channels). If called directly on the
        nifake.Session object, then the method will use all repeated capabilities in the session.
        You can specify a subset of repeated capabilities using the Python index notation on an
        nifake.Session instance, and calling this method on the result.:

            session['0,1'].read_from_channel(maximum_time)

        Args:
            maximum_time (int or timedelta): Specifies the **maximum_time** allowed in years.

        Returns:
            reading (float): The measured value.
        '''
        if str(type(maximum_time)).find("'datetime.timedelta'") != -1:
            years = int(maximum_time.days / 365)
        else:
            years = maximum_time

        return self._read_from_channel(years)

