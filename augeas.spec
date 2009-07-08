%define major 0
%define libname %mklibname augeas %{major}
%define develname %mklibname augeas -d

Name:           augeas
Version:        0.5.1
Release:        %mkrel 3
Summary:        A library for changing configuration files
Group:          Development/C
License:        LGPLv2+
URL:            http://augeas.net/
Source0:        http://augeas.net/download/%{name}-%{version}.tar.gz
BuildRequires:  readline-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
A library for programmatically editing configuration files. Augeas parses
configuration files into a tree structure, which it exposes through its
public API. Changes made through the API are written back to the initially
read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the file
format and the transformation into a tree.

%package -n %develname
Summary:        Development files for %{name}
Group:          Development/C
Provides:       %{name}-devel
Requires:       pkgconfig
Requires:       %{libname} = %{version}-%{release}

%description -n %develname
This package contains libraries and header files for
developing applications that use %{name}.

%package -n %{libname}
Summary:        Libraries for %{name}
Group:          Development/C

%description -n %{libname}
The libraries for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/augtool
%{_bindir}/augparse
%{_bindir}/fadot
%{_mandir}/man1/*
%{_datadir}/augeas

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_libdir}/pkgconfig/augeas.pc

