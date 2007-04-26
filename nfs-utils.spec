# TODO
# - should unmount /proc/fs/nfsd and /var/lib/nfs/rpc_pipefs at package
#	uninstall (or in service nfs stop)
#
# Conditional build:
%bcond_without	nfs4		# without NFSv4 support
%bcond_without	mount		# don't build mount.nfs program
#
Summary:	Kernel NFS server
Summary(pl.UTF-8):	Działający na poziomie jądra serwer NFS
Summary(pt_BR.UTF-8):	Os utilitários para o cliente e servidor NFS do Linux
Summary(ru.UTF-8):	Утилиты для NFS и демоны поддержки для NFS-сервера ядра
Summary(uk.UTF-8):	Утиліти для NFS та демони підтримки для NFS-сервера ядра
Name:		nfs-utils
Version:	1.1.0
%define	_pre	rc1
Release:	0.%{_pre}.1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/nfs/%{name}-%{version}-%{_pre}.tar.gz
# Source0-md5:	924dd05dc3958d4da585d74808bb84c4
Source1:	ftp://ftp.linuxnfs.sourceforge.org/pub/nfs/nfs.doc.tar.gz
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
Patch0:		%{name}-eepro-support.patch
Patch1:		%{name}-install.patch
# http://www.citi.umich.edu/projects/nfsv4/linux/nfs-utils-patches/
#Patch2:		%{name}-1.0.11-CITI_NFS4_ALL-1.dif
Patch2:		%{name}-CITI_NFS4.patch
Patch3:		%{name}-statdpath.patch
Patch4:		%{name}-mount-fake.patch
Patch5:		%{name}-mountd.patch
Patch6:		%{name}-idmapd.conf.patch
Patch7:		%{name}-keytab-path.patch
Patch8:		%{name}-subsys.patch
URL:		http://nfs.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	cpp
BuildRequires:	e2fsprogs-devel >= 1.39-5
%if %{with nfs4}
BuildRequires:	krb5-devel >= 1.6
BuildRequires:	libevent-devel >= 1.2
BuildRequires:	libnfsidmap-devel
BuildRequires:	librpcsecgss-devel >= 0.11-3
%endif
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires(post):	fileutils
Requires(post):	sed >= 4.0
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{version}-%{release}
Requires:	portmap >= 4.0
Requires:	rc-scripts >= 0.4.1.5
Requires:	setup >= 2.4.6-7
Provides:	nfsdaemon
Obsoletes:	knfsd
Obsoletes:	nfs-server
Obsoletes:	nfsdaemon
Conflicts:	kernel < 2.2.5
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
Requires:	portmap >= 4.0
Requires:	rc-scripts
Provides:	group(rpcstatd)
Provides:	user(rpcstatd)
Provides:	nfslockd
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

%description common
Common programs for NFS.

%description common -l pl.UTF-8
Wspólne programy do obsługi NFS.

%prep
%setup -q -a1 -n %{name}-%{version}-%{_pre}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
%configure \
%if %{with nfs4}
	--enable-gss \
	--with-krb5=%{_prefix} \
	--enable-nfsv4 \
%else
	--disable-gss \
	--disable-nfsv4 \
%endif
	%{?with_mount:--enable-mount} \
	--disable-rquotad \
	--enable-nfsv3 \
	--enable-secure-statd \
	--with-statedir=/var/lib/nfs \
	--with-tcp-wrappers

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_sbindir},%{_mandir}/man{5,8}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT%{_var}/lib/nfs/{rpc_pipefs,v4recovery,statd}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cat >$RPM_BUILD_ROOT%{_sbindir}/start-statd <<EOF
#!/bin/sh
# mount.nfs calls this script when mounting a filesystem with locking
# enabled, but when statd does not seem to be running (based on
# /var/run/rpc.statd.pid).
exec /sbin/service nfslock start
EOF

sed -e "s|#!/bin/bash|#!/bin/sh|" utils/gssd/gss_destroy_creds > $RPM_BUILD_ROOT%{_sbindir}/gss_destroy_creds

mv $RPM_BUILD_ROOT%{_sbindir}/rpcdebug $RPM_BUILD_ROOT/sbin
install utils/idmapd/idmapd.conf $RPM_BUILD_ROOT%{_sysconfdir}/

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

rm $RPM_BUILD_ROOT%{_mandir}/man8/rpc.{mountd,nfsd,statd,svcgssd,gssd,idmapd,sm-notify}.8
echo ".so mountd.8"  > 	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.mountd.8
echo ".so nfsd.8"    >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.nfsd.8
echo ".so statd.8"   >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.statd.8
echo ".so sm-notify.8" > $RPM_BUILD_ROOT%{_mandir}/man8/rpc.sm-notify.8
%if %{with nfs4}
echo ".so gssd.8"    >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.gssd.8
echo ".so idmapd.8"  >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.idmapd.8
echo ".so svcgssd.8" >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.svcgssd.8
%endif

touch $RPM_BUILD_ROOT/var/lib/nfs/xtab

