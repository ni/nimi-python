@echo off
cls
echo * Testing with USB-5133
c:\python27\python scope_perf_test.py -n dev1
c:\python34\python scope_perf_test.py -n dev1
c:\python35\python scope_perf_test.py -n dev1
"c:\program files\python36\python" scope_perf_test.py -n dev1
echo * Testing with PXIe-5122
c:\python27\python scope_perf_test.py -n PXI1Slot2
c:\python34\python scope_perf_test.py -n PXI1Slot2
c:\python35\python scope_perf_test.py -n PXI1Slot2
"c:\program files\python36\python" scope_perf_test.py -n PXI1Slot2
