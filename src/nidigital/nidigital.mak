

include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)

# Add custom types to copy
CUSTOM_TYPES_TO_COPY += \
    history_ram_cycle_information.py \

include $(BUILD_HELPER_DIR)/rules.mak

