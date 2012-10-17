%define revision	1097

Name:			vbam
Version:		1.8.0.%{revision}
Release:		%mkrel 1

Summary:	A GameBoy Advance emulator
License:	GPLv2+
Group:		Emulators
URL:		http://sourceforge.net/projects/vbam
Source0:	http://sourceforge.net/projects/vbam/files/VBA-M%20svn%20r%{revision}/%{name}-%{version}.tar.xz
Patch0:		vbam-1.8.0-glibc2.10-fix.patch

BuildRequires:	cmake
BuildRequires:	SDL-devel
BuildRequires:	gtkglextmm-devel
BuildRequires:	libglademm2.4-devel
BuildRequires:	portaudio-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	desktop-file-utils csfml-audio-devel sfml2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
VisualBoyAdvance-M is a GameBoy Advance emulator.
It is based on VisualBoyAdvance and integrates the best 
features from the various other forks.

It also features a GTK frontend.

%prep
%setup -q
%patch0 -p1

%build
cmake . -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} -DENABLE_WX=OFF

%make

%install
%__rm -rf %{buildroot}
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

%clean
%__rm -rf %{buildroot}

%files -f g%{name}.lang
%defattr(-,root,root)
%doc doc/ReadMe.SDL.txt doc/DevInfo.txt
%{_bindir}/*vbam
%config(noreplace) %{_sysconfdir}/vbam.cfg
%{_datadir}/vbam
%{_datadir}/applications/gvbam.desktop
%{_iconsdir}/hicolor/*/apps/vbam.*
%{_mandir}/man1/*



%changelog
* Fri Jan 06 2012 Andrey Bondrov <abondrov@mandriva.org> 1.8.0.1054-1mdv2012.0
+ Revision: 758025
- New version 1.8.0.1054
- Do not remove Game category

* Fri Jul 29 2011 Andrey Bondrov <abondrov@mandriva.org> 1.8.0.1029-1
+ Revision: 692201
- imported package vbam


* Mon Jul 18 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.8.0.1029-1mdv2011.0
- New snapshot
- Fix group
- Rediff patch 0
- Remove PLF references

* Fri Sep 11 2009 Guillaume Bedot <littletux@zarb.org> 1.8.0-0.svn905.1plf2010.0
- new snapshot

* Sat Apr 18 2009 Guillaume Bedot <littletux@zarb.org> 1.8.0-0.svn877.1plf2009.1
- new snapshot

* Fri Jan  9 2009 Guillaume Bedot <littletux@zarb.org> 1.8.0-0.svn847.1plf2009.1
- new snapshot

* Wed Oct 22 2008 Guillaume Bedot <littletux@zarb.org> 1.8.0-0.svn775.1plf2009.1
- First PLF package for vbam
