#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	GraphQL implementation for Python
Summary(pl.UTF-8):	Implementacja GraphQL dla Pythona
Name:		python-graphql-core
# keep 2.x here for python2 support
Version:	2.3.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/graphql-core/
Source0:	https://files.pythonhosted.org/packages/source/g/graphql-core/graphql-core-%{version}.tar.gz
# Source0-md5:	72888f80c6c941c89ca5ed35aaf7d4cf
URL:		https://pypi.org/project/graphql-core/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-promise >= 2.3
BuildRequires:	python-promise < 3
BuildRequires:	python-rx >= 1.6
BuildRequires:	python-rx < 2
BuildRequires:	python-six >= 1.10.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-promise >= 2.3
BuildRequires:	python3-promise < 3
BuildRequires:	python3-rx >= 1.6
BuildRequires:	python3-rx < 2
BuildRequires:	python3-six >= 1.10.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is a port of GraphQL.js to Python and up-to-date with
release 0.6.0.

GraphQL.js is the JavaScript reference implementation for GraphQL, a
query language for APIs created by Facebook.

%description -l pl.UTF-8

%package -n python3-graphql-core
Summary:	GraphQL implementation for Python
Summary(pl.UTF-8):	Implementacja GraphQL dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-graphql-core
This library is a port of GraphQL.js to Python and up-to-date with
release 0.6.0.

GraphQL.js is the JavaScript reference implementation for GraphQL, a
query language for APIs created by Facebook.

%description -n python3-graphql-core -l pl.UTF-8
Ta biblioteka to port GraphQL.js do Pythona, aktualna dla wydania
0.6.0.

GraphQL.js to napisana w JavaScripcie, referencyjna implementacja
GraphQL - języka zapytań dla API Facebooka.

%prep
%setup -q -n graphql-core-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/graphql
%{py_sitescriptdir}/graphql_core-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-graphql-core
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/graphql
%{py3_sitescriptdir}/graphql_core-%{version}-py*.egg-info
%endif
