<p align="center"><a href="#readme"><img src="https://gh.kaos.st/rpmbuilder.svg"/></a></p>

<p align="center">
  <a href="https://kaos.sh/w/rpmbuilder/ci"><img src="https://kaos.sh/w/rpmbuilder/ci.svg" alt="GitHub Actions CI Status" /></a>
  <a href="#license"><img src="https://gh.kaos.st/apache2.svg"></a>
</p>

<p align="center"><a href="#usage-demo">Usage demo</a> • <a href="#installation">Installation</a> • <a href="#tips">Tips</a> • <a href="#usage">Usage</a> • <a href="#build-status">Build Status</a> • <a href="#contributing">Contributing</a> • <a href="#license">License</a></p>

<br/>

`rpmbuilder` is RPM package build helper.

### Usage demo

https://github.com/essentialkaos/rpmbuilder/assets/182020/d0ae6d9c-663e-46cf-a3f3-2c0fa25c97a3

### Installation

#### From [ESSENTIAL KAOS Public Repository](https://pkgs.kaos.st)

```bash
sudo yum install -y https://pkgs.kaos.st/kaos-repo-latest.el$(grep 'CPE_NAME' /etc/os-release | tr -d '"' | cut -d':' -f5).noarch.rpm
sudo yum install rpmbuilder
```

Build node:

```bash
sudo yum install -y https://pkgs.kaos.st/kaos-repo-latest.el$(grep 'CPE_NAME' /etc/os-release | tr -d '"' | cut -d':' -f5).noarch.rpm
sudo yum install rpmbuilder-node
```

#### Using Makefile and Git

```bash
git clone https://kaos.sh/rpmbuilder.git
cd rpmbuilder
sudo make install
```

#### Using Docker

