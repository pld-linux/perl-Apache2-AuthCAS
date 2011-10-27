#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Apache2
%define		pnam	AuthCAS
%include	/usr/lib/rpm/macros.perl
Summary:	Apache2::AuthCAS - A configurable Apache authentication module that enables you to protect content on an Apache server using an existing JA-SIG CAS authentication server
#Summary(pl.UTF-8):
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
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache2::AuthCAS module allows a user to protect arbitrary content
on an Apache server with JA-SIG CAS.

Add the following lines to your Apache configuration file to load the
custom configuration tags for CAS and allow for CAS authentication:

PerlLoadModule APR::Table PerlLoadModule
Apache2::AuthCAS::Configuration PerlLoadModule Apache2::AuthCAS

At this point, the configuration directives may be used. All
directives can be nested in Location, Directory, or VirtualHost
sections.

Add the following lines to an Apache configuration file or .htaccess
file:



# %description -l pl.UTF-8 # TODO

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
