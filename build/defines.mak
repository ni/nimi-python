OUTPUT_DIR := $(BIN_DIR)/$(DRIVER)
LOG_DIR := $(OUTPUT_DIR)/log
MODULE_DIR := $(OUTPUT_DIR)/$(DRIVER)
UNIT_TEST_DIR := $(MODULE_DIR)/tests
TEMPLATE_DIR := $(BUILD_HELPER_DIR)/templates

DRIVER_DIR := $(ROOT_DIR)/src/$(DRIVER)
METADATA_DIR := $(DRIVER_DIR)/metadata

VERSION ?= 0.1
WHEEL := $(OUTPUT_DIR)/dist/$(DRIVER)-$(VERSION)-py2.py3-none-any.whl
SDIST := $(OUTPUT_DIR)/dist/$(DRIVER)-$(VERSION).tar.gz

MKDIRECTORIES += \
                 $(OUTPUT_DIR) \
                 $(MODULE_DIR) \
                 $(UNIT_TEST_DIR) \
                 $(LOG_DIR) \

VPATH = $(TEMPLATE_DIR)

define GENERATE_SCRIPT
python3 -m build --template $1 --dest-dir $2 --metadata $3 $(if $(PRINT),-v,)
endef

ifeq (,$(PRINT))
_hide_cmds := @
endif

TARGETS := $(filter-out run_unit_tests,$(POSSIBLE_TARGETS))

.PHONY:
all: $(TARGETS)

DEFAULT_FILES_TO_GENERATE := \
                     attributes.py \
                     enums.py \
                     library.py \
                     session.py \
                     errors.py \
                     ctypes_library.py \
                     tests/mock_helper.py \
                     __init__.py \

DEFAULT_FILES_TO_COPY := \
                 ctypes_types.py \
                 python_types.py \


