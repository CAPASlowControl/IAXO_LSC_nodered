from pymodbus.client import ModbusSerialClient
from pymodbus.framer import FramerType
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

client = ModbusSerialClient( port = "/dev/ID1_CT_MOIS",  framer = FramerType.RTU, baudrate =  9600, bytesize = 8, parity = 'N', stopbits =  1)
client.connect()

#result = client.read_holding_registers(address=0, count=64 )# , slave=1)
result = client.read_input_registers(address=0, count=64) #, slave=1)
#print(result.isError())
#print(result.registers)
registers= result.registers

print("Measuring Value (ppmV)")
MeasppmV = client.convert_from_registers( registers[0:2], data_type = client.DATATYPE.FLOAT32 )
print(MeasppmV)

print("Measuring Value (ppmW)")
MeasppmW = client.convert_from_registers( registers[8:10], data_type = client.DATATYPE.FLOAT32 )
print(MeasppmW)

print("DewPoint (ºC)")
DewPoint = client.convert_from_registers( registers[10:12], data_type = client.DATATYPE.FLOAT32 )
print(DewPoint)



print("System Status")
SysStat = registers[20]
SysStat_str =  {0: "Normal", 1: "Check Function", 2: "Maintenance Required", 3: "Out of Specification", 4: "Failure"}
print( SysStat,":", SysStat_str[SysStat] )

print("Sensor Status")
SensStat = registers[23]
SensStat_str =  {0: "Normal", 1: "Sensor Check", 2: "Not Clean"}
print( SensStat,":", SensStat_str[SensStat] )

client.close()

