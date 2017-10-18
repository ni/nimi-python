# Changelog

* [Unreleased](#unreleased)
* [0.3.0](#030---2017-10-13)
* [0.2.0](#020---2017-09-20)
* [0.1.0](#010---2017-09-01)

All notable changes to this project will be documented in this file.

## Unreleased
* ### ALL
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-DMM
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-ModInst
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-Switch
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-DCPower
 * #### Added
 * #### Changed
 * #### Removed
* ### NI-FGEN
 * #### Added
  * Initial release
 * #### Changed
 * #### Removed

## 0.3.0 - 2017-10-13
* ### ALL
  * #### Added
    * Support for ViInt64 (64-bit integers)
  * #### Changed
    * Modified how methods with repeated capabilities are invoked. There's no longer (for example) a "channel_name" input. Instead:
      ```python
      # Sets sequence on channels 0 through 3
      session['0-3'].set_sequence(values, source_delays)
      ```
    * Enum value documentation lists the fully qualified name - this is to allow easy copy/paste
* ### NI-DMM
  * #### Changed
    * Added default values to some parameters.
  * #### Removed
    * Removed methods that aren’t useful in the Python bindings.
* ### NI-SWITCH
  * #### Changed
    * Added default values to some parameters.
  * #### Removed
    * Removed methods that aren’t useful in the Python bindings.
* ### NI-DCPower
  * #### Added
    * Initial release

## 0.2.0 - 2017-09-20
* ### ALL
  * #### Added
    * Suport for channel-based properties
  * #### Changed
    * Warnings no longer raise an exception
      * Warnings are now added to warnings.warn()
* ### NI-DMM
  * #### Changed
    * Added support for enums with types other than ViInt32 (Fixes [#330](https://github.com/ni/nimi-python/issues/330))
* ### NI-ModInst
  * #### Changed
    * Device index is now on session not attribute. The correct way is now
      ```python
      i = 0
      with nimodinst.Session('nidmm') as session:
          name = session[i].device_name
      ```
* ### NI-SWITCH
  * #### Added
    * Initial release

## 0.1.0 - 2017-09-01
* ### NI-DMM
  * #### Added
    * Initial release
* ### NI-ModInst
  * #### Added
    * Initial release

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Python Versioning](http://legacy.python.org/dev/peps/pep-0396/).

<!--
## [Unreleased]
* ### ALL
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-DMM
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-ModInst
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-Switch
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-DCPower
 * #### Added
 * #### Changed
 * #### Removed
* ### NI-FGEN
 * #### Added
 * #### Changed
 * #### Removed
-->

