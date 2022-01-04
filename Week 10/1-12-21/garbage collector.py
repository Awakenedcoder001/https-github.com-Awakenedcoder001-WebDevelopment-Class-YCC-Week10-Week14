import gc
print(gc.isenabled())

gc.disable()
print(f"")

print(f"The garbage collector is enabled: {gc.isenabled}")