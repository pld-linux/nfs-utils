Summary:	Kernel NFS server
Summary(pl):	Dzia³aj±cy na poziomie j±dra serwer NFS
Summary(pt_BR):	Os utilitários para o cliente e servidor NFS do Linux
Name:		nfs-utils
Version:	0.3.3
Release:	5
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(es):	Red/Servidores
Group(fr):	Réseau/Serveurs
Group(pl):	Sieciowe/Serwery
Group(pt):	Rede/Server
Group(ru):	óÅÔÅ×ÙÅ/äÅÍÏÎÙ
Source0:	http://download.sourceforge.net/nfs/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.linuxnfs.sourceforge.org/pub/nfs/nfs.doc.tar.gz
Source2:	nfs.init
Source3:	nfslock.init
Source4:	rquotad.init
Source5:	nfs.sysconfig
Source6:	nfslock.sysconfig
Source7:	rquotad.sysconfig
Source8:	nfsfs.init
Patch0:		%{name}-paths.patch
Patch1:		%{name}-time.patch
Patch2:		%{name}-eepro-support.patch
Requires:	portmap >= 4.0
Obsoletes:	nfsdaemon nfs-server knfsd
Provides:	nfsdaemon
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
BuildRequires:	autoconf
ExcludeArch:	armv4l
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Conflicts:	kernel < 2.2.5

%description
This is the *new* kernel NFS server and related tools. It provides a
much higher level of performance than the traditional Linux user-land
NFS server.

%description -l pl
To jest *nowy* dzia³aj±cy na poziomie j±dra serwer NFS oraz zwi±zane z
nim narzêdzia. Serwer ten dostarcza znacznie wiêksz± wydajno¶æ ni¿
tradycyjny, dzia³aj±cy na poziomie uzytkownika serwer NFS.

%description -l pt_BR
O pacote nfs-utils provê os utilitários para o cliente e servidor NFS
do Linux.

%package clients
Summary:	Clients for connecting to a remote NFS server
Summary(pl):	Klienci do ³±czenia siê ze zdalnym serwerem NFS
Group:		Networking
Group(de):	Netzwerkwesen
Group(es):	Red
Group(fr):	Réseau
Group(pl):	Sieciowe
Group(pt_BR):	Rede
Group(pt):	Rede
Group(ru):	óÅÔÅ×ÙÅ
Requires:	psmisc
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
Provides:	nfsclient
Provides:	nfs-server-clients
Obsoletes:	nfsclient
Obsoletes:	nfs-server-clients
Obsoletes:	knfsd-clients

%description clients
The nfs-server-clients package contains the showmount program.
Showmount queries the mount daemon on a remote host for information
about the NFS (Network File System) server on the remote host. For
example, showmount can display the clients which are mounted on that
host. This package is not needed to mount NFS volumes.

%description clients -l pl
Pakiet zawiera program showmount s³u¿±cy do odpytywania serwera NFS.
Showmount pyta demona na zdalnej maszynie o informacje NFS na zdalnym
ho¶cie. Na przyk³ad, showmount potrafi pokazaæ klientów, którzy s±
zamountowani na tym serverze. Ten pakiet nie jest konieczny do
zamountowania zasobów NFS.

%package lock
Summary:	Programs for NFS file locking
Summary(pl):	Programy do obs³ugi blokowania plików poprzez NFS (lock)
#Requires:	kernel >= 2.2.5
Group:		Networking
Group(de):	Netzwerkwesen
Group(es):	Red
Group(fr):	Réseau
Group(pl):	Sieciowe
Group(pt_BR):	Rede
Group(pt):	Rede
Group(ru):	óÅÔÅ×ÙÅ
Requires:	portmap >= 4.0
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
Obsoletes:	nfslockd knfsd-lock
Provides:	nfslockd

%description lock
The nfs-lock pacage contains programs which support the NFS file lock.
Install nfs-lock if you want to use file lock over NFS.

%description lock -l pl
Ten pakiet zawiera programy umo¿liwiaj±ce wykonywanie blokowania
plików (file locking) poprzez NFS.

%package rquotad
Summary:	Remote quota server
Summary(pl):	Zdalny serwer quota
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(es):	Red/Servidores
Group(fr):	Réseau/Serveurs
Group(pl):	Sieciowe/Serwery
Group(pt):	Rede/Server
Group(ru):	óÅÔÅ×ÙÅ/äÅÍÏÎÙ
Prereq:		rc-scripts
Prereq:		/sbin/chkconfig
Obsoletes:	quota-rquotad

