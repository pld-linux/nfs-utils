#
# Conditional build:
%bcond_without	nfs4		# without NFSv4 support
#
Summary:	Kernel NFS server
Summary(pl):	Dzia�aj�cy na poziomie j�dra serwer NFS
Summary(pt_BR):	Os utilit�rios para o cliente e servidor NFS do Linux
Summary(ru):	������� ��� NFS � ������ ��������� ��� NFS-������� ����
Summary(uk):	���̦�� ��� NFS �� ������ Ц������� ��� NFS-������� ����
Name:		nfs-utils
Version:	1.0.8
Release:	0.4
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/nfs/%{name}-%{version}.tar.gz
# Source0-md5:	74fc2dd04b40c9d619ca41d3787ef8db
Source1:	ftp://ftp.linuxnfs.sourceforge.org/pub/nfs/nfs.doc.tar.gz
# Source1-md5:	ae7db9c61c5ad04f83bb99e5caed73da
Source2:	nfs.init
Source3:	nfslock.init
Source4:	rquotad.init
Source5:	nfs.sysconfig
Source6:	nfslock.sysconfig
Source7:	rquotad.sysconfig
Source8:	nfsfs.init
Patch0:		%{name}-time.patch
Patch1:		%{name}-eepro-support.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-nolibs.patch
Patch4:		%{name}-heimdal.patch
Patch5:		%{name}-heimdal-internals.patch
URL:		http://nfs.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
%if %{with nfs4}
BuildRequires:	heimdal-devel
BuildRequires:	libevent-devel
BuildRequires:	libnfsidmap-devel
BuildRequires:	librpcsecgss-devel >= 0.10
%endif
Requires:	%{name}-common = %{version}-%{release}
Requires:	rc-scripts >= 0.4.0
Requires:	setup >= 2.4.6-7
Requires(post,preun):	/sbin/chkconfig
Requires(post):	fileutils
Requires(post):	sed
Requires:	portmap >= 4.0
Provides:	nfsdaemon
Obsoletes:	nfsdaemon
Obsoletes:	knfsd
Obsoletes:	nfs-server
Conflicts:	kernel < 2.2.5
ExcludeArch:	armv4l
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the *new* kernel NFS server and related tools. It provides a
much higher level of performance than the traditional Linux user-land
NFS server.

%description -l pl
To jest *nowy* dzia�aj�cy na poziomie j�dra serwer NFS oraz zwi�zane z
nim narz�dzia. Serwer ten dostarcza znacznie wi�ksz� wydajno�� ni�
tradycyjny, dzia�aj�cy na poziomie u�ytkownika serwer NFS.

%description -l pt_BR
O pacote nfs-utils prov� os utilit�rios para o cliente e servidor NFS
do Linux.

%description -l ru
����� nfs-utils ������������� ������ ��� NFS-�������, ����������� �
����, � ������������� �������, ������� ������������ ������� �������
������������������, ��� ������������ Linux NFS-�������, ������������
������������ �������������.

%description -l uk
����� nfs-utils ����� ������ ��� NFS-�������, ����������� � ����, ��
�����Φ ���̦��, �˦ ������������ �������� ¦���� ���������Φ���, Φ�
�����æ�Φ Linux NFS-�������, �˦ ����������դ ¦��ۦ��� ���������ަ�.

%package clients
Summary:	Clients for connecting to a remote NFS server
Summary(pl):	Klienci do ��czenia si� ze zdalnym serwerem NFS
Group:		Networking
Requires:	rc-scripts
Requires(post,preun):	/sbin/chkconfig
Requires:	%{name}-common = %{version}-%{release}
Requires:	psmisc
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
Pakiet zawiera program showmount s�u��cy do odpytywania serwera NFS.
Showmount pyta demona na zdalnej maszynie o informacje NFS na zdalnym
ho�cie. Na przyk�ad, showmount potrafi pokaza� klient�w, kt�rzy s�
zamountowani na tym serwerze. Ten pakiet nie jest konieczny do
zamountowania zasob�w NFS.

