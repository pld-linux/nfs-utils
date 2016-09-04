#
# Conditional build:
%bcond_with	krb5		# build with MIT Kerberos instead of Heimdal
%bcond_without	tirpc		# use librpcsecgss instead of libtirpc
#
Summary:	Kernel NFS server
Summary(pl.UTF-8):	Działający na poziomie jądra serwer NFS
Summary(pt_BR.UTF-8):	Os utilitários para o cliente e servidor NFS do Linux
Summary(ru.UTF-8):	Утилиты для NFS и демоны поддержки для NFS-сервера ядра
Summary(uk.UTF-8):	Утиліти для NFS та демони підтримки для NFS-сервера ядра
Name:		nfs-utils
Version:	1.3.3
Release:	2
License:	GPL v2
Group:		Networking/Daemons
#Source0:	https://www.kernel.org/pub/linux/utils/nfs/%{name}-%{version}.tar.bz2
Source0:	http://downloads.sourceforge.net/nfs/%{name}-%{version}.tar.bz2
# Source0-md5:	9b87d890669eaaec8e97a2b0a35b2665
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
Source11:	blkmapd.init
Source12:	sunrpc.conf
Source13:	nfs-utils_env.sh
Source102:	nfsd.service
Source103:	nfs-blkmapd.service
Source104:	nfs-exportfs.service
Source105:	nfs-gssd.service
Source106:	nfs-idmapd.service
Source107:	nfs-lock.service
Source108:	nfs-mountd.service
Source109:	nfs-svcgssd.service
Source110:	nfsd.postconfig
Source111:	nfsd.preconfig
Source112:	nfs-lock.preconfig
Patch0:		%{name}-install.patch
Patch1:		%{name}-statdpath.patch
Patch2:		%{name}-subsys.patch
Patch3:		%{name}-union-mount.patch
Patch4:		%{name}-heimdal.patch
Patch5:		%{name}-x32.patch
URL:		http://nfs.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	device-mapper-devel
BuildRequires:	keyutils-devel
BuildRequires:	libblkid-devel >= 1.40
BuildRequires:	libcap-devel
BuildRequires:	libevent-devel >= 1.2
BuildRequires:	libmount-devel
BuildRequires:	libnfsidmap-devel >= 0.24
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	sqlite3-devel >= 3.3
%if %{with tirpc}
BuildRequires:	libtirpc-devel >= 1:0.1.10-4
%else
BuildRequires:	librpcsecgss-devel >= 0.16
%endif
%if %{with krb5}
BuildRequires:	krb5-devel >= 1.6
%else
BuildRequires:	heimdal-devel >= 1.0
%endif
BuildRequires:	rpmbuild(macros) >= 1.623
# lucid context fields mismatch with current version of spkm3.h
BuildConflicts:	gss_mech_spkm3-devel
Requires(post):	fileutils
Requires(post):	sed >= 4.0
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires:	%{name}-common = %{version}-%{release}
Requires:	libevent >= 2.0.14-2
Requires:	rc-scripts >= 0.4.1.5
Requires:	rpcbind >= 0.1.7
Requires:	setup >= 2.4.6-7
Requires:	systemd-units >= 0.38
Provides:	nfsdaemon
Obsoletes:	knfsd
Obsoletes:	nfs-server
Obsoletes:	nfs-utils-systemd
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
Requires(post,preun,postun):	systemd-units >= 38
Requires:	%{name}-common = %{version}-%{release}
Requires:	psmisc
Requires:	rc-scripts
Requires:	systemd-units >= 0.38
Provides:	nfs-server-clients
Provides:	nfsclient
Obsoletes:	knfsd-clients
Obsoletes:	nfs-server-clients
Obsoletes:	nfs-utils-clients-systemd
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

