TOP=..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = qpc
# test.dbd will be created and installed
DBD += qpc.dbd

# test.dbd will be made up from these files:
qpc_DBD += base.dbd
qpc_DBD += asyn.dbd
qpc_DBD += drvAsynSerialPort.dbd
qpc_DBD += drvAsynIPPort.dbd
qpc_DBD += calc.dbd
qpc_DBD += stream.dbd

# Add all the support libraries needed by this IOC
qpc_LIBS += stream
qpc_LIBS += asyn
qpc_LIBS += calc
qpc_LIBS += sscan
qpc_LIBS += seq pv

# test_registerRecordDeviceDriver.cpp derives from test.dbd
qpc_SRCS += qpc_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
qpc_SRCS_DEFAULT += testMain.cpp
qpc_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#qpc_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
qpc_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

