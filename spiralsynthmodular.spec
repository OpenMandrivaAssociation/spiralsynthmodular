%define pkg_name spiralmodular

Summary:	Object oriented modular softsynth / sequencer / sampler
Name:		spiralsynthmodular
Version:	0.2.2a
Release:	%mkrel 4
URL:		http://www.pawfal.org/Software/SSM/
Source0:	%{pkg_name}-%{version}.tar.bz2
Source1: 	SpiralLogo48.png
Source2: 	SpiralLogo32.png
Source3: 	SpiralLogo16.png
Patch0:		spiralmodular-fix-build.patch
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	fltk-devel jackit-devel python-base
BuildRequires:	ladspa-devel libalsa-devel libsndfile-devel
Provides:	SpiralSynthModular
Obsoletes:	SpiralSynthModular

%description
SpiralSynthModular (or SSM) is a object orientated modular softsynth
/ sequencer / sampler.

Audio or control data can be freely passed between the plugins, its
all treated the same. Data can also be fed back on itself for chaotic
effects.

%prep
%setup -q -n %pkg_name-0.2.2
%patch0 -p0

%build
%configure
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/{%{_bindir},%{_libdir}}
%makeinstall

# Mandrake Menu entry
mkdir -p %buildroot%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Encoding=UTF-8
Type=Application
Categories=Audio;
Name=Spiral Modular Synth
Comment=Spiral Modular Software Synthesizer
Exec=/usr/bin/%{name}
Icon=%{name}.png
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%doc CHANGES COPYING README Examples
%{_bindir}/spiralsynthmodular
%{_libdir}/SpiralPlugins
%{_datadir}/applications/mandriva-%{name}.desktop
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

