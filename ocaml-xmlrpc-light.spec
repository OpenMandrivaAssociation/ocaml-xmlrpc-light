Name:           ocaml-xmlrpc-light
Version:        0.6.1
Release:        5
Summary:        OCaml library for writing XML-RPC clients and servers

Group:          Development/Other
License:        LGPLv2 with exceptions
URL:            http://code.google.com/p/xmlrpc-light/
Source0:        http://xmlrpc-light.googlecode.com/files/xmlrpc-light-%{version}.tar.gz
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-ocamlnet-nethttpd-devel
# ocamlnet uses ocaml-pcre
BuildRequires:  ocaml-pcre-devel
BuildRequires:  pcre-devel


%description
XmlRpc-Light is an XmlRpc library written in OCaml.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n xmlrpc-light-%{version}

%build
make

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/ocaml/xmlrpc-light
%exclude %{_libdir}/ocaml/xmlrpc-light/*.a
%exclude %{_libdir}/ocaml/xmlrpc-light/*.cmxa
%exclude %{_libdir}/ocaml/xmlrpc-light/*.mli


%files devel
%defattr(-,root,root,-)
%doc LICENSE doc/xmlrpc-light/{html,latex} README.txt
%{_libdir}/ocaml/xmlrpc-light/*.a
%{_libdir}/ocaml/xmlrpc-light/*.cmxa
%{_libdir}/ocaml/xmlrpc-light/*.mli




%changelog
* Mon Sep 14 2009 Florent Monnier <blue_prawn@mandriva.org> 0.6.1-4mdv2010.0
+ Revision: 440744
- rebuild

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-3mdv2010.0
+ Revision: 390309
- rebuild

* Thu Jun 11 2009 Florent Monnier <blue_prawn@mandriva.org> 0.6.1-2mdv2010.0
+ Revision: 385279
- increm rel nb

* Sat May 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-1mdv2010.0
+ Revision: 379012
- don't suplicate spec-helper job

  + Florent Monnier <blue_prawn@mandriva.org>
    - updated version

* Fri Jan 16 2009 Florent Monnier <blue_prawn@mandriva.org> 0.6-1mdv2009.1
+ Revision: 330287
- import ocaml-xmlrpc-light


* Fri Jan 9 2009 Florent Monnier <fmonnier@linux-nantes.org> 0.6-1mdv
- Initial RPM release made from the fedora rpm .spec file (revision 1.4) by Richard W.M. Jones
  (URL: http://cvs.fedoraproject.org/viewvc/devel/ocaml-xmlrpc-light/ )
