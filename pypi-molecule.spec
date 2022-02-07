#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-molecule
Version  : 3.6.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/11/0e/42f2c3a1d99019b2c8f5e7aadbec10ed72a2bf6305eab0255eaf916ff6cb/molecule-3.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/11/0e/42f2c3a1d99019b2c8f5e7aadbec10ed72a2bf6305eab0255eaf916ff6cb/molecule-3.6.0.tar.gz
Summary  : Molecule aids in the development and testing of Ansible roles
Group    : Development/Tools
License  : MIT
Requires: pypi-molecule-bin = %{version}-%{release}
Requires: pypi-molecule-license = %{version}-%{release}
Requires: pypi-molecule-python = %{version}-%{release}
Requires: pypi-molecule-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(alabaster)
BuildRequires : pypi(ansi2html)
BuildRequires : pypi(ansible_compat)
BuildRequires : pypi(ansible_pygments)
BuildRequires : pypi(arrow)
BuildRequires : pypi(attrs)
BuildRequires : pypi(babel)
BuildRequires : pypi(bcrypt)
BuildRequires : pypi(binaryornot)
BuildRequires : pypi(cached_property)
BuildRequires : pypi(cerberus)
BuildRequires : pypi(certifi)
BuildRequires : pypi(cffi)
BuildRequires : pypi(chardet)
BuildRequires : pypi(charset_normalizer)
BuildRequires : pypi(click)
BuildRequires : pypi(click_help_colors)
BuildRequires : pypi(colorama)
BuildRequires : pypi(commonmark)
BuildRequires : pypi(cookiecutter)
BuildRequires : pypi(coverage)
BuildRequires : pypi(cryptography)
BuildRequires : pypi(dataclasses)
BuildRequires : pypi(distro)
BuildRequires : pypi(docutils)
BuildRequires : pypi(enrich)
BuildRequires : pypi(execnet)
BuildRequires : pypi(filelock)
BuildRequires : pypi(idna)
BuildRequires : pypi(imagesize)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(iniconfig)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jinja2_time)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(more_itertools)
BuildRequires : pypi(packaging)
BuildRequires : pypi(paramiko)
BuildRequires : pypi(pexpect)
BuildRequires : pypi(pip)
BuildRequires : pypi(pluggy)
BuildRequires : pypi(poyo)
BuildRequires : pypi(ptyprocess)
BuildRequires : pypi(py)
BuildRequires : pypi(pycparser)
BuildRequires : pypi(pygments)
BuildRequires : pypi(pynacl)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(python_slugify)
BuildRequires : pypi(pytz)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(requests)
BuildRequires : pypi(rich)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(setuptools_scm_git_archive)
BuildRequires : pypi(simplejson)
BuildRequires : pypi(six)
BuildRequires : pypi(snowballstemmer)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinx_ansible_theme)
BuildRequires : pypi(sphinx_notfound_page)
BuildRequires : pypi(sphinx_rtd_theme)
BuildRequires : pypi(sphinxcontrib_applehelp)
BuildRequires : pypi(sphinxcontrib_devhelp)
BuildRequires : pypi(sphinxcontrib_htmlhelp)
BuildRequires : pypi(sphinxcontrib_jsmath)
BuildRequires : pypi(sphinxcontrib_qthelp)
BuildRequires : pypi(sphinxcontrib_serializinghtml)
BuildRequires : pypi(subprocess_tee)
BuildRequires : pypi(text_unidecode)
BuildRequires : pypi(toml)
BuildRequires : pypi(tomli)
BuildRequires : pypi(typing_extensions)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(wheel)
BuildRequires : pypi(zipp)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
****************
Ansible Molecule
****************
.. image:: https://img.shields.io/pypi/v/molecule
:target: https://pypi.org/project/molecule/
:alt: PyPI Package

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
Requires: pypi(cerberus)
Requires: pypi(click)
Requires: pypi(click_help_colors)
Requires: pypi(cookiecutter)
Requires: pypi(dataclasses)
Requires: pypi(enrich)
Requires: pypi(importlib_metadata)
Requires: pypi(jinja2)
Requires: pypi(packaging)
Requires: pypi(paramiko)
Requires: pypi(pluggy)
Requires: pypi(pyyaml)
Requires: pypi(rich)

%description python3
python3 components for the pypi-molecule package.


%prep
%setup -q -n molecule-3.6.0
cd %{_builddir}/molecule-3.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644249939
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . cerberus
pypi-dep-fix.py . PyYAML
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-molecule
cp %{_builddir}/molecule-3.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-molecule/82314adfc4f5f364b3443f5df8a3393fd2121964
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} cerberus
pypi-dep-fix.py %{buildroot} PyYAML
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mol
/usr/bin/molecule

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-molecule/82314adfc4f5f364b3443f5df8a3393fd2121964

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
