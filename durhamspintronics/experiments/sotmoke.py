from durhamspintronics.instruments.ni import pci6034e

def get_frequency():
  input_device = pci6034e()
  print(f'Frequency = {input_device.frequency}')
  return input_device.frequency
