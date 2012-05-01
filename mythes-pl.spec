Name: mythes-pl
Summary: Polish thesaurus
Version: 1.5
Release: 4.1%{?dist}
Source: http://downloads.sourceforge.net/synonimy/OOo2-Thesaurus-%{version}.zip
Group: Applications/Text
URL: http://synonimy.ux.pl/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python, perl
License: LGPLv2+
BuildArch: noarch

%description
Polish thesaurus.

%prep
%setup -q -c

%build
for i in README_th_pl_PL_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_pl_PL_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_pl_PL_v2.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.5-4.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jul 10 2009 Caolan McNamara <caolanm@redhat.com> - 1.5-3
- clean spec

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue May 13 2008 Caolan McNamara <caolanm@redhat.com> - 1.5-1
- latest version

* Wed Nov 28 2007 Caolan McNamara <caolanm@redhat.com> - 1.4-1
- initial version
