import math
import nidmm
import nimodinst
import warnings
import wx

USE_WIT = True

AppBaseClass = wx.App
if USE_WIT:
    from wx.lib.mixins.inspection import InspectableApp
    AppBaseClass = InspectableApp


def format_meas(reading, function, range, resolution):
    unit_modifiers = {-12: "p", -9: "n", -6: "u", -3: "m", 0: "", 3: "k", 6: "M", 9: "G"}
    function_units = {
        nidmm.Function.AC_VOLTS: "V AC",
        nidmm.Function.DC_VOLTS: "V DC",
        nidmm.Function.AC_CURRENT: "A AC",
        nidmm.Function.DC_CURRENT: "A DC",
        nidmm.Function.DIODE: "V Diode",
        nidmm.Function._2_WIRE_RES: "Ohm",
        nidmm.Function._4_WIRE_RES: "Ohm",
        nidmm.Function.PERIOD: "s",
        nidmm.Function.FREQ: "Hz",
        nidmm.Function.AC_VOLTS_DC_COUPLED: "V AC",
        nidmm.Function.CAPACITANCE: "F",
        nidmm.Function.INDUCTANCE: "H",
        nidmm.Function.TEMPERATURE: "deg C",
    }

    data_width = int(math.floor(resolution) + 1)

    # calculate reading string
    temp_range = range
    if (range * 1.2) < math.fabs(reading):
        temp_range = math.fabs(reading)

    order_of_subunit = int(math.floor(math.log10(temp_range) / 3))
    if order_of_subunit < -4:
        order_of_subunit = -4
    elif order_of_subunit > 3:
        order_of_subunit = 3

    range_order_of_subunit = int(math.floor(math.log10(range) / 3))
    if range_order_of_subunit < -4:
        range_order_of_subunit = -4
    elif range_order_of_subunit > 3:
        range_order_of_subunit = 3

    # function specific overrides
    if function == nidmm.Function.CAPACITANCE:
        if order_of_subunit == -1:
            order_of_subunit = -2
        if range_order_of_subunit == -1:
            range_order_of_subunit = -2
    elif function == nidmm.Function.DC_VOLTS:
        if order_of_subunit == 1:
            order_of_subunit = 0
        if range_order_of_subunit == 1:
            range_order_of_subunit = 0
    elif function == nidmm.Function.TEMPERATURE:
        order_of_subunit = 0
        range_order_of_subunit = 0

    # Calculate the divisor, the number by which to divide the reading to account
    # for the subunit (u,m,k,M).  The number of digits after the decimal point
    # is equal to the total number of digits minus the digits before the decimal
    # point.  Remeber that there needs to be one character for the decimal point
    # and one character for the - sign if present (+ does not appers, just a sp).
    divisor = math.pow(10.0, 3 * order_of_subunit)
    range_divisor = math.pow(10.0, 3 * range_order_of_subunit)

    if math.isnan(reading):
        reading_string = 'OVLD'
    elif math.isinf(reading):
        reading_string = 'UNDRNG'
    else:
        precision = data_width - 1 - int(math.floor(1e-9 + math.log10(temp_range / divisor)))
        if temp_range != range:
            reading_exp = math.floor(math.log10(math.fabs(reading)))
            reading_base = math.fabs(reading / math.pow(10.0, reading_exp))

            if 1.2 < reading_base:
                precision -= 1

        if precision < 0:
            precision = 0

        if precision == 0:
            width = data_width
        else:
            width = data_width + 1

        final_reading = math.fabs(reading / divisor)
        final_reading = math.pow(10.0, -precision) * math.floor(0.5 + math.pow(10.0, precision) * final_reading)
        final_reading = math.fabs(final_reading)

        sign = '-' if reading < 0 and (reading / divisor) * math.pow(10.0, precision) <= -0.5 else ' '

        reading_string = sign + "{value:0{width}.{precision}f}".format(value=float(final_reading), width=width, precision=precision, sign=sign)

    # calculate range string
    range_string = '{:.2f}'.format(range / range_divisor)

    # calculate function string
    function_units = function_units[function] if function in function_units else ''
    function_unit_modifiers = unit_modifiers[order_of_subunit * 3]

    function_string = function_unit_modifiers + function_units

    return function_string, range_string, reading_string


