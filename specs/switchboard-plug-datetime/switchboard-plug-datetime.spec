%global __provides_exclude_from ^%{_libdir}/switchboard/.*\\.so$

%global plug_name datetime
%global plug_type system

Name:           switchboard-plug-%{plug_name}
Summary:        Switchboard Date and Time plug
Version:        2.1.4
Release:        1%{?dist}
License:        GPLv3

URL:            https://github.com/elementary/%{name}
Source0:        https://github.com/elementary/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  vala >= 0.22.0

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(switchboard-2.0)

Requires:       switchboard%{?_isa}
Supplements:    switchboard%{?_isa}


%description
A switchboard plug to configure date and time settings.


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
%license COPYING

%{_libdir}/switchboard/%{plug_type}/lib%{plug_name}.so


%changelog
* Tue Oct 09 2018 Fabio Valentini <decathorpe@gmail.com> - 2.1.4-1
- Update to version 2.1.4.

* Thu Jun 07 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.3-1
- Update to version 0.1.3.

* Thu Jan 04 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-4
- Clean up .spec file.

* Tue Nov 07 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-3
- Rebuild for the granite 0.5 soname bump.

* Tue Jun 20 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-2
- Clean up .spec file.

* Sat Apr 22 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Update to version 0.1.2.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-3
- Clean up spec.

* Thu Sep 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-2
- Mass rebuild.

* Sun Sep 04 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1.1-1
- Update to version 0.1.1.1.

* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1-1
- Update to version 0.1.1.


