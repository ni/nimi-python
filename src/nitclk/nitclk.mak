

include $(BUILD_HELPER_DIR)/defines.mak

# Eventually we will get back to this as we add/update more templates
# MODULE_FILES_TO_GENERATE := $(filter-out enums.py,$(DEFAULT_PY_FILES_TO_GENERATE))
MODULE_FILES_TO_GENERATE := $(filter-out session.py enums.py,$(DEFAULT_PY_FILES_TO_GENERATE))

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(filter-out enums.rst,$(DEFAULT_RST_FILES_TO_GENERATE))


include $(BUILD_HELPER_DIR)/rules.mak

# We need to override the default rule for generating session since we have
# a specialized copy for TClk
$(MODULE_DIR)/session.py: $(DRIVER_DIR)/templates/session.py.mako $(BUILD_HELPER_SCRIPTS) $(METADATA_FILES)
	$(call trace_to_console, "Generating",$@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(MODULE_DIR), $(METADATA_DIR))

