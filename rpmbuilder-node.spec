################################################################################

%define user_name  builder
%define home_dir   /home/%{user_name}

################################################################################

Summary:    Configuration package for rpmbuilder node
Name:       rpmbuilder-node
Version:    1.6.1
Release:    0%{?dist}
License:    Apache License, Version 2.0
Group:      Development/Tools
URL:        https://kaos.sh/rpmbuilder

Source0:    %{name}-%{version}.tar.bz2

BuildArch:  noarch

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:   rpm rpm-build rpmdevtools yum-utils spec-builddep perfecto

Provides:   %{name} = %{version}-%{release}

################################################################################

%description
Package configure remote node for building RPM packages with rpmbuilder
utility.

################################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dDm 755 %{buildroot}%{_unitdir}
install -pm 644 buildmon.service %{buildroot}%{_unitdir}/

install -dDm 755 %{buildroot}%{_sysconfdir}/sudoers.d
install -pm 644 builder.sudoers %{buildroot}%{_sysconfdir}/sudoers.d/%{user_name}

install -dDm 755 %{buildroot}%{home_dir}/.config
install -dDm 700 %{buildroot}%{home_dir}/.ssh
install -pm 755 buildmon %{buildroot}%{home_dir}/
install -pm 755 nodeinfo %{buildroot}%{home_dir}/
install -pm 755 initenv %{buildroot}%{home_dir}/

%if 0%{?rhel} == 8
install -pm 755 rpmmacros_el8 %{buildroot}%{home_dir}/.rpmmacros_rpmbuilder
%endif

%if 0%{?rhel} == 9
install -pm 755 rpmmacros_el9 %{buildroot}%{home_dir}/.rpmmacros_rpmbuilder
%endif

%if 0%{?rhel} == 10
install -pm 755 rpmmacros_el10 %{buildroot}%{home_dir}/.rpmmacros_rpmbuilder
%endif


%clean
rm -rf %{buildroot}

################################################################################

%pre
getent group %{user_name} >/dev/null || groupadd -r %{user_name}
getent passwd %{user_name} >/dev/null || useradd -r -g %{user_name} -d /home/%{user_name} -s /bin/bash %{user_name}

%post
chown -h -R %{user_name}:%{user_name} %{home_dir}

if [[ $1 -eq 1 ]] ; then
  touch %{home_dir}/.ssh/authorized_keys

  # perfecto:ignore
  chmod 0600 %{home_dir}/.ssh/authorized_keys

  sudo -u %{user_name} rpmdev-setuptree
  sudo -u %{user_name} restorecon -R -v %{home_dir}/.ssh &> /dev/null

  cat %{home_dir}/.rpmmacros_rpmbuilder > %{home_dir}/.rpmmacros

  chown -h -R %{user_name}:%{user_name} %{home_dir}

  systemctl enable buildmon.service &>/dev/null || :
  systemctl start buildmon.service &>/dev/null || :

  systemctl reload sshd.service &>/dev/null || :
fi

%preun
if [[ $1 -eq 0 ]] ; then
  systemctl --no-reload disable buildmon.service &>/dev/null || :
  systemctl stop buildmon.service &>/dev/null || :
  userdel -r %{user_name}
  rm -rf %{home_dir}
fi

%postun
if [[ $1 -ge 1 ]] ; then
  systemctl daemon-reload &>/dev/null || :
fi

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_unitdir}/buildmon.service
%{_sysconfdir}/sudoers.d/%{user_name}
%{home_dir}

################################################################################

%changelog
* Thu Aug 07 2025 Anton Novojilov <andy@essentialkaos.com> - 1.7.0-0
- Add EL 10 support

* Thu Sep 05 2024 Anton Novojilov <andy@essentialkaos.com> - 1.6.1-0
- Removed rpmlint from dependencies

* Wed Aug 21 2024 Anton Novojilov <andy@essentialkaos.com> - 1.6.0-0
- Removed EL 7 support
- Init script replaced by systemd service

* Mon Sep 25 2023 Anton Novojilov <andy@essentialkaos.com> - 1.5.0-0
- Added spec-builddep to dependencies

* Mon Mar 27 2023 Anton Novojilov <andy@essentialkaos.com> - 1.4.3-0
- Fixed bug with printing container info in nodeinfo

* Fri Apr 29 2022 Anton Novojilov <andy@essentialkaos.com> - 1.4.2-0
- Dropped CentOS 6 support

* Fri May 29 2020 Anton Novojilov <andy@essentialkaos.com> - 1.4.1-3
- Fixed problems reported by perfecto

* Mon Dec 16 2019 Anton Novojilov <andy@essentialkaos.com> - 1.4.1-2
- Added threads usage for payload packing to rpmmacros files

* Sat Nov 30 2019 Anton Novojilov <andy@essentialkaos.com> - 1.4.1-1
- Added rpmmacros file for CentOS 8

* Fri Jan 04 2019 Anton Novojilov <andy@essentialkaos.com> - 1.4.1-0
- Code refactoring

* Sun May 06 2018 Anton Novojilov <andy@essentialkaos.com> - 1.4.0-0
- Added perfecto support
- Added config for rpmlint

* Sat Dec 23 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.3-0
- Code refactoring

* Sat Mar 11 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.2-0
- Improved nodeinfo output

* Mon Mar 06 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.1-0
- Fixed bug with removing lock file

* Fri Mar 03 2017 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Fixed bug with deleting directories inside rpmbuild directory
- Added initenv utility
- buildmon refactoring

* Mon Jan 30 2017 Anton Novojilov <andy@essentialkaos.com> - 1.2.2-0
- Enable password authentication by default

* Thu Jan 12 2017 Anton Novojilov <andy@essentialkaos.com> - 1.2.1-2
- Added improved rpmmacroses for centos6 and centos7
- Improved spec

* Mon Dec 26 2016 Anton Novojilov <andy@essentialkaos.com> - 1.2.1-0
- Minor UI fixes in nodeinfo utility

* Wed Dec 14 2016 Anton Novojilov <andy@essentialkaos.com> - 1.2.0-0
- Added nodeinfo utility

* Wed Nov 16 2016 Anton Novojilov <andy@essentialkaos.com> - 1.1.0-0
- Improvements

* Wed May 11 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.1-2
- Improved spec file

* Fri May 06 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.1-1
- Removed epel and atrpms repositories from dependencies

* Thu Apr 21 2016 Anton Novojilov <andy@essentialkaos.com> - 1.0.1-0
- yum-utils added to dependencies

* Sat Oct 11 2014 Anton Novojilov <andy@essentialkaos.com> - 1.0-0
- Unstable release
