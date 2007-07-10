Name: x11-driver-video-nv
Version: 2.1.2
Release: %mkrel 1
Summary: The X.org driver for NVidia Cards
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-nv-%{version}.tar.bz2
Patch0: x11-driver-video-nv-riva-videomem-autodetection-debugging.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.2
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11-server < 7.0

%description
The X.org driver for NVidia Cards


%prep
%setup -q -n xf86-video-nv-%{version}
%patch0 -p1 -b .redhat-nv-riva-videomem-autodetection-debugging

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

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
%{_mandir}/man4/nv.4.bz2

