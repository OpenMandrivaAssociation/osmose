%define		oname		Osmose
%define		oversion	0-9-96-QT

Name:		osmose
Version:	0.9.96
Release:	3

Summary:	A Sega Master System emulator
License:	GPLv3
Group:		Emulators
URL:		http://bcz.asterope.fr/
Source0:	http://bcz.asterope.fr/osmose/%{oname}-%{oversion}.zip
Source1:	%{name}.png
Patch0:		Osmose-0-9-96-QT-gcc4.7.patch
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	qt4-devel

%description
Osmose is a Sega Master System Emulator. Now it has Qt4 GUI.

%prep
%setup -q -n %{oname}-%{oversion}
%patch0 -p1

%build
%qmake_qt4 %{oname}-%{oversion}.pro
%make

chmod 644 Readme.txt License.txt

%install
rm -rf %{buildroot}
#makeinstall
install -d -m 0755 %{buildroot}%{_gamesbindir}
install -m 0755 %{oname}-%{oversion} %{buildroot}%{_gamesbindir}/%{name}

install -d -m 0755 %{buildroot}%{_datadir}/pixmaps
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Osmose
Comment=%{summary}
Exec=%{_gamesbindir}/%{name}
Icon=%{_datadir}/pixmaps/%{name}.png
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

%files
%doc Readme.txt License.txt
%{_gamesbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jul 28 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.96-1mdv2012.0
+ Revision: 692073
- Fix _desktopdir -> _datadir/applications, as BS is dumb
- Fix BuildRequires
- imported package osmose


* Sun Jul 24 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 0.9.96-1mdv2011.0
- New version 0.9.96
- Qt4 GUI
- Complete spec rewrite

* Wed Mar 24 2010 Guillaume Bedot <littletux@zarb.org> 0.9.2-1plf2010.1
- 0.9.2 (no more GUI)

* Sat Apr 18 2009 Guillaume Bedot <littletux@zarb.org> 0.9.0-0.beta1plf2009.1
- New beta release 0.9.0beta, with an included GUI

* Sat Jan 17 2009 Guillaume Bedot <littletux@zarb.org> 0.8.5-0.beta1plf2009.1
- Release 0.8.5b, with opengl render and system zlib.

* Wed Aug 15 2007 Guillaume Bedot <littletux@zarb.org> 0.8.2-1plf2008.0
- First package of osmose for PLF
