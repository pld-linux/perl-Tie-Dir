%include	/usr/lib/rpm/macros.perl
%define	pdir	Tie
%define	pnam	Dir
Summary:	Tie::Dir - class definition for reading directories via a tied hash
Summary(pl):	Tie::Dir - definicja klasy do czytania katalogów poprzez powi±zany hasz
Name:		perl-Tie-Dir
Version:	1.02
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a method of reading directories using a hash.

%description -l pl
Ten modu³ udostêpnia sposób czytania katalogów przy u¿yciu hasza.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Tie/Dir.pm
%{_mandir}/man3/*
