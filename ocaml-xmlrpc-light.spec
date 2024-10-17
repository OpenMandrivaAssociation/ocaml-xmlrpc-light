%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml library for writing XML-RPC clients and servers
Name:		ocaml-xmlrpc-light
Version:	0.6.1
Release:	7
Group:		Development/Other
License:	LGPLv2+ with exceptions
Url:		https://code.google.com/p/xmlrpc-light/
Source0:	http://xmlrpc-light.googlecode.com/files/xmlrpc-light-%{version}.tar.gz
Patch0:		debian_patches_0002-Compile-with-ocamlnet-3.3.5.patch
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-ocamlnet-devel
BuildRequires:	ocaml-ocamlnet-nethttpd-devel
# ocamlnet uses ocaml-pcre
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-xml-light-devel
BuildRequires:	pkgconfig(libpcre)

%description
XmlRpc-Light is an XmlRpc library written in OCaml.

%files
%doc LICENSE
%{_libdir}/ocaml/xmlrpc-light
%exclude %{_libdir}/ocaml/xmlrpc-light/*.a
%exclude %{_libdir}/ocaml/xmlrpc-light/*.cmxa
%exclude %{_libdir}/ocaml/xmlrpc-light/*.mli

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc LICENSE doc/xmlrpc-light/{html,latex} README.txt
%{_libdir}/ocaml/xmlrpc-light/*.a
%{_libdir}/ocaml/xmlrpc-light/*.cmxa
%{_libdir}/ocaml/xmlrpc-light/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n xmlrpc-light-%{version}
%patch0 -p1

%build
make

%install
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

