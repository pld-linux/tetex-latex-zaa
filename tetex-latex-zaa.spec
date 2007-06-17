# TODO:
# - check license
%define short_name zaa
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;
Summary:	Formats for Zeitschrift fuer Analysis und ihre Anwendungn
Summary(de.UTF-8):	Formats für Zeitschrift für Analysis und ihre Anwendungn
Summary(en.UTF-8):	Formats for Zeitschrift für Analysis und ihre Anwendungn
Summary(pl.UTF-8):	Formaty do czasopisma "Zeitschrift für Analysis und ihre Anwendungn"
Name:		tetex-latex-%{short_name}
Version:	1.8
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://www.math.uni-leipzig.de/zaa/%{short_name}.tar
# Source0-md5:	95beb9fd6c7074c19c9ff01da58b8f45
URL:		http://www.math.uni-leipzig.de/zaa/
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Journal for Analysis and its Applications aims at disseminating
theoretical knowledge in the field of analysis and, at the same time,
cultivating and extending its applications. To this end, it publishes
research articles on differential equations, functional analysis and
operator theory, notably with applications to mechanics, physics,
engineering and other disciplines of the exact sciences.

%description -l pl.UTF-8
"Zeitschrift für Analysis und ihre Anwendungn" (Czasopismo analizy i
jej zastosowań) specjalizuje się w rozpowszechnianiu wiedzy
teoretycznej z zakresu analizy i jednocześnie kultywowaniu i
rozszerzaniu jej zastosowań. W związku z tym publikuje artykuły
badawcze z zakresu równań różniczkowych, analizy funkcyjnej i teorii
operatorów, w szczególności z zastosowaniami w mechanice, fizyce,
inżynierii i innych dziedzinach nauk ścisłych.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install *.cls $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc *.tex *.pdf *.ps
%dir %{_datadir}/texmf/tex/latex/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}/*.cls
