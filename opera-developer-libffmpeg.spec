%if %{defined rhel}
%global _missing_build_ids_terminate_build 0
%endif

%global build_for_x86_64 1
%global build_for_i386 1
%global debug_package %{nil}
%global clang 1

%if 0%{?fedora} >= 24
%global clang 0
%endif

%define chromium_system_libs 1
%define opera_chan opera-developer
%define opera_ver 37.0.2163.0

Summary:	Additional FFmpeg library for Opera Web browser providing H264 and MP4 support
Name:		%{opera_chan}-libffmpeg
Version:	50.0.2645.4
Release:	1%{?dist}
Epoch:		5

Group:		Applications/Internet
License:	BSD, LGPL
URL:		https://gist.github.com/lukaszzek/ec04d5c953226c062dac

Source0:	chromium-%{version}.clipped.tar.xz
Source1:	gn-binaries.tar.xz
Source2:	depot_tools.tar.xz
Source3:	check_chromium_version.sh

BuildRequires:  SDL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  bison
BuildRequires:  bzip2-devel
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dirac-devel >= 1.0.0
BuildRequires:  elfutils-libelf-devel
BuildRequires:  elfutils-devel
BuildRequires:  expat-devel
BuildRequires:  fdupes
BuildRequires:  flac-devel
BuildRequires:  flex
BuildRequires:  freetype-devel
BuildRequires:  gperf
BuildRequires:  gsm
BuildRequires:  gsm-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  gyp
BuildRequires:  hicolor-icon-theme
BuildRequires:  hunspell-devel
BuildRequires:  imlib2-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  krb5-devel
BuildRequires:  libcap-devel
BuildRequires:  libdc1394
BuildRequires:  libdc1394-devel
BuildRequires:  libdrm-devel
BuildRequires:  libdrm-devel
BuildRequires:  libffi-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  libogg-devel
BuildRequires:  liboil-devel >= 0.3.15
BuildRequires:  libtheora-devel >= 1.1
BuildRequires:  libusbx-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  ncurses-devel
BuildRequires:  ninja-build
BuildRequires:  pam-devel
BuildRequires:  pciutils-devel
BuildRequires:  perl(Switch)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.6
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(nspr) >= 4.9.5
BuildRequires:  pkgconfig(nss) >= 3.14
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  schroedinger-devel
BuildRequires:  slang-devel
BuildRequires:  speech-dispatcher-devel
BuildRequires:  sqlite-devel
BuildRequires:  texinfo
BuildRequires:  util-linux
BuildRequires:  valgrind-devel
%if 0%{?fedora}
BuildRequires:  python-jinja2
BuildRequires:  python-markupsafe
BuildRequires:  python-ply
%endif

%if 0%{?chromium_system_libs}
BuildRequires:  fontconfig-devel
BuildRequires:  libicu-devel >= 5.4
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  perl-JSON
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  re2-devel
BuildRequires:  snappy-devel
BuildRequires:  usbutils
BuildRequires:  yasm
%endif

%if ! %{defined rhel}
BuildRequires:  faac-devel >= 1.28
BuildRequires:  lame-devel
BuildRequires:  opencore-amr-devel
BuildRequires:  wdiff
BuildRequires:  x264-devel
BuildRequires:  xvidcore-devel
%endif

%if 0%{?clang}
BuildRequires:	clang
%endif

Requires:	%{opera_chan} >= 5:%{opera_ver}

%if 0%{?build_for_x86_64}
%if !0%{?build_for_i386}
ExclusiveArch:    x86_64
%else
ExclusiveArch:    x86_64 i686
%endif
%else
%if 0%{?build_for_i386}
ExclusiveArch:    i686
%endif
%endif

%description
Due to changes in Chromium, Opera is no longer able to use the system FFmpeg
library for H264 video playback on Linux, so H264-encoded videos fail to play by
default (but HTML5 video encoded using different formats, like webm, work). For
legal reasons, Opera may not be distributed with H264 compatible FFmpeg library
included into package.

It's possible to build the extra version of Chromium modified FFmpeg providing
H264 and MP4 support. Opera-libffmpeg package includes this library.

%prep
%setup -n chromium-%{version} -q -a 1 -a 2

