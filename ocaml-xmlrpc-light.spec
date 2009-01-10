Name:           ocaml-xmlrpc-light
Version:        0.6
Release:        %mkrel 1
Summary:        OCaml library for writing XML-RPC clients and servers

Group:          Development/Other
License:        LGPLv2 with exceptions
URL:            http://code.google.com/p/xmlrpc-light/
Source0:        http://xmlrpc-light.googlecode.com/files/xmlrpc-light-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  ocaml-ocamlnet-devel
BuildRequires:  ocaml-ocamlnet-nethttpd-devel
BuildRequires:  dos2unix

#define _use_internal_dependency_generator 0
#define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
#define __find_provides /usr/lib/rpm/ocaml-find-provides.sh

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
dos2unix LICENSE
dos2unix README.txt


%build
make


%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install


%clean
rm -rf %{buildroot}


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


