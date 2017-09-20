# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Python Versioning](http://legacy.python.org/dev/peps/pep-0396/).

## [0.2.0] - 2017-09-20
* #### ALL
  * #### Added
    * Suport for channel-based properties
  * #### Changed
    * Warnings no longer raise an exception
      * Warnings are now added to warnings.warn()
* #### NI-DMM
  * #### Changed
    * Added support for enums with types other than ViInt32 (Fixes [#330](https://github.com/ni/nimi-python/issues/330))
* #### NI-ModInst
  * #### Changed
    * Device index is now on session not attribute. The correct way is now
      ```python
      i = 0
      with nimodinst.Session('nidmm') as session:
          name = session[i].device_name
      ```
* #### NI-Switch
  * #### Added
    * Initial Release

## [0.1.0] - 2017-09-01
* ### NI-DMM
  * #### Added
    * Initial release
* ### NI-ModInst
  * #### Added
    * Initial release


<!--
## [Unreleased]
* #### ALL
  * #### Added
  * #### Changed
  * #### Removed
* #### NI-DMM
  * #### Added
  * #### Changed
  * #### Removed
* #### NI-ModInst
  * #### Added
  * #### Changed
  * #### Removed
* #### NI-Switch
  * #### Added
  * #### Changed
  * #### Removed
-->