ln -sf /bin/true $RPM_BUILD_ROOT/sbin/fsck.nfs

cp -a nfs html

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add nfs
%service nfs restart "NFS daemon"
%if %{with nfs4}
/sbin/chkconfig --add svcgssd
%service svcgssd restart "RPC svcgssd"
%endif

%preun
if [ "$1" = "0" ]; then
	%service nfs stop
	/sbin/chkconfig --del nfs
%if %{with nfs4}
	%service svcgssd stop
	/sbin/chkconfig --del svcgssd
%endif
fi

%post clients
/sbin/chkconfig --add nfsfs
%service nfsfs restart
%if %{with nfs4}
/sbin/chkconfig --add gssd
%service gssd restart "RPC gssd"
%endif

%preun clients
if [ "$1" = "0" ]; then
	%service nfsfs stop
	/sbin/chkconfig --del nfsfs
%if %{with nfs4}
	%service gssd stop
	/sbin/chkconfig --del gssd
%endif
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

%if %{with nfs4}
%post common
/sbin/chkconfig --add idmapd
%service idmapd restart "RPC idmapd"

%preun common
if [ "$1" = "0" ]; then
	%service idmapd stop
	/sbin/chkconfig --del idmapd
fi
%endif

%triggerpostun -- %{name} <= 1.1.0-0.rc1.1
/sbin/chkconfig nfs reset
%if %{with nfs4}
/sbin/chkconfig svcgssd reset
%endif

%triggerpostun lock -- %{name}-lock <= 1.1.0-0.rc1.1
/sbin/chkconfig nfslock reset

%triggerpostun clients -- %{name}-clients < 1.1.0-0.rc1.1
if [ -f /etc/sysconfig/nfsclient.rpmsave ]; then
	mv -f /etc/sysconfig/nfsfs{,.rpmnew}
	mv -f /etc/sysconfig/nfsclient.rpmsave /etc/sysconfig/nfsfs
fi
/sbin/chkconfig nfsfs reset
%if %{with nfs4}
/sbin/chkconfig gssd reset
%endif

%if %{with nfs4}
%triggerpostun common -- %{name}-common <= 1.1.0-0.rc1.1
/sbin/chkconfig idmapd reset
%endif

%files
%defattr(644,root,root,755)
%doc ChangeLog README html
%attr(755,root,root) /sbin/rpcdebug
%attr(755,root,root) /sbin/fsck.nfs
%attr(755,root,root) %{_sbindir}/exportfs
%attr(755,root,root) %{_sbindir}/rpc.mountd
%attr(755,root,root) %{_sbindir}/rpc.nfsd
%attr(755,root,root) %{_sbindir}/nfsstat

%attr(754,root,root) /etc/rc.d/init.d/nfs

%attr(664,root,fileshare) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/exports
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
%{_mandir}/man8/rpcdebug.8*
%if %{with nfs4}
%attr(754,root,root) /etc/rc.d/init.d/svcgssd
%attr(755,root,root) %{_sbindir}/rpc.svcgssd
%{_mandir}/man8/*svcgss*
%endif

%files lock
%defattr(644,root,root,755)
%attr(700,rpcstatd,rpcstatd) %dir %{_var}/lib/nfs/statd
%attr(755,root,root) %{_sbindir}/rpc.statd
%attr(755,root,root) %{_sbindir}/sm-notify
%attr(755,root,root) %{_sbindir}/start-statd
%attr(754,root,root) /etc/rc.d/init.d/nfslock
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/nfslock
%{_mandir}/man8/*statd.8*
%{_mandir}/man8/*sm-notify.8*
%config(noreplace) %verify(not md5 mtime size) %{_var}/lib/nfs/state

%files clients
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/nfsfs
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/nfsfs
%attr(755,root,root) %{_sbindir}/showmount
%{_mandir}/man8/showmount.8*
%if %{with mount}
%attr(4755,root,root) /sbin/mount.nfs
%attr(4755,root,root) /sbin/mount.nfs4
%attr(4755,root,root) /sbin/umount.nfs
%attr(4755,root,root) /sbin/umount.nfs4
%{_mandir}/man8/*mount.nfs.8*
%endif
%if %{with nfs4}
%attr(754,root,root) /etc/rc.d/init.d/gssd
%attr(755,root,root) %{_sbindir}/rpc.gssd
%{_mandir}/man8/rpc.gssd*
%{_mandir}/man8/gssd*
%endif

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %dir %{_var}/lib/nfs
%attr(755,root,root) %dir %{_var}/lib/nfs/rpc_pipefs
%attr(755,root,root) %dir %{_var}/lib/nfs/v4recovery
%{_mandir}/man5/nfs*
%if %{with nfs4}
%attr(754,root,root) /etc/rc.d/init.d/idmapd
%attr(755,root,root) %{_sbindir}/gss_*
%attr(755,root,root) %{_sbindir}/rpc.idmapd
%attr(660,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/idmapd.conf
%{_mandir}/man[58]/*idmap*
%endif
