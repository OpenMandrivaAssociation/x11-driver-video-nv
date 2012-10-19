Name:		x11-driver-video-nv
Version:	2.1.20
Release:	2
Summary:	X.org driver for NVidia Cards
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-nv-%{version}.tar.bz2
Patch1:		0001-RedHat-nv-riva-videomem-autodetection-debugging.patch

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	pkgconfig(xorg-server) >= 1.13
BuildRequires:	x11-util-macros >= 1.0.1

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

Conflicts:	xorg-x11-server < 7.0

%description
x11-driver-video-nv is the X.org driver for NVidia Cards.

%prep
%setup -qn xf86-video-nv-%{version}
%apply_patches
autoreconf -ifs

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/nv_drv.so
%{_mandir}/man4/nv*
