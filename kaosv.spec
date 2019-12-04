################################################################################

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
%define _loc_datarootdir  %{_loc_prefix}/share
%define _loc_includedir   %{_loc_prefix}/include
%define _loc_mandir       %{_loc_datarootdir}/man
%define _rpmstatedir      %{_sharedstatedir}/rpm-state
%define _pkgconfigdir     %{_libdir}/pkgconfig

################################################################################

Summary:         Bash lib for SysV init scripts
Name:            kaosv
Version:         2.15.5
Release:         0%{?dist}
Group:           Applications/System
License:         EKOL
URL:             https://github.com/essentialkaos/kaosv
Vendor:          ESSENTIAL KAOS

Source0:         https://source.kaos.st/%{name}/%{name}-%{version}.tar.bz2

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:        daemonize bash >= 4.0 rpm

################################################################################

%description
Bash lib for SysV init scripts.

################################################################################

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_initddir}
install -dm 755 %{buildroot}%{_loc_datarootdir}/%{name}

install -pm 644 %{name} %{buildroot}%{_initddir}/
install -pm 755 supervisor %{buildroot}%{_loc_datarootdir}/%{name}/

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE.EN LICENSE.RU
%{_initddir}/%{name}
%{_loc_datarootdir}/%{name}/supervisor

################################################################################

%changelog
* Wed Dec 04 2019 Anton Novojilov <andy@essentialkaos.com> - 2.15.5-0
- Removed handler for script errors

* Sat Nov 30 2019 Anton Novojilov <andy@essentialkaos.com> - 2.15.4-0
- Added handling of SCRIPT_DEBUG environment variable for enabling debug mode
- Added handler for script errors

* Sat May 25 2019 Anton Novojilov <andy@essentialkaos.com> - 2.15.3-0
- Improved forced stop handling
- Improved PID search mechanic

* Thu Mar 21 2019 Anton Novojilov <andy@essentialkaos.com> - 2.15.2-0
- Disallowed direct script execution

* Wed Feb 28 2018 Anton Novojilov <andy@essentialkaos.com> - 2.15.1-0
- Fixed bug with changing pid directory owner to root if kv[user] not defined

* Fri Feb 23 2018 Anton Novojilov <andy@essentialkaos.com> - 2.15.0-0
- Brand new PID searching system which works without search pattern
- Print error if user try to source init script (e.g . script)
- Fixed bug with searching real username in tmux session

* Thu Feb 15 2018 Anton Novojilov <andy@essentialkaos.com> - 2.14.1-0
- Fixed bug with lack of exiting from script on error
- Fixed bug with help content output
- Code refactoring

* Mon Feb 12 2018 Anton Novojilov <andy@essentialkaos.com> - 2.14.0-0
- Fixed bug with searching PID
- Removed unclear part with exiting from script inside kv.error method

* Mon Dec 11 2017 Anton Novojilov <andy@essentialkaos.com> - 2.13.5-0
- Code refactoring

* Sat Oct 21 2017 Anton Novojilov <andy@essentialkaos.com> - 2.13.4-0
- Added warning about unsupported handler name in kv.disableOutputRedirect

* Tue Oct 17 2017 Anton Novojilov <andy@essentialkaos.com> - 2.13.3-0
- Minor improvements

* Sat Aug 26 2017 Anton Novojilov <andy@essentialkaos.com> - 2.13.2-0
- Minor improvements

* Sat Aug 26 2017 Anton Novojilov <andy@essentialkaos.com> - 2.13.1-0
- Minor improvements

* Thu Apr 06 2017 Anton Novojilov <andy@essentialkaos.com> - 2.13.0-0
- Output error and warning messages to stderr
- Minor improvements

* Tue Mar 21 2017 Anton Novojilov <andy@essentialkaos.com> - 2.12.4-0
- Fixed bug with service restart after a system reboot
- Removed dot from the end of log messages

* Tue Mar 14 2017 Anton Novojilov <andy@essentialkaos.com> - 2.12.3-0
- More detailed warning messages for status command

* Sat Mar 11 2017 Anton Novojilov <andy@essentialkaos.com> - 2.12.2-0
- Default status handler now insecure (can be run without root privileges)
- Improved documentation
- Overall minor improvements

* Mon Jan 30 2017 Anton Novojilov <andy@essentialkaos.com> - 2.12.1-0
- Minor error handling improvements

* Thu Dec 01 2016 Anton Novojilov <andy@essentialkaos.com> - 2.12.0-0
- Default restart handler now checks current service state and restart
  service only if it is running
- Using 'is running' instead of 'is working'
- STATUS_WORKS replaced by STATUS_RUNNING (STATUS_WORKS still accessible
  for compatibility with previous versions of kaosv)

* Wed Nov 30 2016 Anton Novojilov <andy@essentialkaos.com> - 2.11.0-0
- Improved setting system limits process

* Mon Nov 21 2016 Anton Novojilov <andy@essentialkaos.com> - 2.10.2-0
- Fixed bug with reading system limits

* Tue Nov 15 2016 Anton Novojilov <andy@essentialkaos.com> - 2.10.1-0
- Code refactoring

* Fri Nov 11 2016 Anton Novojilov <andy@essentialkaos.com> - 2.10.0-0
- Improved compatibility with systemd
- Improved service status detection after system reboot

