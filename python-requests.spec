%global debug_package %{nil}

Name: python-requests
Epoch: 100
Version: 2.27.0
Release: 1%{?dist}
BuildArch: noarch
Summary: HTTP library, written in Python, for human beings
License: Apache-2.0
URL: https://github.com/psf/requests/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: ca-certificates
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-charset-normalizer >= 2.0.0
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Most existing Python modules for sending HTTP requests are extremely
verbose and cumbersome. Python’s built-in urllib2 module provides most
of the HTTP capabilities you should need, but the API is thoroughly
broken. This library is designed to make HTTP requests easy for
developers.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python_version_nodots}-requests
Summary: HTTP library, written in Python, for human beings
Requires: ca-certificates
Requires: python3
Requires: python3-certifi >= 2017.4.17
Requires: python3-chardet >= 3.0.2
Requires: python3-charset-normalizer >= 2.0.0
Requires: python3-idna >= 2.5
Requires: python3-urllib3 >= 1.21.1
Provides: python3-requests = %{epoch}:%{version}-%{release}
Provides: python3dist(requests) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-requests = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(requests) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-requests = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(requests) = %{epoch}:%{version}-%{release}

%description -n python%{python_version_nodots}-requests
Most existing Python modules for sending HTTP requests are extremely
verbose and cumbersome. Python’s built-in urllib2 module provides most
of the HTTP capabilities you should need, but the API is thoroughly
broken. This library is designed to make HTTP requests easy for
developers.

%files -n python%{python_version_nodots}-requests
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-requests
Summary: HTTP library, written in Python, for human beings
Requires: ca-certificates
Requires: python3
Requires: python3-certifi >= 2017.4.17
Requires: python3-chardet >= 3.0.2
Requires: python3-charset-normalizer >= 2.0.0
Requires: python3-idna >= 2.5
Requires: python3-urllib3 >= 1.21.1
Provides: python3-requests = %{epoch}:%{version}-%{release}
Provides: python3dist(requests) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-requests = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(requests) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-requests = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(requests) = %{epoch}:%{version}-%{release}

%description -n python3-requests
Most existing Python modules for sending HTTP requests are extremely
verbose and cumbersome. Python’s built-in urllib2 module provides most
of the HTTP capabilities you should need, but the API is thoroughly
broken. This library is designed to make HTTP requests easy for
developers.

%files -n python3-requests
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
