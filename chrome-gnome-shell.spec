Name:           chrome-gnome-shell
Version:        8.2
Release:        4%{?dist}
Summary:        GNOME Shell integration for Chrome
License:        GPL-3.0+
Group:          System/GUI/GNOME
Url:            https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome

Source0:        %{name}-%{version}.tar.gz
Source1: 	%{name}.1

ExclusiveArch:  x86_64
BuildRequires:  cmake
BuildRequires:  python-devel
BuildRequires:  jq

Requires:       python
Requires:       python-gobject
Requires:	gnome-shell

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Web extension for Google Chrome/Chromium, Vivaldi, Opera (and other WebExtensions capable browsers) and native host messaging connector that provides integration with GNOME Shell and the corresponding extensions repository https://extensions.gnome.org.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DBUILD_EXTENSION=OFF

%install
pushd build
  %make_install
popd
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/man/man1/%{name}.1


%files
%defattr(-,root,root)
%doc README.md
%doc LICENSE*
%{_mandir}/man?/%{name}*.?.*
%{_bindir}/chrome-gnome-shell
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%dir %{_sysconfdir}/chromium/policies
%dir %{_sysconfdir}/chromium/policies/managed
%config(noreplace) %{_sysconfdir}/chromium/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%config(noreplace) %{_sysconfdir}/chromium/policies/managed/chrome-gnome-shell.json
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts
%dir %{_sysconfdir}/opt/chrome/policies
%dir %{_sysconfdir}/opt/chrome/policies/managed
%config(noreplace) %{_sysconfdir}/opt/chrome/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%config(noreplace) %{_sysconfdir}/opt/chrome/policies/managed/chrome-gnome-shell.json
%{python_sitelib}/chrome_gnome_shell-*.egg-info

%dir %{_datadir}/dbus-1
%dir %{_datadir}/icons/gnome
%dir %{_datadir}/icons/gnome/128x128
%dir %{_datadir}/icons/gnome/16x16
%dir %{_datadir}/icons/gnome/48x48
%dir %{_datadir}/icons/gnome/128x128/apps
%dir %{_datadir}/icons/gnome/16x16/apps
%dir %{_datadir}/icons/gnome/48x48/apps
%dir %{_datadir}/dbus-1/services/
%dir %{_prefix}/%{_lib}/mozilla
%dir %{_prefix}/%{_lib}/mozilla/native-messaging-hosts/

%{_datadir}/icons/*/*/*/*
%{_datadir}/applications/org.gnome.ChromeGnomeShell.desktop
%{_datadir}/dbus-1/services/org.gnome.ChromeGnomeShell.service
%{_prefix}/lib64/mozilla/native-messaging-hosts/org.gnome.chrome_gnome_shell.json


%changelog
* Sat Mar 4 2017 Raúl Romero García <raul@bgta.net> - 8.2-1.R
- Updated to version 8.1
* Mon Feb 13 2017 Raúl Romero García <raul@bgta.net> - 8.1-1.R
- Updated to version 8.1
* Sun Jan 8 2017 Raúl Romero García <raul@bgta.net> - 8-1.R
- Updated to version 8
* Tue Dec 27 2016 Raúl Romero García <raul@bgta.net> - 7.2.1-1.R
- Updated to version 7.2.1
* Sat Oct 01 2016 Raúl Romero García <raul@bgta.net> - 7.1-4.R
- Added licese file as %%doc. (Try to fix build error on openSUSE_Leap_42.1).
- Added man page.
* Mon Sep 26 2016 Raúl Romero García <raul@bgta.net> - 7.1-2.R
- Removed unnecessary build step.
* Sun Sep 25 2016 Raúl Romero García <raul@bgta.net> - 7-1.R
- Initial package
