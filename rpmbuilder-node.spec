###############################################################################

%define _posixroot        /
%define _root             /root
%define _bin              /bin
%define _sbin             /sbin
%define _srv              /srv
%define _home             /home
%define _lib32            %{_posixroot}lib
%define _lib64            %{_posixroot}lib64
%define _libdir32         %{_prefix}%{_lib32}
%define _libdir64         %{_prefix}%{_lib64}
%define _logdir           %{_localstatedir}/log
%define _rundir           %{_localstatedir}/run
%define _lockdir          %{_localstatedir}/lock/subsys
%define _cachedir         %{_localstatedir}/cache
%define _spooldir         %{_localstatedir}/spool
%define _crondir          %{_sysconfdir}/cron.d
%define _loc_prefix       %{_prefix}/local
%define _loc_exec_prefix  %{_loc_prefix}
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_libdir       %{_loc_exec_prefix}/%{_lib}
%define _loc_libdir32     %{_loc_exec_prefix}/%{_lib32}
%define _loc_libdir64     %{_loc_exec_prefix}/%{_lib64}
%define _loc_libexecdir   %{_loc_exec_prefix}/libexec
%define _loc_sbindir      %{_loc_exec_prefix}/sbin
%define _loc_bindir       %{_loc_exec_prefix}/bin
%define _loc_datarootdir  %{_loc_prefix}/share
%define _loc_includedir   %{_loc_prefix}/include
%define _loc_mandir       %{_loc_datarootdir}/man
%define _rpmstatedir      %{_sharedstatedir}/rpm-state
%define _pkgconfigdir     %{_libdir}/pkgconfig

%define __ln              %{_bin}/ln
%define __touch           %{_bin}/touch
%define __service         %{_sbin}/service
%define __chkconfig       %{_sbin}/chkconfig
%define __ldconfig        %{_sbin}/ldconfig
%define __groupadd        %{_sbindir}/groupadd
%define __useradd         %{_sbindir}/useradd
%define __userdel         %{_sbindir}/userdel

###############################################################################

%define user_name         builder
%define home_dir          %{_home}/%{user_name}
%define service_name      buildmon

###############################################################################

Summary:         Configuration package for rpmbuilder node
Name:            rpmbuilder-node
Version:         1.2.0
Release:         0%{?dist}
License:         EKOL
Group:           Development/Tools
URL:             https://github.com/essentialkaos/rpmbuilder

Source0:         rpmmacros
Source1:         %{service_name}
Source2:         %{service_name}.init
Source3:         %{user_name}.sudoers
Source4:         nodeinfo

BuildArch:       noarch

BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        rpm >= 4.8.0 rpm-build rpmdevtools
Requires:        rpmlint kaosv yum-utils

Provides:        %{name} = %{version}-%{release}

###############################################################################

%description
Package creates user for remote package building with rpmbuilder.

###############################################################################

%prep
%build

%pre
getent group %{user_name} >/dev/null || groupadd -r %{user_name}
getent passwd %{user_name} >/dev/null || useradd -r -g %{user_name} -d %{_home}/%{user_name} -s /bin/bash %{user_name}

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_initddir}
install -dm 755 %{buildroot}%{_sysconfdir}/sysconfig
install -dm 755 %{buildroot}%{_sysconfdir}/sudoers.d
install -dm 755 %{buildroot}%{home_dir}
install -dm 700 %{buildroot}%{home_dir}/.ssh

install -pm 755 %{SOURCE0} %{buildroot}%{home_dir}/.rpmbld
install -pm 755 %{SOURCE1} %{buildroot}%{home_dir}/
install -pm 755 %{SOURCE2} %{buildroot}%{_initddir}/%{service_name}
install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sudoers.d/%{user_name}
install -pm 755 %{SOURCE4} %{buildroot}%{home_dir}/

%clean
rm -rf %{buildroot}

###############################################################################

%post
%{__chown} %{user_name}:%{user_name} %{home_dir} -R

if [[ $1 -eq 1 ]] ; then
  touch %{home_dir}/.ssh/authorized_keys
  chmod 0600 %{home_dir}/.ssh/authorized_keys

  sudo -u %{user_name} rpmdev-setuptree
  sudo -u %{user_name} restorecon -R -v %{home_dir}/.ssh &> /dev/null

  cat %{home_dir}/.rpmbld > %{home_dir}/.rpmmacros

  %{__service} %{service_name} start &> /dev/null || :
  %{__chkconfig} --add %{service_name}
fi

%postun
if [[ $1 -eq 0 ]] ; then
  %{__service} %{service_name} stop &> /dev/null || :
  %{__chkconfig} --del %{service_name}
  %{__userdel} -r %{user_name}
  rm -rf %{home_dir}
fi

###############################################################################

%files
%defattr(-,root,root,-)
%{_initddir}/%{service_name}
%{_sysconfdir}/sudoers.d/%{user_name}
%{home_dir}

###############################################################################

%changelog
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
