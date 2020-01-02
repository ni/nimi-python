.. _about-section:

About
=====

The **nimi-python** repository generates Python bindings (Application Programming Interface) for interacting with the Modular Instrument drivers. Currently, the following drivers are supported:

* NI-DCPower (Python module: nidcpower)
* NI-Digital Pattern Driver (Python module: nidigital)
* NI-DMM (Python module: nidmm)
* NI-FGEN (Python module: nifgen)
* NI-ModInst (Python module: nimodinst)
* NI-SCOPE (Python module: niscope)
* NI Switch Executive (Python module: nise)
* NI-SWITCH (Python module: niswitch)
* NI-TClk (Python module: nitclk)

It is implemented as a set of `Mako templates <http://makotemplates.org>`_ and per-driver metafiles that produce a Python module for each driver. The driver is called through its public C API using the
`ctypes <https://docs.python.org/2/library/ctypes.html>`_ Python library.

**nimi-python** supports all the Operating Systems supported by the underlying driver.

**nimi-python** follows Python Organization's life cycle plan. Current versions supported: Python 3.5 and later using CPython or PyPy.

**note** Beginning in 2020 nimi-python will begin following the Python organization's support life cycle. This will mean that the next release will drop support for Python 2.7 and Python 3.4

