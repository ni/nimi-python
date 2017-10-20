#!/usr/bin/python

import nimodinst

with nimodinst.Session('') as session:
    if len(session) > 0:
        print("%d items" % len(session))
        print("{: >20} {: >15} {: >10}".format('Name', 'Model', 'S/N'))
    for d in session:
        print("{: >20} {: >15} {: >10}".format(d.device_name, d.device_model, d.serial_number))


