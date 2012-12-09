Name: x11-driver-video-nv
Version: 2.1.20
Release: 2
Summary: X.org driver for NVidia Cards
Group: System/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-nv-%{version}.tar.bz2
Patch1: 0001-RedHat-nv-riva-videomem-autodetection-debugging.patch

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.12
BuildRequires: x11-util-macros >= 1.0.1

Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-nv is the X.org driver for NVidia Cards.

%prep
%setup -qn xf86-video-nv-%{version}
%apply_patches

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/nv_drv.so
%{_mandir}/man4/nv*



%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.1.20-1
+ Revision: 810706
- version update 2.1.20

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2.1.18-8
+ Revision: 787237
- Rebuild for x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.1.18-7
+ Revision: 748442
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 2.1.18-6
+ Revision: 703737
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 2.1.18-5
+ Revision: 683580
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.18-4
+ Revision: 671158
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 2.1.18-3mdv2011.0
+ Revision: 595721
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 2.1.18-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Sat Jul 31 2010 Thierry Vignaud <tv@mandriva.org> 2.1.18-1mdv2011.0
+ Revision: 563947
- new release

* Wed Mar 17 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.1.17-2mdv2010.1
+ Revision: 523763
- New version: 2.1.17

* Wed Dec 16 2009 Frederik Himpe <fhimpe@mandriva.org> 2.1.16-1mdv2010.1
+ Revision: 479583
- update to new version 2.1.16

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 2.1.15-2mdv2010.1
+ Revision: 464294
- Rebuild for new server

* Fri Sep 25 2009 Thierry Vignaud <tv@mandriva.org> 2.1.15-1mdv2010.0
+ Revision: 448655
- new release

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 2.1.14-1mdv2010.0
+ Revision: 391941
- update to new version 2.1.14

* Wed Apr 08 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 2.1.13-1mdv2009.1
+ Revision: 365205
- new version (2.1.13)

* Mon Mar 30 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 2.1.12-4mdv2009.1
+ Revision: 362475
- Do E-EDID if the server supports it
- Add missing pci id for GeForce 7100 GS

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 2.1.12-3mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 2.1.12-2mdv2009.1
+ Revision: 308171
- rebuild for new X server

* Thu Aug 28 2008 Colin Guthrie <cguthrie@mandriva.org> 2.1.12-1mdv2009.0
+ Revision: 277013
- New version: 2.1.12

* Wed Aug 27 2008 Ander Conselvan de Oliveira <ander@mandriva.com> 2.1.11-1mdv2009.0
+ Revision: 276513
- Update to version 2.1.11

* Wed Jul 02 2008 Thierry Vignaud <tv@mandriva.org> 2.1.10-1mdv2009.0
+ Revision: 230634
- new release
- improved description
- add missing dot at end of description
- improved summary

* Mon May 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 2.1.9-1mdv2009.0
+ Revision: 206308
- Update to upstream release 2.1.9.

* Fri Mar 07 2008 Thierry Vignaud <tv@mandriva.org> 2.1.8-1mdv2008.1
+ Revision: 181287
- new release

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 2.1.7-1mdv2008.1
+ Revision: 165587
- Revert to use upstream tarball and remove local patches.
  New upstream release version 2.1.7.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.1.6-3mdv2008.1
+ Revision: 156614
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 2.1.6-2mdv2008.1
+ Revision: 154842
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-nv-2.1.6@mandriva suggested on upstream
  Tag at git checkout 100f5e24da2cbc79ed761083daa9a00b107008ab
  Existing tag nv-2.1.6 not used just to have a common pattern in all tag
  names.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 24 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.1.6-1mdv2008.1
+ Revision: 101810
- new upstream version: 2.1.6
  (G80: fixes initialization in some laptops)

* Thu Oct 11 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.1.5-1mdv2008.1
+ Revision: 97103
- new upstream version: 2.1.5
  . preliminary pci-rework support
  . added a few more product names
  . LVDS flat panel detection fix
- minor spec cleanup

* Thu Aug 16 2007 Thierry Vignaud <tv@mandriva.org> 2.1.3-1mdv2008.0
+ Revision: 64284
- do not hardcode man pages extension
- new release

* Tue Jul 10 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.1.2-1mdv2008.0
+ Revision: 51061
- new upstream version: 2.1.2

* Mon Jul 02 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.1.1-1mdv2008.0
+ Revision: 47271
- new upstream version: 2.1.1
- no need for autoreconf on %%build, so remove it.

* Tue Jun 19 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.1.0-1mdv2008.0
+ Revision: 41440
- New upstream release: 2.1.1

* Thu May 17 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.0.96-1mdv2008.0
+ Revision: 27658
- new version: 2.0.96

* Thu May 03 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 2.0.95-1mdv2008.0
+ Revision: 22101
- new version: 2.0.95
  Notice this new version requires x11-server >= 1.2 due
  to the RandR 1.1 compatibility layer

* Fri Apr 20 2007 Thierry Vignaud <tv@mandriva.org> 2.0.2-1mdv2008.0
+ Revision: 16016
- new release (riva128 is dead; use nv_drv.so instead)

