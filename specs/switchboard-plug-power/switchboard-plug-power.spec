%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_name power
%global plug_type hardware
%global plug_rdnn io.elementary.switchboard.power

Name:           switchboard-plug-%{plug_name}
Summary:        Switchboard Power Plug
Version:        2.4.0
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala >= 0.30.0

BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}

Requires:       dbus
Requires:       elementary-dpms-helper


%description
Control system power consumption with this Switchboard preference plug.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so

%{_libexecdir}/io.elementary.logind.helper

%{_datadir}/dbus-1/system.d/io.elementary.logind.helper.conf
%{_datadir}/dbus-1/system-services/io.elementary.logind.helper.service
%{_datadir}/metainfo/%{plug_rdnn}.appdata.xml
%{_datadir}/polkit-1/actions/io.elementary.switchboard.power.policy


%changelog
* Sat Nov 16 2019 Fabio Valentini <decathorpe@gmail.com> - 2.4.0-1
- Update to version 2.4.0.

* Tue Jan 29 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.5-1
- Update to version 2.3.5.

* Thu Oct 11 2018 Fabio Valentini <decathorpe@gmail.com> - 2.3.4-1
- Update to version 2.3.4.

* Fri Jun 08 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.3-1
- Update to version 0.3.3.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-4
- Clean up .spec file.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-3
- Rebuild for the granite 0.5 soname bump.

* Sun Aug 06 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-2
- Add patch to remove elementary-dpms-helper usage and dependency.

* Wed Jul 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.2-1
- Update to version 0.3.2.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-2
- Clean up .spec file.

* Fri May 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Update to version 0.3.1.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3-2
- Mass rebuild.

* Tue Sep 13 2016 Fabio Valentini <decathorpe@gmail.com> - 0.3-1
- Update to version 0.3.


