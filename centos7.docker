FROM centos:7

RUN yum -y -q install https://yum.kaos.st/7/release/x86_64/kaos-repo-9.1-0.el7.noarch.rpm && \
    yum -y -q install epel-release centos-release-scl && \
    yum -y -q clean metadata && \
    yum -y -q update

RUN yum -y -q install sudo make which rpmbuilder

RUN curl -o /usr/local/bin/gosu -sSL "https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64" && \
		chmod +x /usr/local/bin/gosu

COPY SOURCES/conf/builder.sudoers /etc/sudoers.d/rpmbuilder
COPY SOURCES/conf/rpmmacros_centos7 /home/builder/.rpmmacros
COPY SOURCES/docker-entrypoint /usr/local/bin/docker-entrypoint

RUN chmod +x /usr/local/bin/docker-entrypoint

VOLUME /rpmbuilder
WORKDIR /rpmbuilder

ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]
