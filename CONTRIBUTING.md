Contributing to nimi-python
===========================

Contributions to **[`nimi-python`](https://github.com/ni/nimi-python)** are welcome from all!

**[`nimi-python`](https://github.com/ni/nimi-python)** is managed via [Git](https://git-scm.com), with the canonical
upstream repository hosted on [GitHub](http://developercertificate.org/).

**[`nimi-python`](https://github.com/ni/nimi-python)** follows a pull request model for development.
If you wish to contribute, you will need to create a GitHub account, fork this project,
push a branch with your changes to your project, and then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/)
for more details.


Setting up your system
----------------------

In order to have the ability to build and run the tests you will need a few things to be set up on your system.

### Windows:

-  Install and enable [Windows Subsystem for Linux](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)
- Install GNU Make: ``sudo apt-get install make``
- Install zip: ``sudo apt-get install zip``
- Install [Python 3.9](https://www.python.org/downloads/)
    - Add ``Python install path`` and ``python install path``\Scripts to Windows path
    - Copy ``Python install path``\python.exe to ``python install path``\python3.exe

### macOS:

- Install [Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)
- Install command line developer tools
- Install [Python 3.9](https://www.python.org/downloads/)

### Linux:

- Install Python 3.9 and [PyPI](https://pypi.python.org/pypi): ``sudo apt-get install python3-pip (Linux)``

### All:

Once your system has been setup with the above, install required additional Python modules using PyPI.

        sudo pip install pytest tox --upgrade


Building **[`nimi-python`](https://github.com/ni/nimi-python)**
---------------------------------------------------------------

1. Fork [the repository](https://github.com/ni/nimi-python) on GitHub and clone it to your local system.
1. On a terminal, navigate to the **[`nimi-python`](https://github.com/ni/nimi-python)** root
   directory. Then run

       tox

   It will do the following, for each driver:

      * Generate Python bindings
      * Generate [RST documentation](http://www.sphinx-doc.org/)
      * Create installer packages
      * Run [flake8](http://flake8.pycqa.org/)
      * Generate [HTML documentation](http://www.sphinx-doc.org/)
      * Iterate over all python versions and run the NI-FAKE unit tests for each installed version of Python

1. To clean everything and start fresh

        tox -e clean


Running the system tests
------------------------

**[`nimi-python`](https://github.com/ni/nimi-python)** includes system tests that exercise the Python modules against the real driver runtimes. Our CI includes invoking [`nimibot`](https://github.com/ni/nimi-python/wiki/nimibot-System-Test-machine) to run these tests for you on PRs pending admin approval.

But it is recommended that during development you run the system tests locally, especially if the areas of the code affected by your changes may impact interaction with the driver runtimes.

In order to run the **[nimi-python](https://github.com/ni/nimi-python)** system tests locally:

### Install the corresponding driver runtimes.

Download and install the latest versions for the supported driver runtimes from [ni.com](http://www.ni.com/downloads/ni-drivers/):
* NI-DCPower
* NI-Digital Pattern Driver
* NI-DMM
* NI-FGEN
* NI-SCOPE
* NI-SWITCH
* NI Switch Executive

NI-ModInst and NI-TClk are included with the above, they have no separate installers.

### Install build artifacts

After you have successfully built **[nimi-python](https://github.com/ni/nimi-python)**, install the locally built PyPI packages using PyPI:

    find generated | grep \.whl | xargs sudo python3 -m pip install -U

Once the Python bindings are installed, run the system tests for the desired driver. For example:

    pytest src/nidmm/system_tests

You can also use ``tox`` to run the system tests for the desired driver, *using all installed Python versions*. For example:

    tox -c generated\nidmm\tox-system-tests.ini


Contributing
------------

After you've verified that you can successfully build and run system tests for
**[`nimi-python`](https://github.com/ni/nimi-python)**, you may
begin contributing to to the project.

1. If applicable, write a failing test for the new feature / bugfix.
    * If you are modifying the code generator, write new [NI-FAKE](src/nifake/tests) unit
      tests. If the new functionality requires changes to [metadata](src/nifake/metadata),
      apply those to NI-FAKE.
    * If you are modifying driver-specific metadata, write new
      [system tests](src/nidmm/system_tests).
1. Make your change.
1. Verify all tests, including the new ones, pass.
1. Update CHANGELOG.md for customer-visible changes.
    * If the change applies to all generated driver bindings, put the change into the **ALL** section
    * If it only applies to a single driver binding, put the change in the section associated with that driver
    * DO NOT MENTION: Internal-only changes like refactors or test improvements.
1. Commit modifications to generated files.
1. On GitHub, send a New pull request to the main repository's master branch. GitHub
   pull requests are the expected method of code collaboration on this project.


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

(taken from [developercertificate.org](http://developercertificate.org/))

See [LICENSE](https://github.com/ni/nimi-python/blob/master/LICENSE) for details about
how **[`nimi-python`](https://github.com/ni/nimi-python)** is licensed.


