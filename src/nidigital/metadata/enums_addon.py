# These dictionaries are applied to the generated enums dictionary at build time
# Any changes to the API should be made here. enums.py is code generated

enums_override_metadata = {
    'PinState': {
        '__str__':"""    if self.name == 'ZERO':
            return str(0)
        elif self.name == 'ONE':
            return str(1)
        elif self.name == 'NOT_A_PIN_STATE':
            return "Not a Pin State"
        elif self.name == 'PIN_STATE_NOT_ACQUIRED':
            return "Pin State Not Acquired"
        else:
            return str(self.name)\n"""
    },
    'WriteStaticPinState': {
        '__str__':"""    if self.name == 'ZERO':
            return str(0)
        elif self.name == 'ONE':
            return str(1)
        else:
            return str(self.name)\n"""
    }
}