%package common
Summary:	Common programs for NFS
Summary(pl.UTF-8):	Wspólne programy do obsługi NFS
Group:		Networking
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Provides:	user(rpcstatd)
Provides:	group(rpcstatd)
Provides:	nfslockd
Provides:	nfs-utils-lock
Requires:	libnfsidmap >= 0.25-3
Requires:	rc-scripts
Requires:	rpcbind >= 0.1.7
Requires:	systemd-units >= 0.38
Obsoletes:	nfs-utils-common-systemd
Obsoletes:	nfs-utils-lock
Obsoletes:	knfsd-lock
Obsoletes:	nfslockd
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
	--enable-nfsv4 \
	--enable-nfsv41 \
	--enable-gss \
	--enable-mount \
	--enable-mountconfig \
	--enable-libmount-mount \
	--enable-svcgss \
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
	--with-start-statd=/sbin/start-statd \
	--with-tcp-wrappers \
	--without-gssglue \
	--with-krb5

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig,exports.d,modprobe.d} \
	$RPM_BUILD_ROOT%{_var}/lib/nfs/{rpc_pipefs,v4recovery} \
	$RPM_BUILD_ROOT{%{systemdunitdir},%{_datadir}/nfs-utils}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -p utils/mount/nfsmount.conf $RPM_BUILD_ROOT/etc

%{__rm} $RPM_BUILD_ROOT%{_sbindir}/start-statd
cat >$RPM_BUILD_ROOT/sbin/start-statd <<EOF
#!/bin/sh
# mount.nfs calls this script when mounting a filesystem with locking
# enabled, but when statd does not seem to be running (based on
# /var/run/rpc.statd.pid).
exec /sbin/rpc.statd --no-notify
EOF

%{__sed} -i -e 's|%{_sbindir}nfsidmap|/sbin/nfsidmap|g' $RPM_BUILD_ROOT%{_mandir}/man8/nfsidmap.8

for f in rpcdebug blkmapd nfsidmap rpc.gssd rpc.idmapd rpc.statd ; do
	mv $RPM_BUILD_ROOT%{_sbindir}/$f $RPM_BUILD_ROOT/sbin
done

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfs
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfslock
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfsfs
install %{SOURCE5} $RPM_BUILD_ROOT/etc/rc.d/init.d/idmapd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/gssd
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/svcgssd
install %{SOURCE11} $RPM_BUILD_ROOT/etc/rc.d/init.d/blkmapd
install %{SOURCE8} $RPM_BUILD_ROOT/etc/sysconfig/nfsd
install %{SOURCE9} $RPM_BUILD_ROOT/etc/sysconfig/nfslock
install %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/nfsfs

install %{SOURCE12} $RPM_BUILD_ROOT/etc/modprobe.d/sunrpc.conf

install systemd/proc-fs-nfsd.mount $RPM_BUILD_ROOT%{systemdunitdir}/proc-fs-nfsd.mount
install systemd/var-lib-nfs-rpc_pipefs.mount $RPM_BUILD_ROOT%{systemdunitdir}/var-lib-nfs-rpc_pipefs.mount
install %{SOURCE102} $RPM_BUILD_ROOT%{systemdunitdir}/nfsd.service
install %{SOURCE103} $RPM_BUILD_ROOT%{systemdunitdir}/blkmapd.service
install %{SOURCE104} $RPM_BUILD_ROOT%{systemdunitdir}/nfsd-exportfs.service
install %{SOURCE105} $RPM_BUILD_ROOT%{systemdunitdir}/gssd.service
install %{SOURCE106} $RPM_BUILD_ROOT%{systemdunitdir}/idmapd.service
install %{SOURCE107} $RPM_BUILD_ROOT%{systemdunitdir}/nfslock.service
install %{SOURCE108} $RPM_BUILD_ROOT%{systemdunitdir}/nfsd-mountd.service
install %{SOURCE109} $RPM_BUILD_ROOT%{systemdunitdir}/svcgssd.service
install %{SOURCE110} $RPM_BUILD_ROOT%{_datadir}/nfs-utils/nfsd.postconfig
install %{SOURCE111} $RPM_BUILD_ROOT%{_datadir}/nfs-utils/nfsd.preconfig
install %{SOURCE112} $RPM_BUILD_ROOT%{_datadir}/nfs-utils/nfslock.preconfig

# Disable old SysV service for systemd installs
ln -s /dev/null $RPM_BUILD_ROOT%{systemdunitdir}/nfs.service
ln -s /dev/null $RPM_BUILD_ROOT%{systemdunitdir}/nfsfs.service

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
%systemd_post nfsd.service nfsd-exportfs.service nfsd-mountd.service svcgssd.service

%preun
if [ "$1" = "0" ]; then
	%service nfs stop
	/sbin/chkconfig --del nfs
	%service svcgssd stop
	/sbin/chkconfig --del svcgssd
