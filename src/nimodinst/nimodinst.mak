

include $(BUILD_HELPER_DIR)/defines.mak

# We want everything but enums.py
FILES_TO_GENERATE := $(filter-out enums.py,$(DEFAULT_FILES_TO_GENERATE))

FILES_TO_COPY := $(DEFAULT_FILES_TO_COPY)

include $(BUILD_HELPER_DIR)/rules.mak

# We need to override the default rule for generating session since we have
# a specialized copy for ModInst
$(MODULE_DIR)/session.py: $(DRIVER_DIR)/templates/session.py.mako
	@echo Creating $(notdir $@)
	$(_hide_cmds)$(call GENERATE_SCRIPT, $<, $(MODULE_DIR), $(METADATA_DIR))

