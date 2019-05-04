#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x42C9C8D3AF5EA5E3 (agaida@siduction.org)
#
Name     : libqtxdg
Version  : 3.3.1
Release  : 5
URL      : https://downloads.lxqt.org/downloads/libqtxdg/3.3.1/libqtxdg-3.3.1.tar.xz
Source0  : https://downloads.lxqt.org/downloads/libqtxdg/3.3.1/libqtxdg-3.3.1.tar.xz
Source99 : https://downloads.lxqt.org/downloads/libqtxdg/3.3.1/libqtxdg-3.3.1.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: libqtxdg-data = %{version}-%{release}
Requires: libqtxdg-lib = %{version}-%{release}
Requires: libqtxdg-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : lxqt-build-tools
BuildRequires : qtbase-dev mesa-dev

%description
An example of how to write an CMakeLists.txt to use libqtxdg.
To build this example just use:
cmake ..

%package data
Summary: data components for the libqtxdg package.
Group: Data

%description data
data components for the libqtxdg package.


%package dev
Summary: dev components for the libqtxdg package.
Group: Development
Requires: libqtxdg-lib = %{version}-%{release}
Requires: libqtxdg-data = %{version}-%{release}
Provides: libqtxdg-devel = %{version}-%{release}
Requires: libqtxdg = %{version}-%{release}

%description dev
dev components for the libqtxdg package.


%package lib
Summary: lib components for the libqtxdg package.
Group: Libraries
Requires: libqtxdg-data = %{version}-%{release}
Requires: libqtxdg-license = %{version}-%{release}

%description lib
lib components for the libqtxdg package.


%package license
Summary: license components for the libqtxdg package.
Group: Default

%description license
license components for the libqtxdg package.


%prep
%setup -q -n libqtxdg-3.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556946106
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1556946106
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libqtxdg
cp COPYING %{buildroot}/usr/share/package-licenses/libqtxdg/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/qt5xdg/XdgAction
/usr/include/qt5xdg/XdgAutoStart
/usr/include/qt5xdg/XdgDesktopFile
/usr/include/qt5xdg/XdgDirs
/usr/include/qt5xdg/XdgIcon
/usr/include/qt5xdg/XdgMenu
/usr/include/qt5xdg/XdgMenuWidget
/usr/include/qt5xdg/XdgMimeType
/usr/include/qt5xdg/XmlHelper
/usr/include/qt5xdg/xdgaction.h
/usr/include/qt5xdg/xdgautostart.h
/usr/include/qt5xdg/xdgdesktopfile.h
/usr/include/qt5xdg/xdgdirs.h
/usr/include/qt5xdg/xdgicon.h
/usr/include/qt5xdg/xdgmacros.h
/usr/include/qt5xdg/xdgmenu.h
/usr/include/qt5xdg/xdgmenuwidget.h
/usr/include/qt5xdg/xdgmimetype.h
/usr/include/qt5xdg/xmlhelper.h
/usr/include/qt5xdgiconloader/3.3.1/private/xdgiconloader/xdgiconloader_p.h
/usr/include/qt5xdgiconloader/xdgiconloader_export.h
/usr/lib64/libQt5Xdg.so
/usr/lib64/libQt5XdgIconLoader.so
/usr/lib64/pkgconfig/Qt5Xdg.pc
/usr/lib64/pkgconfig/Qt5XdgIconLoader.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Xdg.so.3
/usr/lib64/libQt5Xdg.so.3.3.1
/usr/lib64/libQt5XdgIconLoader.so.3
/usr/lib64/libQt5XdgIconLoader.so.3.3.1
/usr/lib64/qt5/plugins/iconengines/libQt5XdgIconPlugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libqtxdg/COPYING
