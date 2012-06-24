Summary:	NT SAM password recovery utility
Summary(pl):	Narz�dzie do odtwarzania hase� NT SAM
Name:		chntpw
Version:	040116
Release:	0.1
License:	chntpw
Group:		Applications/System
Source0:	http://home.eunet.no/~pnordahl/ntpasswd/%{name}-source-%{version}.zip
# Source0-md5:	6c75ac2cf1bf878d107a3f4ebb606959
Patch0:		%{name}-debian.patch
URL:		http://home.eunet.no/~pnordahl/ntpasswd/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chntpw is NT SAM password recovery utility. This little program
provides a way to view information and change user passwords in a
Windows NT/2000 userdatabase file. Old passwords need not be known
since they are overwritten. In addition it also contains a simple
registry editor (same size data writes) and an hex-editor which
enables you to fiddle around with bits and bytes in the file as you
wish. If you want GNU/Linux bootdisks for offline password recovery
you can add this utility to custom image disks or use those provided
at the tools homepage.

%description -l pl
chntpw to narz�dzie do odtwarzania hase� NT SAM. Ten ma�y program
dostarcza spos�b na ogl�danie informacji i zmian� hase� u�ytkownik�w
w pliku bazy u�ytkownik�w Windows NT/2000. Nie trzeba zna� starych
hase�, poniewa� zostan� one nadpisane. Ponadto pakiet zawiera prosty
edytor rejestru (zapis danych o tym samym rozmiarze) i edytor
szesnastkowy pozwalaj�cy na modyfikowanie bit�w i bajt�w w dowolnym
pliku. Je�li chcemy mie� bootkietk� z Linuksem do odtwarzania hase�,
mo�emy doda� to narz�dzie do w�asnych obraz�w lub u�y� obraz�w ze
strony domowej.

%prep
%setup -q -c
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D chntpw $RPM_BUILD_ROOT%{_bindir}/chntpw
install -D chntpw.8 $RPM_BUILD_ROOT%{_mandir}/man8/chntpw.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
