Summary:	X.org driver for NVidia Cards
Name:		x11-driver-video-nv
Version:	2.1.20
Release:	9
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-nv-%{version}.tar.bz2
Patch0:		remove_mibstore_h.patch
Patch1:		0001-RedHat-nv-riva-videomem-autodetection-debugging.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

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
%makeinstall_std

%files
%{_libdir}/xorg/modules/drivers/nv_drv.so
%{_mandir}/man4/nv*

