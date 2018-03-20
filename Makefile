
ALL_DRIVERS := nifake nidcpower nidmm nifgen niscope niswitch nimodinst
DRIVERS ?= $(ALL_DRIVERS)

ROOT_DIR := $(abspath .)
export ROOT_DIR

# build related source files
BUILD_HELPER_DIR := $(ROOT_DIR)/build
export BUILD_HELPER_DIR

BIN_DIR := $(ROOT_DIR)/bin
export BIN_DIR

MAKE_NUMBER_OF_JOBS ?= 8
export MAKE_NUMBER_OF_JOBS

include $(BUILD_HELPER_DIR)/Makefile

