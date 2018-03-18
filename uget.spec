%define Werror_cflags %{nil}
%define iconname %{name}.png

Summary:	Download manager that uses GTK+
Name:		uget
Version:	2.2.1
Release:	1
Group:		Networking/File transfer
License:	GPL
Url:		http://ugetdm.com/
Source0:	http://downloads.sourceforge.net/urlget/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(appindicator3-0.1)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	intltool
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(libpcre)
Requires:	wget
%rename		urlgfe
%rename		urlget

%description
uGet is a download manager with downloads queue, pause/resume, clipboard
monitor, batch downloads, browser integration (Firefox & Chrome),
multiple connections, speed limit controls, powerful category based
control and much more. Each Category has an independent configuration
that can be inherited by each download in that category.

%files -f %{name}.lang
%doc COPYING INSTALL
%{_bindir}/*
%{_datadir}/applications/%{name}-gtk.desktop
%{_iconsdir}/*
%{_datadir}/sounds/%{name}/*.wav
%{_datadir}/pixmaps/%{name}

#--------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x \
        --with-gnutls \
        --without-openssl

%make

%install
%makeinstall_std INSTALL="install -p"

desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        --delete-original \
        %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop


%find_lang %{name} 


