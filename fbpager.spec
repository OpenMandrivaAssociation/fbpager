Name:             fbpager
Version:          0.1.4
Release:          %mkrel 1
Summary:          fbpager is a workspace pager dockapp for Fluxbox
License:          MIT
Group:            User Interface/Desktops
Source:           %{name}-%{version}.tar.gz
URL:              http://fluxbox.sourceforge.net/fbpager/
BuildRoot:        %{_tmppath}/%{name}-%{version}-root

BuildRequires:    X11-devel libstdc++-devel
Requires:         libxorg-x11 fluxbox libstdc++

%description
Fbpager is a workspace pager dockapp, particularly useful with the
fbpager window manager. It is largely based on bbpager for Blackbox.

For additional information, see the included README and INSTALL text
files.

%prep

%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS  COPYING ChangeLog INSTALL NEWS README  TODO
%{_bindir}/*
