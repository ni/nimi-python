import nirfsg
import numpy as np
import nirfsg.enums
 
# RFSG session create
options = "Simulate=0, DriverSetup=Model:5841"
session  = nirfsg.Session('5841', id_query=False, reset_device=False, options=options)
# session = nirfsg.Session("5841", id_query=False, reset_device=False, options=options)
 
# configure frequency to 1Ghz, power level to -10db and iq rate to 1M
session.configure_rf(
    1e9, # frequency
    -10  # powerLevel
    )
#session.iq_rate = 1e6
session.generation_mode = nirfsg.GenerationMode.CW
 
# Start generation
with session.initiate():
    # Generation context
    input("Press Enter to stop generation")
 
session.close()