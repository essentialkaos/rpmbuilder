
########################################################################################

export PATH := shellcheck-latest:$(PATH)

########################################################################################

IMAGE_REPO ?= essentialkaos/rpmbuilder
PUB_KEY_FILE ?= ~/.ssh/buildnode.pub

########################################################################################

.DEFAULT_GOAL := help
.PHONY = images images-base images-node run-nodes get-shellcheck test help

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

images: images-base images-node ## Build all docker images

images-base: ## Build base docker images
	docker build -f .docker/centos7.docker -t $(IMAGE_REPO):centos7 .
	docker build -f .docker/ol7.docker -t $(IMAGE_REPO):ol7 .
	docker build -f .docker/ol8.docker -t $(IMAGE_REPO):ol8 .
	docker build -f .docker/ol9.docker -t $(IMAGE_REPO):ol9 .

images-node: ## Build node docker images
	docker build -f .docker/node-centos7.docker -t $(IMAGE_REPO):node-centos7 .
	docker build -f .docker/node-ol7.docker -t $(IMAGE_REPO):node-ol7 .
	docker build -f .docker/node-ol8.docker -t $(IMAGE_REPO):node-ol8 .
	docker build -f .docker/node-ol9.docker -t $(IMAGE_REPO):node-ol9 .

run-nodes: ## Run nodes containers
ifneq (,$(wildcard $(PUB_KEY_FILE)))
	docker run -e PUB_KEY="$(shell cat $(PUB_KEY_FILE))" -p 2037:2037 -d $(IMAGE_REPO):node-ol7
	docker run -e PUB_KEY="$(shell cat $(PUB_KEY_FILE))" -p 2038:2038 -d $(IMAGE_REPO):node-ol8
	docker run -e PUB_KEY="$(shell cat $(PUB_KEY_FILE))" -p 2039:2039 -d $(IMAGE_REPO):node-ol9
endif

help: ## Show this info
	@echo -e '\nSupported targets:\n'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[33m%-15s\033[0m %s\n", $$1, $$2}'
	@echo -e ''

################################################################################
