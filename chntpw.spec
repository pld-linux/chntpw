Summary:	NT SAM password recovery utility
Summary(pl.UTF-8):	Narzędzie do odtwarzania haseł NT SAM
Name:		chntpw
Version:	080526
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://home.eunet.no/~pnordahl/ntpasswd/%{name}-source-%{version}.zip
# Source0-md5:	09addfe7ae469677da39ed66d83858d3
Patch0:		%{name}-debian.patch
URL:		http://home.eunet.no/~pnordahl/ntpasswd/
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	unzip
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

%description -l pl.UTF-8
chntpw to narzędzie do odtwarzania haseł NT SAM. Ten mały program
dostarcza sposób na oglądanie informacji i zmianę haseł użytkowników w
pliku bazy użytkowników Windows NT/2000. Nie trzeba znać starych
haseł, ponieważ zostaną one nadpisane. Ponadto pakiet zawiera prosty
edytor rejestru (zapis danych o tym samym rozmiarze) i edytor
szesnastkowy pozwalający na modyfikowanie bitów i bajtów w dowolnym
pliku. Jeśli chcemy mieć bootkietkę z Linuksem do odtwarzania haseł,
możemy dodać to narzędzie do własnych obrazów lub użyć obrazów ze
strony domowej.

%prep
%setup -q
%patch0 -p1

%build
%{__make} chntpw cpnt reged \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install {chntpw,cpnt,reged} $RPM_BUILD_ROOT%{_bindir}
install -D chntpw.8 $RPM_BUILD_ROOT%{_mandir}/man8/chntpw.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
