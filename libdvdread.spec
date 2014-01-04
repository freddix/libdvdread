Summary:	Library to read DVD images
Name:		libdvdread
Version:	4.2.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dvdnav.mplayerhq.hu/releases/%{name}-%{version}.tar.xz
# Source0-md5:	68cf65b46478ff894be6e91d97dae41a
URL:		http://dvdnav.mplayerhq.hu
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdread provides a simple foundation for reading DVD-Video images.
For reading CSS-encrypted DVDs you will also need libdvdcss package.

%package devel
Summary:	%{name} library headers
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS TODO NEWS
%attr(755,root,root) %{_bindir}/dvdread-config
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/dvdread
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc

