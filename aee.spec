Summary:	An easy to use text editor
Summary(pl):	�atwy w u�yciu edytor tekstowy
Name:		aee
Version:	2.2.15b
Release:	1
License:	Artistic
Group:		Applications/Editors
URL:		http://mahon.cwx.net/
Source0:	http://mahon.cwx.net/sources/%{name}-%{version}.tar.gz
Patch0:		%{name}-conf.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An easy to use text editor. Intended to be usable with little or no
instruction. Provides both a terminal (curses based) interface and
native X-Windows interface (in which case the executable is called
xae). Features include pop-up menus, journalling (to recover from
system crash or loss of connection), cut-and-paste, multiple buffers
(associated with files or not), and much more.

%prep
%setup -q
%patch0 -p1

%build
%{__make} both \
	OPTFLAGS="%{rpmcflags} -L%{_prefix}/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D xae $RPM_BUILD_ROOT%{_bindir}/xae
install -D %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -D help.ae $RPM_BUILD_ROOT%{_datadir}/%{name}/help.ae
ln -sf aee $RPM_BUILD_ROOT%{_bindir}/rae
ln -sf xae $RPM_BUILD_ROOT%{_bindir}/rxae

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Artistic README.aee aee.1.ps aee.i18n.guide keypad
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help.ae
%{_mandir}/man1/*