#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Apache2
%define		pnam	AuthCAS
%include	/usr/lib/rpm/macros.perl
Summary:	Apache2::AuthCAS - A configurable Apache authentication module
Name:		perl-Apache2-AuthCAS
Version:	0.4
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Apache2/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0ffb1596c34d8cfa437af504fe292245
URL:		http://search.cpan.org/dist/Apache2-AuthCAS/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	apache-mod_perl >= 2.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache2::AuthCAS module allows a user to protect arbitrary content
on an Apache server with JA-SIG CAS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Apache2/*.pm
%{perl_vendorlib}/Apache2/AuthCAS
%{_mandir}/man3/*
