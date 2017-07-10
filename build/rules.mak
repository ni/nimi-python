
MODULE_FILES := \
                $(addprefix $(MODULE_DIR)/,$(FILES_TO_GENERATE)) \
                $(addprefix $(MODULE_DIR)/,$(FILES_TO_COPY))

overall_all: unit_test

MKDIR: $(MKDIRECTORIES)

define mkdir_rule
$1:
	$(_hide_cmds)mkdir -p $1
endef
$(foreach d,$(MKDIRECTORIES),$(eval $(call mkdir_rule,$(d))))

$(MODULE_DIR)/%.py: %.py.mako
	@echo Creating $(notdir $@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR))

$(MODULE_DIR)/tests/%.py: %.py.mako
	@echo Creating $(notdir $@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR))

$(MODULE_DIR)/%.py: %.py
	@echo Creating $(notdir $@)
	$(_hide_cmds)cp $< $@

UNIT_TEST_FILES_TO_COPY := $(wildcard $(DRIVER_DIR)/tests/*.py)
UNIT_TEST_FILES := $(addprefix $(UNIT_TEST_DIR)/,$(notdir $(UNIT_TEST_FILES_TO_COPY)))

$(UNIT_TEST_DIR)/%.py: $(DRIVER_DIR)/tests/%.py
	@echo Creating $(notdir $@)
	$(_hide_cmds)cp $< $@

clean:

.PHONY: module unit_tests sdist wheel
$(UNIT_TEST_FILES): $(MODULE_FILES)
module: $(MODULE_FILES)

$(UNIT_TEST_FILES): $(MODULE_FILES)
unit_tests: $(UNIT_TEST_FILES)

$(LOG_DIR)/test_results.log:
	@echo Running unit tests
	$(_hide_cmds)cd $(OUTPUT_DIR) && python3 -m pytest -s > $(LOG_DIR)/test_results.log

$(OUTPUT_DIR)/README.rst: $(ROOT_DIR)/README.rst
	@echo Creating $(notdir $@)
	$(_hide_cmds)cp $< $@

$(OUTPUT_DIR)/setup.py: $(TEMPLATE_DIR)/setup.py.mako
	@echo Creating $(notdir $@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(dir $@), $(METADATA_DIR))

sdist: $(SDIST)
$(SDIST): $(OUTPUT_DIR)/setup.py $(OUTPUT_DIR)/README.rst $(MODULE_FILES) $(LOG_DIR)/test_results.log
	@echo Creating Source distribution
	$(_hide_cmds)cd $(OUTPUT_DIR) && python3 setup.py sdist > $(LOG_DIR)/sdist.log

wheel: $(WHEEL)
$(WHEEL): $(OUTPUT_DIR)/setup.py $(OUTPUT_DIR)/README.rst $(MODULE_FILES) $(LOG_DIR)/test_results.log
	@echo Creating Wheel distribution
	$(_hide_cmds)cd $(OUTPUT_DIR) && python3 setup.py bdist_wheel --universal > $(LOG_DIR)/wheel.log

# From https://stackoverflow.com/questions/16467718/how-to-print-out-a-variable-in-makefile
print-%: ; $(info $(DRIVER): $* is $(flavor $*) variable set to [$($*)]) @true

