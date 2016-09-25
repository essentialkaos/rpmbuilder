###############################################################################

Summary:         RPM package build helper
Name:            rpmbuilder
Version:         1.1.4
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
* Sun Sep 25 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.4-0
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
- Improved dependecies installation process

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
