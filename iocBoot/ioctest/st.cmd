#!../../bin/linux-x86_64/qpc

#< envPaths

epicsEnvSet("EPICS_DB_INCLUDE_PATH", "$(PWD)/../../db:.")
epicsEnvSet("STREAM_PROTOCOL_PATH", "$(PWD)/../../protocol")

## Register all support components
dbLoadDatabase("../../dbd/qpc.dbd",0,0)
qpc_registerRecordDeviceDriver(pdbbase) 

#drvAsynSerialPortConfigure("qpc1","/dev/ttyUSB0",0,0,0)
#asynSetOption("qpc1", -1, "baud", "9600")
#asynSetOption("qpc1", -1, "bits", "8")
#asynSetOption("qpc1", -1, "parity", "none")
#asynSetOption("qpc1", -1, "stop", "1")
#asynSetOption("qpc1", -1, "clocal", "Y")
#asynSetOption("qpc1", -1, "crtscts", "N")

drvAsynIPPortConfigure("qpc1", "192.168.99.15:23", 0, 0, 0)

#asynSetTraceMask("qpc1",0,0x3f)
#asynSetTraceIOMask("qpc1",0,2)

#asynSetTraceMask("qpc1",0,0x29)
#asynSetTraceIOMask("qpc1",0,2)

# A controller
dbLoadRecords("digitelQPCController.template","QPCBUS=Ethernet,QPC=TST:QPC1,port=qpc1")
# 4x channels of this controller
# TODO: autosave for HV, pump size, etc.
dbLoadRecords("digitelQpcIonp.template", "QPCBUS=Ethernet,device=TST:CH1,port=qpc1,unit=01,SPLY=1,SIZE=500,HV=3000,spon=1.0E-8,spoff=2.0E-8")
dbLoadRecords("digitelQpcIonp.template", "QPCBUS=Ethernet,device=TST:CH2,port=qpc1,unit=02,SPLY=2,SIZE=500,HV=3000,spon=1.0E-8,spoff=2.0E-8")
dbLoadRecords("digitelQpcIonp.template", "QPCBUS=Ethernet,device=TST:CH3,port=qpc1,unit=03,SPLY=3,SIZE=500,HV=3000,spon=1.0E-8,spoff=2.0E-8")
dbLoadRecords("digitelQpcIonp.template", "QPCBUS=Ethernet,device=TST:CH4,port=qpc1,unit=04,SPLY=4,SIZE=500,HV=3000,spon=1.0E-8,spoff=2.0E-8")

iocInit()
