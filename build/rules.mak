
MODULE_FILES := \
                $(addprefix $(MODULE_DIR)/,$(FILES_TO_GENERATE)) \
                $(addprefix $(MODULE_DIR)/,$(FILES_TO_COPY))

overall_all: unit_test


MKDIR:
	mkdir -p $(MKDIRECTORIES)

$(MODULE_DIR)/%.py: %.py.mako MKDIR
	@echo Creating $(notdir $@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(MODULE_DIR), $(METADATA_DIR))

$(MODULE_DIR)/%.py: %.py
	@echo Creating $(notdir $@)
	$(_hide_cmds)cp $< $@

UNIT_TEST_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/tests/*.py)
UNIT_TEST_FILES := $(addprefix $(UNIT_TEST_DIR)/,$(notdir $(UNIT_TEST_FILES_TO_COPY)))

$(UNIT_TEST_DIR)/%.py: $(DRIVER_DIR)/tests/%.py MKDIR
	@echo Creating $(notdir $@)
	$(_hide_cmds)cp $< $@

clean:

module: $(MODULE_FILES)
unit_tests: module $(UNIT_TEST_FILES)
run_unit_tests: unit_tests
	cd $(OUTPUT_DIR) && python3 -m pytest -s


