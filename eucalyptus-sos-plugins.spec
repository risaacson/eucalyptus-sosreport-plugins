%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Summary: A plugin to sosreport to collect data about Eucalyptus clouds
Name: eucalyptus-sos-plugins
Version: 0.1.3
Release: 0%{?dist}
Source0: %{name}-%{version}.tar.gz
Group: Applications/System
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://github.com/risaacson/eucalyptus-sosreport-plugins
BuildRequires: python-devel
Requires: sos

%description
Eucalyptus is open source software for building AWS-compatible
private and hybrid clouds. Sosreport is a set of tools that
gathers information about system hardware and configuration.
This package contains plugins for sosreport to gather
information on Eucalyptus clouds.

%prep
%setup -q

%build

%install
install -m 0755 -d $RPM_BUILD_ROOT/%{python_sitelib}/sos/plugins
install -m 0755 sos/plugins/*.py $RPM_BUILD_ROOT/%{python_sitelib}/sos/plugins

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
