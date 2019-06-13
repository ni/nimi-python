# In alphabetical order except put nifake first and nimodinst last
# - nifake first to get the most code generator coverage
# - nimodinst last so that the version from nimodinst is used for any global versions (docs/conf.py)
ALL_DRIVERS := nifake nitclk nidcpower nidigital nidmm nifgen niscope niswitch nise nimodinst
DRIVERS ?= $(ALL_DRIVERS)

ROOT_DIR := $(abspath .)
export ROOT_DIR

# build related source files
BUILD_HELPER_DIR := $(ROOT_DIR)/build
export BUILD_HELPER_DIR

BIN_DIR := $(ROOT_DIR)/bin
export BIN_DIR

include $(BUILD_HELPER_DIR)/Makefile

