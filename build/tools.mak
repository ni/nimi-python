# Useful functions

# Traces to console, nicely formatted.
# $1 is the Action, for example: "Generating"
# $2 is a Path.
# Action will be padded on the left so colons align, for readability.
# Path will be turned from absolute to relative, for readability.
define trace_to_console
	@echo "$(shell printf '%15s' $1): $(subst $(CURRENT_DIR)/,,$2)"
endef

# Executes a command, then logs it to $(COMMAND_LOG).
# $1 is the command.
define log_command
	$1
	@echo '$1' >> $(COMMAND_LOG)
endef

# Helper function for running a command with a tracking file
# created/updated upon completion
# $1 is tracking file path
# $2 is command to run
define make_with_tracking_file
	$(_hide_cmds)$(call log_command,touch $1)
	$(_hide_cmds)$(call log_command,rm $1)
	$(_hide_cmds)$(call log_command,$2)
	$(_hide_cmds)$(call log_command,touch $1)
endef