%if 0%{?chromium_system_libs}
# files we do not want from upstream source bundles
rm -rf breakpad/src/processor/testdata/
rm -rf chrome/app/test_data/dlls/
rm -rf chrome/common/extensions/docs/
#rm -rf chrome/test/data/
rm -rf chrome/tools/test/reference_build/chrome_linux/
rm -rf components/test/data/component_updater/jebgalgnebhfojomionfpkfelancnnkf/component1.dll
rm -rf content/test/data/
rm -rf net/data/
rm -rf ppapi/examples/
rm -rf ppapi/native_client/tests/
rm -rf third_party/apache-win32/
rm -rf third_party/binutils/
rm -rf third_party/expat/files/
rm -rf third_party/flac/include
rm -rf third_party/flac/src
rm -rf third_party/icu/android
rm -rf third_party/icu/linux
rm -rf third_party/icu/mac
rm -rf third_party/icu/patches
rm -rf third_party/icu/public
rm -rf third_party/icu/source
rm -rf third_party/icu/windows
rm -rf third_party/lcov
rm -rf third_party/libevent/*/*
rm -rf third_party/libevent/*.[ch]
rm -rf libexif/sources
rm -rf libjpeg/*.[ch]
rm -rf libjpeg_turbo
rm -rf libpng/*.[ch]
rm -rf libxslt/libexslt
rm -rf libxslt/libxslt
rm -rf libxslt/linux
rm -rf libxslt/mac
rm -rf libxslt/win32
rm -rf mesa/src/src
rm -rf swig
rm -rf third_party/WebKit/LayoutTests/
rm -rf third_party/WebKit/Tools/Scripts/
rm -rf third_party/xdg-utils/tests/
rm -rf third_party/yasm/source/
rm -rf tools/gyp/test/
rm -rf v8/test/
%endif

# Hard code extra version
FILE=chrome/common/channel_info_posix.cc
sed -i.orig -e 's/getenv("CHROME_VERSION_EXTRA")/"Russian Fedora"/' $FILE
cmp $FILE $FILE.orig && exit 1

%build
# https://groups.google.com/a/chromium.org/forum/#!topic/chromium-packagers/9JX1N2nf4PU
touch chrome/test/data/webui/i18n_process_css_test.html
touch chrome/test/data/webui_test_resources.grd

buildconfig+="-Dwerror=
		-Dlinux_sandbox_chrome_path=%{_libdir}/chromium/chrome
                -Duse_system_ffmpeg=0
                -Dbuild_ffmpegsumo=1
                -Dproprietary_codecs=1
                -Dremove_webcore_debug_symbols=1
                -Dlogging_like_official_build=1
                -Dlinux_fpic=1
                -Ddisable_sse2=1
                -Dcomponent=shared_library
                -Dtoolkit_uses_gtk=0
                -Dffmpeg_branding=Chrome
                -Ddisable_nacl=1
                -Ddisable_glibc=0
                -Ddisable_pnacl=1
                -Ddisable_newlib_untar=0
                -Duse_system_xdg_utils=1
                -Denable_hotwording=0
                -Denable_widevine=1
                -Duse_aura=1
                -Denable_hidpi=1
                -Denable_touch_ui=1
                -Duse_sysroot=0"

%if ! %{defined rhel}
buildconfig+=" -Dlibspeechd_h_prefix=speech-dispatcher/"
%endif

%if 0%{?clang}
buildconfig+=" -Dclang=1
		-Dclang_use_chrome_plugins=0"
%else
buildconfig+=" -Dclang=0"
%endif

%if 0%{?chromium_system_libs}
buildconfig+=" -Duse_system_icu=0
		-Duse_system_flac=1
                -Duse_system_speex=1
                -Duse_system_expat=1
                -Duse_system_libexif=1
                -Duse_system_libevent=1
                -Duse_system_libmtp=1
                -Duse_system_opus=1
                -Duse_system_bzip2=1
                -Duse_system_harfbuzz=1
                -Duse_system_libjpeg=1
                -Duse_system_libpng=1
                -Duse_system_libxslt=1
                -Duse_system_libxml=1
                -Duse_system_libyuv=1
                -Duse_system_nspr=1
                -Duse_system_protobuf=0
                -Duse_system_yasm=1"
%else
buildconfig+=" -Duse_system_icu=0
                -Duse_system_flac=0
                -Duse_system_speex=0
                -Duse_system_expat=0
                -Duse_system_libexif=0
                -Duse_system_libevent=0
                -Duse_system_libmtp=0
                -Duse_system_opus=0
                -Duse_system_bzip2=0
                -Duse_system_harfbuzz=0
                -Duse_system_libjpeg=0
                -Duse_system_libpng=0
                -Duse_system_libxslt=0
                -Duse_system_libxml=0
                -Duse_system_libyuv=0
                -Duse_system_nspr=0
                -Duse_system_protobuf=0
                -Duse_system_yasm=0"
%endif

%ifarch x86_64
buildconfig+=" -Dsystem_libdir=lib64
		-Dtarget_arch=x64"
%endif

buildconfig+=" -Duse_pulseaudio=1
                -Dlinux_link_libpci=1
                -Dlinux_link_gnome_keyring=1
                -Dlinux_link_gsettings=1
                -Dlinux_link_libgps=1
                -Dlinux_link_libspeechd=1
                -Djavascript_engine=v8
                -Dlinux_use_gold_binary=0
                -Dlinux_use_gold_flags=0
                -Dgoogle_api_key=AIzaSyD1hTe85_a14kr1Ks8T3Ce75rvbR1_Dx7Q
                -Dgoogle_default_client_id=4139804441.apps.googleusercontent.com
                -Dgoogle_default_client_secret=KDTRKEZk2jwT_7CDpcmMA--P"

%if 0%{?clang}
export CC=/usr/bin/clang
export CXX=/usr/bin/clang++
# Modern Clang produces a *lot* of warnings 
export CXXFLAGS="${CXXFLAGS} -Wno-unknown-warning-option -Wno-unused-local-typedef -Wunknown-attributes -Wno-tautological-undefined-compare"
export GYP_DEFINES="clang=1"
%endif

%if 0%{?fedora}
# Look, I don't know. This package is spit and chewing gum. Sorry.
rm -rf third_party/jinja2 third_party/markupsafe
ln -s %{python_sitelib}/jinja2 third_party/jinja2
ln -s %{python_sitearch}/markupsafe third_party/markupsafe
%endif

build/linux/unbundle/replace_gyp_files.py $buildconfig

export GYP_GENERATORS='ninja'
./build/gyp_chromium build/all.gyp --depth=. $buildconfig

mkdir -p out/Release

ninja-build -C out/Release ffmpeg

%install
mkdir -p %{buildroot}%{_libdir}/%{opera_chan}/lib_extra
install -m 644 %{_builddir}/chromium-%{version}/out/Release/lib/libffmpeg.so %{buildroot}%{_libdir}/%{opera_chan}/lib_extra/

%files
%{_libdir}/%{opera_chan}/lib_extra/libffmpeg.so

%changelog
* Fri Mar 11 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:50.0.2645.4-1
- Update to 50.0.2645.4
- Match Opera version 37.0.2163.0
- Move libffmpeg.so into */lib_extra/ instead */lib/

