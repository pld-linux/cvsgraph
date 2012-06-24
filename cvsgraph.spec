Summary:	Create graphs of branches and revisions for files in a CVS repository
Summary(pl):	Tworzenie graf�w rozga��zie� i rewizji dla plik�w w repozytorium CVS
Name:		cvsgraph
Version:	1.3.0
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.akhphd.au.dk/~bertho/cvsgraph/release/%{name}-%{version}.tar.gz
URL:		http://www.akhphd.au.dk/~bertho/cvsgraph/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gd-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CvsGraph is a utility to make a graphical representation of all
revisions and branches of a file in a CVS/RCS repository. It has been
inspired by the 'graph' option in WinCVS, but I could not find a
stand-alone version of this graph code. So, it was time to write one.

%description -l pl
CvsGraph to narz�dzie do tworzenia graficznej reprezentacji wszystkich
rewizji i rozga��zie� pliku w repozytorium CVS/RCS. Jest zainspirowane
opcj� 'graph' w programie WinCVS - poniewa� autor nie m�g� znale��
samodzielnej wersji tego kodu, uzna�, �e czas tak� napisa�.

%prep
%setup -q

%build
%configure2_13 \
	--sysconfdir=%{_sysconfdir}/%{name}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5},%{_sysconfdir}/%{name}}

install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{name}.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README cvsgraphwrapper.php3 mkimage.php3
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man?/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}/%{name}.conf
