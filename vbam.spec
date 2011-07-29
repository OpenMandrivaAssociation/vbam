%define revision	1029

Name:			vbam
Version:		1.8.0.%{revision}
Release:		%mkrel 1

Summary:	A GameBoy Advance emulator
License:	GPLv2+
Group:		Emulators
URL:		http://sourceforge.net/projects/vbam
Source0:	%{name}-%{revision}.tar.bz2
Patch0:		vbam-1.8.0-glibc2.10-fix.patch

BuildRequires:	cmake
BuildRequires:	SDL-devel
BuildRequires:	gtkglextmm-devel
BuildRequires:	libglademm2.4-devel
BuildRequires:	portaudio-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
VisualBoyAdvance-M is a GameBoy Advance emulator.
It is based on VisualBoyAdvance and integrates the best 
features from the various other forks.

It also features a GTK frontend.

%prep
%setup -q -n %{name}-%{revision}
%patch0 -p1

%build
cmake . -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DENABLE_WX=OFF

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#man page
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 debian/vbam.1 %{buildroot}%{_mandir}/man1

#xdg menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Game" \
  --remove-key="Encoding" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%find_lang g%{name}

%if %mdkversion < 200900
%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f g%{name}.lang
%defattr(-,root,root)
%doc doc/ReadMe.SDL.txt doc/DevInfo.txt
%{_bindir}/*vbam
%config(noreplace) %{_sysconfdir}/vbam.cfg
%{_datadir}/vbam
%{_datadir}/applications/gvbam.desktop
%{_iconsdir}/hicolor/*/apps/vbam.*
%{_mandir}/man1/*

