# This file was generated
<%
config            = template_parameters['metadata'].config
files_to_generate = config['files_to_generate']
module_name       = config['module_name']
%>

$(OUTPUT_DIR)/${module_name}:
	mkdir --parents $(OUTPUT_DIR)/${module_name}

% for f in files_to_generate:
TARGETS += $(OUTPUT_DIR)/${module_name}/${f}

$(OUTPUT_DIR)/${module_name}/${f}: $(GENERATOR_SCRIPT) $(METADATA_FILES_${module_name}) $(OUTPUT_DIR)/${module_name} $(TEMPLATE_FOLDER)/${f}.mako
	@echo Generating ${module_name}/${f}
	@$(GENERATOR_COMMAND) --template $(TEMPLATE_FOLDER)/${f}.mako --driver ${module_name} --dest-dir $(OUTPUT_DIR)/${module_name}

% endfor