fi
%systemd_preun nfsd.service nfsd-exportfs.service nfsd-mountd.service svcgssd.service

%postun
%systemd_reload

%post clients
/sbin/chkconfig --add nfsfs
%service nfsfs restart
/sbin/chkconfig --add gssd
%service gssd restart "RPC gssd"
/sbin/chkconfig --add blkmapd
%service blkmapd restart "pNFS blkmapd"
%systemd_post blkmapd.service gssd.service

%preun clients
if [ "$1" = "0" ]; then
	%service nfsfs stop
	/sbin/chkconfig --del nfsfs
	%service gssd stop
	/sbin/chkconfig --del gssd
	%service blkmapd stop
	/sbin/chkconfig --del blkmapd
fi
%systemd_preun blkmapd.service gssd.service

%postun clients
%systemd_reload

%pre common
%groupadd -g 191 rpcstatd
%useradd -u 191 -d /var/lib/nfs/statd -s /bin/false -c "RPC statd user" -g rpcstatd rpcstatd

%post common
/sbin/chkconfig --add idmapd
%service idmapd restart "RPC idmapd"
/sbin/chkconfig --add nfslock
%service nfslock restart "RPC statd"
%systemd_post idmapd.service nfslock.service

%preun common
if [ "$1" = "0" ]; then
	%service idmapd stop
	/sbin/chkconfig --del idmapd
	%service nfslock stop
	/sbin/chkconfig --del nfslock
fi
%systemd_preun idmapd.service nfslock.service

%postun common
if [ "$1" = "0" ]; then
	%userremove rpcstatd
	%groupremove rpcstatd
fi
%systemd_reload

%triggerpostun -- %{name} < 1.2.5-7
if [ -f /etc/sysconfig/nfsd ]; then
	. /etc/sysconfig/nfsd
	__RPCMOUNTDOPTIONS=
	[ -n "$MOUNTD_PORT" ] && __RPCMOUNTDOPTIONS="-p $MOUNTD_PORT"
	for vers in 2 3 4 ; do
		__var=$(eval echo \$NFSv$vers)
		[ -n "$__var" -a "$__var" != "yes" ] && \
			__RPCMOUNTDOPTIONS="$__RPCMOUNTDOPTIONS --no-nfs-version $vers"
	done
	if [ -n "$__RPCMOUNTDOPTIONS" ]; then
		%{__cp} -f /etc/sysconfig/nfsd{,.rpmsave}
		echo >>/etc/sysconfig/nfsd
		echo "# Added by rpm trigger" >>/etc/sysconfig/nfsd
		echo "RPCMOUNTDOPTIONS=\"$RPCMOUNTOPTIONS $__RPCMOUNTDOPTIONS\"" >>/etc/sysconfig/nfsd
	fi
fi
%systemd_trigger nfsd.service nfsd-exportfs.service nfsd-mountd.service svcgssd.service

%triggerpostun clients -- %{name}-clients < 1.2.5-7
%systemd_trigger blkmapd.service gssd.service

%triggerpostun common -- %{name}-lock < 1.2.5-3
if [ -f /etc/sysconfig/nfslock.rpmsave ]; then
	mv -f /etc/sysconfig/nfslock{,.rpmnew}
	mv -f /etc/sysconfig/nfslock.rpmsave /etc/sysconfig/nfslock
fi

%triggerpostun common -- %{name}-common < 1.2.5-7
if [ -f /etc/sysconfig/nfslock ]; then
	. /etc/sysconfig/nfslock
	[ -n "$STATD_PORT" ] && STATDOPTS="$STATDOPTS -p $STATD_PORT"
	[ -n "$STATD_OUTPORT" ] && STATDOPTS="$STATDOPTS -o $STATD_OUTPORT"
	if [ -n "$STATDOPTS" ]; then
		%{__cp} -f /etc/sysconfig/nfslock{,.rpmsave}
		echo >>/etc/sysconfig/nfslock
		echo "# Added by rpm trigger" >>/etc/sysconfig/nfslock
		echo "STATDOPTIONS=\"$STATDOPTS\"" >>/etc/sysconfig/nfslock
	fi
fi
%systemd_trigger idmapd.service nfslock.service

