[33mcommit 34c8a79051c7037254ae4498dc77e1e4175c9c82[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m)[m
Merge: c0a5b524 0e4bf09b
Author: iadamjee <imran.adamjee@ni.com>
Date:   Wed May 26 12:53:37 2021 -0500

    Merge branch 'master' of https://github.com/imranadamjee/nimi-python

[33mcommit c0a5b524902247e682938b497d0107da8bfb39d1[m
Author: iadamjee <imran.adamjee@ni.com>
Date:   Thu Apr 22 14:42:59 2021 -0500

    Brand update, Issue #1490
    
    * As per the issue, updated to NI in the README's.
    * GitHub wiki was good from the start.
    * Updated the copyright to the recommendation from ni-central.

[33mcommit c631e3d8d034ac8c2ec8224363b78d5fd67b82af[m[33m ([m[1;31mupstream/master[m[33m)[m
Author: Marcos <marcoskirsch@users.noreply.github.com>
Date:   Tue May 25 15:45:50 2021 -0500

    New PAT with with updated format (#1611)
    
    * New PAT with with updated format
    
    GitHub said:
    
    """
    We noticed your personal access token, nimi-bot system tests,
    has an outdated format and was used to access the GitHub API on
    May 19th, 2021 at 17:14 (UTC) with a user-agent header of
    Java/1.8.0_144.
    
    We recently updated the format of our API authentication tokens,
    providing additional security benefits to all our customers.
    
    In order to benefit from this new format, please regenerate your
    personal access token, nimi-bot system tests, using the button below.
    """
    
    * Don't store PAT in git

[33mcommit 2844f476a46eed05fa140685ec7c1c2f02d63015[m
Author: luisgomes252 <80292064+luisgomes252@users.noreply.github.com>
Date:   Fri May 14 16:24:24 2021 -0500

    US1198692: Instrument-based repeated capabilities for attributes (#1599)
    
    * Add support for instrument-based repeated capabilities
    
    * Replace channel_based and instrument_based bools with a supported_rep_caps array
    
    * Update metadata from official export (after removing unrelated metadata content that hasn't yetmigrated to this repo)
    
    * Address miscellaneous code review feedback
    
    * Address additional code review feedback

[33mcommit 5b736ab471a4b8fa161dfb0139020ac12af1fa61[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Thu May 13 12:44:45 2021 -0500

    Replace the Sphinx library call `add_stylesheet` with `add_css_file` (#1603)

[33mcommit e6dab64c1091cbec98ebe4f8902d4aa11702db41[m
Author: luisgomes252 <80292064+luisgomes252@users.noreply.github.com>
Date:   Tue May 11 11:33:37 2021 -0500

    Use explicit metadata attribute to avoid adding repeated capability in a parameter for which its name would otherwise require it, but for which its python_name might not (e.g. get_channel_names) (#1601)

[33mcommit 1537484b16952be6592649c55ade2929805d019e[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Mon May 10 10:14:01 2021 -0500

    Update "Driver Version Tested Against" (#1597)

[33mcommit 753c21fd87a6fbe7db76d9dfdf4a28a246633f80[m
Author: luisgomes252 <80292064+luisgomes252@users.noreply.github.com>
Date:   Mon May 10 09:50:27 2021 -0500

    US1198694: add `nidcpower.Session.get_channel_names()` (#1578)
    
    * Ignore files generated during system test execution
    
    * Add get_channel_names test
    
    * get_channel_names implementation (plus some additional metadata changes that hadn't yet been codegen'd)
    
    * Update changelog
    
    * Address code review feedback (https://github.com/ni/nimi-python/pull/1578)
    
    * Fix whitespace
    
    * Some additional code review feedback from Marcos
    
    * wait for a different PR to update .gitignore
    
    * Restore blank line
    
    * Take into account python_name parameter overrides when determining repeated capabilities
    
    * Address some additional feedback from Shreyas: 1. always create `python_name_override` and 2. avoid mixing camel-cased and snake-cased parameter names when comparing them
    
    * Add test for python_name override
    
    * Add tests for snake_case / camel_case conversions
    
    * Revert changes to _add_is_repeated_capability() based on code review feedback. I will fix the incorrect repeated capability for the parameter names later, by adding  metadata is_repeated_capability tags to the get_channel_names parameters.

[33mcommit 0e4bf09bb1c84bf97a22223a7af7cd1896c6ab5a[m[33m ([m[1;31morigin/master[m[33m, [m[1;31morigin/HEAD[m[33m)[m
Author: iadamjee <imran.adamjee@ni.com>
Date:   Thu Apr 22 14:42:59 2021 -0500

    Brand update, Issue #1490
    
    * As per the issue, updated to NI in the README's.
    * GitHub wiki was good from the start.
    * Updated the copyright to the recommendation from ni-central.

[33mcommit 661c2f327220255eb6c72fd7b0395309bf149e4e[m
Author: Erik Crank <76133060+ni-erikcrank@users.noreply.github.com>
Date:   Wed Apr 21 13:16:40 2021 -0500

    Add support for repeated capabilities on methods that support independent channels (#1589)
    
    * added try/except for function not found
    
    * refined error message
    
    * add repeated capabilities
    
    * removed get_channel_names
    
    * fixed reference to create_advanced_sequence_step
    
    * added new error class;add function to catch errors
    
    * replaced fake function name fred
    
    * add unit test for library too old error
    
    * code cleanup
    
    Co-authored-by: Erik Crank <null>

[33mcommit f9979a75967ba7e018e1974fc41534c5931b8e16[m
Author: Erik Crank <76133060+ni-erikcrank@users.noreply.github.com>
Date:   Tue Apr 20 11:16:19 2021 -0500

    Improve error message when function not found in driver runtime (#1581)
    
    * added try/except for function not found
    
    * refined error message
    
    * added new error class;add function to catch errors
    
    * replaced fake function name fred
    
    * add unit test for library too old error
    
    * code cleanup
    
    Co-authored-by: Erik Crank <null>

[33mcommit 4de3cf2e46ba092dff1c2b4fe2f3c201fa2ff9ff[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Mon Apr 12 17:04:39 2021 -0500

    API parity with NI-DCPower 20.7.0 (#1580)
    
    * Update nidcpower Python bindings to support NI-DCPower 20.7.0 driver Runtime
    
    * Update CHANGELOG.md with list of properties and methods.

[33mcommit 70d383137685640858b667a55689d68c6ca22531[m
Author: Erik Crank <76133060+ni-erikcrank@users.noreply.github.com>
Date:   Mon Apr 5 10:21:41 2021 -0500

    regenerated files (#1577)
    
    Co-authored-by: Erik Crank <null>

[33mcommit 2342da240a73c841a473f898749f762b0ee66df7[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Tue Mar 30 15:21:02 2021 -0500

     Post release changes for 1.3.3 (#1571)
    
    * Update version in config_addon.py
    
    * Update generated files
    
    * Update examples.rst
    
    * Update CHANGELOG.md

[33mcommit edac3327b1dd8fe0741cafc8453dd54f8d064019[m
Author: Erik Crank <76133060+ni-erikcrank@users.noreply.github.com>
Date:   Tue Mar 30 12:27:55 2021 -0500

    Modified repeated capabilities converter to support resource names (#1576)
    
    * updated converter to support resource names
    
    * update comment;add another unit test
    
    Co-authored-by: Erik Crank <null>

[33mcommit f56dafb87c50808bc9fa018d3403f5b74c5a15df[m
Author: Erik Crank <76133060+ni-erikcrank@users.noreply.github.com>
Date:   Thu Mar 25 13:21:26 2021 -0500

    replace backslash path separators (#1574)
    
    Co-authored-by: Erik Crank <null>

[33mcommit c796a6df972d8f5edb335a93121280c83de483b9[m[33m ([m[1;33mtag: 1.3.3[m[33m)[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Tue Mar 2 10:38:08 2021 -0600

    Release nidigital 1.0.0 and 1.3.3 of other modules (#1569)
    
    * Update CHANGELOG.md
    
    * Update latest_runtime_version_tested_against to 20.6.0, in nidigital
    
    * Update versions in config_addon.py and LATEST_RELEASE
    
    * Update generated files with new version
    
    * Remove "Unreleased" from CHANGELOG.md

[33mcommit d1c627043d5b8d1481743cc4d66ff9a7edcb7193[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Fri Feb 26 00:40:16 2021 -0600

    Fix code-generated examples.rst files (#1568)

[33mcommit b40dda91bd06b0009c6ebfe0a7c7edb858b082b8[m
Author: gfisher-NI <68872082+gfisher-NI@users.noreply.github.com>
Date:   Wed Feb 24 16:03:47 2021 -0600

    Create nitclk_niscope_synchronize_with_trigger.py (#1540)
    
    * Create nitclk_master_trigger.py
    
    This is a short example showing how to configure two FGEN cards with a master trigger configuration.
    
    * Update nitclk_master_trigger.py
    
    * Update nitclk_master_trigger.py
    
    * Update nitclk_master_trigger.py
    
    * Update CHANGELOG.md
    
    * Update examples.rst
    
    * Delete nitclk_configure.py
    
    * Update and rename nitclk_master_trigger.py to nitclk_synchronize_trigger.py
    
    * Update CHANGELOG.md
    
    * Update CHANGELOG.md
    
    * Update nitclk_synchronize_trigger.py
    
    * Update nitclk_synchronize_trigger.py
    
    * Update CHANGELOG.md
    
    * Update examples.rst
    
    * Rename nitclk_synchronize_trigger.py to nitclk_niscope_synchronize_with_trigger.py
    
    * Update examples.rst
    
    * Update CHANGELOG.md

[33mcommit 99d6c3690e37d92dedea3851aebd21a303ff260a[m
Author: gfisher-NI <68872082+gfisher-NI@users.noreply.github.com>
Date:   Wed Feb 24 13:26:21 2021 -0600

    Create nifgen_trigger.py (#1541)
    
    * Create nifgen_trigger_example.py
    
    * Update nifgen_trigger_example.py
    
    * Update nifgen_trigger_example.py
    
    Fixed the "expected 2 blank lines" issues in the CI test.
    
    * Update nifgen_trigger_example.py
    
    * Update CHANGELOG.md
    
    * Update examples.rst
    
    * Update and rename nifgen_trigger_example.py to nifgen_trigger.py
    
    * Update CHANGELOG.md
    
    * Update CHANGELOG.md
    
    * Update CHANGELOG.md
    
    * Update CHANGELOG.md

[33mcommit bcdd44bc72e0cdbbc0c6431f023228ea50aa21b3[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Sat Feb 20 15:19:41 2021 -0600

    Remove enum values (constant values in underlying driver) from nidigital API reference documentation (#1567)

[33mcommit b6e36a70b511f31322d24b9af4861cb885f05771[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Fri Feb 19 14:03:15 2021 -0600

    Fix MinGW link in Contributing guide

[33mcommit 78f115b057b51fa81594413c5fb72578a40f5e82[m
Author: ni-jxie <77028785+ni-jxie@users.noreply.github.com>
Date:   Wed Feb 17 18:14:14 2021 -0600

    Update string representation of PinState and WriteStaticPinState enum… (#1551)
    
    * Update string representation of PinState and WriteStaticPinState enums to be more user-friendly
    
    * Update test_history_ram_cycle_information_string()
    
    * Instead of adding _str_ method, key off a new field pretty-name
    
    * Remove pretty_name for values that does not need it
    
    * Removing unnecessary call to str()
    
    * Instead of nested if statement, using a dictionary

[33mcommit 06d0ec16e939b3fdb398ce065b75c2cd625e3778[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Wed Feb 17 17:58:27 2021 -0600

    Release version of docs link to release version of example files (#1566)

[33mcommit d447109cbcecd023777e145c6c98748ea5cbe8de[m
Author: Shreyas Bethur <48041236+sbethur@users.noreply.github.com>
Date:   Fri Feb 12 15:02:52 2021 -0600

    Add support for frequency counter measurement mode in nidigital (#1565)

[33mcommit 0f44906c11dbd6c465e0a912391730d65f01d8f5[m
Author: Phil Hindman <77023184+phindman@users.noreply.github.com>
Date:   Fri Feb 12 10:15:11 2021 -0600

    Replace private functions with public Fancy functions (#1564)

[33mcommit 2f5a6eff1e66f6c69600655c5c05946e1a7ba96e[m
Author: Phil Hindman <77023184+phindman@users.noreply.github.com>
Date:   Wed Feb 10 11:30:31 2021 -0600

    Add docs for WriteStaticPinState enum values (#1562)

[33mcommit c602e8b10a6780b04f2512b9379775b85156d0e8[m
Author: ni-jxie <77028785+ni-jxie@users.noreply.github.com>
Date:   Wed Feb 10 10:12:58 2021 -0600

    Delete nidigital_do_nothing example (#1548)
    
    * Delete nidigital_do_nothing example
    
    * Update examples.rst too

[33mcommit 55c86088480107ea8dc8896c7a9828e4e068b6b8[m
Author: ni-jxie <77028785+ni-jxie@users.noreply.github.com>
Date:   Tue Feb 9 17:42:45 2021 -0600

    Fix issue #1558 (#1559)

[33mcommit d02f1c6784c1d12544578237ba94a423dde39351[m
Author: ni-jxie <77028785+ni-jxie@users.noreply.github.com>
Date:   Tue Feb 9 17:41:56 2021 -0600

    Create nidigital_configure_time_set_and_voltage_levels example (#1547)
    
    * Create nidigital_burst_with_programmatic_configuration example
    
    * Incorporate feedbacks from burst example
    
    * Fix simulate argument parsing
    
    * Restructure directory layout
    
    * Update file path that was missed in previous commit
    
    * Rename example + addressing Shreyas comment
    
    * rename example in example.rst too
    
    * Remove default values for example params and fix some formatting issues

[33mcommit 4972fab48a3d5dfc4a45f9011340de72eb0c4eab[m
Author: Phil Hindman <77023184+phindman@users.noreply.github.com>
Date:   Tue Feb 9 17:36:22 2021 -0600

    Replace private functions with public ones in the selected_function docs (#1560)

[33mcommit a1c356a022c36d8d63e825ce2621a6ee39376bf4[m
Author: Phil Hindman <77023184+phindman@users.noreply.github.com>
Date:   Tue Feb 9 17:35:01 2021 -0600

    Make get_pattern_name and get_time_set_name private (#1561)
    
    * Make get_pattern_name and get_time_set_name private
    
    * Remove _get_pattern_name and _get_time_set_name from system_tests

[33mcommit c559a44e95fe1a766e6f6a7f81171d1afc544f8d[m
Author: Phil Hindman <77023184+phindman@users.noreply.github.com>
Date:   Tue Feb 9 08:53:22 2021 -0600

    Add API reference documentation for NI-Digital (#1552)
    
    * Add API reference documentation for NI-Digital
    
    * Add generated files that were updated due to previous commit to the repo
    
    * Address feedback from Shreyas
    
    * Address more feedback
    
    * Add carat character
    * Fix how burst_pattern appears in doc strings
    * Refer to repeated capabilities
    * Copy doc strings to addon metadata
    
    * Fix docs for get_pin_results_pin_information and add docs for 'pin state not acquired'
    
    * More documentation updates
    
    * Add docs for SoftwareTrigger enum (copied from ExportSignal enum)
    
    * Address more feedback:
    
    * Fix references to some enum values (e.g. STROBE2)
    * waveformName --> waveform_name
    * niDigital_Initiate --> initiate
    * Remove docs for internal functions (GetPatternName and GetTimeSetName)
    * Delete unnecessary description in GetPatternPinList
    * Fix reference to NIDIGITAL_ATTR_START_LABEL
    * Add docs for 'reset' and 'reset device'
    
    * Add self test docs
    
    * Add more information to self test docs
    
    * Remove extraneous 'not'
    
    * Add docs for write_source_waveform_site_unique
    
    * Fix typo: nane --> name

[33mcommit f45d1c45d86e476ad7c3b1bbc3e51bf1eb4bd5cc[m
Author: ni-jxie <77028785+ni-jxie@users.noreply.github.com>
Date:   Thu Feb 4 15:52:42 2021 -0600

    Create nidigital_burst_with_start_trigger example (#1544)
    
    * Create nidigital_burst_with_start_trigger example
    
    * Replacing 6570 with 6571 and National Instruments with NI. Instead of snake-casing DPE generated file, use the DPE default filename style instead
    
    * Addressing Shreyas's comments round 1
    
    * Addressing Shreyas's comments round 2
    
    * Combine if statements and update help description according to Marcos' comment
    
    * Update example directory structure
    
    * Rename example subfolder
    
    * Fix up examples.rst by recursively looking through the examples folder

[33mcommit 9492b770c4a7aa81bff5df1acd153aca8a653323[m
Author: nisundar <63660074+nisundar@users.noreply.github.com>
Date:   Thu Feb 4 15:29:26 2021 -0600

    Python metadata changes for NI-DCPower 20.6 release (#1546)
    
    * Python metadata changes for NI DCPower 20.6 release
    
    * Updates from latest nimi-python plugin export
    
    Manually reverting unintended 'channel_based' attribute changes
    
    * Adding nimi-python generated docs and seesions.py file in response to changes to src/nidcpower/
    
    * Update "Driver Version Tested Against"
    
    * Update CHANGELOG.md
