###############################################################################

Summary:         RPM package build helper
Name:            rpmbuilder
Version:         1.0.7
Release:         0%{?dist}
License:         EKOL
Group:           Applications/System
Vendor:          ESSENTIALKAOS
URL:             http://essentialkaos.com

Source0:         https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        rpm >= 4.8.0 rpm-build rpmdevtools
Requires:        rpmlint sshpass coreutils tmux

Provides:        %{name} = %{version}-%{release}

%description
RPM package build helper

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
