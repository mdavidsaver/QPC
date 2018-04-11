TOP=../..

include $(TOP)/configure/CONFIG
#-----------------------------------------------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================================================================


#=============================================================================
# Build an IOC support library
LIBRARY_IOC += vacSupport

#-----------------------------------------------------------------------------
# Install database definition files into <top>/dbd
#DBD += devXXX.dbd


DBDINC += vsRecord
#DBDINC += $(VACUUM)/dbd/digitelRecord
vacSupport_SRCS += vsRecord.c
#vacSupport_SRCS += $(VACUUM)/vacApp/src/digitelRecord.c


#-----------------------------------------------------------------------------
# The following are compiled and added to the Support library
vacSupport_SRCS += devVacSen.c
#vacSupport_SRCS += $(VACUUM)/vacApp/src/devDigitelPump.c

vacSupport_SRCS += devTelevac.c

vacSupport_LIBS += asyn
vacSupport_LIBS += $(EPICS_BASE_IOC_LIBS)
#
#==============================================================================


#=============================================================================
# Build an ioc application <name>
PROD_IOC = vac

#-----------------------------------------------------------------------------
# <name>.dbd and <name>VX.dbd will be created and installed
DBD += vac.dbd

vac_DBD += base.dbd
vac_DBD += $(ASYN)/asyn.dbd
vac_DBD += vsRecord.dbd
vac_DBD += $(VACUUM)/dbd/digitelRecord.dbd
vac_DBD += devVacSen.dbd
vac_DBD += $(VACUUM)/dbd/devDigitelPump.dbd
vac_DBD += devTelevac.dbd


# example_registerRecordDeviceDriver.cpp derives from example.dbd
vac_SRCS += vac_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
vac_SRCS_DEFAULT += vacMain.cpp

# Link in the code from the support library
vac_LIBS += vac vacSupport

# Finally link to the EPICS Base libraries
vac_LIBS += asyn
vac_LIBS += $(EPICS_BASE_IOC_LIBS)


#
#==============================================================================

include $(TOP)/configure/RULES
#------------------------------------------------------------------------------
#  ADD RULES AFTER THIS LINE

