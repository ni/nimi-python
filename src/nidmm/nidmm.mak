

include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

# nidmm has been chosen to represent all the drivers for the purpose
# of getting the version for documentation
module: $(DOCS_DIR)/conf.py

$(DOCS_DIR)/conf.py: $(TEMPLATE_DIR)/conf.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(DOCS_DIR), $(METADATA_DIR))
# Need to signal the top level makefile to run tests again
	$(_hide_cmds)$(call trigger_unit_tests)

include $(BUILD_HELPER_DIR)/rules.mak

