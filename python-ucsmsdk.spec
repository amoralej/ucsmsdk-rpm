%global package_name ucsmsdk
Name:           python-%{package_name}
Version:        0.9.3.2 
Release:        1%{?dist}
Summary:        Python SDK for Cisco UCS Manager
License:        ASL 2.0
URL:            https://pypi.org/pypi/%{package_name}
Source0:        https://pypi.python.org/packages/source/U/ucsmsdk/ucsmsdk-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
%global _description\
Python development kit for Cisco UCS
%description %_description
%package -n python2-ucsmsdk
Summary: %summary
%{?python_provide:%python_provide python2-ucsmsdk}
%description -n python2-ucsmsdk %_description
%prep
%setup -q -n %{package_name}-%{version}
%build
%{__python2} setup.py build
%install
%{__python2} setup.py install --skip-build --root %{buildroot}
%files -n python2-ucsmsdk
%{python2_sitelib}/%{package_name}/
%{python2_sitelib}/%{package_name}*.egg-info
%doc README.md
%license LICENSE.txt
%changelog
* Wed Jun 13 2018 Sandhya Dasu <sadasu@cisco.com> 0.9.3.2-1
- Initial RPM release
