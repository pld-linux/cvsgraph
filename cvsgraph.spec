Summary:	Create graphs of branches and revisions for files in a CVS repository
Summary(pl.UTF-8):	Tworzenie grafów rozgałęzień i rewizji dla plików w repozytorium CVS
Name:		cvsgraph
Version:	1.7.0
Release:	3
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.akhphd.au.dk/~bertho/cvsgraph/release/%{name}-%{version}.tar.gz
# Source0-md5:	8194c0c6f6837fcfa3ad0fab5dfc0597
Patch0:		%{name}-config.patch
URL:		http://www.akhphd.au.dk/~bertho/cvsgraph/
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gd-devel >= 2.0.28
Requires:	gd >= 2.0.28
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/%{name}

%description
CvsGraph is a utility to make a graphical representation of all
revisions and branches of a file in a CVS/RCS repository. It has been
inspired by the 'graph' option in WinCVS, but I could not find a
stand-alone version of this graph code. So, it was time to write one.

%description -l pl.UTF-8
CvsGraph to narzędzie do tworzenia graficznej reprezentacji wszystkich
rewizji i rozgałęzień pliku w repozytorium CVS/RCS. Jest zainspirowane
opcją 'graph' w programie WinCVS - ponieważ autor nie mógł znaleźć
samodzielnej wersji tego kodu, uznał, że czas taką napisać.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_sysconfdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name}.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README contrib/
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/*
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
