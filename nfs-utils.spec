# TODO
# - where to package pNFS blkmapd client deamon (clients or separate package)
# - consider enabling: libmount-mount
# - should unmount /proc/fs/nfsd and /var/lib/nfs/rpc_pipefs at package
#	uninstall (or in service nfs stop)
#
# Conditional build:
%bcond_with	krb5		# build with MIT Kerberos (+libgssglue) instead of Heimdal
%bcond_without	tirpc		# use librpcsecgss instead of libtirpc
#
Summary:	Kernel NFS server
Summary(pl.UTF-8):	Działający na poziomie jądra serwer NFS
Summary(pt_BR.UTF-8):	Os utilitários para o cliente e servidor NFS do Linux
Summary(ru.UTF-8):	Утилиты для NFS и демоны поддержки для NFS-сервера ядра
Summary(uk.UTF-8):	Утиліти для NFS та демони підтримки для NFS-сервера ядра
Name:		nfs-utils
Version:	1.2.5
Release:	2
License:	GPL v2
Group:		Networking/Daemons
#Source0:	http://www.kernel.org/pub/linux/utils/nfs/%{name}-%{version}.tar.bz2
Source0:	http://downloads.sourceforge.net/project/nfs/nfs-utils/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	8395ac770720b83c5c469f88306d7765
#Source1:	ftp://ftp.linuxnfs.sourceforge.org/pub/nfs/nfs.doc.tar.gz
Source1:	nfs.doc.tar.gz
# Source1-md5:	ae7db9c61c5ad04f83bb99e5caed73da
Source2:	nfs.init
Source3:	nfslock.init
Source4:	nfsfs.init
Source5:	rpcidmapd.init
Source6:	rpcgssd.init
Source7:	rpcsvcgssd.init
Source8:	nfs.sysconfig
Source9:	nfslock.sysconfig
Source10:	nfsfs.sysconfig
Patch0:		%{name}-install.patch
Patch1:		%{name}-statdpath.patch
Patch2:		%{name}-subsys.patch
Patch3:		%{name}-union-mount.patch
Patch4:		%{name}-heimdal.patch
Patch5:		%{name}-heimdal-kcm.patch
URL:		http://nfs.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	keyutils-devel
BuildRequires:	libblkid-devel >= 1.40
BuildRequires:	libmount-devel
BuildRequires:	libcap-devel
BuildRequires:	device-mapper-devel
BuildRequires:	libevent-devel >= 1.2
BuildRequires:	libnfsidmap-devel >= 0.24
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
%if %{with tirpc}
BuildRequires:	libtirpc-devel >= 1:0.1.10-4
%else
BuildRequires:	librpcsecgss-devel >= 0.16
%endif
%if %{with krb5}
BuildRequires:	krb5-devel >= 1.6
BuildRequires:	libgssglue-devel >= 0.1
%else
BuildRequires:	heimdal-devel >= 1.0
%endif
# lucid context fields mismatch with current version of spkm3.h
BuildConflicts:	gss_mech_spkm3-devel
Requires(post):	fileutils
Requires(post):	sed >= 4.0
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-scripts >= 0.4.1.5
Requires:	rpcbind >= 0.1.7
Requires:	setup >= 2.4.6-7
Provides:	nfsdaemon
Obsoletes:	knfsd
Obsoletes:	nfs-server
Obsoletes:	nfsdaemon
Conflicts:	kernel < 2.2.5
Conflicts:	krb5-common < 1.7
ExcludeArch:	armv4l
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the *new* kernel NFS server and related tools. It provides a
much higher level of performance than the traditional Linux user-land
NFS server.

%description -l pl.UTF-8
To jest *nowy* działający na poziomie jądra serwer NFS oraz związane z
nim narzędzia. Serwer ten dostarcza znacznie większą wydajność niż
tradycyjny, działający na poziomie użytkownika serwer NFS.

%description -l pt_BR.UTF-8
O pacote nfs-utils provê os utilitários para o cliente e servidor NFS
do Linux.

