Name: x11-driver-video-nv
Version: 2.1.12
Release: %mkrel 4
Summary: X.org driver for NVidia Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-nv-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.2
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

Patch1: 0001-RedHat-nv-riva-videomem-autodetection-debugging.patch
Patch2: 0002-Do-E-EDID-if-built-against-a-server-that-supports-it.patch
Patch3: 0003-Build-fix-s-pNv-pRiva.patch
Patch4: 0004-Add-missing-pci-id-for-GeForce-7100-GS.patch

%description
x11-driver-video-nv is the X.org driver for NVidia Cards.

%prep
%setup -q -n xf86-video-nv-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/nv_drv.la
%{_libdir}/xorg/modules/drivers/nv_drv.so
%{_mandir}/man4/nv*