class SFP(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SFP.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((500, 600))

        # Menu Bar
        self.menu_bar = wx.MenuBar()
        self.SetMenuBar(self.menu_bar)
        # Menu Bar end
        self._devices = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self._function = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self._digits = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self._range = wx.SpinCtrlDouble(self, wx.ID_ANY, "1", min=0, max=1000)
        self.Bind(wx.EVT_SPINCTRLDOUBLE, self.OnConfigUpdate, self._range)
        self._range_display = wx.StaticText(self, wx.ID_ANY, "")
        self._reading_display = wx.StaticText(self, wx.ID_ANY, "")
        self._status = wx.StaticText(self, wx.ID_ANY, "Good!")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TEXT, self.OnConfigUpdate, self._function)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnConfigUpdate, self._function)
        self.Bind(wx.EVT_COMBOBOX, self.OnConfigUpdate, self._digits)
        self.Bind(wx.EVT_TEXT, self.OnConfigUpdate, self._digits)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnConfigUpdate, self._digits)
        # end wxGlade

        self._session = None
        self._modinst_session = None
        self._dev_name = None

        # and a menu
        menu = wx.Menu()

        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Exit this simple sample")

        # bind the menu event to an event handler
        # self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        self.menu_bar.Append(menu, "&File")
        self.SetMenuBar(self.menu_bar)

        self.CreateStatusBar()

        self._modinst_session = nimodinst.Session('nidmm')
        for dev in self._modinst_session:
            dev_name = dev.device_name
            self._devices.Append('{0}'.format(dev_name))

        self._devices.SetSelection(0)

        for f in list(nidmm.Function.__members__.keys()):
            self._function.Append('{0}'.format(f))

        self._function.SetSelection(0)

        digits = [3.5, 4.5, 5.5, 6.5, 7.5]
        for d in digits:
            self._digits.Append('{0}'.format(d))

        self._digits.SetSelection(2)

        self._timer = wx.Timer(self, wx.ID_ANY)
        self.Bind(wx.EVT_TIMER, self.OnUpdate, self._timer)

        self.OnConfigUpdate(None)
        self._timer.Start(250)

    def __set_properties(self):
        # begin wxGlade: SFP.__set_properties
        self.SetTitle("NI-DMM Simple Soft Front Panel")
        self._range_display.SetFont(wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, ""))
        self._reading_display.SetFont(wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SFP.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_10 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Status"), wx.HORIZONTAL)
        sizer_5 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Results:"), wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, "Configuration"), wx.VERTICAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Device:  ")
        label_1.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        sizer_3.Add(label_1, 0, 0, 0)
        sizer_3.Add(self._devices, 0, 0, 0)
        sizer_1.Add(sizer_3, 3, wx.EXPAND, 0)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(static_line_1, 1, wx.EXPAND, 0)
        sizer_1.Add((20, 20), 1, 0, 0)
        label_8 = wx.StaticText(self, wx.ID_ANY, "Function:")
        sizer_8.Add(label_8, 0, 0, 0)
        sizer_8.Add(self._function, 0, 0, 0)
        sizer_8.Add((20, 20), 0, 0, 0)
        label_9 = wx.StaticText(self, wx.ID_ANY, "Resolution")
        sizer_8.Add(label_9, 0, 0, 0)
        sizer_8.Add(self._digits, 0, 0, 0)
        sizer_8.Add((20, 20), 0, 0, 0)
        sizer_2.Add(sizer_8, 1, wx.EXPAND, 0)
        label_10 = wx.StaticText(self, wx.ID_ANY, "Range:")
        sizer_9.Add(label_10, 0, 0, 0)
        sizer_9.Add(self._range, 0, 0, 0)
        sizer_9.Add((20, 20), 0, 0, 0)
        sizer_2.Add(sizer_9, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 15, wx.EXPAND, 0)
        sizer_1.Add((20, 20), 1, 0, 0)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Range:  ")
        sizer_6.Add(label_6, 20, 0, 0)
        sizer_6.Add(self._range_display, 30, 0, 0)
        sizer_6.Add((20, 20), 50, 0, 0)
        sizer_5.Add(sizer_6, 1, wx.EXPAND, 0)
        label_7 = wx.StaticText(self, wx.ID_ANY, "Reading:  ")
        sizer_7.Add(label_7, 20, 0, 0)
        sizer_7.Add(self._reading_display, 30, 0, 0)
        sizer_7.Add((20, 20), 50, 0, 0)
        sizer_5.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_5, 15, wx.EXPAND, 0)
        sizer_1.Add((20, 20), 1, 0, 0)
        sizer_10.Add(self._status, 100, 0, 0)
        sizer_1.Add(sizer_10, 25, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def OnUpdate(self, event):  # noqa: N802
        points_ready, _ = self._session.read_status()
        with warnings.catch_warnings(record=True) as w:
            points = self._session.fetch_multi_point(points_ready)
            if len(w) > 0:  # that means we got a warning so we will put it in the status area
                self._status.SetLabel(str(w[0].message))

        actual_range = self._session.range
        if len(points) > 0:
            mode_str, range_str, data_str = format_meas(points[-1], nidmm.Function[self._dev_function], actual_range, self._dev_digits)
            reading_display = data_str + ' ' + mode_str
            range_display = range_str + ' ' + mode_str
            self._reading_display.SetLabel(reading_display)
            self._range_display.SetLabel(range_display)

    def OnConfigUpdate(self, event):  # noqa: N802
        current_dev_name = self._devices.GetStringSelection()
        current_function = self._function.GetStringSelection()
        try:
            current_range = float(self._range.GetValue())
        except TypeError:
            current_range = 1.0
        current_digits = float(self._digits.GetStringSelection())

        try:
            if current_dev_name != self._dev_name:
                if self._session is not None:
                    self._session.close()
                self._session = nidmm.Session(current_dev_name)
                self._session.configure_multi_point(trigger_count=0, sample_count=0, sample_trigger=nidmm.SampleTrigger.IMMEDIATE, sample_interval=-1)

            self._session.configure_measurement_digits(nidmm.Function[current_function], current_range, current_digits)
            self._session._initiate()
        except nidmm.Error as e:
            self._status.SetLabel(str(e))

        self._dev_name = current_dev_name
        self._dev_function = current_function
        self._dev_range = current_range
        self._dev_digits = current_digits

    def OnCloseWindow(self, event):  # noqa: N802
        self._session.close()
        self.Destroy()

    def OnIdle(self, event):  # noqa: N802
        self.idleCtrl.SetValue(str(self.count))
        self.count = self.count + 1

    def OnSize(self, event):  # noqa: N802
        size = event.GetSize()
        self.sizeCtrl.SetValue("%s, %s" % (size.width, size.height))
        event.Skip()

    def OnMove(self, event):  # noqa: N802
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))


class SFPApp(AppBaseClass):

    def OnInit(self):  # noqa: N802
        self.frame = SFP(None, wx.ID_ANY, "NI-DMM Python SFP")
        self.SetTopWindow(self.frame)

        if USE_WIT:
            self.InitInspection()

        self.frame.Show(True)
        return True


app = SFPApp(False)
app.MainLoop()


