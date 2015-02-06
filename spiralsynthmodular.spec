%define pkg_name spiralmodular

Summary:    Object oriented modular softsynth / sequencer / sampler
Name:       spiralsynthmodular
Version:    0.2.2a
Release:    10
URL:        http://www.pawfal.org/Software/SSM/
Source0:    %{pkg_name}-%{version}.tar.bz2
Source1:    SpiralLogo48.png
Source2:    SpiralLogo32.png
Source3:    SpiralLogo16.png
Patch0:     spiralmodular-fix-build.patch
Patch1:     spiralmodular-0.2.2-gcc43.patch
Patch2:     spiralmodular-0.2.2-newer-fltk.patch
License:    GPL
Group:      Sound
BuildRoot:  %{_tmppath}/%{name}-root
BuildRequires:  fltk-devel jackit-devel python-base
BuildRequires:  ladspa-devel libalsa-devel sndfile-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pixman-1)

%description
SpiralSynthModular (or SSM) is a object orientated modular softsynth
/ sequencer / sampler.

Audio or control data can be freely passed between the plugins, its
all treated the same. Data can also be fed back on itself for chaotic
effects.

%prep
%setup -q -n %pkg_name-0.2.2
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%configure
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/{%{_bindir},%{_libdir}}
%makeinstall

# Mandriva Menu entry
mkdir -p %buildroot%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Categories=Audio;
Name=Spiral Modular Synth
Comment=Spiral Modular Software Synthesizer
Exec=/usr/bin/%{name}
Icon=%{name}
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png


%files
%defattr(-,root,root)
%doc CHANGES COPYING README Examples
%{_bindir}/spiralsynthmodular
%{_libdir}/SpiralPlugins
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.2a-9mdv2011.0
+ Revision: 614949
- the mass rebuild of 2010.1 packages

* Mon Jan 18 2010 Jérôme Brenier <incubusss@mandriva.org> 0.2.2a-8mdv2010.1
+ Revision: 493339
- rebuild for new fltk

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Dec 14 2008 Funda Wang <fwang@mandriva.org> 0.2.2a-6mdv2009.1
+ Revision: 314215
- add patches

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - kill hardcoded icon extension
    - s/Mandrake/Mandriva/
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 0.2.2a-4mdv2008.0
+ Revision: 72256
- buildrequires python-base
- convert menu to XDG
- patch 0: fix build
- use %%mkrel


* Tue Sep 06 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.2.2a-3mdk
- annual rebuild

* Mon Aug 02 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.2a-2mdk
- rebuild for new g++

* Thu Apr 01 2004 Austin Acton <austin@mandrake.org> 0.2.2a-1mdk
- 0.2.2a

* Fri Mar 14 2003 Austin Acton <aacton@yorku.ca> 0.2.1-1mdk
- 0.2.1
- remove patches
- use spiral icon

* Sun Feb 02 2003 Buchan Milne <bgmilne@linux-mandrake.com> 0.2.0-1mdk
- CCRMA->contrib
- Add menu

* Sat Jan 04 2003 Fernando Pablo Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.0
- updated to 0.2.2
- added JackPlugin.so to the list of patches to list

* Sun Dec 08 2002 Fernando Pablo Lopez-Lezcano <nando@ccrma.stanford.edu> 0.2.0rc2
- jack enabled with better ladspa support: 0.2.0 release candidate 2 from:
  http://sourceforge.net/project/showfiles.php?group_id=62620
  (thanks to Steve Harris for the link)

* Mon Oct 21 2002 Fernando Pablo Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.1-1
- updated to 0.1.1

* Thu Jun 27 2002 Fernando Pablo Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-2
- depend explicitly on the fltk version we compiled with

* Fri Jun 21 2002 Fernando Pablo Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.0-1
- upgraded to 0.1.0
- added patches to make jack plugin compile with jack 0.34

* Wed Apr 24 2002 Fernando Pablo Lopez-Lezcano <nando@ccrma.stanford.edu>
- Initial build.
- added patch for jack compilation