%package lock
Summary:	Programs for NFS file locking
Summary(pl):	Programy do obs�ugi blokowania plik�w poprzez NFS (lock)
Group:		Networking
Requires:	rc-scripts
Requires(post,preun):	/sbin/chkconfig
#Requires:	kernel >= 2.2.5
Requires:	portmap >= 4.0
Provides:	nfslockd
Obsoletes:	nfslockd
Obsoletes:	knfsd-lock

%description lock
The nfs-lock pacage contains programs which support the NFS file lock.
Install nfs-lock if you want to use file lock over NFS.

%description lock -l pl
Ten pakiet zawiera programy umo�liwiaj�ce wykonywanie blokowania
plik�w (file locking) poprzez NFS.

%package rquotad
Summary:	Remote quota server
Summary(pl):	Zdalny serwer quota
Group:		Networking/Daemons
Requires:	rc-scripts
Requires(post,preun):	/sbin/chkconfig
Obsoletes:	quota-rquotad

%description rquotad
rquotad is an rpc(3N) server which returns quotas for a user of a
local file system which is mounted by a remote machine over the NFS.
The results are used by quota(1) to display user quotas for remote
file systems.

%description rquotad -l pl
rquotad jest serverem rpc(3N), kt�ry zwraca quoty u�ytkownika
lokalnego systemu plik�w, kt�ry jest zamountowany przez zdaln� maszyn�
poprzez NFS. Rezultaty s� u�ywane przez quota(1), aby wy�wietli� quot�
dla zdalnego systemu plik�w.

%package common                                                                       
Summary:	Common programs for NFS
Summary(pl):	Wsp�lne programy do obs�ugi NFS
Group:		Networking

%description common
Common programs for NFS.

%description common -l pl
Wsp�lne programy do obs�ugi NFS.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%if "%{_lib}" == "lib64"
sed -i -e 's#/lib/#/%{_lib}/#g' aclocal/kerberos5.m4
%endif
sed -i -e 's#libroken.a#libroken.so#g' aclocal/kerberos5.m4
%{__aclocal} -I aclocal
%{__autoconf}
%{__automake}
%configure \
%if %{with nfs4}
	--enable-gss \
	--with-krb5=%{_prefix} \
	--enable-nfsv4 \
%else
	--disable-gss \
	--disable-nfsv4 \
%endif
	--enable-nfsv3 \
	--enable-secure-statd \
	--with-statedir=/var/lib/nfs

%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_sbindir},%{_mandir}/man{5,8}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/{rc.d/init.d,sysconfig} \
	$RPM_BUILD_ROOT%{_var}/lib/nfs/{rpc_pipefs,v4recovery}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install tools/rpcdebug/rpcdebug $RPM_BUILD_ROOT/sbin
install utils/idmapd/idmapd.conf $RPM_BUILD_ROOT%{_sysconfdir}/

install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfs
install %{SOURCE3} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfslock
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/rquotad
install %{SOURCE8} $RPM_BUILD_ROOT/etc/rc.d/init.d/nfsfs
install %{SOURCE5} $RPM_BUILD_ROOT/etc/sysconfig/nfsd
install %{SOURCE6} $RPM_BUILD_ROOT/etc/sysconfig/nfslock
install %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/rquotad

> $RPM_BUILD_ROOT%{_var}/lib/nfs/rmtab
> $RPM_BUILD_ROOT%{_sysconfdir}/exports

rm -f $RPM_BUILD_ROOT%{_mandir}/man8/rpc.{mountd,nfsd,rquotad,statd,lockd,svcgssd,gssd,idmapd}.8
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/rpc.idmapd.conf.5
echo ".so lockd.8"   > 	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.lockd.8
echo ".so mountd.8"  > 	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.mountd.8
echo ".so nfsd.8"    >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.nfsd.8
echo ".so rquotad.8" >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.rquotad.8
echo ".so statd.8"   >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.statd.8
%if %{with nfs4}
echo ".so gssd.8"    >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.gssd.8
echo ".so idmapd.8"  >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.idmapd.8
echo ".so svcgssd.8" >	$RPM_BUILD_ROOT%{_mandir}/man8/rpc.svcgssd.8
echo ".so idmapd.conf.5" > $RPM_BUILD_ROOT%{_mandir}/man5/rpc.idmapd.conf.5
%endif

