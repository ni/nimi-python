import nifgen
import nitclk
import time

with nifgen.Session('PXI1Slot12', [0,1]) as dev1, nifgen.Session('PXI1Slot16', [0,1]) as dev2:
    dev_list = [dev1, dev2]
    for dev in dev_list:
        dev.start_trigger_type = nifgen.StartTriggerType.TRIG_NONE
        dev.output_mode = nifgen.OutputMode.FUNC
        dev.configure_standard_waveform(waveform=nifgen.Waveform.SINE, amplitude=1.0, frequency=10000, dc_offset=0.0, start_phase=0.0)
        
    dev1.start_trigger_type = nifgen.StartTriggerType.SOFTWARE_EDGE
    dev1.digital_edge_start_trigger_edge = nifgen.StartTriggerDigitalEdgeEdge.RISING
    
    nitclk.configure_for_homogeneous_triggers(dev_list)
    nitclk.synchronize(dev_list, 200e-9) 
    nitclk.initiate(dev_list)

    dev1.send_software_edge_trigger(nifgen.Trigger.START)
    time.sleep(1)
