%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_name parental-controls
%global plug_type system

Name:           switchboard-plug-%{plug_name}
Summary:        Switchboard Parental Controls plug
Version:        2.1.5
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  systemd
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

%{?systemd_requires}

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
An easy parental controls plug.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/pantheon-parental-controls-client.desktop


%post
%systemd_post pantheon-parental-controls.service

%preun
%systemd_preun pantheon-parental-controls.service

%postun
%systemd_postun_with_restart pantheon-parental-controls.service


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%dir %{_sysconfdir}/pantheon-%{plug_name}
%config(noreplace) %{_sysconfdir}/pantheon-%{plug_name}/daemon.conf

%{_sysconfdir}/dbus-1/system.d/org.pantheon.ParentalControls.conf

%{_bindir}/pantheon-%{plug_name}-daemon

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_libexecdir}/pantheon-%{plug_name}-client

%{_datadir}/applications/pantheon-%{plug_name}-client.desktop
%{_datadir}/dbus-1/system-services/org.pantheon.ParentalControls.service
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.%{plug_name}.policy

%{_unitdir}/pantheon-%{plug_name}.service


%changelog
* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.5-1
- Update to version 2.1.5.

* Fri Jul 06 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.4-1
- Update to version 0.1.4.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-4
- Clean up .spec file.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-3
- Rebuild for the granite 0.5 soname bump.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-2
- Clean up .spec file.

* Sat Feb 11 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Update to version 0.1.3.

* Tue Jan 03 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-3
- Mass rebuild.

* Fri Sep 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-2
- Add systemd service file back again.

* Thu Sep 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1-1
- Update to version 0.1.


