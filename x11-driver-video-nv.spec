Summary:	X.org driver for NVidia Cards
Name:		x11-driver-video-nv
Version:	2.1.23.1
Release:	1
Group:		System/X11
License:	MIT
Url:		https://xorg.freedesktop.org
# Replace not maintained freedesktop version with Xlibre
Source0:  https://github.com/X11Libre/xf86-video-nv/archive/refs/tags/xlibre-xf86-video-nv-%{version}.tar.gz
#Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-nv-%{version}.tar.xz
#Patch1:		0001-RedHat-nv-riva-videomem-autodetection-debugging.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-nv is the X.org driver for NVidia Cards.

%prep
%autosetup -n xf86-video-nv-xlibre-xf86-video-nv-%{version} -p1

%build
autoreconf -ifs
%configure
%make_build

%install
%make_install

%files
%{_libdir}/xorg/modules/drivers/nv_drv.so
%{_mandir}/man4/nv*
