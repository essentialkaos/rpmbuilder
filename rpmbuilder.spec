################################################################################

%global crc_check pushd ../SOURCES ; sha512sum -c %{SOURCE100} ; popd

################################################################################

Summary:    RPM package build helper
Name:       rpmbuilder
Version:    3.4.2
Release:    0%{?dist}
License:    Apache License, Version 2.0
Group:      Development/Tools
URL:        https://kaos.sh/rpmbuilder

Source0:    https://source.kaos.st/%{name}/%{name}-%{version}.tar.bz2

Source100:  checksum.sha512

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:   rpm rpm-build rpmdevtools spec-builddep yum-utils
Requires:   sshpass coreutils gawk tmux perfecto

Provides:   %{name} = %{version}-%{release}

################################################################################

%description
RPM package build helper.

################################################################################

%prep
%crc_check
%autosetup

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -dm 755 %{buildroot}%{_libexecdir}/%{name}

install -pm 755 rpmbuilder %{buildroot}%{_bindir}/rpmbuilder
install -pm 755 rpmunbuilder %{buildroot}%{_bindir}/rpmunbuilder
install -pm 644 libexec/* %{buildroot}%{_libexecdir}/%{name}/

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_libexecdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/rpmunbuilder

################################################################################

%changelog
* Fri Dec 06 2024 Anton Novojilov <andy@essentialkaos.com> - 3.4.2-0
- Improved options parsing

* Wed Sep 11 2024 Anton Novojilov <andy@essentialkaos.com> - 3.4.1-0
- Improved spec validation

* Mon Sep 09 2024 Anton Novojilov <andy@essentialkaos.com> - 3.4.0-0
- Added 'define' option validation
- Pass macros from 'define' option to spec-builddep
- Changed macro definition from 'name=value' to 'name:value'
- Code refactoring

* Thu Sep 05 2024 Anton Novojilov <andy@essentialkaos.com> - 3.3.4-0
- Removed rpmlint from dependencies
- Improved support of rpmlint installed from pip/uv

* Wed Aug 21 2024 Anton Novojilov <andy@essentialkaos.com> - 3.3.3-0
- Improved spec validation

* Fri Jun 07 2024 Anton Novojilov <andy@essentialkaos.com> - 3.3.2-0
- Improved formatting of help content

* Wed Nov 29 2023 Anton Novojilov <andy@essentialkaos.com> - 3.3.1-0
- Code refactoring

* Tue Nov 28 2023 Anton Novojilov <andy@essentialkaos.com> - 3.3.0-0
- Option '-k'/'--key' now accepts base64 encoded data with private key
- Option '-r'/'--remote' can now be passed multiple times
- Added private key validation
- Added tmux check for parallel build
- Improved version info output
- Improved '-r'/'--remote' option validation
- Run tmux with UTF-8 support
- Code refactoring
- Fixed bug with useless build host info parsing on multibuild
- Fixed bug with cleaning temporary data on multibuild
- Fixed bug with rendering help content when using Docker

* Mon Sep 25 2023 Anton Novojilov <andy@essentialkaos.com> - 3.2.0-0
- Use spec-builddep instead of yum-builddep for installing dependencies
- Added option '--install-latest/-IL' for installing the latest versions of
  dependencies

* Tue Aug 22 2023 Anton Novojilov <andy@essentialkaos.com> - 3.1.1-0
- Fixed output of dependencies versions in version info

* Tue Jul 25 2023 Anton Novojilov <andy@essentialkaos.com> - 3.1.0-0
- Added connection caching feature

* Tue Jul 04 2023 Anton Novojilov <andy@essentialkaos.com> - 3.0.3-0
- Improved version output

* Thu May 18 2023 Anton Novojilov <andy@essentialkaos.com> - 3.0.2-0
- Fixed bug with parsing in-spec variables with asterisk symbols
- Fixed bug with installing dependencies if path to spec file is not relative

* Wed Mar 22 2023 Anton Novojilov <andy@essentialkaos.com> - 3.0.1-0
- Fixed bug with local build due to lack of upload.shx file
- Improved container engine check in nodeinfo
- Minor UI improvements

* Sat Nov 05 2022 Anton Novojilov <andy@essentialkaos.com> - 3.0.0-0
- Added new option for defining build nodes indices
- Added panes naming in parallel build
- Added HUP signal handling
- Better Docker and Podman support
- Improved remote hostname parsing
- Improved usage info formatting
- Option '--depinstall'/'-di' renamed to '--install'/'-I'
- Removed packages uploading feature

* Mon Jul 04 2022 Anton Novojilov <andy@essentialkaos.com> - 2.12.2-0
- Fixed UI bugs
- Code refactoring

* Tue Jun 28 2022 Anton Novojilov <andy@essentialkaos.com> - 2.12.1-0
- Minor UI improvements

* Thu Apr 28 2022 Anton Novojilov <andy@essentialkaos.com> - 2.12.0-0
- Fixed bug with fetching sources from GitHub using git
- Much faster data fetching from git repositories

* Tue Feb 15 2022 Anton Novojilov <andy@essentialkaos.com> - 2.11.5-0
- Fixed bug with downloading files from GitHub

* Mon Dec 06 2021 Anton Novojilov <andy@essentialkaos.com> - 2.11.4-0
- Fixed minor bug with printing build stage
- Code refactoring

* Wed Nov 17 2021 Anton Novojilov <andy@essentialkaos.com> - 2.11.3-0
- Fixed major bug with checking the availability of utilities for checking
  remote node accessibility

* Mon Nov 15 2021 Anton Novojilov <andy@essentialkaos.com> - 2.11.2-0
- Fixed problems reported by shellcheck

* Sat Nov 06 2021 Anton Novojilov <andy@essentialkaos.com> - 2.11.1-0
- Code refactoring
- Added fallback accessibility check using nc

* Thu Sep 09 2021 Anton Novojilov <andy@essentialkaos.com> - 2.11.0-0
- Improved UI
- Code refactoring

* Thu Aug 26 2021 Anton Novojilov <andy@essentialkaos.com> - 2.10.0-0
- Improved fetching data from remote sources
- Code refactoring

* Tue Aug 17 2021 Anton Novojilov <andy@essentialkaos.com> - 2.9.0-0
- Improved sources cleanup process

* Thu May 14 2020 Anton Novojilov <andy@essentialkaos.com> - 2.8.0-0
- Speeded up fetching data from git repositories
- Show info about packaged sources size
- Automatic directory search for downloads

* Wed Mar 25 2020 Anton Novojilov <andy@essentialkaos.com> - 2.7.3-0
- Use /var/tmp instead of /tmp for storing temporary data

* Tue Mar 10 2020 Anton Novojilov <andy@essentialkaos.com> - 2.7.2-0
- Fixed bug with handling macros defined through --define option while
  downloading sources and patches

* Wed Feb 05 2020 Anton Novojilov <andy@essentialkaos.com> - 2.7.1-0
- Fixed handling --download option with predefined options in preferences file

* Tue Feb 04 2020 Anton Novojilov <andy@essentialkaos.com> - 2.7.0-0
- Updated options parser to the latest version
- Improved preferences parser
- Refactoring

* Fri Dec 13 2019 Anton Novojilov <andy@essentialkaos.com> - 2.6.0-0
- Added validation for downloaded files

* Wed Dec 04 2019 Anton Novojilov <andy@essentialkaos.com> - 2.5.2-0
- Removed handler for script errors

* Sat Nov 30 2019 Anton Novojilov <andy@essentialkaos.com> - 2.5.1-0
- Added handling of SCRIPT_DEBUG environment variable for enabling debug mode
- Added handler for script errors

* Thu Aug 08 2019 Anton Novojilov <andy@essentialkaos.com> - 2.5.0-0
- Automatic SHA-512 CRC generation feature

* Wed Jul 03 2019 Anton Novojilov <andy@essentialkaos.com> - 2.4.3-0
- Fixed bug with handling build node index in --parallel option
- Fixed bug with handling names of built packages

* Sat May 25 2019 Anton Novojilov <andy@essentialkaos.com> - 2.4.2-0
- Added checking options after reading inspec options
- Minor UI improvements

* Thu Jan 17 2019 Anton Novojilov <andy@essentialkaos.com> - 2.4.1-0
- Source repositories disabled by default for dependencies install
- Improved changelog's version extractor (part of package validator)

* Sat Nov 17 2018 Anton Novojilov <andy@essentialkaos.com> - 2.4.0-0
- Added sources validation feature
- Minor UI improvements

* Sat Nov 03 2018 Anton Novojilov <andy@essentialkaos.com> - 2.3.0-0
- Improved package validation
- Minor UI improvements

* Thu Sep 13 2018 Anton Novojilov <andy@essentialkaos.com> - 2.2.3-0
- Minor UI bugfixes

* Mon Aug 27 2018 Anton Novojilov <andy@essentialkaos.com> - 2.2.2-0
- Fixed bug with handling --without argument

* Sat Jun 23 2018 Anton Novojilov <andy@essentialkaos.com> - 2.2.1-0
- Updated argument parser
- Fixed bug in rpmunbuilder

* Sun May 06 2018 Anton Novojilov <andy@essentialkaos.com> - 2.2.0-0
- Perfecto used by default for specs validation
- Added option '--perfect'/'-3' for the most strict spec check
- Code refactoring

* Thu Nov 30 2017 Anton Novojilov <andy@essentialkaos.com> - 2.1.0-0
- Added option '--attach'/'-A' for attaching to parallel build session in tmux
- Minor improvements
- Code refactoring

* Wed Nov 29 2017 Anton Novojilov <andy@essentialkaos.com> - 2.0.0-0
- Source code divided to separate files
- Code refactoring
- Using 'spectool' instead of manual spec parsing for macro evaluation
- Improved UI
- Fixed bug with processing build options when '--with' or '--without'
  options is defined
- Fixed minor bug with processing spec values
- Fixed minor bug with processing sources
- Fixed bug with uploading packages to remote host

* Mon Sep 18 2017 Anton Novojilov <andy@essentialkaos.com> - 1.10.1-0
- Fixed compatibility with latest version of gopack

* Fri Jul 07 2017 Anton Novojilov <andy@essentialkaos.com> - 1.10.0-0
- Added option '--exclude-package/-EX' for excluding some packages
  from installation

* Sat Jun 17 2017 Anton Novojilov <andy@essentialkaos.com> - 1.9.0-0
- Improved tmux support

* Wed May 17 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.2-0
- Fixed compatibility with latest version of gopack

* Mon May 15 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.1-0
- Improved separator output in tmux
- Improved help output

* Wed May 10 2017 Anton Novojilov <andy@essentialkaos.com> - 1.8.0-0
- Improved gopack support
- Improved getting sources from DVCS/VCS
- Use custom user-agent
- Full-size separator support
- Fixed bug with storing golang sources to defined directory
- Fixed bug with downloading golang sources even if file already exist

* Wed Apr 26 2017 Anton Novojilov <andy@essentialkaos.com> - 1.7.3-0
- Fixed bug with cleaning temporary data

* Sun Apr 23 2017 Anton Novojilov <andy@essentialkaos.com> - 1.7.2-0
- Improved signals handling
- Code refactoring

* Tue Apr 04 2017 Anton Novojilov <andy@essentialkaos.com> - 1.7.1-0
- Fixed bug with lack of removing lock file for local build in some cases
- Fixed bug with wrong message about existing lock file
- Output errors to stderr

* Thu Mar 23 2017 Anton Novojilov <andy@essentialkaos.com> - 1.7.0-0
- Added error message if dependencies can't be installed
- Improved UI
- Some minor bugfixes

* Tue Mar 21 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.4-0
- Fixed bug with using --without flag

* Fri Mar 17 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.3-0
- Minor UI fixes

* Sat Mar 11 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.2-0
- Fixed bug with colors disabling
- Fixed bug with changing permissions on local lock
- Improved help content
- Improved error messages
- Code refactoring

* Mon Mar 06 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.1-0
- Fixed bug with handling errors during package validation

* Fri Mar 03 2017 Anton Novojilov <andy@essentialkaos.com> - 1.6.0-0
- Added compatibility with latest version of rpmbuilder-node package
- Failed validation now fail entire build
- Improved gloang sources packing
- Minor improvements

* Mon Jan 23 2017 Anton Novojilov <andy@essentialkaos.com> - 1.5.2-0
- Improved checking remote sources availability

* Thu Jan 12 2017 Anton Novojilov <andy@essentialkaos.com> - 1.5.1-0
- Simplified key definition support
- Removed scp output in situation when key-based auth is used

* Mon Dec 26 2016 Anton Novojilov <andy@essentialkaos.com> - 1.5.0-0
- Git submodules fetching support
- Download cache usage for sources from VCS's
- Fetching sources from VCS's if --download argument is used
- Fixed bug with downloading sources from VCS's when source file already exist

* Wed Dec 14 2016 Anton Novojilov <andy@essentialkaos.com> - 1.4.0-0
- Added nodeinfo usage support
- Added gopack support

* Mon Dec 12 2016 Anton Novojilov <andy@essentialkaos.com> - 1.3.1-0
- Minor fixes

* Wed Nov 30 2016 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Added package validation after build

* Wed Nov 23 2016 Anton Novojilov <andy@essentialkaos.com> - 1.2.3-0
- Fixed bug with unbuilding src package

* Wed Nov 23 2016 Anton Novojilov <andy@essentialkaos.com> - 1.2.2-0
- Fixed bug with packaging sources from SVN repository

* Thu Nov 17 2016 Anton Novojilov <andy@essentialkaos.com> - 1.2.1-0
- Fixed bug with missing characters escaping in regular expressions

* Mon Nov 14 2016 Anton Novojilov <andy@essentialkaos.com> - 1.2.0-0
- Code refactoring
- Improved help output

* Sun Sep 25 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.5-0
- UI improvements
- Fixed typos in help output
- Fixed bug with processing "remote" argument

* Wed May 11 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.3-0
- Code refactoring

* Wed May 11 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.2-1
- Improved spec file

* Mon Apr 25 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.2-0
- Fixed bug with disabling repository

* Sun Apr 24 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.1-0
- -dl without given path download files to current directory

* Thu Apr 21 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.0-0
- Improved dependencies installation process

* Wed Apr 20 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.8-0
- Improved working with yum cache

* Wed Apr 20 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.7-0
- Fixed bug with parsing remote build definition

* Thu Apr 07 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.6-0
- Package install feature
- Code refactoring

* Tue Apr 05 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.5-0
- Host key checking disabled by default

* Fri Mar 18 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.4-0
- Fixed bug with downloading local files which contains http/ftp/https in name

* Sun Oct 04 2015 Anton Novojilov <andy@essentialkaos.com> - 1.0.3-0
- Suppressing packing errors

* Thu Aug 06 2015 Anton Novojilov <andy@essentialkaos.com> - 1.0.2-0
- Double bell replaced by single bell after log build

* Tue Aug 04 2015 Anton Novojilov <andy@essentialkaos.com> - 1.0.1-0
- Fixed bug with base access rights for lock files

* Fri Oct 03 2014 Anton Novojilov <andy@essentialkaos.com> - 1.0.0-0
- Latest non-stable version
