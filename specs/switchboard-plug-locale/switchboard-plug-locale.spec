%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

Name:           switchboard-plug-locale
Summary:        Adjust Locale settings from Switchboard
Version:        0.2.3
Release:        6%{?dist}
License:        LGPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  vala >= 0.22.0
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(switchboard-2.0)

Supplements:    switchboard%{?_isa}


%description
Adjust Locale settings from Switchboard.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd

%find_lang locale-plug


%files -f locale-plug.lang
%doc README.md
%license COPYING

%{_libdir}/switchboard/personal/pantheon-locale/

%{_datadir}/glib-2.0/schemas/org.pantheon.switchboard.plug.locale.gschema.xml
%{_datadir}/polkit-1/actions/org.pantheon.switchboard.locale.policy


%changelog
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


