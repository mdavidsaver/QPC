TOP=../..

ifdef EPICS_HOST_ARCH

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# Create and install (or just install)
# databases, templates, substitutions like this
DB += digitelQpc.template
DB += digitelQpcIonp.template
DB += digitelQpcIonpSps.template
DB += digitelQpcTsp.template
DB += digitelQpcTspDummy.template
DB += digitelQpcIonpGroup.template
DB += digitelQpcTspGroup.template
DB += dummyIonp.template
DB += digitelQPCController.template
DB += vacuum-gamma-ion-pump.template
#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE


else

include $(TOP)/config/CONFIG_APP
include $(TOP)/config/RULES_ARCHS

endif
