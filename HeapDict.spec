#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : HeapDict
Version  : 1.0.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/e2/ca/f5feba2f939c97629dbce52a17acc95a0d10256ef620334795379dda8ce6/HeapDict-1.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e2/ca/f5feba2f939c97629dbce52a17acc95a0d10256ef620334795379dda8ce6/HeapDict-1.0.0.tar.gz
Summary  : a heap with decrease-key and increase-key operations
Group    : Development/Tools
License  : BSD-3-Clause
Requires: HeapDict-license = %{version}-%{release}
Requires: HeapDict-python = %{version}-%{release}
Requires: HeapDict-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
heapdict: a heap with decreased-key and increase-key operations
===============================================================

%package license
Summary: license components for the HeapDict package.
Group: Default

%description license
license components for the HeapDict package.


%package python
Summary: python components for the HeapDict package.
Group: Default
Requires: HeapDict-python3 = %{version}-%{release}
Provides: heapdict-python

%description python
python components for the HeapDict package.


%package python3
Summary: python3 components for the HeapDict package.
Group: Default
Requires: python3-core

%description python3
python3 components for the HeapDict package.


%prep
%setup -q -n HeapDict-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551152443
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/HeapDict
cp LICENSE %{buildroot}/usr/share/package-licenses/HeapDict/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/HeapDict/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