touch $RPM_BUILD_ROOT/var/lib/nfs/xtab

ln -sf /bin/true $RPM_BUILD_ROOT/sbin/fsck.nfs

mv -f nfs html

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add nfs
if [ -r /var/lock/subsys/nfs ]; then
	/etc/rc.d/init.d/nfs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/nfs start\" to start NFS daemon."
fi
umask 022
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
	echo "Run \"/etc/rc.d/init.d/nfsfs start\" to mount all NFS volumes."
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
%doc ChangeLog README html
%attr(755,root,root) /sbin/rpcdebug
%attr(755,root,root) /sbin/fsck.nfs
%attr(755,root,root) %{_sbindir}/exportfs
%attr(755,root,root) %{_sbindir}/rpc.mountd
%attr(755,root,root) %{_sbindir}/rpc.nfsd
%attr(755,root,root) %{_sbindir}/nfsstat
%attr(755,root,root) %{_sbindir}/nhfsgraph
%attr(755,root,root) %{_sbindir}/nhfsnums
%attr(755,root,root) %{_sbindir}/nhfsrun
%attr(755,root,root) %{_sbindir}/nhfsstone

%attr(754,root,root) /etc/rc.d/init.d/nfs

%attr(755,root,root) %dir %{_var}/lib/nfs
%attr(755,root,root) %dir %{_var}/lib/nfs/rpc_pipefs
%attr(755,root,root) %dir %{_var}/lib/nfs/v4recovery

%attr(664,root,fileshare) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/exports
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/nfsd
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/nfs/xtab
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/nfs/etab
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/nfs/rmtab

%{_mandir}/man5/exports.5*
%{_mandir}/man7/nfsd.7*
%{_mandir}/man8/exportfs.8*
%{_mandir}/man8/mountd.8*
%{_mandir}/man8/nhfsgraph.8*
%{_mandir}/man8/nhfsnums.8*
%{_mandir}/man8/nhfsrun.8*
%{_mandir}/man8/nhfsstone.8*
%{_mandir}/man8/nfsd.8*
%{_mandir}/man8/nfsstat.8*
%{_mandir}/man8/rpc.mountd.8*
%{_mandir}/man8/rpc.nfsd.8*
%if %{with nfs4}
%attr(755,root,root) %{_sbindir}/rpc.svcgssd
%{_mandir}/man8/*svcgss*
%endif

%files lock
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/rpc.lockd
%attr(755,root,root) %{_sbindir}/rpc.statd
%attr(754,root,root) /etc/rc.d/init.d/nfslock
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/nfslock
%{_mandir}/man8/rpc.lockd.8*
%{_mandir}/man8/lockd.8*
%{_mandir}/man8/rpc.statd.8*
%{_mandir}/man8/statd.8*
%config(noreplace) %verify(not size mtime md5) %{_var}/lib/nfs/state

%files clients
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/nfsfs
%attr(755,root,root) %{_sbindir}/showmount
%{_mandir}/man8/showmount.8*

%if %{with nfs4}
%attr(755,root,root) %{_sbindir}/rpc.gssd
%{_mandir}/man8/rpc.gssd*
%{_mandir}/man8/gssd*
%endif

#%files rquotad
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_sbindir}/rpc.rquotad
#%attr(754,root,root) /etc/rc.d/init.d/rquotad
#%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rquotad
#%%{_mandir}/man8/rpc.rquotad.8*

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %dir %{_var}/lib/nfs
%attr(755,root,root) %dir %{_var}/lib/nfs/rpc_pipefs
%attr(755,root,root) %dir %{_var}/lib/nfs/v4recovery
%if %{with nfs4}
%attr(755,root,root) %{_sbindir}/gss_*
%attr(755,root,root) %{_sbindir}/rpc.idmapd
%attr(660,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/idmapd.conf
%{_mandir}/man[58]/*idmap*
%endif
