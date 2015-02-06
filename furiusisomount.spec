%define debug_package %{nil}

Summary:	An ISO, IMG, BIN, MDF and NRG Image management utility
Name:		furiusisomount
Version:	0.11.3.1
Release:	3
License:	GPLv3+
Group:		Archiving/Cd burning
Url:		https://launchpad.net/furiusisomount
Source0:	https://launchpad.net/furiusisomount/python/%{version}/+download/%{name}_%{version}.tar.gz
Patch0:		furiusisomount_0.11.3.1-desktop.patch
Requires:	fuseiso
Requires:	pygtk2.0

%description
Simple Gtk+ Interface to Mount ISO, IMG, BIN, MDF and NRG Image files without
burning to disk.

%files
%{_bindir}/%{name}
%dir %{python_sitelib}/%{name}
%{python_sitelib}/%{name}/*
%{_datadir}/applications/%{name}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

#Remove unneeded files
rm -fr .bzr
rm -fr .project
rm -fr .pydevproject
rm -fr .settings
rm -fr %{name}

%build

%install
install -dm 755 %{buildroot}%{python_sitelib}/%{name}
install -dm 755 %{buildroot}%{_bindir}

cp -r * %{buildroot}%{python_sitelib}/%{name}
install -Dm644 app.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

#Create a working launch script (the included one doesn't work when you move the files around)
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh

python "%{python_sitelib}/%{name}/src/main.py" \$1

EOF

chmod 755 %{buildroot}%{_bindir}/%{name}

