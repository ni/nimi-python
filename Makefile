
ALL_DRIVERS := nifake nidigital nidcpower nidmm nifgen niscope niswitch nimodinst 
DRIVERS ?= $(ALL_DRIVERS)

ROOT_DIR := $(abspath .)
export ROOT_DIR

# build related source files
BUILD_HELPER_DIR := $(ROOT_DIR)/build
export BUILD_HELPER_DIR

BIN_DIR := $(ROOT_DIR)/bin
export BIN_DIR

include $(BUILD_HELPER_DIR)/Makefile

