Name: neon
Version: 0.30.0
Release: 1
Summary: An HTTP and WebDAV Client Library
License: LGPL-2.0
Group: Social & Content/Libraries
BuildRequires: krb5-devel
BuildRequires: libexpat-devel
BuildRequires: pkgconfig(gnutls)
BuildRequires: libtool
BuildRequires: pkg-config
BuildRequires: zlib-devel
Url: http://www.webdav.org/neon
Source0: neon-%{version}.tar.gz

%description
neon is an HTTP and WebDAV client library with a C interface.

%package -n libneon
Summary: An HTTP and WebDAV Client Library
Group: Social & Content/Libraries


%description -n libneon
neon is an HTTP and WebDAV client library with a C interface.

%package -n libneon-devel
Summary: An HTTP and WebDAV Client Library
Group: Social & Content/Libraries
Requires: glibc-devel
Requires: libneon = %{version}

%description -n libneon-devel
neon is an HTTP and WebDAV client library with a C interface.

%prep
%setup -q -n %{name}-%{version}

%build
rm -f aclocal.m4 ltmain.sh
sh autogen.sh
%configure \
    --with-ssl=gnutls \
    --enable-threadsafe-ssl=posix \
    --with-expat \
    --disable-nls \
    --enable-shared \
    --disable-static \
    --enable-warnings \
    --with-pic
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}/%{_datadir}/doc/neon-%{version}/html


%post -n libneon -p /sbin/ldconfig
%postun -n libneon -p /sbin/ldconfig

%files -n libneon
%{_libdir}/*.so.27*


%files -n libneon-devel
%{_bindir}/neon-config
%dir %{_includedir}/neon
%{_includedir}/neon/*.h
%{_mandir}/*/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/neon.pc
