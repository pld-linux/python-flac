%define		module	pyflac
Summary:	A Python module for the FLAC library
Summary(pl.UTF-8):   Moduł Pythona do biblioteki FLAC
Name:		python-%{module}
Version:	0.0.4
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://www.sacredchao.net/~piman/software/%{module}-%{version}.tar.gz
# Source0-md5:	521bd01bf737030381d5c8aa7de62733
URL:		http://www.sacredchao.net/~piman/
BuildRequires:	flac-devel
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.174
BuildRequires:	swig-python
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Python module for the the FLAC library.

%description -l pl.UTF-8
Moduł Pythona do biblioteki FLAC.

%prep
%setup -q -n %{module}-%{version}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/flac/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/flac
%attr(755,root,root) %{py_sitedir}/flac/*.so
%{py_sitedir}/flac/*.py[co]
