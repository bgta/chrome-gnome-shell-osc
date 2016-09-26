Name:           chrome-gnome-shell
Version:        7.1
Release:        2%{?dist}
Summary:        GNOME Shell integration for Chrome
License:        GPL-3.0+
Group:          System/GUI/GNOME
Url:            https://wiki.gnome.org/Projects/GnomeShellIntegrationForChrome

Source0:        chrome-gnome-shell-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  cmake
BuildRequires:  python-devel

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


%files
%doc README.md
%license LICENSE
%{_bindir}/chrome-gnome-shell
%dir %{_sysconfdir}/chromium
%dir %{_sysconfdir}/chromium/native-messaging-hosts
%dir %{_sysconfdir}/chromium/policies
%dir %{_sysconfdir}/chromium/policies/managed
%config(noreplace) %{_sysconfdir}/chromium/native-messaging-hosts/io.github.ne0sight.gs_chrome_connector.json
%config(noreplace) %{_sysconfdir}/chromium/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%config(noreplace) %{_sysconfdir}/chromium/policies/managed/chrome-gnome-shell.json
%dir %{_sysconfdir}/opt/chrome
%dir %{_sysconfdir}/opt/chrome/native-messaging-hosts
%dir %{_sysconfdir}/opt/chrome/policies
%dir %{_sysconfdir}/opt/chrome/policies/managed
%config(noreplace) %{_sysconfdir}/opt/chrome/native-messaging-hosts/io.github.ne0sight.gs_chrome_connector.json
%config(noreplace) %{_sysconfdir}/opt/chrome/native-messaging-hosts/org.gnome.chrome_gnome_shell.json
%config(noreplace) %{_sysconfdir}/opt/chrome/policies/managed/chrome-gnome-shell.json
%{python_sitelib}/chrome_gnome_shell-*.egg-info

%changelog
* Sun Sep 26 2016 Raúl Romero García <raul@bgta.net> - 7-2.R
- Removed unnecessary build step.
* Sun Sep 25 2016 Raúl Romero García <raul@bgta.net> - 7-1.R
- Initial package
