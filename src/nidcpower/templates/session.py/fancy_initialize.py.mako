<%page args="f, config, method_template"/>\
<%
    '''
    Dispatches to the proper initialize method based on input parameters.
    Stores independent_channels argument in an instance variable for use by session lock and unlock.
    '''
    import build.helper as helper

    suffix = method_template['method_python_name_suffix']
%>\
    # TODO: Remove the following code as described in issue 1596. https://github.com/ni/nimi-python/issues/1596

    # create a weak value dict for storing references to session objects
    import weakref
    _sessions = weakref.WeakValueDictionary()

    # cache super class lock and unlock methods for decorating via monkey patching
    _super_lock_session = _SessionBase._lock_session
    _super_unlock = _SessionBase.unlock

    # create fancy functions
    @staticmethod
    def _fancy_lock_session(self):
        session = Session._sessions[self._vi]
        if hasattr(session, '_pylock'):
            session._pylock.acquire()
            return
        else:
            return Session._super_lock_session(self)

    @staticmethod
    def _fancy_unlock(self):
        session = Session._sessions[self._vi]
        if hasattr(session, '_pylock'):
            session._pylock.release()
            return
        else:
            return Session._super_unlock(self)

    # monkey patch super class lock and unlock methods to use this class' fancy functions
    _SessionBase._lock_session = lambda self: Session._fancy_lock_session(self)
    _SessionBase.unlock = lambda self: Session._fancy_unlock(self)

    def ${f['python_name']}${suffix}(${helper.get_params_snippet(f, helper.ParameterUsageOptions.SESSION_METHOD_DECLARATION)}):
        '''${f['python_name']}

        ${helper.get_function_docstring(f, False, config, indent=8)}
        '''
        if independent_channels:
            if channels:
                import warnings
                warnings.warn(
                    "Attempting to initialize an independent channels session with a channels argument. "
                    "Channels will be combined with the resource name to form a fully-qualified channel list. "
                    "To avoid this warning, use a fully-qualified channel list as the resource name instead "
                    "of providing a channels argument.",
                    DeprecationWarning
                )

                # if we have a channels arg, we need to try and combine it with the resource name
                # before calling into initialize with independent channels
                if "," in resource_name:
                    raise ValueError(
                        "Channels can't be combined with multiple devices in resource name. "
                        "Use a single device in the resource name or provide a list of fully-qualified channels "
                        "as the resource name instead of supplying a channels argument."
                    )
                channel_list = (f"{resource_name}/{channel}" for channel in channels.split(","))
                resource_name = ",".join(channel_list)

            # TODO: Modify this line as described in issue 1596. https://github.com/ni/nimi-python/issues/1596
            self._vi = self._initialize_with_independent_channels(resource_name, reset, option_string)

        else:
            import warnings
            warnings.warn("Initializing session without independent channels enabled.", DeprecationWarning)

            # TODO: Modify this line as described in issue 1596. https://github.com/ni/nimi-python/issues/1596
            self._vi = self._initialize_with_channels(resource_name, channels, reset, option_string)

        # TODO: Remove the following code as described in issue 1596. https://github.com/ni/nimi-python/issues/1596
        # cache session before calling lock to avoid a key error in fancy functions
        self._sessions[self._vi] = self

        # test to see if runtime supports locking session
        try:
            self.lock()  # self._pylock not yet defined, will dispatch to driver lock
        except errors.DriverError:
            self._get_error()  # clear error from lock
            import threading
            self._pylock = threading.RLock()  # define a recursive lock to be used henceforth
        else:
            self.unlock()  # lock succeeded, unlock session

        return self._vi

