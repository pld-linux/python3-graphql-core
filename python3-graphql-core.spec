#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	GraphQL implementation for Python
Summary(pl.UTF-8):	Implementacja GraphQL dla Pythona
Name:		python3-graphql-core
Version:	3.2.3
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/graphql-core/
Source0:	https://files.pythonhosted.org/packages/source/g/graphql-core/graphql-core-%{version}.tar.gz
# Source0-md5:	49790781ef70f3dd1714b44d99e06e0e
URL:		https://pypi.org/project/graphql-core/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:59
%if %{with tests}
BuildRequires:	python3-pytest >= 7.1
BuildRequires:	python3-pytest-asyncio >= 0.16
#BuildRequires:	python3-pytest-describe >= 2
BuildRequires:	python3-pytest-timeout
# >= 2
%if "%{py3_ver}" == "3.6"
BuildRequires:	python3-typing-extensions >= 4.2
%endif
%if "%{py3_ver}" == "3.7"
BuildRequires:	python3-typing-extensions >= 4.3
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme >= 1
BuildRequires:	sphinx-pdg-3 >= 4.3
%endif
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library is a port of GraphQL.js to Python and up-to-date with
release 0.6.0.

GraphQL.js is the JavaScript reference implementation for GraphQL, a
query language for APIs created by Facebook.

%description -l pl.UTF-8
Ta biblioteka to port GraphQL.js do Pythona, aktualna dla wydania
0.6.0.

GraphQL.js to napisana w JavaScripcie, referencyjna implementacja
GraphQL - języka zapytań dla API Facebooka.

%package apidocs
Summary:	API documentation for Python graphql-core module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona graphql-core
Group:		Documentation

%description apidocs
API documentation for Python graphql-core module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona graphql-core.

%prep
%setup -q -n graphql-core-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_asyncio.plugin,pytest_benchmark.plugin,pytest_timeout \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md SECURITY.md
%{py3_sitescriptdir}/graphql
%{py3_sitescriptdir}/graphql_core-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,modules,usage,*.html,*.js}
%endif
