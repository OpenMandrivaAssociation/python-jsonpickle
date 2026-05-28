%define module jsonpickle
%bcond tests 1

Name:		python-jsonpickle
Version:	4.1.2
Release:	1
Summary:	Python library for serializing any arbitrary object graph into JSON
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/jsonpickle/jsonpickle
Source0:	https://github.com/jsonpickle/jsonpickle/archive/v%{version}/%{name}-%{version}.tar.gz

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

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}"
# NOTE fuzzing tests require atheris which is not packaged, ignore them.
export CI=true
pytest --ignore=fuzzing -W ignore::DeprecationWarning
%endif

%files
%doc README.rst
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info

