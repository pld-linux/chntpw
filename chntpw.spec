Summary:	NT SAM password recovery utility
Summary(pl):	Narzêdzie do odtwarzania hase³ NT SAM
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
chntpw to narzêdzie do odtwarzania hase³ NT SAM. Ten ma³y program
dostarcza sposób na ogl±danie informacji i zmianê hase³ u¿ytkowników
w pliku bazy u¿ytkowników Windows NT/2000. Nie trzeba znaæ starych
hase³, poniewa¿ zostan± one nadpisane. Ponadto pakiet zawiera prosty
edytor rejestru (zapis danych o tym samym rozmiarze) i edytor
szesnastkowy pozwalaj±cy na modyfikowanie bitów i bajtów w dowolnym
pliku. Je¶li chcemy mieæ bootkietkê z Linuksem do odtwarzania hase³,
mo¿emy dodaæ to narzêdzie do w³asnych obrazów lub u¿yæ obrazów ze
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
