OUTPUT_DIR := $(GENERATED_DIR)/$(DRIVER)
LOG_DIR := $(OUTPUT_DIR)/log
MODULE_DIR := $(OUTPUT_DIR)/$(DRIVER)
UNIT_TEST_DIR := $(MODULE_DIR)/unit_tests
TEMPLATE_DIR := $(BUILD_HELPER_DIR)/templates
TOX_INI := $(OUTPUT_DIR)/tox.ini

TOX_INI := $(OUTPUT_DIR)/tox.ini

DRIVER_DIR := $(ROOT_DIR)/src/$(DRIVER)
METADATA_DIR := $(DRIVER_DIR)/metadata
METADATA_FILES := $(wildcard $(METADATA_DIR)/*.py)

BUILD_HELPER_SCRIPTS := $(wildcard $(BUILD_HELPER_DIR)/helper/*)

DRIVER_DOCS_DIR := $(DOCS_DIR)/$(DRIVER)

MKDIRECTORIES += \
    $(DRIVER_DOCS_DIR) \
    $(OUTPUT_DIR) \
    $(MODULE_DIR) \
    $(UNIT_TEST_DIR) \
    $(LOG_DIR) \

VPATH = $(TEMPLATE_DIR)

PYTHON_CMD ?= python
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
    _attributes.py \
    enums.py \
    _library.py \
    _library_singleton.py \
    session.py \
    errors.py \
    unit_tests/_converters_test.py \
    unit_tests/_mock_helper.py \
    unit_tests/_matchers.py \
    __init__.py \
    _converters.py \
    VERSION \

DEFAULT_PY_FILES_TO_COPY := \
    _visatype.py \

DEFAULT_RST_FILES_TO_GENERATE := \
    enums.rst \
    examples.rst \
    installation.inc \
    status.inc \
    class.rst \
    toc.inc \
    errors.rst \
    rep_caps.rst \

# Files for tracking parts of the build
WHEEL_BUILD_DONE := $(LOG_DIR)/wheel_build_done
SDIST_BUILD_DONE := $(LOG_DIR)/sdist_build_done
GENERATED_FILES_COPY_DONE := $(LOG_DIR)/generated_files_copy_done

