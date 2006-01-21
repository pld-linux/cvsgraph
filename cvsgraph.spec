Summary:	Create graphs of branches and revisions for files in a CVS repository
Summary(pl):	Tworzenie grafów rozga³êzieñ i rewizji dla plików w repozytorium CVS
Name:		cvsgraph
Version:	1.6.0
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.akhphd.au.dk/~bertho/cvsgraph/release/%{name}-%{version}.tar.gz
# Source0-md5:	d8919dc9617ab4cf8bf658b7fbd1df0e
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

%description -l pl
CvsGraph to narzêdzie do tworzenia graficznej reprezentacji wszystkich
rewizji i rozga³êzieñ pliku w repozytorium CVS/RCS. Jest zainspirowane
opcj± 'graph' w programie WinCVS - poniewa¿ autor nie móg³ znale¼æ
samodzielnej wersji tego kodu, uzna³, ¿e czas tak± napisaæ.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
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
