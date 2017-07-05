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

define GENERATE_SCRIPT
python3 -m build --template $1 --dest-dir $2 --metadata $3 $(if $(PRINT),-v,)
endef

ifeq (,$(PRINT))
_hide_cmds := @
endif

ifeq (,$(MAKECMDGOALS))
TARGETS := $(POSSIBLE_TARGETS)
endif

.PHONY:
all: $(TARGETS)


