Contributing to nimi-python
===========================

Contributions to **[nimi-python](https://github.com/ni/nimi-python)** are welcome from all!

**[nimi-python](https://github.com/ni/nimi-python)** is managed via [Git](https://git-scm.com), with the canonical
upstream repository hosted on [GitHub](http://developercertificate.org/).

**[nimi-python](https://github.com/ni/nimi-python)** follows a pull request model for development.
If you wish to contribute, you will need to create a GitHub account, fork this project,
push a branch with your changes to your project, and then submit a pull request.

See [GitHub's official documentation](https://help.github.com/articles/using-pull-requests/)
for more details.

Getting Started
---------------

To contribute to this project, it is recommended that you follow these steps:

### System Requirements

In order to build **[nimi-python](https://github.com/ni/nimi-python)**, you must have the
following installed:

* [Python](https://www.python.org/downloads/)
    - If you're on Windows (Not Windows Subsystem for Linux)
        - Install at least one Python 3.x x64 - anything between 3.4 and 3.8 should work
        - Optional - 32 bit versions
        - Ensure pip support is installed for all versions
        - Install paths can either be in the appropriate Program Files for the bitness, or c:\pythonXY for 64 bit and c:\pythonXY-32 for 32 bit
    - Add ``python Install Path`` and ``python Install Path``\Scripts to Windows path
    - Copy ``python Install Path``\python.exe to ``python Install Path``\python3.exe

* [GNU Make](https://www.gnu.org/software/make/)
    - If you're on Windows 10 (using Windows Subsystem for Linux)
        - Install and enable [Windows Subsystem for Linux](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)
        - Install make

                sudo apt-get install make

    - If you're on Windows 7, 8 or 10 (not using WSL):
        - [Install mingw (msys-base)](https://osdn.net/projects/mingw/).
        - Add ``mingw Install Path``\msys\1.0\bin to Windows path.

    - If you're on macOS
        - Install [Xcode](https://itunes.apple.com/us/app/xcode/id497799835?mt=12)
        - Install command line developer tools

* [PyPI](https://pip.pypa.io/en/latest/installation/)

        sudo apt-get install python3-pip (Linux)
        sudo pip3 install pip --upgrade (Windows)

* Additional Python Modules (install using [PyPI](https://pypi.python.org/pypi))

        sudo pip install pytest tox tox-globinterpreter --upgrade

In order to run **[nimi-python](https://github.com/ni/nimi-python)** System Tests:

* Install corresponding driver runtimes.
    * Download the latest installers for NI-DMM, NI-SCOPE, NI-DCPower, NI-SWITCH, NI-FGEN, NI Switch Executive
    from [ni.com](http://www.ni.com/downloads/ni-drivers/)
    * NI-ModInst is included as part of these runtimes.
    * NI-TClk is included as part of NI-SCOPE and NI-FGEN.

### How to build

1. Fork the repository on GitHub and clone it to your local system.
1. On a terminal, CD to the **[nimi-python](https://github.com/ni/nimi-python)** root
   directory. Then type:

    1. python3 -m tox -e build_test,codegen,installers,flake8,docs,pkg
    1. tox

   The first line will

   * For each driver
      * Generate Python bindings
      * Generate [RST documentation](http://www.sphinx-doc.org/)
      * Create installer packages
   * Run [flake8](http://flake8.pycqa.org/)
   * Generate [HTML documentation](http://www.sphinx-doc.org/)

   The second line will iterate over all python versions and run the NI-FAKE unit tests
   for each version that is installed and registered using `tox --scan`

1. To clean everything and start fresh, type:

         python3 -m tox -e clean

### Running System Tests

System tests exercise the Python bindings. After you have successfully built
**[nimi-python](https://github.com/ni/nimi-python)**, install the locally built PyPI
packages using PyPI. For example:

    python3 -m pip install -U generated/nidmm/dist/nidmm-0.1.0.dev4-py2.py3-none-any.whl

You can install all locally built packages in one fell swoop using the following command.
This will work on Unix-based systems including Windows Subsystem for Linux.

    find generated | grep \.whl | xargs sudo python3 -m pip install -U

Then run the system tests for the desired driver, for example:

    pytest src/nidmm/system_tests

You can also use tox to run the system tests using all installed 64 bit Python versions

    tox -e py27-system_tests,py34-system_tests,py35-system_tests,py36-system_tests

You can also use tox to run the system tests using all installed 32 bit Python versions

    tox --32 -e py27-system_tests,py34-system_tests,py35-system_tests,py36-system_tests


Contributing
------------

After you've verified that you can successfully build and run system tests for
**[nimi-python](https://github.com/ni/nimi-python)**, you may fork the repository and
begin contributing to to the project.

1. Write a failing test for the new feature / bugfix.
    * If you are modifying the code generator, write new [NI-FAKE](src/nifake/tests) unit
      tests. If the new functionality requires changes to [metadata](src/nifake/metadata),
      apply those to NI-FAKE.
    * If you are modifying driver-specific metadata, write new
      [system tests](src/nidmm/system_tests).
1. Make your change.
1. Verify all tests, including the new ones, pass.
1. Update CHANGELOG.md if applicable.
    * If the change applies to all generated driver bindings, put the change into the **ALL** section
    * If it only applies to a single driver binding, put the change in the section associated with that driver
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
how **[nimi-python](https://github.com/ni/nimi-python)** is licensed.


