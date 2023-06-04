

include $(BUILD_HELPER_DIR)/defines.mak

MODULE_FILES_TO_GENERATE := $(DEFAULT_PY_FILES_TO_GENERATE)

MODULE_FILES_TO_COPY := $(DEFAULT_PY_FILES_TO_COPY)

# We are not building any nifake documentation
# RST_FILES_TO_GENERATE := $(DEFAULT_RST_FILES_TO_GENERATE)
# SPHINX_CONF_PY := $(DEFAULT_SPHINX_CONF_PY)

CUSTOM_TYPES_TO_COPY += \
    custom_struct.py \
    custom_struct_typedef.py \
    custom_struct_nested_typedef.py \

include $(BUILD_HELPER_DIR)/rules.mak

