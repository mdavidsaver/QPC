TOP = ../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

# overrides from configure/CONFIG_COMMON in Base
INSTALL_DB = $(INSTALL_LOCATION)/protocol

# Copy all protocol files into data directory
DB += $(patsubst ../%, %, $(wildcard ../*.proto))

include $(TOP)/configure/RULES
