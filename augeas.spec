%define	major	0
%define	famajor	1
%define	libname	%mklibname augeas %{major}
%define	libfa	%mklibname fa %{famajor}
%define	devname	%mklibname augeas -d

Name:		augeas
Version:	0.10.0
Release:	3
Summary:	A library for changing configuration files
Group:		Development/C
License:	LGPLv2.1+
URL:		http://augeas.net/
Source0:	http://augeas.net/download/%{name}-%{version}.tar.gz
Source1:	http://augeas.net/download/%{name}-%{version}.tar.gz.sig
Patch0:		augeas-0.10.0-add-libxml2-pkgconfig-dependency.patch
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(libxml-2.0)
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
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{libfa} = %{EVRD}

%description -n	%{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%package -n	%{libname}
Summary:	Library for %{name}
Requires:	%{name}-lenses = %{EVRD}
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
%patch0 -p1 -b .libxml2_pc~

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
%doc AUTHORS NEWS
%{_datadir}/augeas

%files -n %{libname}
%{_libdir}/libaugeas.so.%{major}*

%files -n %{libfa}
%{_libdir}/libfa.so.%{famajor}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/augeas.pc


%changelog
* Wed Mar 07 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.10.0-2
+ Revision: 783199
- add libxml-2.0 dependency to pkgconfig (P0)

* Wed Mar 07 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.10.0-1
+ Revision: 782730
- add buildrequires on pkgconfig(libxml-2.0)
- fix typo in license
- don't ship 'COPYING' as package is LGPL
- fix license version
- use %%{EVRD} macro
- cleanups
- new version

* Thu Dec 15 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.9.0-2
+ Revision: 741420
- added missing asterisks for DSO libs
- rebuild
- split out libfa
- employed majors for both libs
- disabled static
- removed .la files
- cleaned spec

* Fri Aug 19 2011 Michael Scherer <misc@mandriva.org> 0.9.0-1
+ Revision: 695266
- upgrade to latest release

* Tue Jul 12 2011 Wiliam Alves de Souza <wiliam@mandriva.com> 0.8.1-0
+ Revision: 689791
- update to 0.8.1

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-2
+ Revision: 662891
- mass rebuild

* Sat Feb 26 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.8.0-1
+ Revision: 640109
- new version 0.8.0

* Sat Nov 20 2010 Bruno Cornec <bcornec@mandriva.org> 0.7.4-1mdv2011.0
+ Revision: 599201
- Updating augeas to 0.7.4 upstream

* Sat Aug 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.7.3-2mdv2011.0
+ Revision: 569816
- really add signature

* Sat Aug 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.7.3-1mdv2011.0
+ Revision: 569808
- new version
- add signature

* Mon Jul 12 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.7.2-1mdv2011.0
+ Revision: 551229
- new version 0.7.2

* Fri Apr 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.7.1-1mdv2010.1
+ Revision: 538138
- update to 0.7.1

* Thu Jan 28 2010 Frederik Himpe <fhimpe@mandriva.org> 0.7.0-2mdv2010.1
+ Revision: 497703
- Update to new version 0.7.0
- Remove patch integrated upstream

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.0-2mdv2010.1
+ Revision: 484191
- Fix vim syntax file (bug #56363)

* Thu Dec 10 2009 Frederik Himpe <fhimpe@mandriva.org> 0.6.0-1mdv2010.1
+ Revision: 476131
- Update to new version 0.6.0

* Tue Sep 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.3-1mdv2010.0
+ Revision: 443125
- update to new version 0.5.3

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.2-3mdv2010.0
+ Revision: 397167
- fix lib package dependencies

* Sat Jul 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.2-2mdv2010.0
+ Revision: 397142
- split lenses into their own subpackage, and force a dependency from the library package

* Tue Jul 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.5.2-1mdv2010.0
+ Revision: 395898
- update to new version 0.5.2

  + Bruno Cornec <bcornec@mandriva.org>
    - Adds a ruby BuildRequire dep in order to have tests passing correctly

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - enable tests

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.1-3mdv2010.0
+ Revision: 393710
- really fix library package name

* Wed Jul 08 2009 Pascal Terjan <pterjan@mandriva.org> 0.5.1-2mdv2010.0
+ Revision: 393464
- Fix library name

* Tue Jul 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.1-1mdv2010.0
+ Revision: 393237
- import augeas


* Fri Jun  5 2009 David Lutterkort <lutter@redhat.com> - 0.5.1-1
- Install fadot

* Fri Mar 27 2009 David Lutterkort <lutter@redhat.com> - 0.5.0-2
- fadot isn't being installed just yet

* Tue Mar 24 2009 David Lutterkort <lutter@redhat.com> - 0.5.0-1
- New program /usr/bin/fadot

* Mon Mar  9 2009 David Lutterkort <lutter@redhat.com> - 0.4.2-1
- New version

* Fri Feb 27 2009 David Lutterkort <lutter@redhat.com> - 0.4.1-1
- New version

* Fri Feb  6 2009 David Lutterkort <lutter@redhat.com> - 0.4.0-1
- New version

* Mon Jan 26 2009 David Lutterkort <lutter@redhat.com> - 0.3.6-1
- New version

* Tue Dec 23 2008 David Lutterkort <lutter@redhat.com> - 0.3.5-1
- New version

* Mon Feb 25 2008 David Lutterkort <dlutter@redhat.com> - 0.0.4-1
- Initial specfile
