%define revision	1159

Name:		vbam
Version:	1.8.0.%{revision}
Release:	2

Summary:	A GameBoy Advance emulator
License:	GPLv2+
Group:		Emulators
URL:		http://sourceforge.net/projects/vbam
Source0:	http://sourceforge.net/projects/vbam/files/VBA-M%20svn%20r%{revision}/%{name}-%{version}-src.tar.bz2
Patch0:		vbam-1.8.0-glibc2.10-fix.patch

BuildRequires:	cmake
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(gtkglextmm-1.2)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	ffmpeg-devel
BuildRequires:	sfml-graphics-devel
BuildRequires:	sfml-network-devel
BuildRequires:	sfml-system-devel
BuildRequires:	sfml-window-devel
BuildRequires:	desktop-file-utils

%description
VisualBoyAdvance-M is a GameBoy Advance emulator.
It is based on VisualBoyAdvance and integrates the best 
features from the various other forks.

It also features a GTK frontend.

%prep
%setup -q -c
%patch0 -p1

%build
cmake . -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DENABLE_WX=OFF

%make

%install
%makeinstall_std

#man page
%__install -d -m 755 %{buildroot}%{_mandir}/man1
%__install -m 644 debian/vbam.1 %{buildroot}%{_mandir}/man1

#xdg menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-key="Encoding" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%find_lang g%{name}

%files -f g%{name}.lang
%doc doc/ReadMe.SDL.txt doc/DevInfo.txt
%{_bindir}/*vbam
%config(noreplace) %{_sysconfdir}/vbam.cfg
%{_datadir}/vbam
%{_datadir}/applications/gvbam.desktop
%{_iconsdir}/hicolor/*/apps/vbam.*
%{_mandir}/man1/*


