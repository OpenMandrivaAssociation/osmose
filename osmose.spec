%define		oname		Osmose
%define		oversion	0-9-96-QT

Name:			osmose
Version:		0.9.96
Release:		%mkrel 1

Summary:	A Sega Master System emulator
License:	GPLv3
Group:		Emulators
URL:		http://bcz.asterope.fr/
Source0:	http://bcz.asterope.fr/osmose/%{oname}-%{oversion}.zip
Source1:	%{name}.png
BuildRequires:	libalsa2-devel
BuildRequires:	libz-devel
BuildRequires:	qt4-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Osmose is a Sega Master System Emulator. Now it has Qt4 GUI.

%prep
%setup -q -n %{oname}-%{oversion}

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

install -d -m 755 %{buildroot}%{_desktopdir}
cat > %{buildroot}%{_desktopdir}/%{name}.desktop << EOF
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
%defattr(-,root,root,-)
%doc Readme.txt License.txt
%{_gamesbindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

