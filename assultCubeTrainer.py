from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()

process = rwm.get_process_by_name('ac_client.exe')
process.open()


process.write(process.get_pointer(0x50F4F4, offsets=[0xF8]), 9999)
process.write(process.get_pointer(0x50F4F4, offsets=[0x378, 0x14, 0x0]), 9999)
process.write(process.get_pointer(0x50F4F4, offsets=[0x128]), 9999)
process.write(process.get_pointer(0x50F4F4, offsets=[0x13C]), 9999)
process.write(process.get_pointer(0x50F4F4, offsets=[0x114]), 9999)
process.write(process.get_pointer(0x50F4F4, offsets=[0x158]), 9999)
process.write(process.get_pointer(0x50F4F4, offsets=[0xFC]), 9999)
process.write(process.get_pointer(0x510CDC, offsets=[]), 200)

process.close()