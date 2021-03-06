Name:           perl-Spiffy
Version:        0.46
Release:        4%{?dist}
Summary:        Spiffy Perl Interface Framework For You
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Spiffy/
Source0:        http://www.cpan.org/authors/id/I/IN/INGY/Spiffy-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:v5.8.1
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(Filter::Util::Call)
Provides:       perl(Spiffy)

%description
"Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It attempts
to fix all the nits and warts of traditional Perl OO, in a clean,
straightforward and (perhaps someday) standard way.

%prep
%setup -q -n Spiffy-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes CONTRIBUTING LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon May 22 2017 Yichun Zhang (agentzh) <yichun@openresty.com> 0.46-3
- added missing dependency, Filter::Util::Call.
* Mon May 22 2017 Yichun Zhang (agentzh) <yichun@openresty.com> 0.46-2
- added missing build dependency, Test::More.
* Sun May 21 2017 Yichun Zhang (agentzh) <yichun@openresty.com> 0.46-1
- Specfile autogenerated by cpanspec 1.78.
