import gc, random, neopixel, machine, math, micropython #webrepl, esp, network, json, os, time, upip

#upip.install("module_name") for modules

micropython.alloc_emergency_exception_buf(100)

gc.collect()
gc.enable()
print()
print()
print(gc.mem_alloc())
print()
print()
print(gc.mem_free())
print()
print()
print('boot_ended')