%description -l ru.UTF-8
Пакет nfs-utils предоставляет демона для NFS-сервера, включенного в
ядро, и сопутствующие утилиты, которые обеспечивают намного большую
производительность, чем традиционные Linux NFS-сервера, используемые
большинством пользователей.

%description -l uk.UTF-8
Пакет nfs-utils надає демона для NFS-сервера, вбудованого в ядро, та
супутні утиліти, які забезпечують набагато більшу продуктивність, ніж
традиційні Linux NFS-сервери, які використовує більшість користувачів.

%package clients
Summary:	Clients for connecting to a remote NFS server
Summary(pl.UTF-8):	Klienci do łączenia się ze zdalnym serwerem NFS
Group:		Networking
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{version}-%{release}
Requires:	psmisc
Requires:	rc-scripts
Provides:	nfs-server-clients
Provides:	nfsclient
Obsoletes:	knfsd-clients
Obsoletes:	nfs-server-clients
Obsoletes:	nfsclient
Conflicts:	krb5-common < 1.7

%description clients
The nfs-server-clients package contains the showmount program.
Showmount queries the mount daemon on a remote host for information
about the NFS (Network File System) server on the remote host. For
example, showmount can display the clients which are mounted on that
host. This package is not needed to mount NFS volumes.

%description clients -l pl.UTF-8
Pakiet zawiera program showmount służący do odpytywania serwera NFS.
Showmount pyta demona na zdalnej maszynie o informacje NFS na zdalnym
hoście. Na przykład, showmount potrafi pokazać klientów, którzy są
zamountowani na tym serwerze. Ten pakiet nie jest konieczny do
zamountowania zasobów NFS.

%package lock
Summary:	Programs for NFS file locking
Summary(pl.UTF-8):	Programy do obsługi blokowania plików poprzez NFS (lock)
Group:		Networking
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Requires:	rpcbind >= 0.1.7
Provides:	group(rpcstatd)
Provides:	nfslockd
Provides:	user(rpcstatd)
Obsoletes:	knfsd-lock
Obsoletes:	nfslockd

%description lock
The nfs-lock pacage contains programs which support the NFS file lock.
Install nfs-lock if you want to use file lock over NFS.

%description lock -l pl.UTF-8
Ten pakiet zawiera programy umożliwiające wykonywanie blokowania
plików (file locking) poprzez NFS.

%package common
Summary:	Common programs for NFS
Summary(pl.UTF-8):	Wspólne programy do obsługi NFS
Group:		Networking
Requires:	libnfsidmap >= 0.21-3
Conflicts:	mount < 2.13-0.pre7.1

%description common
Common programs for NFS.

%description common -l pl.UTF-8
Wspólne programy do obsługi NFS.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%{__libtoolize}
%{__aclocal} -I aclocal
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-nfsv3 \
	--enable-nfsv4 \
	--enable-nfsv41 \
	--enable-gss \
	--enable-mount \
	--enable-mountconfig \
	--enable-libmount-mount \
%if %{with tirpc}
	--enable-tirpc \
	--enable-ipv6 \
%else
	--disable-tirpc \
	--disable-ipv6 \
%endif
	--with-statdpath=/var/lib/nfs/statd \
	--with-statedir=/var/lib/nfs \
	--with-statduser=rpcstatd \
	--with-start-statd=%{_sbindir}/start-statd \
	--with-tcp-wrappers \
	--with-krb5

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig,exports.d} \
	$RPM_BUILD_ROOT%{_var}/lib/nfs/{rpc_pipefs,v4recovery}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p utils/mount/nfsmount.conf $RPM_BUILD_ROOT/etc

cat >$RPM_BUILD_ROOT%{_sbindir}/start-statd <<EOF
#!/bin/sh
# mount.nfs calls this script when mounting a filesystem with locking
# enabled, but when statd does not seem to be running (based on
# /var/run/rpc.statd.pid).
exec /sbin/service nfslock start
EOF

sed -e "s|#!/bin/bash|#!/bin/sh|" utils/gssd/gss_destroy_creds > $RPM_BUILD_ROOT%{_sbindir}/gss_destroy_creds

