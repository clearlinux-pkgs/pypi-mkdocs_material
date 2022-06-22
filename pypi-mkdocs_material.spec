#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-mkdocs_material
Version  : 8.3.7
Release  : 31
URL      : https://files.pythonhosted.org/packages/10/48/8b1f65a21afbd955b5a3a2129bbbfdb72e613ef1d25956010f75374220d9/mkdocs-material-8.3.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/10/48/8b1f65a21afbd955b5a3a2129bbbfdb72e613ef1d25956010f75374220d9/mkdocs-material-8.3.7.tar.gz
Summary  : Documentation that simply works
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: pypi-mkdocs_material-license = %{version}-%{release}
Requires: pypi-mkdocs_material-python = %{version}-%{release}
Requires: pypi-mkdocs_material-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jinja2)
BuildRequires : pypi(markdown)
BuildRequires : pypi(mkdocs)
BuildRequires : pypi(mkdocs_material_extensions)
BuildRequires : pypi(pygments)
BuildRequires : pypi(pymdown_extensions)

%description
<p align="center">
<a href="https://squidfunk.github.io/mkdocs-material/">
<img src="https://raw.githubusercontent.com/squidfunk/mkdocs-material/master/.github/assets/logo.svg" width="320" alt="Material for MkDocs">
</a>
</p>

%package license
Summary: license components for the pypi-mkdocs_material package.
Group: Default

%description license
license components for the pypi-mkdocs_material package.


%package python
Summary: python components for the pypi-mkdocs_material package.
Group: Default
Requires: pypi-mkdocs_material-python3 = %{version}-%{release}

%description python
python components for the pypi-mkdocs_material package.


%package python3
Summary: python3 components for the pypi-mkdocs_material package.
Group: Default
Requires: python3-core
Provides: pypi(mkdocs_material)
Requires: pypi(jinja2)
Requires: pypi(markdown)
Requires: pypi(mkdocs)
Requires: pypi(mkdocs_material_extensions)
Requires: pypi(pygments)
Requires: pypi(pymdown_extensions)

%description python3
python3 components for the pypi-mkdocs_material package.


%prep
%setup -q -n mkdocs-material-8.3.7
cd %{_builddir}/mkdocs-material-8.3.7
pushd ..
cp -a mkdocs-material-8.3.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655910321
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mkdocs_material
cp %{_builddir}/mkdocs-material-8.3.7/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mkdocs_material/c04750a54aad0aac5aa08619287d869ee66df4b4
cp %{_builddir}/mkdocs-material-8.3.7/material/.icons/fontawesome/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-mkdocs_material/80fb80e63f6d77304c296cefd98e3b5b6ad6fdc9
cp %{_builddir}/mkdocs-material-8.3.7/material/.icons/material/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mkdocs_material/b0e637b59cdb1bcaf705cb3d90e6c4573dcd363e
cp %{_builddir}/mkdocs-material-8.3.7/material/.icons/octicons/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mkdocs_material/9ac1a9e1c7eee2d1d386714412f99d7b1fca0681
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-mkdocs_material/80fb80e63f6d77304c296cefd98e3b5b6ad6fdc9
/usr/share/package-licenses/pypi-mkdocs_material/9ac1a9e1c7eee2d1d386714412f99d7b1fca0681
/usr/share/package-licenses/pypi-mkdocs_material/b0e637b59cdb1bcaf705cb3d90e6c4573dcd363e
/usr/share/package-licenses/pypi-mkdocs_material/c04750a54aad0aac5aa08619287d869ee66df4b4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
