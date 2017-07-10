
ALL_DRIVERS := nidmm nimodinst
DRIVERS ?= $(ALL_DRIVERS)

ROOT_DIR := $(abspath .)
export ROOT_DIR

BUILD_DIR := $(ROOT_DIR)/build
export BUILD_DIR


include $(BUILD_DIR)/Makefile

