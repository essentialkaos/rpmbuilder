
########################################################################################

export PATH := shellcheck-latest:$(PATH)

########################################################################################

IMAGE_REPO ?= essentialkaos/rpmbuilder
PUB_KEY_FILE ?= ~/.ssh/buildnode.pub

########################################################################################

.DEFAULT_GOAL := help
.PHONY = install uninstall images images-base images-node run-nodes get-shellcheck test help

########################################################################################

get-shellcheck: ## Download and install the latest version of shellcheck (requires sudo)
ifneq ($(shell id -u), 0)
	@echo -e "\e[31m▲ This target requires sudo\e[0m"
	@exit 1
endif

	@echo -e "\e[1;36;49m\nDownloading shellcheck…\n\e[0m"
	curl -#L -o shellcheck-latest.linux.x86_64.tar.xz https://github.com/koalaman/shellcheck/releases/download/latest/shellcheck-latest.linux.x86_64.tar.xz
	tar xf shellcheck-latest.linux.x86_64.tar.xz
	rm -f shellcheck-latest.linux.x86_64.tar.xz
	cp shellcheck-latest/shellcheck /usr/bin/shellcheck || :
	rm -rf shellcheck-latest

	@echo -e "\e[1;32;49m\nShellcheck successfully downloaded and installed!\n\e[0m"

test: ## Run shellcheck tests
	shellcheck SOURCES/rpmbuilder SOURCES/libexec/*.shx
	shellcheck SOURCES/rpmunbuilder
	shellcheck SOURCES/buildmon
	shellcheck SOURCES/initenv
	shellcheck SOURCES/nodeinfo
	shellcheck .docker/entrypoint
	shellcheck .docker/node-entrypoint
	shellcheck rpmbuilder-docker

install: ## Install app to current system (requires sudo)
ifneq ($(shell id -u), 0)
	@echo -e "\e[31m▲ This target requires sudo\e[0m"
	@exit 1
endif

	@echo -e "\e[1;36;49m\nInstalling app…\n\e[0m"
	install -dDm 755 /usr/libexec/rpmbuilder
	install -pm 755 SOURCES/rpmbuilder /usr/bin/
	install -pm 755 SOURCES/rpmunbuilder /usr/bin/
	install -pm 644 SOURCES/libexec/* /usr/libexec/rpmbuilder/

	@echo -e "\e[1;32;49m\nApp successfully installed!\n\e[0m"

uninstall: ## Uninstall app from current system (requires sudo)
ifneq ($(shell id -u), 0)
	@echo -e "\e[31m▲ This target requires sudo\e[0m"
	@exit 1
endif

	@echo -e "\e[1;36;49m\nUninstalling app…\n\e[0m"
	rm -f /usr/bin/rpmbuilder || :
	rm -f /usr/bin/rpmunbuilder || :
	rm -rf /usr/libexec/rpmbuilder || :

	@echo -e "\e[1;32;49m\nApp successfully uninstalled!\n\e[0m"

build-images: build-images-base build-images-node ## Build all docker images

build-images-base: ## Build base docker images
	docker build -f .docker/centos7.docker -t $(IMAGE_REPO):centos7 .
	docker build -f .docker/ol7.docker -t $(IMAGE_REPO):ol7 .
	docker build -f .docker/ol8.docker -t $(IMAGE_REPO):ol8 .
	docker build -f .docker/ol9.docker -t $(IMAGE_REPO):ol9 .

build-images-node: ## Build node docker images
	docker build -f .docker/node-centos7.docker -t $(IMAGE_REPO):node-centos7 .
	docker build -f .docker/node-ol7.docker -t $(IMAGE_REPO):node-ol7 .
	docker build -f .docker/node-ol8.docker -t $(IMAGE_REPO):node-ol8 .
	docker build -f .docker/node-ol9.docker -t $(IMAGE_REPO):node-ol9 .

push-images: push-images-base push-images-node ## Push all images to registry

push-images-base: ## Push base images to registry
ifneq (,$(wildcard ~/.docker/config.json))
	docker push $(IMAGE_REPO):centos7
	docker push $(IMAGE_REPO):ol7
	docker push $(IMAGE_REPO):ol8
	docker push $(IMAGE_REPO):ol9
endif

push-images-node: ## Push node images to registry
ifneq (,$(wildcard ~/.docker/config.json))
	docker push $(IMAGE_REPO):node-centos7
	docker push $(IMAGE_REPO):node-ol7
	docker push $(IMAGE_REPO):node-ol8
	docker push $(IMAGE_REPO):node-ol9
endif

run-nodes: ## Run nodes containers
ifneq (,$(wildcard $(PUB_KEY_FILE)))
	docker run -e PUB_KEY="$(shell cat $(PUB_KEY_FILE))" -p 2037:2037 -d $(IMAGE_REPO):node-ol7
	docker run -e PUB_KEY="$(shell cat $(PUB_KEY_FILE))" -p 2038:2038 -d $(IMAGE_REPO):node-ol8
	docker run -e PUB_KEY="$(shell cat $(PUB_KEY_FILE))" -p 2039:2039 -d $(IMAGE_REPO):node-ol9
endif

help: ## Show this info
	@echo -e '\nSupported targets:\n'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[33m%-18s\033[0m %s\n", $$1, $$2}'
	@echo -e ''

################################################################################