%description rquotad
rquotad is an rpc(3N) server which returns quotas for a user of a
local file system which is mounted by a remote machine over the NFS.
The results are used by quota(1) to display user quotas for remote
file systems.

%description rquotad -l pl
rquotad jest serverem rpc(3N), który zwraca quoty u¿ytkownika
lokalnego systemu plików, który jest zamountowany przez zdaln± maszynê
poprzez NFS. Rezultaty s± u¿ywane przez quota(1), aby wy¶wietliæ quote
dla zdalnego systemu plików.

%prep
%setup  -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
%configure \
	--with-statedir=/var/lib/nfs \
	--enable-nfsv3 \
	--enable-secure-statd
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_sbindir},%{_mandir}/man{5,8}} \
	$RPM_BUILD_ROOT{%{_sysconfdir}/{rc.d/init.d,sysconfig},%{_var}/lib/nfs}

%{__make} install install_prefix="$RPM_BUILD_ROOT"

install tools/rpcdebug/rpcdebug $RPM_BUILD_ROOT/sbin
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfs
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfslock
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/rquotad
install %{SOURCE8} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfsfs
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/nfsd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/nfslock
install %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/rquotad

> $RPM_BUILD_ROOT%{_var}/lib/nfs/rmtab
> $RPM_BUILD_ROOT%{_sysconfdir}/exports

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/rpc.{mountd,nfsd,rquotad,statd,lockd}.8
echo ".so lockd.8"   > 	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.lockd.8
echo ".so mountd.8"  > 	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.mountd.8
echo ".so nfsd.8"    >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.nfsd.8
echo ".so rquotad.8" >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.rquotad.8
echo ".so statd.8"   >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.statd.8

touch $RPM_BUILD_ROOT/var/lib/nfs/xtab

gzip -9nf ChangeLog README nfs/*.ps

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
	if [ -r /var/lock/subsys/nfs ]; then
		/etc/rc.d/init.d/nfs stop >&2
	fi
	/sbin/chkconfig --del nfs
fi

%post clients
/sbin/chkconfig --add nfsfs
if [ -r /var/lock/subsys/nfsfs ]; then
	/etc/rc.d/init.d/nfsfs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/nfsfs start\" to mount all NFS volumens."
fi

%preun clients
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/nfsfs ]; then
		/etc/rc.d/init.d/nfsfs stop >&2
	fi
	/sbin/chkconfig --del nfsfs
fi

%post lock
/sbin/chkconfig --add nfslock
if [ -r /var/lock/subsys/nfslock ]; then
	/etc/rc.d/init.d/nfslock restart >&2
else
	echo "Run \"/etc/rc.d/init.d/nfslock start\" to start nfslock daemon."
fi

%preun lock
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/nfslock ]; then
		/etc/rc.d/init.d/nfslock stop >&2
	fi
	/sbin/chkconfig --del nfslock
fi

%post rquotad
/sbin/chkconfig --add rquotad
if [ -r /var/lock/subsys/rquotad ]; then
	/etc/rc.d/init.d/rquotad restart >&2
else
	echo "Run \"/etc/rc.d/init.d/rquotad start\" to start NFS quota daemon."
fi

%preun rquotad
if [ "$1" = "0" ]; then
	if [ -r /var/lock/subsys/rquotad ]; then
		/etc/rc.d/init.d/rquotad stop >&2
	fi
	/sbin/chkconfig --del rquotad
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

%attr(755,root,root) %dir %{_var}/lib/nfs

%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/exports
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/nfsd
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/nfs/xtab
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/nfs/etab
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/nfs/rmtab

%{_mandir}/man8/exportfs.8*
%{_mandir}/man8/mountd.8*
%{_mandir}/man8/nfsd.8*
%{_mandir}/man8/nfsstat.8*
%{_mandir}/man8/rpc.mountd.8*
%{_mandir}/man8/rpc.nfsd.8*
%{_mandir}/man5/exports.5*

%files lock
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rpc.lockd
%attr(755,root,root) %{_sbindir}/rpc.statd
%attr(754,root,root) /etc/rc.d/init.d/nfslock
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/nfslock
%attr(755,root,root) %dir %{_var}/lib/nfs
%{_mandir}/man8/rpc.lockd.8*
%{_mandir}/man8/lockd.8*
%{_mandir}/man8/rpc.statd.8*
%{_mandir}/man8/statd.8*

%files clients
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/nfsfs
%attr(755,root,root) %{_sbindir}/showmount
%{_mandir}/man8/showmount.8*

%files rquotad
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rpc.rquotad
%attr(754,root,root) /etc/rc.d/init.d/rquotad
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rquotad
%{_mandir}/man8/rpc.rquotad.8*
