import ctypes

lib = ctypes.CDLL('/mnt/d/GitHub/nimi-python/libctype_test.so')
#class ViChar(ctypes.c_char):
#    pass
#
#class ViInt32(ctypes.c_long):
#    pass
#
#lib = ctypes.CDLL('/mnt/d/GitHub/nimi-python/libctype_test.so')
#
#lib.take_char_array.argtypes = [ctypes.POINTER(ViChar)]
#lib.take_char_array.restype = ctypes.c_long

#s_string1 = "Testing!"
#b_string1 = s_string1.encode('ascii')
#v_string1 = ctypes.cast(ctypes.create_string_buffer(b_string1), ctypes.POINTER(ViChar))

#r = lib.take_char_array(v_string1)
#print(r)
#
#lib.ivi_dance.argtypes = [ViInt32, ctypes.POINTER(ViChar)]
#lib.ivi_dance.restype = ctypes.c_long
#
#r = lib.ivi_dance(0, None)
#print(r)
#
#buf = ctypes.create_string_buffer(r)
#v_string1 = ctypes.cast(buf, ctypes.POINTER(ViChar))
#
#r = lib.ivi_dance(r, v_string1)
#v_string2 = ctypes.cast(v_string1, ctypes.POINTER(ctypes.c_char))
#b_string2 = v_string2.value
#s_string2 = b_string2.decode('ascii')
#print(s_string2)
#print(type(s_string2))
#print(type(b_string2))
#print(type(v_string2))

ViChar = ctypes.c_char
ViInt32 = ctypes.c_long

lib.take_char_array.argtypes = [ctypes.POINTER(ViChar)]
lib.take_char_array.restype = ViInt32

s_string1 = "Testing!"
b_string1 = s_string1.encode('ascii')
#v_string1 = ctypes.cast(ctypes.create_string_buffer(b_string1), ctypes.POINTER(ViChar))

r = lib.take_char_array(b_string1)
print(r)


lib.ivi_dance.argtypes = [ViInt32, ctypes.POINTER(ViChar)]
lib.ivi_dance.restype = ctypes.c_long

r = lib.ivi_dance(0, None)
print(r)

v_string1 = ctypes.create_string_buffer(r)
#v_string1 = ctypes.cast(buf, ctypes.POINTER(ViChar))

r = lib.ivi_dance(r, v_string1)
#v_string2 = ctypes.cast(v_string1, ctypes.POINTER(ctypes.c_char))
b_string2 = v_string1.value
s_string2 = b_string2.decode('ascii')
print(s_string2)


lib.fixed.argtypes = [ViInt32, ctypes.POINTER(ViChar)] 
lib.fixed.restype = ViInt32

s = 100
v_string1 = ctypes.create_string_buffer(s)
r = lib.fixed(s, v_string1)
b_string3 = v_string1.value
s_string3 = b_string3.decode('ascii')
print(s_string3)
