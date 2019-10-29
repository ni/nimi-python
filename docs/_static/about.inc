.. _about-section:

About
=====

The **nimi-python** repository generates Python bindings (Application Programming Interface) for interacting with the Modular Instrument drivers. Currently, the following drivers are supported:

* NI-DCPower (Python module: nidcpower)
* NI-DMM (Python module: nidmm)
* NI-FGEN (Python module: nifgen)
* NI-SCOPE (Python module: niscope)
* NI-SWITCH (Python module: niswitch)
* NI-ModInst (Python module: nimodinst)
* NI Switch Executive (Python module: nise)

It is implemented as a set of `Mako templates <http://makotemplates.org>`_ and per-driver metafiles that produce a Python module for each driver. The driver is called through its public C API using the
`ctypes <https://docs.python.org/2/library/ctypes.html>`_ Python library.

**nimi-python** supports all the Operating Systems supported by the underlying driver.

**nimi-python** supports Python 2.7, 3.4 and later using CPython or PyPy.

