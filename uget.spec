%define Werror_cflags %{nil}
%define iconname %{name}.png

# Workaround duplicate symbols
%global optflags %{optflags} -fcommon

Summary:	Download manager that uses GTK+
Name:		uget
Version:	2.2.3
Release:	6
Group:		Networking/File transfer
License:	GPL
Url:		https://ugetdm.com/
Source0:	https://downloads.sourceforge.net/urlget/%{name}-%{version}-1.tar.gz
Patch0:		uget-2.2.3-use-ayatanta-appindicator.patch

BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(ayatana-appindicator3-0.1)
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
# aria2 is optional but make it recommends because it enable more download features
Recommends:     aria2
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
%autosetup -p1

%build
%configure \
        --with-gnutls \
		--enable-appindicator \
        --without-openssl \
		%nil

%make_build

%install
%make_install INSTALL="install -p"

# .desktop
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        --delete-original \
        %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop

# locales
%find_lang %{name} 