mv $RPM_BUILD_ROOT%{_sbindir}/rpcdebug $RPM_BUILD_ROOT/sbin

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfs
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfslock
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfsfs
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/idmapd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/gssd
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/svcgssd
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/nfsd
install %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/nfslock
install %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/nfsfs

> $RPM_BUILD_ROOT%{_var}/lib/nfs/rmtab
> $RPM_BUILD_ROOT%{_sysconfdir}/exports

%{__rm} $RPM_BUILD_ROOT%{_mandir}/man8/rpc.{mountd,nfsd,statd,sm-notify,svcgssd,gssd,idmapd}.8
echo ".so mountd.8"  > 	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.mountd.8
echo ".so nfsd.8"    >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.nfsd.8
echo ".so statd.8"   >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.statd.8
echo ".so sm-notify.8" > $RPM_BUILD_ROOT%{_mandir}/man8/rpc.sm-notify.8
echo ".so gssd.8"    >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.gssd.8
echo ".so idmapd.8"  >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.idmapd.8
echo ".so svcgssd.8" >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.svcgssd.8

touch $RPM_BUILD_ROOT/var/lib/nfs/xtab

ln -sf /bin/true $RPM_BUILD_ROOT/sbin/fsck.nfs

cp -a nfs html

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add nfs
%service nfs restart "NFS daemon"
/sbin/chkconfig --add svcgssd
%service svcgssd restart "RPC svcgssd"

%preun
if [ "$1" = "0" ]; then
	%service nfs stop
	/sbin/chkconfig --del nfs
	%service svcgssd stop
	/sbin/chkconfig --del svcgssd
fi

%post clients
/sbin/chkconfig --add nfsfs
%service nfsfs restart
/sbin/chkconfig --add gssd
%service gssd restart "RPC gssd"

%preun clients
if [ "$1" = "0" ]; then
	%service nfsfs stop
	/sbin/chkconfig --del nfsfs
	%service gssd stop
	/sbin/chkconfig --del gssd
fi

%pre lock
%groupadd -g 191 rpcstatd
%useradd -u 191 -d /var/lib/nfs/statd -s /bin/false -c "RPC statd user" -g rpcstatd rpcstatd

%post lock
/sbin/chkconfig --add nfslock
%service nfslock restart "RPC statd"

%preun lock
if [ "$1" = "0" ]; then
	%service nfslock stop
	/sbin/chkconfig --del nfslock
fi

%postun lock
if [ "$1" = "0" ]; then
	%userremove rpcstatd
	%groupremove rpcstatd
fi

%post common
/sbin/chkconfig --add idmapd
%service idmapd restart "RPC idmapd"

%preun common
if [ "$1" = "0" ]; then
	%service idmapd stop
	/sbin/chkconfig --del idmapd
fi

%triggerpostun -- %{name} < 1.1.0-0.rc1.1
/sbin/chkconfig nfs reset
/sbin/chkconfig svcgssd reset

%triggerpostun lock -- %{name}-lock < 1.1.0-0.rc1.1
/sbin/chkconfig nfslock reset

%triggerpostun clients -- %{name}-clients < 1.1.0-0.rc1.1
if [ -f /etc/sysconfig/nfsclient.rpmsave ]; then
	mv -f /etc/sysconfig/nfsfs{,.rpmnew}
	mv -f /etc/sysconfig/nfsclient.rpmsave /etc/sysconfig/nfsfs
fi
/sbin/chkconfig nfsfs reset
/sbin/chkconfig gssd reset

%triggerpostun common -- %{name}-common < 1.1.0-0.rc1.1
/sbin/chkconfig idmapd reset

%files
%defattr(644,root,root,755)
%doc ChangeLog README html
%attr(755,root,root) /sbin/rpcdebug
%attr(755,root,root) /sbin/fsck.nfs
%attr(755,root,root) %{_sbindir}/exportfs
%attr(755,root,root) %{_sbindir}/rpc.mountd
%attr(755,root,root) %{_sbindir}/rpc.nfsd
%attr(755,root,root) %{_sbindir}/rpc.svcgssd
%attr(755,root,root) %{_sbindir}/nfsstat

