OUTPUT_DIR := $(BIN_DIR)/$(DRIVER)
LOG_DIR := $(OUTPUT_DIR)/log
MODULE_DIR := $(OUTPUT_DIR)/$(DRIVER)
UNIT_TEST_DIR := $(MODULE_DIR)/tests
SYSTEM_TEST_DIR := $(OUTPUT_DIR)/system_tests
EXAMPLES_DIR := $(OUTPUT_DIR)/examples
TEMPLATE_DIR := $(BUILD_HELPER_DIR)/templates
TOX_INI := $(OUTPUT_DIR)/tox.ini

TOX_INI := $(OUTPUT_DIR)/tox.ini

DRIVER_DIR := $(ROOT_DIR)/src/$(DRIVER)
METADATA_DIR := $(DRIVER_DIR)/metadata
METADATA_FILES := $(wildcard $(METADATA_DIR)/*.py)

BUILD_HELPER_SCRIPT := $(BUILD_HELPER_DIR)/helper.py

DRIVER_GENERATED_DIR := $(GENERATED_DIR)/$(DRIVER)

DOCS_DIR := $(ROOT_DIR)/docs
DRIVER_DOCS_DIR := $(DOCS_DIR)/$(DRIVER)

VERSION ?= 0.1
WHEEL := $(OUTPUT_DIR)/dist/$(DRIVER)-$(VERSION)-py2.py3-none-any.whl
SDIST := $(OUTPUT_DIR)/dist/$(DRIVER)-$(VERSION).tar.gz

MKDIRECTORIES += \
    $(DRIVER_DOCS_DIR) \
    $(OUTPUT_DIR) \
    $(MODULE_DIR) \
    $(UNIT_TEST_DIR) \
    $(LOG_DIR) \
    $(SYSTEM_TEST_DIR) \
    $(EXAMPLES_DIR) \
    $(DRIVER_GENERATED_DIR) \

VPATH = $(TEMPLATE_DIR)

PYTHON_CMD ?= python3
define GENERATE_SCRIPT
$(PYTHON_CMD) -m build --template $1 --dest-dir $2 --metadata $3 $(if $(PRINT),-v,)
endef

ifeq (,$(PRINT))
_hide_cmds := @
LOG_OUTPUT := >
else
LOG_OUTPUT := | tee
endif

TARGETS := $(filter-out run_unit_tests,$(DEFAULT_TARGETS))

.PHONY:
all: $(TARGETS)

DEFAULT_PY_FILES_TO_GENERATE := \
    attributes.py \
    enums.py \
    library.py \
    library_singleton.py \
    session.py \
    errors.py \
    tests/mock_helper.py \
    __init__.py \

DEFAULT_PY_FILES_TO_COPY := \
    ctypes_types.py \
    python_types.py \

DEFAULT_RST_FILES_TO_GENERATE := \
    session.rst \
    enums.rst \
    attributes.rst \
    functions.rst \
    examples.rst \

# Files for tracking parts of the build
WHEEL_BUILD_DONE := $(LOG_DIR)/wheel_build_done
SDIST_BUILD_DONE := $(LOG_DIR)/sdist_build_done
GENERATED_FILES_COPY_DONE := $(LOG_DIR)/generated_files_copy_done

