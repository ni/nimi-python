

OUTPUT_DIR := bin/$(DRIVER)
MODULE_DIR := $(OUTPUT_DIR)/$(DRIVER)
UNIT_TEST_DIR := $(MODULE_DIR)/tests
DRIVER_DIR := src/$(DRIVER)
METADATA_DIR := $(DRIVER_DIR)/metadata

FILES_TO_GENERATE := attributes.py enums.py library.py session.py errors.py __init__.py
FILES_TO_COPY := ctypes_types.py python_types.py

MODULE_FILES := \
                $(addprefix $(MODULE_DIR)/,$(FILES_TO_GENERATE)) \
                $(addprefix $(MODULE_DIR)/,$(FILES_TO_COPY))

all: module unit_test

VPATH = $(DRIVER_DIR)/templates build/templates

$(MODULE_DIR):
	mkdir -p $@

$(MODULE_DIR)/%.py: %.py.mako $(MODULE_DIR)
	@echo Creating $(notdir $@)
	@python3 -m build --template $< --dest-dir $(MODULE_DIR) --metadata $(METADATA_DIR)

$(MODULE_DIR)/%.py: %.py
	@echo Creating $(notdir $@)
	@cp $< $@

UNIT_TEST_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/tests/*.py)
UNIT_TEST_FILES := $(addprefix $(UNIT_TEST_DIR)/,$(notdir $(UNIT_TEST_FILES_TO_COPY)))

$(UNIT_TEST_DIR):
	mkdir -p $@

$(UNIT_TEST_DIR)/%.py: $(DRIVER_DIR)/tests/%.py $(UNIT_TEST_DIR)
	@echo Creating $(notdir $@)
	@cp $< $@

clean:
module: $(MODULE_FILES)
unit_test: module $(UNIT_TEST_FILES)
	cd $(OUTPUT_DIR) && python3 -m pytest -s


