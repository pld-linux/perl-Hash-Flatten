#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Hash
%define	pnam	Flatten
Summary:	Hash::Flatten - flatten/unflatten complex data hashes
Summary(pl.UTF-8):	Hash::Flatten - wygładź/pomarszcz wartości funkcji skrótu dla złożonych danych
Name:		perl-Hash-Flatten
Version:	1.19
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/B/BB/BBC/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cc2ffc365858b90192dbb8be52311267
URL:		http://search.cpan.org/dist/Hash-Flatten/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Log::Trace)
BuildRequires:	perl(Test::Assertions)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Converts back and forth between a nested hash structure and a flat
hash of delimited key-value pairs. Useful for protocols that only
support key-value pairs (such as CGI and DBMs).

%description -l pl.UTF-8
Konwertuje przód i tył pomiędzy zagnieżdzoną strukturą wartości
funkcji skrótu i płaską wartością funkcji skrótu jako rozdzielone pary
kluczy i wartości.

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
%{perl_vendorlib}/Hash/*.pm
%{_mandir}/man3/*
