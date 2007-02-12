#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tie
%define		pnam	Dir
Summary:	Tie::Dir - class definition for reading directories via a tied hash
Summary(pl.UTF-8):   Tie::Dir - definicja klasy do czytania katalogów poprzez powiązany hasz
Name:		perl-Tie-Dir
Version:	1.02
Release:	11
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f0ebfdc20e137dc96dec86f916efbc2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a method of reading directories using a hash.

%description -l pl.UTF-8
Ten moduł udostępnia sposób czytania katalogów przy użyciu hasza.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Tie/Dir.pm
%{_mandir}/man3/*
