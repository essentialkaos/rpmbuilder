###############################################################################

Summary:         RPM package build helper
Name:            rpmbuilder
Version:         1.7.1
Release:         0%{?dist}
License:         EKOL
Group:           Development/Tools
URL:             https://github.com/essentialkaos/rpmbuilder

Source0:         https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        rpm >= 4.8.0 rpm-build rpmdevtools yum-utils
Requires:        rpmlint sshpass coreutils tmux

Provides:        %{name} = %{version}-%{release}

###############################################################################

%description
RPM package build helper.

###############################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}

install -pm 755 rpmbuilder %{buildroot}%{_bindir}/rpmbuilder
install -pm 755 rpmunbuilder %{buildroot}%{_bindir}/rpmunbuilder

%clean
rm -rf %{buildroot}

###############################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE.EN LICENSE.RU
%{_bindir}/%{name}
%{_bindir}/rpmunbuilder

###############################################################################

%changelog
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
- Removed scp output in situtation when key-based auth is used

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
