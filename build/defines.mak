OUTPUT_DIR := $(ROOT_DIR)/bin/$(DRIVER)
MODULE_DIR := $(OUTPUT_DIR)/$(DRIVER)
UNIT_TEST_DIR := $(MODULE_DIR)/tests

TEMPLATE_DIR := $(ROOT_DIR)/build/templates

DRIVER_DIR := $(ROOT_DIR)/src/$(DRIVER)
METADATA_DIR := $(DRIVER_DIR)/metadata

MKDIRECTORIES += \
                 $(OUTPUT_DIR) \
                 $(MODULE_DIR) \
                 $(UNIT_TEST_DIR) \

VPATH = $(TEMPLATE_DIR)

.PHONY
all: 