* Wed Feb 17 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:50.0.2638.0-1
- Update to 50.0.2638.0
- Match Opera version 37.0.2142.0

* Thu Feb 04 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:49.0.2623.23-1
- Update to 49.0.2623.23
- Match Opera version 36.0.2129.0

* Sat Jan 30 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:49.0.2612.0-3
- One more fix get_sources.sh

* Sat Jan 30 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:49.0.2612.0-2
- Fix get_sources.sh

* Sat Jan 30 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:49.0.2612.0-1
- Change package numeration due to Chromium version
- Match Opera version 36.0.2120.0
- Remove Nosource: 0
- Clip chromium source archive

* Sat Jan 16 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru>
- Add Nosource: 0

* Thu Jan 14 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:36.0.2106.0-2
- Fix i386 build
- Clean up *.spec file

* Wed Jan 13 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:36.0.2106.0-1
- Update to 36.0.2106.0

* Mon Dec 21 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:36.0.2079.0-1
- Update to 36.0.2079.0

* Sat Dec 12 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:36.0.2072.0-1
- Update to 36.0.2072.0

* Thu Dec 03 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:35.0.2064.0-1
- Update to 35.0.2064.0

* Sat Nov 28 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:35.0.2060.0-2
- Remove %{opera_major_ver} due to upstream changes

* Fri Nov 27 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:35.0.2060.0-1
- Update to 35.0.2060.0

* Wed Nov 25 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:35.0.2052.0-1
- Update to 35.0.2052.0

* Thu Nov 12 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:34.0.2044.0-1
- Update to 34.0.2044.0

* Fri Nov 06 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:34.0.2036.2-1
- Update to 34.0.2036.2

* Tue Oct 27 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:34.0.2026.0-1
- Update to 34.0.2026.0

* Tue Oct 20 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:34.0.2023.0-1
- Update to 34.0.2023.0

* Fri Oct 09 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:34.0.2011.0-1
- Update to 34.0.2011.0

* Wed Sep 23 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:34.0.1996.0-1
- Update to 34.0.1996.0

* Thu Sep 10 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:33.0.1982.0-1
- Update to 33.0.1982.0

* Mon Aug 31 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:33.0.1967.0-1.R
- Update to 33.0.1967.0

* Sat Aug 22 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:33.0.1963.0-3.R
- Add workaround for "No such file or directory" build error (affects Chromium >= 46)

* Sat Aug 22 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:33.0.1963.0-2.R
- Rework patch

* Sat Aug 22 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:33.0.1963.0-1.R
- Update to 33.0.1963.0

* Fri Aug 21 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:32.0.1933.0-2.R
- Drop empty debuginfo package (affects Fedora >= 24)

* Thu Aug 20 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:32.0.1933.0-1.R
- Rename to opera-developer-libffmpeg according to new channel
- Update to 32.0.1933.0

* Thu Aug 20 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:31.0.1889.174-1.R
- Update to 31.0.1889.174
- Add check_chromium_version.sh

* Wed Aug 12 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:31.0.1889.99-1.R
- Initial build
