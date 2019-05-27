%define major 0
%define famajor 1
%define libname %mklibname augeas %{major}
%define libfa %mklibname fa %{famajor}
%define devname %mklibname augeas -d

# (tpg) optimize it a bit
%global optflags %optflags -O3

Summary:	A library for changing configuration files
Name:		augeas
Version:	1.12.0
Release:	1
Group:		Development/C
License:	LGPLv2.1+
URL:		http://augeas.net/
Source0:	http://download.augeas.net/augeas-%{version}.tar.gz
Patch0:		add-missing-argz-conditional.patch
Patch1:		augeas-1.10.1-check-for-__builtin_mul_overflow_p.patch
BuildRequires:	readline-devel >= 7.0
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(icu-i18n)
BuildRequires:	bison
BuildRequires:	flex

%description
A library for programmatically editing configuration files. Augeas parses
configuration files into a tree structure, which it exposes through its
public API. Changes made through the API are written back to the initially
read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the file
format and the transformation into a tree.

%package lenses
Summary:	Lenses for %{name}
Group:		Development/C

%description lenses
The lenses for %{name}.

%package -n %{libname}
Summary:	Library for %{name}
Group:		Development/C
Requires:	%{name}-lenses = %{EVRD}

%description -n %{libname}
The library for %{name}.

%package -n %{libfa}
Summary:	Library for %{name}
Group:		Development/C
Conflicts:	%{libname} < 0.9.0-2

%description -n %{libfa}
The library for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{libfa} = %{EVRD}

%description -n %{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
# As of augeas 1.11.0, clang 7.0.1:
#BUILDSTDERR: safe-alloc.c:54: error: undefined reference to '__muloti4'
#BUILDSTDERR: safe-alloc.c:94: error: undefined reference to '__muloti4'
export CC=gcc
export CXX=g++

%configure --disable-static
%make_build

%check
#make check

%install
%make_install

mkdir %{buildroot}/%{_lib}
mv %{buildroot}%{_libdir}/libaugeas.so.%{major}* %{buildroot}/%{_lib}
ln -srf %{buildroot}/%{_lib}/libaugeas.so.%{major}.*.* %{buildroot}%{_libdir}/libaugeas.so
mv %{buildroot}%{_libdir}/libfa.so.%{famajor}* %{buildroot}/%{_lib}
ln -srf %{buildroot}/%{_lib}/libfa.so.%{famajor}.*.* %{buildroot}%{_libdir}/libfa.so

# The tests/ subdirectory contains lenses used only for testing, and
# so it shouldn't be packaged.
rm -r %{buildroot}%{_datadir}/augeas/lenses/dist/tests

# In 1.9.0, the example /usr/bin/dump gets installed inadvertently
rm -f %{buildroot}%{_bindir}/dump

%files
%{_bindir}/augmatch
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/fadot
%{_mandir}/man1/*
%{_datadir}/vim/vimfiles/ftdetect/augeas.vim
%{_datadir}/vim/vimfiles/syntax/augeas.vim

%files lenses
%{_datadir}/augeas

%files -n %{libname}
/%{_lib}/libaugeas.so.%{major}*

%files -n %{libfa}
/%{_lib}/libfa.so.%{famajor}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libaugeas.so
%{_libdir}/libfa.so
%{_libdir}/pkgconfig/augeas.pc
