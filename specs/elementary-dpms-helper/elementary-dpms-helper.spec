%global srcname dpms-helper
%global appname io.elementary.dpms-helper

Name:           elementary-dpms-helper
Summary:        DPMS helper utiluty for elementary
Version:        1.0
Release:        2%{?dist}
License:        GPLv2

URL:            https://github.com/elementary/%{srcname}
Source0:        https://github.com/elementary/dpms-helper/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  meson

Requires:       glib2

BuildArch:      noarch


%description
Sets DPMS settings found in org.pantheon.dpms.

This program is designed to be called by elementary directly when GNOME
Settings Daemon is not managing the related settings.


%prep
%autosetup -n %{srcname}-%{version}


%build
%meson
%meson_build


%install
%meson_install


%check
# Pantheon is not yet a valid Desktop Environment everywhere
desktop-file-validate \
    %{buildroot}/%{_sysconfdir}/xdg/autostart/%{appname}.desktop || :


%files
%license COPYING
%doc README.md

%config(noreplace) %{_sysconfdir}/xdg/autostart/%{appname}.desktop

%{_bindir}/%{appname}

%{_datadir}/glib-2.0/schemas/io.elementary.dpms.gschema.xml


%changelog
* Thu Oct 25 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0-2
- Ignore desktop-file-validate errors.

* Fri May 18 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0-1
- Initial package for fedora.


