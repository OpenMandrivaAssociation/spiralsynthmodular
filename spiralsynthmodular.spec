%define pkg_name spiralmodular

Summary:	Object oriented modular softsynth / sequencer / sampler
Name:		spiralsynthmodular
Version:	0.2.2a
Release:	%mkrel 3
URL:		http://www.pawfal.org/Software/SSM/
Source0:	%{pkg_name}-%{version}.tar.bz2
Source1: 	SpiralLogo48.png
Source2: 	SpiralLogo32.png
Source3: 	SpiralLogo16.png
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	fltk-devel jackit-devel 
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

%build
%configure
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/{%{_bindir},%{_libdir}}
%makeinstall

# Mandrake Menu entry
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): \
needs="x11" \
section="Multimedia/Sound" \
title="Spiral Modular Synth" \
longtitle="Spiral Modular Software Synthesizer" \
command="/usr/bin/%{name}" \
icon="%{name}.png"
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
%{_menudir}/%{name}
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

