Name: x11-driver-video-nv
Version: 2.1.6
Release: %mkrel 2
Summary: The X.org driver for NVidia Cards
Group: System/X11
URL: http://xorg.freedesktop.org
# Note local tag xf86-video-nv-2.1.6@mandriva suggested on upstream
# Tag at git checkout 100f5e24da2cbc79ed761083daa9a00b107008ab
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-nv  xorg/drivers/xf86-video-nv
# cd xorg/drivers/xf86-video/nv
# git-archive --format=tar --prefix=xf86-video-nv-2.1.6/ xf86-video-nv-2.1.6@mandriva | bzip2 -9 > xf86-video-nv-2.1.6.tar.bz2
########################################################################
Source0: xf86-video-nv-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-nv-2.1.6@mandriva..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch2: 0002-RedHat-nv-riva-videomem-autodetection-debugging.patch
########################################################################
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.2
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: x11-util-modular
Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for NVidia Cards

%prep
%setup -q -n xf86-video-nv-%{version}

%patch1 -p1
%patch2 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/nv_drv.so
%{_mandir}/man4/nv*
