
########################################################################################

export PATH := shellcheck-latest:$(PATH)

########################################################################################

.DEFAULT_GOAL := help
.PHONY = test help

########################################################################################

get-shellcheck: ## Download latest version of shellcheck
	wget https://storage.googleapis.com/shellcheck/shellcheck-latest.linux.x86_64.tar.xz
	tar xf shellcheck-latest.linux.x86_64.tar.xz

test: ## Run shellcheck tests
	shellcheck SOURCES/rpmbuilder SOURCES/libexec/*.shx
	shellcheck SOURCES/rpmunbuilder
	shellcheck SOURCES/buildmon
	shellcheck SOURCES/initenv
	shellcheck SOURCES/nodeinfo
	shellcheck .docker/entrypoint
	shellcheck .docker/node-entrypoint
	shellcheck rpmbuilder-docker

help: ## Show this info
	@echo -e '\nSupported targets:\n'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[33m%-12s\033[0m %s\n", $$1, $$2}'
	@echo -e ''

################################################################################