* Thu Sep 29 2016 Anton Novojilov <andy@essentialkaos.com> - 2.9.1-0
- Improved process pid search

* Tue Sep 13 2016 Anton Novojilov <andy@essentialkaos.com> - 2.9.0-0
- Added method kv.isServiceWorks for checking another service status

* Sun Sep 11 2016 Anton Novojilov <andy@essentialkaos.com> - 2.8.2-0
- Using dark grey color instead light grey color

* Thu Apr 28 2016 Anton Novojilov <andy@essentialkaos.com> - 2.8.1-0
- Using 'is working' instead of 'is works'

* Fri Apr 01 2016 Anton Novojilov <andy@essentialkaos.com> - 2.8.0-0
- Method kv.addCommandVars renamed to kv.addCommandArgs

* Tue Nov 17 2015 Anton Novojilov <andy@essentialkaos.com> - 2.7.2-0
- Improved working with limits

* Tue Nov 10 2015 Anton Novojilov <andy@essentialkaos.com> - 2.7.1-0
- Fixed minor bug with output for unknown commands

* Wed Oct 28 2015 Anton Novojilov <andy@essentialkaos.com> - 2.7.0-0
- Return exit code 3 for status command if service is stoppped

* Sat Oct 24 2015 Anton Novojilov <andy@essentialkaos.com> - 2.6.1-0
- Minor improvements

* Tue Aug 11 2015 Anton Novojilov <andy@essentialkaos.com> - 2.6.0-0
- Added methods for executing default handlers (kv.start, kv.stop, kv.restart,
  kv.status, kv.usage)
- Added method for kaosv version compatibility check (kv.require)
- Code refactoring

* Sun Jul 26 2015 Anton Novojilov <andy@essentialkaos.com> - 2.5.5-0
- Fixed bug with status command which works only with sudo privileges

* Fri Jul 24 2015 Anton Novojilov <andy@essentialkaos.com> - 2.5.4-0
- Fixed bug with pid and lock files naming

* Tue Jun 02 2015 Anton Novojilov <andy@essentialkaos.com> - 2.5.3-0
- Fixed minor bug with log file overriding with kv.daemonize

* Wed Mar 25 2015 Anton Novojilov <andy@essentialkaos.com> - 2.5.2-0
- Fixed bug with unchanged owner for pid dir
- Added restart pre and post handlers

* Sat Feb 21 2015 Anton Novojilov <andy@essentialkaos.com> - 2.5.1-0
- Fixed bug with checking safe paths
- Fixed bug with pid creation with kv.daemonize

* Mon Feb 02 2015 Anton Novojilov <andy@essentialkaos.com> - 2.5-0
- Fixed bug with redefining basic commands
- Fixed bug with reading property from file
- Some minor improvements
- Refactoring

* Wed Dec 31 2014 Anton Novojilov <andy@essentialkaos.com> - 2.4-0
- Added property oom_adj for setting oom killer adjustment level

* Mon Dec 29 2014 Anton Novojilov <andy@essentialkaos.com> - 2.3.1-0
- Fixed minor bug with user checking

* Fri Dec 26 2014 Anton Novojilov <andy@essentialkaos.com> - 2.3-0
- kv.daemonize create pid only if auto_pid is true

* Tue Dec 23 2014 Anton Novojilov <andy@essentialkaos.com> - 2.2-0
- Added supervisor feature

* Sat Nov 15 2014 Anton Novojilov <andy@essentialkaos.com> - 2.1-0
- Added stdout and stderr redirection to kv[log] for kv.daemonize

* Fri Nov 07 2014 Anton Novojilov <andy@essentialkaos.com> - 2.0.1-0
- Fixed typo

* Sat Oct 18 2014 Anton Novojilov <andy@essentialkaos.com> - 2.0-0
- Changed syntax for kv.run function
- Added kv.error and kv.warn functions
- kv.run now uses user property by default
- Added kv.runAs function
- Added limits support in kv.daemonize
- Added ionice configuration
- Added nice and ionice support in kv.daemonize
- Added ionice support in kv.run (kv.runAs)
- Added support for nofile and nproc limits in kv.run and kv.daemonize
- daemonize_user property renamed to user
- daemonize_dir renamed to dir
- Added additional checks for dir and user properties
- Added property auto_actions_log for activation automatic logging about
  user actions (start, stop, etc...)
- Fixed major bug with limits while kv.daemonize usage
- Fixed major bug with arguments scope in kv.run
- Fixed minor bug with wrong pid owner after pid file restore
- Performance improvements

* Fri Oct 17 2014 Anton Novojilov <andy@essentialkaos.com> - 1.5.1-0
- Fixed bug with output redirection to log and default logger
- Small improvements

* Thu Oct 16 2014 Anton Novojilov <andy@essentialkaos.com> - 1.5.0-0
- Added method kv.checkSELinux for checking selinux mode

* Fri Oct 10 2014 Anton Novojilov <andy@essentialkaos.com> - 1.4.0-0
- Fixed bug in prepare stage (users can't execute some commands without
  superuser privileges)
- Improved problems fixing
- Some minor improvements

* Tue Sep 16 2014 Anton Novojilov <andy@essentialkaos.com> - 1.3.0-0
- Fixed major bug with directory creation in / directory
- Some minor improvements
