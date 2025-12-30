%define module jsonpickle
%bcond_without tests

Name:		python-jsonpickle
Version:	4.1.1
Release:	3
Summary:	Python library for serializing any arbitrary object graph into JSON
URL:		https://github.com/jsonpickle/jsonpickle
License:	BSD-3-Clause
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/j/jsonpickle/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
# see NOTE in check section
#BuildRequires:	python%%{pyver}dist(atheris)
BuildRequires:	python%{pyver}dist(bson)
BuildRequires:	python%{pyver}dist(ecdsa)
BuildRequires:	python%{pyver}dist(feedparser)
BuildRequires:	python%{pyver}dist(gmpy2)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pandas)
BuildRequires:	python%{pyver}dist(pymongo)
BuildRequires:	python%{pyver}dist(pyyaml)
BuildRequires:	python%{pyver}dist(scikit-learn)
BuildRequires:	python%{pyver}dist(scipy)
BuildRequires:	python%{pyver}dist(simplejson)
BuildRequires:	python%{pyver}dist(sqlalchemy)
BuildRequires:	python%{pyver}dist(ujson)
BuildRequires:	python%{pyver}dist(mypy)
%endif

%description
Python library for serializing any arbitrary object graph into JSON.
It can take almost any Python object and turn the object into JSON.
Additionally, it can reconstitute the object back into Python.

%prep
%autosetup -n %{module}-%{version} -p1

# remove remote git badges from readme
sed -i '1,19d;' README.rst

%build
%py_build

%install
%py_install

%if %{with tests}
%check
# NOTE fuzzing tests require atheris which is not packaged, ignore them.
export CI=true
%{__python} -m pytest -v --ignore=fuzzing
%endif

%files
%{py_sitedir}/jsonpickle
%{py_sitedir}/jsonpickle-*.*-info
%doc README.rst
%license LICENSE
