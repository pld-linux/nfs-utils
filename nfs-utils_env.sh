#!/bin/sh

# extract configuration from /etc/sysconfig/nfs* and write
# environment to /run/sysconfig/nfs-utils to be used by systemd unit
# files.

[ -f /etc/sysconfig/nfslock ] && . /etc/sysconfig/nfslock
[ -f /etc/sysconfig/nfsfs ] && . /etc/sysconfig/nfsfs
[ -f /etc/sysconfig/nfsd ] && . /etc/sysconfig/nfsd

STATDARGS="$STATDOPTIONS"

# Set the ports lockd should listen on
if [ -n "$LOCKD_TCPPORT" ]; then
	STATDARGS="$STATDARGS -T $LOCKD_TCPPORT"
	/sbin/sysctl -w fs.nfs.nlm_tcpport=$LOCKD_TCPPORT >/dev/null 2>&1
fi
if [ -n "$LOCKD_UDPPORT" ]; then
	STATDARGS="$STATDARGS -U $LOCKD_UDPPORT"
	/sbin/sysctl -w fs.nfs.nlm_udpport=$LOCKD_UDPPORT >/dev/null 2>&1
fi

# Set v4 grace period if requested
if [ -n "$NFSD_V4_GRACE" ]; then
	echo "$NFSD_V4_GRACE" > /proc/fs/nfsd/nfsv4gracetime >/dev/null 2>&1
fi

RPCMOUNTDARGS="$RPCMOUNTDOPTIONS"
SVCGSSDARGS="$RPCSVCGSSOPTIONS"
RPCIDMAPDARGS="$RPCIDMAPOPTIONS"
GSSDARGS="$RPCGSSOPTIONS"
if [ "$RPCNFSDCOUNT" -gt 0 ]; then
	RPCNFSDARGS="$RPCNFSDCOUNT"
else
	RPCNFSDARGS="8"
fi
if [ -n "$RPCNFSDOPTIONS" ]; then
	RPCNFSDARGS="$RPCNFSDOPTIONS $RPCNFSDARGS"
fi

BLKMAPDARGS="$BLKMAPDOPTIONS"

#mkdir -p /run/sysconfig
{
	[ -z "$STATDARGS" ] || echo STATDARGS=\""$STATDARGS"\"
	[ -z "$RPCMOUNTDARGS" ] || echo RPCMOUNTDARGS=\""$RPCMOUNTDARGS"\"
	[ -z "$SVCGSSDARGS" ] || echo SVCGSSDARGS=\""$SVCGSSDARGS"\"
	[ -z "$RPCIDMAPDARGS" ] || echo RPCIDMAPDARGS=\""$RPCIDMAPDARGS"\"
	[ -z "$GSSDARGS" ] || echo GSSDARGS=\""$GSSDARGS"\"
	[ -z "$RPCNFSDARGS" ] || echo RPCNFSDARGS=\""$RPCNFSDARGS"\"
	[ -z "$BLKMAPDARGS" ] || echo BLKMAPDARGS=\""$BLKMAPDARGS"\"
} > xxx
#} > /run/sysconfig/nfs-utils
