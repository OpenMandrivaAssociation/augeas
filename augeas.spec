%define major 0
%define famajor 1
%define libname %mklibname augeas
%define oldlibname %mklibname augeas 0
%define libfa %mklibname fa
%define oldlibfa %mklibname fa 1
%define devname %mklibname augeas -d

# (tpg) optimize it a bit
%global optflags %optflags -O3

Summary:	A library for changing configuration files
Name:		augeas
Version:	1.14.1
Release:	2
Group:		Development/C
License:	LGPLv2.1+
URL:		https://augeas.net/
# download.augeas.net doesn't have any versions newer than 1.12.0
#Source0:	http://download.augeas.net/augeas-%{version}.tar.gz
# so let's use the github repo instead https://github.com/hercules-team/augeas
Source0:	https://github.com/hercules-team/augeas/releases/download/release-%{version}/augeas-%{version}.tar.gz
BuildSystem:	autotools
BuildRequires:	automake
BuildRequires:	readline-devel >= 7.0
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(icu-i18n)
BuildRequires:	bison
BuildRequires:	flex
%if %{cross_compiling}
BuildOption:	--disable-gnulib-tests
%endif

%patchlist
add-missing-argz-conditional.patch
augeas-1.14.1-fix-out-of-tree-build.patch

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
%rename %{oldlibname}

%description -n %{libname}
The library for %{name}.

%package -n %{libfa}
Summary:	Library for %{name}
Group:		Development/C
Conflicts:	%{libname} < 0.9.0-2
%rename %{oldlibfa}

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

%files
%{_bindir}/augmatch
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/augprint
%{_bindir}/fadot
%{_mandir}/man1/*
%{_datadir}/vim/vimfiles/ftdetect/augeas.vim
%{_datadir}/vim/vimfiles/syntax/augeas.vim
%{_datadir}/bash-completion/completions/*

%files lenses
%{_datadir}/augeas

%files -n %{libname}
%{_libdir}/libaugeas.so.%{major}*

%files -n %{libfa}
%{_libdir}/libfa.so.%{famajor}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libaugeas.so
%{_libdir}/libfa.so
%{_libdir}/pkgconfig/augeas.pc