%attr(754,root,root) /etc/rc.d/init.d/nfs
%attr(754,root,root) /etc/rc.d/init.d/svcgssd

%attr(664,root,fileshare) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/exports
%dir %{_sysconfdir}/exports.d

%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/nfsd
%config(noreplace) %verify(not md5 mtime size) %{_var}/lib/nfs/xtab
%config(noreplace) %verify(not md5 mtime size) %{_var}/lib/nfs/etab
%config(noreplace) %verify(not md5 mtime size) %{_var}/lib/nfs/rmtab

%{_mandir}/man5/exports.5*
%{_mandir}/man7/nfsd.7*
%{_mandir}/man8/exportfs.8*
%{_mandir}/man8/mountd.8*
%{_mandir}/man8/nfsd.8*
%{_mandir}/man8/nfsstat.8*
%{_mandir}/man8/rpc.mountd.8*
%{_mandir}/man8/rpc.nfsd.8*
%{_mandir}/man8/rpc.svcgssd.8*
%{_mandir}/man8/rpcdebug.8*
%{_mandir}/man8/svcgssd.8*

%files lock
%defattr(644,root,root,755)
%attr(700,rpcstatd,rpcstatd) %dir %{_var}/lib/nfs/statd
%attr(700,rpcstatd,rpcstatd) %dir %{_var}/lib/nfs/statd/sm
%attr(700,rpcstatd,rpcstatd) %dir %{_var}/lib/nfs/statd/sm.bak
%attr(600,rpcstatd,rpcstatd) %config(noreplace) %verify(not md5 mtime size) %{_var}/lib/nfs/statd/state
%attr(755,root,root) %{_sbindir}/rpc.statd
%attr(755,root,root) %{_sbindir}/sm-notify
%attr(755,root,root) %{_sbindir}/start-statd
%attr(754,root,root) /etc/rc.d/init.d/nfslock
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/nfslock
%{_mandir}/man8/rpc.sm-notify.8*
%{_mandir}/man8/rpc.statd.8*
%{_mandir}/man8/sm-notify.8*
%{_mandir}/man8/statd.8*

%files clients
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/nfsfs
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/nfsfs
%attr(664,root,fileshare) %config(noreplace) %verify(not md5 mtime size) /etc/nfsmount.conf
%attr(4755,root,root) /sbin/mount.nfs
%attr(4755,root,root) /sbin/umount.nfs
%attr(4755,root,root) /sbin/mount.nfs4
%attr(4755,root,root) /sbin/umount.nfs4
%attr(755,root,root) %{_sbindir}/mountstats
%attr(755,root,root) %{_sbindir}/nfsiostat
%attr(755,root,root) %{_sbindir}/showmount
%attr(755,root,root) %{_sbindir}/rpc.gssd
%attr(754,root,root) /etc/rc.d/init.d/gssd
%{_mandir}/man5/nfsmount.conf.5*
%{_mandir}/man8/gssd.8*
%{_mandir}/man8/mount.nfs.8*
%{_mandir}/man8/mountstats.8*
%{_mandir}/man8/nfsiostat.8*
%{_mandir}/man8/rpc.gssd.8*
%{_mandir}/man8/showmount.8*
%{_mandir}/man8/umount.nfs.8*

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/gss_clnt_send_err
%attr(755,root,root) %{_sbindir}/gss_destroy_creds
%attr(755,root,root) %{_sbindir}/nfsidmap
%attr(755,root,root) %{_sbindir}/rpc.idmapd
%attr(754,root,root) /etc/rc.d/init.d/idmapd
%dir %{_var}/lib/nfs
%dir %{_var}/lib/nfs/rpc_pipefs
%dir %{_var}/lib/nfs/v4recovery
%{_mandir}/man5/nfs.5*
%{_mandir}/man8/idmapd.8*
%{_mandir}/man8/nfsidmap.8*
%{_mandir}/man8/rpc.idmapd.8*
