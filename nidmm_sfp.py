import nimodinst
import nidmm
import pyforms
from pyforms            import BaseWidget
from pyforms.Controls   import ControlCombo

class SFP(BaseWidget):
    def __init__(self):
        super(SFP, self).__init__('NI-DMM SFP')
        self._devices = ControlCombo('Device')
        
        with nimodinst.Session('nidmm') as session:
            dev_name = session.device_name
            dev_model = session.device_model
            self._devices.add_item('{0} ({1}'.format(dev_name, dev_model), dev_name)
            
            
#Execute the application
if __name__ == "__main__":   pyforms.start_app(SFP)
            
