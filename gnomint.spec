#
Summary:	gnoMint - an X.509 Certification Authority management tool
Name:		gnomint
Version:	1.0.0
Release:	1
License:	GPLv3
Group:		Applications
Source0:	http://dl.sourceforge.net/gnomint/%{name}-%{version}.tar.gz
# Source0-md5:	20de7af89f71ebd6c45b41aeab59207c
URL:		http://gnomint.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.6.0
BuildRequires:	gnutls-devel >= 2.7.4
BuildRequires:	gtk+2-devel >= 2.10.0
BuildRequires:	intltool
BuildRequires:	iso-codes >= 0.35
BuildRequires:	libglade2-devel >= 2.5.0
BuildRequires:	libtool
BuildRequires:	sqlite3-devel
Requires(post,preun):   GConf2 >= 2.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnoMint is an X.509 Certification Authority management tool.

Currently, it has two different interfaces: one for GTK/Gnome
environments, and another one for command-line.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_mime_database
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_uninstall %{name}.schemas

%postun
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_datadir}/mime/packages/*.xml
%{_pixmapsdir}/*
