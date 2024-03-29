#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : HeapDict
Version  : 1.0.1
Release  : 26
URL      : https://files.pythonhosted.org/packages/5a/9b/d8963ae7e388270b695f3b556b6dc9adb70ae9618fba09aa1e7b1886652d/HeapDict-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/9b/d8963ae7e388270b695f3b556b6dc9adb70ae9618fba09aa1e7b1886652d/HeapDict-1.0.1.tar.gz
Summary  : a heap with decrease-key and increase-key operations
Group    : Development/Tools
License  : BSD-3-Clause
Requires: HeapDict-license = %{version}-%{release}
Requires: HeapDict-python = %{version}-%{release}
Requires: HeapDict-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
===============================================================
        
        heapdict implements the MutableMapping ABC, meaning it works pretty
        much like a regular Python dict.  It's designed to be used as a

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
Provides: pypi(heapdict)

%description python3
python3 components for the HeapDict package.


%prep
%setup -q -n HeapDict-1.0.1
cd %{_builddir}/HeapDict-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635739159
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/HeapDict
cp %{_builddir}/HeapDict-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/HeapDict/31a389d465048a3fadc191a3c2ffc9f74a79c3b1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/HeapDict/31a389d465048a3fadc191a3c2ffc9f74a79c3b1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
