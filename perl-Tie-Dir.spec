%define	pdir	Tie
%define	pnam	Dir
%include	/usr/lib/rpm/macros.perl
Summary:	Tie-Dir perl module
Summary(pl):	Modu³ perla Tie-Dir
Name:		perl-Tie-Dir
Version:	1.02
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tie-Dir perl module.

%description -l pl
Modu³ perla Tie-Dir.

%prep
%setup -q -n Tie-Dir-%{version}

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
