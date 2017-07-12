Contributing to nimi-python
===========================

Contributions to ** nimi-python** are welcome from all!

**nimi-python** is managed via `git <https://git-scm.com>`_, with the canonical
upstream repository hosted on `GitHub <http://developercertificate.org/>`_.

**nimi-python** follows a pull-request model for development. If you wish to
contribute, you will need to create a GitHub account, fork this project,
push a branch with your changes to your project, and then submit a pull
request.

See `GitHub's official documentation <https://help.github.com/articles/using-pull-requests/>`_
for more details.

Getting Started
---------------

To contribute to this project, it is recommended that you follow these steps:

1. Fork the repository on GitHub.
2. Build. Unit tests will execute as part of this.
      To build on a Windows Machine
      1. Install Python
      2. Install PyPI
      3. pip install Wheel
      4. pip install Mock
      5. pip install Mako
      6. Install mingw (msys-base) following http://www.mingw.org/wiki/Getting_Started
      7. Add C:\MinGW\msys\1.0\bin to Windows path
      8. Call "make clean"
      9. Call "make"
3. Run system tests on your system (see Testing section). At this point,
   if any tests fail, do not begin development. Try to investigate these
   failures. If you're unable to do so, report an issue through our
   `GitHub issues page <http://github.com/nimi-python/issues>`_.
4. Write new unit tests  and system tests that demonstrate your bug or feature. Ensure that these
   new tests fail.
5. Make your change.
6. Run all the tests again (which include the tests you just added),
   and confirm that they all pass.
7. Send a GitHub Pull Request to the main repository's master branch. GitHub
   Pull Requests are the expected method of code collaboration on this project.

.. _testing-section:

Testing
-------

Unit tests are self-contained and invoked as part of the build process.

System tests are distinct on a per-driver basis and require the following:

  - Full driver or runtime is installed (i.e. NI-DMM).
  - Supported version of CPython is installed.
  - Compatible device is connected to it (i.e. NI 4080).

* TODO(marcoskirsch): update all this when we have clearer information*

NI-DMM system tests assume your device has a specific alias "DMM1" specified in MAX. Rename your device in MAX to match.

To run the **nidmm** unit tests in a specific version of Python, run the following command in the root of the distribution::

  $ <Python executable> setup.py test

To run the unit tests in all Python interpreters supported by **nidmm**,
run the following commands in the root of the distribution::

  $ pip install tox
  $ tox

This requires you to have all the Python interpreters supported by
**nidmm** installed on your machine.

Developer Certificate of Origin (DCO)
-------------------------------------

Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I
    have the right to submit it under the open source license
    indicated in the file; or

(b) The contribution is based upon previous work that, to the best
    of my knowledge, is covered under an appropriate open source
    license and I have the right under that license to submit that
    work with modifications, whether created in whole or in part
    by me, under the same open source license (unless I am
    permitted to submit under a different license), as indicated
    in the file; or

(c) The contribution was provided directly to me by some other
    person who certified (a), (b) or (c) and I have not modified
    it.

(d) I understand and agree that this project and the contribution
    are public and that a record of the contribution (including all
    personal information I submit with it, including my sign-off) is
    maintained indefinitely and may be redistributed consistent with
    this project or the open source license(s) involved.

(taken from `developercertificate.org <http://developercertificate.org/>`_)

See `LICENSE <https://github.com/ni/nimi-python/blob/master/LICENSE>`_
for details about how **nimi-python** is licensed.
