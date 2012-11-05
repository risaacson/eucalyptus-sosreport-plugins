%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: A plugin to sosreport to collect data about Eucalyptus clouds
Name: eucalyptus-sosreport
Version: 0.1
Release: 0%{?dist}
Group: Applications/System
Source0: https://fedorahosted.org/releases/s/o/sos/%{name}-%{version}.tar.gz
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://github.com/eucalyptus/eucalyptus-sosreport
BuildRequires: python-devel
BuildRequires: gettext
Requires: sosreport

%description
Eucalyptus is open source software for building AWS-compatible
private and hybrid clouds. Sosreport is a set of tools that
gathers information about system hardware and configuration.
This package contains a plugin for sosreport to gather 
information on Eucalyptus clouds.

%prep
%setup -q

%build
make

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} install
%find_lang %{name} || echo 0

%clean
rm -rf ${RPM_BUILD_ROOT}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_sbindir}/sosreport
%{_datadir}/%{name}
%{python_sitelib}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%doc README TODO LICENSE ChangeLog doc/*
%config(noreplace) %{_sysconfdir}/sos.conf

%changelog
* Mon Nov 05 2012 Tom Ellis <tom dot ellis at eucalyptus dot com> = 0.1-0
- Initial Eucalyptus plugin packaging for EL6 