%files
%defattr(644,root,root,755)
%doc README html
%attr(755,root,root) /sbin/nfsdcltrack
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
%{_mandir}/man8/nfsdcltrack.8*
%{_mandir}/man8/nfsstat.8*
%{_mandir}/man8/rpc.mountd.8*
%{_mandir}/man8/rpc.nfsd.8*
%{_mandir}/man8/rpc.svcgssd.8*
%{_mandir}/man8/rpcdebug.8*
%{_mandir}/man8/svcgssd.8*

%{systemdunitdir}/nfs.service
%{systemdunitdir}/nfsd.service
%{systemdunitdir}/nfsd-exportfs.service
%{systemdunitdir}/nfsd-mountd.service
%{systemdunitdir}/svcgssd.service
%{systemdunitdir}/proc-fs-nfsd.mount
%attr(755,root,root) %{_datadir}/nfs-utils/nfsd.postconfig
%attr(755,root,root) %{_datadir}/nfs-utils/nfsd.preconfig

%files clients
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/blkmapd
%attr(754,root,root) /etc/rc.d/init.d/gssd
%attr(754,root,root) /etc/rc.d/init.d/nfsfs
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/nfsfs
%attr(664,root,fileshare) %config(noreplace) %verify(not md5 mtime size) /etc/nfsmount.conf
%attr(4755,root,root) /sbin/mount.nfs
%attr(4755,root,root) /sbin/umount.nfs
%attr(4755,root,root) /sbin/mount.nfs4
%attr(4755,root,root) /sbin/umount.nfs4
%attr(755,root,root) /sbin/blkmapd
%attr(755,root,root) /sbin/osd_login
%attr(755,root,root) /sbin/rpc.gssd
%attr(755,root,root) %{_sbindir}/mountstats
%attr(755,root,root) %{_sbindir}/nfsiostat
%attr(755,root,root) %{_sbindir}/showmount
%{_mandir}/man5/nfsmount.conf.5*
%{_mandir}/man8/blkmapd.8*
%{_mandir}/man8/gssd.8*
%{_mandir}/man8/mount.nfs.8*
%{_mandir}/man8/mountstats.8*
%{_mandir}/man8/nfsiostat.8*
%{_mandir}/man8/rpc.gssd.8*
%{_mandir}/man8/showmount.8*
%{_mandir}/man8/umount.nfs.8*

%{systemdunitdir}/nfsfs.service
%{systemdunitdir}/blkmapd.service
%{systemdunitdir}/gssd.service

%files common
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/nfslock
%attr(754,root,root) /etc/rc.d/init.d/idmapd
%attr(754,root,root) /etc/rc.d/init.d/nfslock
%config(noreplace) %verify(not md5 mtime size) /etc/modprobe.d/sunrpc.conf
%attr(755,root,root) %{_sbindir}/sm-notify
%attr(755,root,root) /sbin/nfsidmap
%attr(755,root,root) /sbin/rpc.idmapd
%attr(755,root,root) /sbin/rpc.statd
%attr(755,root,root) /sbin/start-statd
%dir %{_var}/lib/nfs
%dir %{_var}/lib/nfs/rpc_pipefs
%dir %{_var}/lib/nfs/v4recovery
%attr(700,rpcstatd,rpcstatd) %dir %{_var}/lib/nfs/statd
%attr(700,rpcstatd,rpcstatd) %dir %{_var}/lib/nfs/statd/sm
%attr(700,rpcstatd,rpcstatd) %dir %{_var}/lib/nfs/statd/sm.bak
%attr(600,rpcstatd,rpcstatd) %config(noreplace) %verify(not md5 mtime size) %{_var}/lib/nfs/statd/state
%{_mandir}/man5/nfs.5*
%{_mandir}/man8/idmapd.8*
%{_mandir}/man8/nfsidmap.8*
%{_mandir}/man8/rpc.idmapd.8*
%{_mandir}/man8/rpc.sm-notify.8*
%{_mandir}/man8/rpc.statd.8*
%{_mandir}/man8/sm-notify.8*
%{_mandir}/man8/statd.8*

%{systemdunitdir}/idmapd.service
%{systemdunitdir}/nfslock.service
%{systemdunitdir}/var-lib-nfs-rpc_pipefs.mount
%dir %{_datadir}/nfs-utils
%attr(755,root,root) %{_datadir}/nfs-utils/nfslock.preconfig
