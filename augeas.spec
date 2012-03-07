%define	major	0
%define	famajor	1
%define	libname	%mklibname augeas %{major}
%define	libfa	%mklibname fa %{famajor}
%define	devname	%mklibname augeas -d

Name:		augeas
Version:	0.10.0
Release:	1
Summary:	A library for changing configuration files
Group:		Development/C
License:	LGPv2+
URL:		http://augeas.net/
Source0:	http://augeas.net/download/%{name}-%{version}.tar.gz
Source1:	http://augeas.net/download/%{name}-%{version}.tar.gz.sig
BuildRequires:	readline-devel
BuildRequires:	ruby

%description
A library for programmatically editing configuration files. Augeas parses
configuration files into a tree structure, which it exposes through its
public API. Changes made through the API are written back to the initially
read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the file
format and the transformation into a tree.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Provides:	%{name}-devel
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libfa} = %{version}-%{release}

%description -n	%{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%package -n	%{libname}
Summary:	Library for %{name}
Requires:	%{name}-lenses = %{version}-%{release}
Group:		Development/C

%description -n	%{libname}
The library for %{name}.

%package -n	%{libfa}
Summary:	Library for %{name}
Group:		Development/C
Conflicts:	%{libname} < 0.9.0-2

%description -n	%{libfa}
The library for %{name}.

%package	lenses
Summary:	Lenses for %{name}
Group:		Development/C

%description	lenses
The lenses for %{name}.

%prep
%setup -q

%build
%configure2_5x	--disable-static
%make

%check
%make check

%install
%makeinstall_std

%files
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/fadot
%{_mandir}/man1/*
%{_datadir}/vim/vimfiles/ftdetect/augeas.vim
%{_datadir}/vim/vimfiles/syntax/augeas.vim

%files lenses
%doc AUTHORS COPYING NEWS
%{_datadir}/augeas

%files -n %{libname}
%{_libdir}/libaugeas.so.%{major}*

%files -n %{libfa}
%{_libdir}/libfa.so.%{famajor}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/augeas.pc
