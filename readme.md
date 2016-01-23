### RPMBuilder

`rpmbuilder` is RPM package build helper

#### Installation

###### From ESSENTIAL KAOS Public repo for RHEL6/CentOS6

```
sudo yum install -y http://release.yum.kaos.io/i386/kaos-repo-6.8-0.el6.noarch.rpm
sudo yum install rpmbuilder
```

Build node:
```
sudo yum install -y http://release.yum.kaos.io/i386/kaos-repo-6.8-0.el6.noarch.rpm
sudo yum install rpmbuilder-node
sudo passwd builder
... change builder user password here
sudo service buildmon start
```

#### Usage

```
Usage: rpmbuilder <spec-file> <options>

Spec file:

  You can define absolute or relative path to spec file. You also can define only spec name (without extension).
  In this case, rpmbuilder try use {name}.spec file for build and try to find {name}.source file and use as 
  sources list.

Source packaging:

  --pack, -p <files>                  Pack specified files to tgz archive with default source name (mergeable)
  --relative-pack, -R                 Use relative path in source archive instead of absolute
  --source-dir, -sd <path>            Path to directory which contains source files specified in spec file
  --source-list, -sl <file>           Path to file which contains list of source files specified in spec file,
                                      and will be packed to tgz archive with default source name
  --dlcache, -dc <path>               Path to directory for downloads caching
  --download, -dl <path>              Download all remote sources to specified directory

  --git <url>                         Fetch sources from Git repository (macro supported)
  --svn <url>                         Fetch sources from SVN repository (macro supported)
  --hg <url>                          Fetch sources from Mercurial repository (macro supported)
  --bzr <url>                         Fetch sources from Bazar repository (macro supported)
  --path, -rp <path>                  Path to directory with sources in repo
  --branch, -rb <name>                Use specified repository branch (macro supported)
  --revision, -rr <name>              Use specified revision
  --tag, -rt <name>                   Use specified tag (macro supported)
  --svn-user, -su <username>          Username for access to svn repository
  --svn-pass, -sp <password>          Password for access to svn repository

  --github, -gh <url>                 Fetch sources from github.com repository by url (macro supported)
  --github, -gh <user>:<project>      Fetch sources from github.com repository by user and project
  --github, -gh <user>/<project>      Fetch sources from github.com repository by user and project
  --bitbucket, -bb <url>              Fetch sources from bitbucket.org repository by url (macro supported)
  --bitbucket, -bb <user>:<project>   Fetch sources from bitbucket.org repository by user and project
  --bitbucket, -bb <user>/<project>   Fetch sources from bitbucket.org repository by user and project
  --launchpad, -lp <url>              Fetch sources from launchpad.net repository by url (macro supported)
  --launchpad, -lp <project-name>     Fetch sources from launchpad.net repository by project name

  Examples:

    rpmbuilder package.spec -sl sources/current -d ~/mypackages
    rpmbuilder package.spec --source-list files.list --dest ~/mypackages
    rpmbuilder package.spec --pack "file1 file2 dir1 dir2 file3"
    rpmbuilder package.spec -p "file1 file2" -p "dir1 dir2 file3" -p file4
    rpmbuilder package.spec --git git://github.com/user/project.git --tag 1.3-12
    rpmbuilder package.spec --git git://github.com/%{vendor}/%{name}.git --tag "v%{version}-%{release}"
    rpmbuilder package.spec --git git://github.com/user/project.git -rb develop
    rpmbuilder package.spec --git git://github.com/user/project.git -rr f8debbfdbebb97f5d0ee2218edf1425ac219cff5
    rpmbuilder package.spec -bb user:project
    rpmbuilder package.spec --github https://github.com/user/project/

Dependencies install:

  --dep-install, --depinstall, -di     Automatically install necessary packages for build
  --enable-repo, -ER <repo-name>       Enable repositories (mergeable)
  --disable-repo, -DR <repo-name>      Disable repositories (mergeable)

Remote build:

  --parallel, -P                       Parallel build on all build servers in same time
  --remote, -r                         Build rpm package on remote server
  --remote, -r user:pass@host          Build rpm package on the remote server with specified host, user and pass
  --remote, -r <file>                  Build rpm package on the remote servers listed in specified file
  --host, -hh <host>                   Remote host ip or domain name
  --user, -uu <user>                   Remote host user
  --pass, -pp <password>               Password for specified user
  --key, -kk <file>                    Path to private key for specified user

  Examples:

    rpmbuilder package.spec --remote -ru builder -rp mypass -rh 127.0.0.1
    rpmbuilder package.spec -r builder:mypass@127.0.0.1 -i ~/.ssh/id_dsa
    rpmbuilder package.spec --remote ~/servers.list --key ~/.ssh/id_dsa

Build options:

  --no-build, -nb                      Don't execute any build stages
  --no-clean, -nc                      Don't remove source files and spec file after build
  --no-deps, -nd                       Don't verify build dependencies
  --no-binary, -nr                     Don't build binary packages
  --no-source, -ns                     Don't build source package
  --arch, -a <arch>                    Override target arch for build
  --qa-rpaths="<value>,<value>,..."    Ignoring rpaths check

Arguments passing:

  --with, -w <params>                  Pass conditional parameters into a rpmbuild (mergeable)
  --without, -W <params>               Pass conditional parameters into a rpmbuild (mergeable)
  --define, -D "<macro>"               Define MACRO with value (exist macro will be not redefined)

  Examples:

    rpmbuilder package.spec --with ssl --with ldap
    rpmbuilder package.spec -w ssl -W ldap
    rpmbuilder package.spec --with "ssl ldap"
    rpmbuilder package.spec --define="_tmp_dir /some/dir"

  More info: http://rpm5.org/docs/api/conditionalbuilds.html

Spec validation:

  --no-lint, -0                        Don't check spec file before package build
  --strict, -1                         Don't build package if linter found errors in spec file
  --pedantic, -2                       Don't build package if linter found errors or warnings in spec file

Other:

  --sign, -s                           Sign package after build
  --dest, --dest-dir, -d <path>        Save builded packages to specified directory
  --keep-log, -kl                      Save build log after unsuccessful build
  --bump, -b                           Bump release in spec file after successful package build
  --bump-comment, -bc <comment>        Comment which will be added while release bump
  --tmp <path>                         Path to temporary directory
  --verbose, -V                        Verbose output
  --help, --usage, -h                  Show this help message
  --ver, --version, -v                 Show information about version
```

#### License

[EKOL](https://essentialkaos.com/ekol)
