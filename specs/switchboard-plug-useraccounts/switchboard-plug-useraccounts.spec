%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_name useraccounts
%global plug_type system

Name:           switchboard-plug-%{plug_name}
Summary:        Switchboard User Accounts Plug
Version:        2.2.0
Release:        1%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.34.1

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
Switchboard Plug for managing local user accounts.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{plug_name}-plug


%files -f %{plug_name}-plug.lang
%doc README.md
%license COPYING COPYRIGHT

%{_libdir}/switchboard/system/lib%{plug_name}.so
%{_libdir}/switchboard/system/pantheon-%{plug_name}/

%{_datadir}/polkit-1/actions/org.pantheon.switchboard.user-accounts.policy


%changelog
* Tue Oct 23 2018 Fabio Valentini <decathorpe@gmail.com> - 2.2.0-1
- Update to version 2.2.0.

* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.7-1
- Update to version 2.1.7.

* Wed Aug 29 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6-5
- Add missing BR: gcc, gcc-c++.

* Sun Jun 03 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6-4
- Rebuild for fedora changes.

* Fri Jan 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.6-3
- Clean up .spec file.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.6-2
- Rebuild for the granite 0.5 soname bump.

* Thu Oct 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.6-1
- Update to version 0.1.6.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5-1
- Update to version 0.1.5.

* Wed Jun 28 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.5-1
- Update to version 0.1.5.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4-2
- Clean up .spec file.

* Mon May 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.4-1
- Update to version 0.1.4.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-2
- Mass rebuild.

* Tue Aug 23 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Update to version 0.1.3.


