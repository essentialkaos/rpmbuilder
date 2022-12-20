## REGISTRY CONFIGURATION ######################################################

ARG REGISTRY="ghcr.io"

## FINAL IMAGE #################################################################

FROM ${REGISTRY}/essentialkaos/oraclelinux:8

ARG SHELLCHECK_VERSION=0.9.0

ENV CODESPACES=true

# hadolint ignore=DL3031,DL3041
RUN dnf -y -q install https://yum.kaos.st/kaos-repo-latest.el8.noarch.rpm && \
    dnf -y -q install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm && \
    sed -i 's/gpgcheck=1/gpgcheck=1\nmodule_hotfixes=1/g' /etc/yum.repos.d/epel.repo && \
    dnf -y install make wget git xz zsh && \
    wget https://github.com/koalaman/shellcheck/releases/download/v${SHELLCHECK_VERSION}/shellcheck-v${SHELLCHECK_VERSION}.linux.x86_64.tar.xz && \
    tar xf shellcheck-v${SHELLCHECK_VERSION}.linux.x86_64.tar.xz && \
    wget https://andy.one/dotfiles/install.sh && bash install.sh && rm -f install.sh && \
    rm -rf /var/cache/dnf /var/log/dnf.*

WORKDIR /root

ENTRYPOINT ["/usr/bin/zsh"]
