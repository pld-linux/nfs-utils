Name:		nfs-utils
Version:	0.1.3
Release:	1
Summary:	Kernel NFS server.
Summary(pl):	Dzia³aj±cy na poziomie j±dra serwer NFS.
Source0:	ftp://ftp.linuxnfs.sourceforge.org/pub/nfs/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.linuxnfs.sourceforge.org/pub/nfs/nfs.doc.tdar.gz
Source2:	nfs.init
Source3:	nfslock.init
Source4:	nfs.sysconfig
Source5:	nfslock.sysconfig
Patch0:		knfsd-paths.patch
Patch1:		knfsd-non_root_build.patch
Patch2:		knfsd-rquotad.patch
#Requires:	kernel >= 2.2.5
Requires:	portmap >= 4.0
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Obsoletes:	nfsdaemon nfs-server knfsd
Provides:	nfsdaemon
Requires:	rc-scripts
Copyright:	GPL
#Requires:	/dev/nfsd_netlink
BuildRoot:	/tmp/%{name}-%{version}-root
ExcludeArch:	armv4l

%description
This is the *new* kernel NFS server and related tools.  It provides a much
higher level of performance than the traditional Linux user-land NFS server.

%description -l pl
To jest *nowy* dzia³aj±cy na poziomie j±dra serwer NFS oraz zwi±zane
z nim narzêdzia. Serwer ten dostarcza znacznie wiêksz± wydajno¶æ
ni¿ tradycyjny, dzia³aj±cy na poziomie urzytkownika serwer NFS.

%package clients
Obsoletes:	nfs-server-clients
Provides:	nfs-server-clients
Summary:	Clients for connecting to a remote NFS server.
Summary(pl):	Klienci do ³±czenia siê ze zdalnym serwerem NFS.
Group:		Networking
Group(pl):	Sieciowe
Obsoletes:	nfsclient nfs-server-clients knfsd-clients
Provides:	nfsclient

%description clients
The nfs-server-clients package contains the showmount program.
Showmount queries the mount daemon on a remote host for information
about the NFS (Network File System) server on the remote host.  For
example, showmount can display the clients which are mounted on that
host.  This package is not needed to mount NFS volumes.

%description -l pl clients
Pakiet zawiera program showmount s³u¿±cy do odpytywania
serwera NFS.

%package lock
Summary:	Programs for NFS file locking.
Summary(pl):	Programy do obs³ugi blokowania plików poprzez NFS (lock).
#Requires:	kernel >= 2.2.5
Requires:	portmap >= 4.0
Requires:	%{name} = %{version}
Obsoletes:	nfslockd knfsd-lock
Provides:	nfslockd
Group:          Networking
Group(pl):      Sieciowe

%description lock
The nfs-lock pacage contains programs which support the NFS file lock.
Install nfs-lock if you want to use file lock over NFS.

%description -l pl lock
Ten pakiet zawiera programy umo¿liwiaj±ce wykonywanie
blokowania plików (file locking) poprzez NFS.

%prep
%setup  -q -a1
%patch0 -p1
#%patch1 -p1
%patch2 -p1

%build
%configure \
	--with-statedir=/var/state/nfs \
	--enable-nfsv3 \
	--enable-secure-statd
make all

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{/sbin,%{_sbindir},%{_mandir}/man{5,8}}
install -d $RPM_BUILD_ROOT{/etc/{rc.d/init.d,sysconfig},%{_var}/state/nfs}

make install install_prefix="$RPM_BUILD_ROOT"

install	-s tools/rpcdebug/rpcdebug $RPM_BUILD_ROOT/sbin
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfs
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfslock
install %{SOURCE4} $RPM_BUILD_ROOT/etc/sysconfig/nfsd
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/nfslock
touch $RPM_BUILD_ROOT/%{_var}/state/nfs/rmtab

touch $RPM_BUILD_ROOT/etc/exports

rm $RPM_BUILD_ROOT%{_mandir}/man8/rpc.{mountd,nfsd,rquotad,statd}.8
echo ".so mountd.8"  > 	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.mountd.8
echo ".so nfsd.8"    >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.nfsd.8
echo ".so rquotad.8" >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.rquotad.8
echo ".so statd.8"   >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.statd.8

strip --strip-unneeded $RPM_BUILD_ROOT{/sbin/*,%{_sbindir}/*} || :

touch $RPM_BUILD_ROOT/var/state/nfs/xtab

gzip -9nf ChangeLog README nfs/*.ps \
	$RPM_BUILD_ROOT%{_mandir}/man*/*

mv -f nfs/*.ps.gz ./
mv -f nfs html

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add nfs
if [ -r /var/lock/subsys/nfs ]; then
	/etc/rc.d/init.d/nfs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/nfs start\" to start nfs daemon."
fi
sed -e 's/NFSDTYPE=.*/NFSDTYPE=K/' /etc/sysconfig/nfsd > /etc/sysconfig/nfsd.new
mv -f /etc/sysconfig/nfsd.new /etc/sysconfig/nfsd

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del nfs
	/etc/rc.d/init.d/nfs stop >&2
fi

%post lock
/sbin/chkconfig --add nfslock
if [ -r /var/lock/subsys/nfslock ]; then
	/etc/rc.d/init.d/nfslock restart >&2
else
	echo "Run \"/etc/rc.d/init.d/nfs start\" to start nfslock daemon."
fi

%preun lock
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del nfslock
	/etc/rc.d/init.d/nfslock stop >&2
fi

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,*.ps}.gz html
%attr(755,root,root) /sbin/rpcdebug
%attr(755,root,root) %{_sbindir}/exportfs
%attr(755,root,root) %{_sbindir}/rpc.mountd
%attr(755,root,root) %{_sbindir}/rpc.nfsd
%attr(755,root,root) %{_sbindir}/nfsstat
%attr(755,root,root) %{_sbindir}/nhfsstone

%attr(754,root,root) /etc/rc.d/init.d/nfs

%attr(755,root,root) %dir %{_var}/state/nfs

%config(noreplace) %verify(not size mtime md5) /etc/exports
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/nfsd
%config(noreplace) %verify(not size mtime md5) %{_var}/state/nfs/xtab
%config(noreplace) %verify(not size mtime md5) %{_var}/state/nfs/etab
%config(noreplace) %verify(not size mtime md5) %{_var}/state/nfs/rmtab

%{_mandir}/man8/exportfs.8*
%{_mandir}/man8/mountd.8*
%{_mandir}/man8/nfsd.8*
%{_mandir}/man8/nfsstat.8*
%{_mandir}/man8/rpc.mountd.8*
%{_mandir}/man8/rpc.nfsd.8*
%{_mandir}/man8/rpc.rquotad.8*
%{_mandir}/man5/exports.5*

%files lock
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rpc.lockd
%attr(755,root,root) %{_sbindir}/rpc.statd
%attr(754,root,root) /etc/rc.d/init.d/nfslock
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/nfslock

%{_mandir}/man8/rpc.statd.8*
%{_mandir}/man8/statd.8*

%files clients
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/showmount
%{_mandir}/man8/showmount.8*