We provide a big variety of Docker images available on [GitHub Container Registry](https://kaos.sh/p/rpmbuilder) and [Docker Hub](http://kaos.sh/d/rpmbuilder).

<details><summary><b>Official images</b></summary><p>

Basic images:

- `ghcr.io/essentialkaos/rpmbuilder:centos7` (_CentOS 7_)
- `ghcr.io/essentialkaos/rpmbuilder:ol7` (_OracleLinux 7_)
- `ghcr.io/essentialkaos/rpmbuilder:ol8` (_OracleLinux 8_)
- `ghcr.io/essentialkaos/rpmbuilder:ol9` (_OracleLinux 9_)
- `essentialkaos/rpmbuilder:centos7` (_CentOS 7_) **`[Not Recommended]`**
- `essentialkaos/rpmbuilder:ol7` (_OracleLinux 7_) **`[Not Recommended]`**
- `essentialkaos/rpmbuilder:ol8` (_OracleLinux 8_) **`[Not Recommended]`**
- `essentialkaos/rpmbuilder:ol9` (_OracleLinux 9_) **`[Not Recommended]`**

Build node images:

- `ghcr.io/essentialkaos/rpmbuilder:node-centos7` (_CentOS 7_ | Port: `2027`)
- `ghcr.io/essentialkaos/rpmbuilder:node-ol7` (_OracleLinux 7_ | Port: `2037`)
- `ghcr.io/essentialkaos/rpmbuilder:node-ol8` (_OracleLinux 8_ | Port: `2038`)
- `ghcr.io/essentialkaos/rpmbuilder:node-ol9` (_OracleLinux 9_ | Port: `2039`)
- `essentialkaos/rpmbuilder:node-centos7` (_CentOS 7_ | Port: `2027`) **`[Not Recommended]`**
- `essentialkaos/rpmbuilder:node-ol7` (_OracleLinux 7_ | Port: `2037`) **`[Not Recommended]`**
- `essentialkaos/rpmbuilder:node-ol8` (_OracleLinux 8_ | Port: `2038`) **`[Not Recommended]`**
- `essentialkaos/rpmbuilder:node-ol9` (_OracleLinux 9_ | Port: `2039`) **`[Not Recommended]`**

</p></details>

Package build using base image:

```bash
# Download and install rpmbuilder-docker script
curl -fL# -o rpmbuilder-docker https://kaos.sh/rpmbuilder/rpmbuilder-docker
chmod +x rpmbuilder-docker
sudo mv rpmbuilder-docker /usr/bin/

# Pull rpmbuilder image based on OracleLinux 8
docker pull ghcr.io/essentialkaos/rpmbuilder:ol8
export IMAGE=ghcr.io/essentialkaos/rpmbuilder:ol8

# Build package locally
cd my-package-dir
rpmbuilder-docker my-package.spec

# Build package using build nodes
rpmbuilder-docker my-package.spec -r buildnode-ol7.acme.corp:2022 -r buildnode-ol8.acme.corp:2022 -k $(base64 -w0 ~/.ssh/buildnode)
```

Package build using build node image:

```bash
docker pull ghcr.io/essentialkaos/rpmbuilder:node-ol8
docker run -e PUB_KEY="$(cat ~/.ssh/buildnode.pub)" -p 2038:2038 -d ghcr.io/essentialkaos/rpmbuilder:node-ol8

cd my-package-dir

# Using local version of rpmbuilder (if you are use RHEL, Alma, Rocky, CentOS…)
rpmbuilder my-package.spec -r builder@localhost:2038 -k ~/.ssh/buildnode

# With docker helper script (any Linux distro or macOS)
rpmbuilder-docker my-package.spec -r builder@localhost:2038 -k $(base64 -w0 ~/.ssh/buildnode)
```

You can bootstrap your own build farm using Docker and `rpmbuilder-farm` script:

```bash
curl -fL# -o rpmbuilder-farm https://kaos.sh/rpmbuilder/rpmbuilder-farm
chmod +x rpmbuilder-farm
sudo mv rpmbuilder-farm /usr/bin/

# Install farm script
sudo rpmbuilder-farm install

# Create user bob and add public key
sudo farm add-user bob

# Start all containers for user bob
sudo farm start bob
```

<p align="center">
  <img src="https://gh.kaos.st/rpmbuilder-farm.png"  alt="rpmbuilder-farm preview" />
</p>

### Tips

* You could define rpmbuilder options inside your specs ([example](https://github.com/essentialkaos/kaos-repo/blob/develop/specs/libnut/libnut.spec#L3-L4)). It very helpful for determining information about external sources.
* If you have a big bunch of default options, you can define them in the preferences file. [More info](https://github.com/essentialkaos/rpmbuilder/wiki/Preferences-file).
* Since version 2.5.0 rpmbuilder provides automatic checksum generation feature. [More info](https://github.com/essentialkaos/rpmbuilder/wiki/Automatic-SHA-512-checksum-generation).

### Usage

```
Usage: rpmbuilder {spec-file} {options}

Spec file:

  You can define absolute or relative path to spec file. You also can define only spec name (without extension).
  In this case, rpmbuilder try use {name}.spec file for build and try to find {name}.source file and use as
  sources list.

Source packaging:

  --pack, -p files                     Pack specified files to archive with default source name (mergeable)
  --relative-pack, -R                  Use relative path in source archive instead of absolute
  --source-dir, -sd path               Path to a directory which contains source files specified in spec file
  --source-list, -sl file              Path to file which contains a list of source files specified in spec file
  --dlcache, -dc dir                   Path to a directory for downloads caching
  --download, -dl dir                  Download all remote sources to a specified directory
  --no-validate, -nv                   Don't validate sources

  --git url                            Fetch sources from Git repository
  --svn url                            Fetch sources from SVN repository
  --hg url                             Fetch sources from Mercurial repository
  --bzr url                            Fetch sources from Bazaar repository
  --path, -rp path                     Path to a directory with sources in repository
  --branch, -rb branch                 Use specified repository branch
  --revision, -rr rev                  Use specified revision
  --tag, -rt tag                       Use specified tag
  --svn-user, -su username             Username for access to SVN repository
  --svn-pass, -sp password             Password for access to SVN repository

┌ --github, -gh url                    Fetch sources from github.com repository by url
│ --github, -gh user:project           Fetch sources from github.com repository by user and project
└ --github, -gh user/project           Fetch sources from github.com repository by user and project
┌ --bitbucket, -bb url                 Fetch sources from bitbucket.org repository by url
│ --bitbucket, -bb user:project        Fetch sources from bitbucket.org repository by user and project
└ --bitbucket, -bb user/project        Fetch sources from bitbucket.org repository by user and project
┌ --launchpad, -lp url                 Fetch sources from launchpad.net repository by url
└ --launchpad, -lp project-name        Fetch sources from launchpad.net repository by project name

  --gopack, -G url                     Fetch and pack golang sources using gopack

  Examples:

    rpmbuilder package.spec -sl sources/current -d ~/mypackages
    rpmbuilder package.spec --source-list files.list --dest ~/mypackages
    rpmbuilder package.spec --pack "file1 file2 dir1 dir2 file3"
    rpmbuilder package.spec -p "file1 file2" -p "dir1 dir2 file3" -p file4
    rpmbuilder package.spec --git git://github.com/user/project.git --tag 1.3-12
    rpmbuilder package.spec --git git://github.com/user/project.git -rb develop
    rpmbuilder package.spec --git git://github.com/user/project.git -rr f8debbfdbebb97f5d0ee2218edf1425ac219cff5
    rpmbuilder package.spec -bb user:project
    rpmbuilder package.spec --github https://github.com/user/project/
    rpmbuilder package.spec --gopack github.com/user/project --tag v1.2.3

Dependencies install:

  --install, -I                        Install build dependencies before build process
  --install-latest, -IL                Install the latest versions of build dependencies before build process
  --enable-repo, -ER repo-name         Enable repositories (mergeable)
  --disable-repo, -DR repo-name        Disable repositories (mergeable)
  --exclude-package, -EX package       Exclude package by name or glob (mergeable)

Remote build:

  --parallel, -P                       Parallel build on all build nodes in the same time (tmux is required)
┌ --remote, -r user:pass@host:port     Build rpm package on the remote node with specified host, username and password (mergeable)
└ --remote, -r file                    Build rpm package on the remote nodes listed in specified file
┌ --key, -k file                       Path to the private key for specified user
└ --key, -k data                       Base64-encoded private key for specified user
  --node, -N index-or-name             Node index or name from the file with build nodes
  --attach, -A                         Attach to parallel build session in tmux

  Examples:

    rpmbuilder package.spec -r builder@192.168.1.100 -r builder@192.168.1.101 -k ~/.ssh/id_rsa
    rpmbuilder package.spec -r builder:mypass@127.0.0.1:2022~i386 -k ~/.ssh/id_ed25519
    rpmbuilder package.spec --remote ~/buildnodes.list --key ~/.ssh/id_ed25519
    rpmbuilder package.spec --remote builder@127.0.0.1:5001 --key $(base64 -w0 ~/.ssh/id_ed25519)
    rpmbuilder package.spec --parallel --remote ~/buildnodes.list --node 1,2

Build options:

  --no-build, -NB                      Don't execute any build stages
  --no-clean, -NC                      Don't remove source files and spec file after build
  --no-deps, -ND                       Don't verify build dependencies
  --no-binary, -NR                     Don't build binary packages
  --no-source, -NS                     Don't build source package
  --arch, -a arch                      Override target arch for a build
  --qa-rpaths "<value>,<value>,..."    Ignoring rpaths check

Arguments passing:

  --with, -w param                     Pass conditional parameters into a rpmbuild (mergeable)
  --without, -W param                  Pass conditional parameters into a rpmbuild (mergeable)
  --define, -D "macro=value"           Define MACRO with value (exist macro will be not redefined) (mergeable)

  Examples:

    rpmbuilder package.spec --with ssl --with ldap
    rpmbuilder package.spec -w ssl -w static -W ldap
    rpmbuilder package.spec --with "ssl ldap"
    rpmbuilder package.spec --define "install_dir=/some/dir" --define "service_user=someone"

  More info: https://kaos.sh/rpmbuilder/w/Conditional-Builds

Spec validation:

  --no-lint, -0                        Don't check spec file before package build
  --strict, -1                         Don't build package if perfecto found major problems in spec file
  --pedantic, -2                       Don't build package if perfecto found minor problems in spec file
  --perfect, -3                        Don't build package if perfecto found any problems in spec file

Other:

  --sign, -s                           Sign package after build
  --dest, -d dir                       Save built packages to a specified directory
  --keep-log, -kl                      Save build log after an unsuccessful build
  --bump, -b                           Bump release in spec file after a successful build
  --bump-comment, -bc comment          Comment which will be added while release bump
  --tmp dir                            Path to a temporary directory (default: /var/tmp)
  --verbose, -V                        Verbose output
  --no-color, -nc                      Disable colors in output
  --help, -h                           Show this help message
  --version, -v                        Show information about version
```

### Build Status

| Branch | Status |
|--------|--------|
| `master` | [![CI](https://kaos.sh/w/rpmbuilder/ci.svg?branch=master)](https://kaos.sh/w/rpmbuilder/ci?query=branch:master) |
| `develop` | [![CI](https://kaos.sh/w/rpmbuilder/ci.svg?branch=master)](https://kaos.sh/w/rpmbuilder/ci?query=branch:develop) |

### Contributing

Before contributing to this project please read our [Contributing Guidelines](https://github.com/essentialkaos/contributing-guidelines#contributing-guidelines).

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
