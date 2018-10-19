%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_type personal
%global plug_name locale

%global appname io.elementary.switchboard.locale

Name:           switchboard-plug-locale
Summary:        Adjust Locale settings from Switchboard
Version:        2.4.0
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  vala

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
Adjust Locale settings from Switchboard.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%check
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{appname}.appdata.xml


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}-plug.so
%{_libdir}/switchboard/%{plug_type}/pantheon-%{plug_name}/

%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.appdata.xml
%{_datadir}/polkit-1/actions/%{appname}.policy


%changelog
* Fri Oct 19 2018 Fabio Valentini <decathorpe@gmail.com> - 2.4.0-1
- Update to version 2.4.0.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-6
- Add missing BR: gcc, gcc-c++.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-5
- Rebuild for fedora changes.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-4
- Clean up .spec file.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-3
- Rebuild for the granite 0.5 soname bump.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-2
- Clean up .spec file.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.3-1
- Update to version 0.2.3.

* Fri May 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2-1
- Update to version 0.2.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-2
- Mass rebuild.

* Mon Aug 22 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-1
- Update to version 0.2.1.


