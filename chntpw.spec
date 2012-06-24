Summary:	NT SAM password recovery utility
Name:		chntpw
Version:	030126
Release:	0.1
License:	chntpw
Group:		Applications/System
Source0:	http://ntpass.blaa.net/%{name}-source-%{version}.zip
# Source0-md5:	776a7cb0d6eaf7e41cb67efb6caad577
Patch0:		%{name}-debian.patch
URL:		http://home.eunet.no/~pnordahl/ntpasswd/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NT SAM password recovery utility This little program provides a way to
view information and change user passwords in a Windows NT/2000
userdatabase file. Old passwords need not be known since they are
overwritten. In addition it also contains a simple registry editor
(same size data writes) and an hex-editor which enables you to fiddle
around with bits and bytes in the file as you wish. If you want
GNU/Linux bootdisks for offline password recovery you can add this
utility to custom image disks or use those provided at the tools
homepage.

%prep
%setup -q -c
%patch0 -p1

%build
%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D chntpw $RPM_BUILD_ROOT/%{_bindir}/chntpw
install -D chntpw.8 $RPM_BUILD_ROOT/%{_mandir}/man8/chntpw.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
