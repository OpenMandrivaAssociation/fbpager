Name:             fbpager
Version:          0.1.4
Release:          10
Summary:          Workspace pager dockapp for Fluxbox
License:          MIT
Group:            Graphical desktop/Other
Source:           %{name}-%{version}.tar.gz
Patch0:           01-fix_g++_build_error.patch
Patch1:		  fbpager-0.1.4-gcc43.patch
URL:              https://fluxbox.sourceforge.net/fbpager/
BuildRequires:    pkgconfig(x11)
BuildRequires:    pkgconfig(xrender)
Requires:         fluxbox

%description
Fbpager is a workspace pager dockapp, particularly useful with the
fbpager window manager. It is largely based on bbpager for Blackbox.

For additional information, see the included README and INSTALL text
files.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS  COPYING ChangeLog INSTALL NEWS README  TODO
%{_bindir}/*


%changelog
* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 0.1.4-8mdv2011.0
+ Revision: 635414
- tighten BR

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.4-7mdv2011.0
+ Revision: 618258
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.1.4-6mdv2010.0
+ Revision: 428709
- rebuild

* Wed Aug 13 2008 Funda Wang <fwang@mandriva.org> 0.1.4-5mdv2009.0
+ Revision: 271538
- add gcc 4.3 patch from gentoo

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Feb 22 2008 Thierry Vignaud <tv@mandriva.org> 0.1.4-3mdv2008.1
+ Revision: 173840
- make it installable (removing manual lib dependancies)

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 0.1.4-2mdv2008.1
+ Revision: 168492
- rebuild
- fix summary
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Oct 24 2007 Jérôme Soyer <saispo@mandriva.org> 0.1.4-1mdv2008.1
+ Revision: 101712
- Add patch for building
- Add patch for building
- import fbpager


