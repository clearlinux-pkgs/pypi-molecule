#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-molecule
Version  : 6.0.2
Release  : 24
URL      : https://files.pythonhosted.org/packages/e6/60/cc687cbccfb3543b17ba5d404007f7e43edcb7fa3c780b4f9ec1cadee83f/molecule-6.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/e6/60/cc687cbccfb3543b17ba5d404007f7e43edcb7fa3c780b4f9ec1cadee83f/molecule-6.0.2.tar.gz
Summary  : Molecule aids in the development and testing of Ansible roles
Group    : Development/Tools
License  : MIT
Requires: pypi-molecule-bin = %{version}-%{release}
Requires: pypi-molecule-license = %{version}-%{release}
Requires: pypi-molecule-python = %{version}-%{release}
Requires: pypi-molecule-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Molecule provides support for testing with multiple instances, operating
systems and distributions, virtualization providers, test frameworks and
testing scenarios.

%package bin
Summary: bin components for the pypi-molecule package.
Group: Binaries
Requires: pypi-molecule-license = %{version}-%{release}

%description bin
bin components for the pypi-molecule package.


%package license
Summary: license components for the pypi-molecule package.
Group: Default

%description license
license components for the pypi-molecule package.


%package python
Summary: python components for the pypi-molecule package.
Group: Default
Requires: pypi-molecule-python3 = %{version}-%{release}

%description python
python components for the pypi-molecule package.


%package python3
Summary: python3 components for the pypi-molecule package.
Group: Default
Requires: python3-core
Provides: pypi(molecule)
Requires: pypi(ansible_compat)
Requires: pypi(ansible_core)
Requires: pypi(click)
Requires: pypi(click_help_colors)
Requires: pypi(enrich)
Requires: pypi(jinja2)
Requires: pypi(jsonschema)
Requires: pypi(packaging)
Requires: pypi(pluggy)
Requires: pypi(pyyaml)
Requires: pypi(rich)
Requires: pypi(wcmatch)

%description python3
python3 components for the pypi-molecule package.


%prep
%setup -q -n molecule-6.0.2
cd %{_builddir}/molecule-6.0.2
pushd ..
cp -a molecule-6.0.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693409159
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . cerberus
pypi-dep-fix.py . PyYAML
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . cerberus
pypi-dep-fix.py . PyYAML
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-molecule
cp %{_builddir}/molecule-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-molecule/82314adfc4f5f364b3443f5df8a3393fd2121964 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} cerberus
pypi-dep-fix.py %{buildroot} PyYAML
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/molecule

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-molecule/82314adfc4f5f364b3443f5df8a3393fd2121964

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
