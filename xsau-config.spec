# install root
%define DESTDIR  /

Requires(post): coreutils

Summary: XS default service configuration
Name: xsau-config
Version: 0.7.0.4
Release: 1AUXSjv
BuildRoot: %{_builddir}/%{name}-root
Distribution: OLPC XS/XSX School Server
Group: Base System/Administration Tools
License: GPLv2
Packager: Jerry Vonau <jvonau@shaw.ca>
Source: %{name}-%{version}.tar.gz
#URL: http://dev.laptop.org/git.do?p=projects/xs-config;a=summary
Vendor: OLPC

#  Requires a few tools 
Requires: usbmount
Requires: git
Requires: make
Requires: python
Requires: authconfig  
Requires: initscripts  
Requires: nscd  
Requires: nss  
Requires: radvd  
Requires: rpm  
Requires: selinux-policy
Requires: setup  
Requires: smartmontools  
Requires: sudo  
Requires: syslog 

#a list of packages modified by xs-config
Requires: openssh-server  
Requires: httpd
Requires: moodle-xs
Requires: postgresql-server
Requires: xml-common  
Requires: php-common
Requires: xs-rsync
Requires: xsactivation

%prep
%setup
%install
echo $PWD
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT/%{DESTDIR} install
%clean
rm -rf $RPM_BUILD_ROOT

%define BADLINKS /etc/named-xs.conf \
	/etc/named.conf   \
	/etc/squid/squid.conf   \
	/etc/sysconfig/olpc-scripts/TURN_SQUID_OFF \
	/etc/sysconfig/olpc-scripts/TURN_SQUID_ON \
	/etc/sysconfig/olpc-scripts/auxiliary_config \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.1    \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.1.aux \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.2    \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.2.aux \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.3     \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.3.aux \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.4     \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.4.aux \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.5     \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.5.aux \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.6     \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.6.aux \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.7     \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.7.aux \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.8     \
	/etc/sysconfig/olpc-scripts/dhcpd.conf.8.aux \
	/etc/sysconfig/olpc-scripts/resolv.conf \
	/etc/sysconfig/olpc-scripts/domain_config    \
	/etc/sysconfig/olpc-scripts/domain_config.d/dhcpd    \
	/etc/sysconfig/olpc-scripts/domain_config.d/ejabberd \
	/etc/sysconfig/olpc-scripts/domain_config.d/idmgr    \
	/etc/sysconfig/olpc-scripts/domain_config.d/named    \
	/etc/sysconfig/olpc-scripts/domain_config.d/squid    \
	/etc/sysconfig/olpc-scripts/domain_config.d/dhcpd.orig    \
	/etc/sysconfig/olpc-scripts/domain_config.d/idmgr.orig    \
	/etc/sysconfig/olpc-scripts/domain_config.d/ejabberd.rej  \
	/etc/sysconfig/olpc-scripts/domain_config.d/named.orig    \
	/etc/sysconfig/olpc-scripts/domain_config.d/ejabberd.orig \
	/etc/sysconfig/olpc-scripts/ifcfg-dummy0             \
	/etc/sysconfig/olpc-scripts/ifcfg-eth0               \
	/etc/sysconfig/olpc-scripts/ifcfg-eth0.auxiliary     \
	/etc/sysconfig/olpc-scripts/ifcfg-eth1               \
	/etc/sysconfig/olpc-scripts/ifcfg-msh0               \
	/etc/sysconfig/olpc-scripts/ifcfg-msh1               \
	/etc/sysconfig/olpc-scripts/ifcfg-msh2               \
	/etc/sysconfig/olpc-scripts/ifcfg-tun0               \
	/etc/sysconfig/olpc-scripts/ip6tables                \
	/etc/sysconfig/olpc-scripts/mkaccount                \
	/etc/sysconfig/olpc-scripts/network_config           \
	/etc/sysconfig/olpc-scripts/principal_config         \
	/etc/ejabberd/ejabberd.pem                           \
	/etc/ejabberd/ejabberd.cfg                           \
                                                             \
	/etc/ppp/chap-secrets         \
	/etc/ppp/pap-secrets          \
	/etc/ppp/peers/isdn/arcor     \
	/etc/ppp/peers/isdn/avm       \
	/etc/ppp/peers/isdn/avm-ml    \
	/etc/ppp/peers/isdn/leased    \
	/etc/ppp/peers/isdn/otelo     \
	/etc/ppp/peers/isdn/talkline  \
	/etc/ppp/peers/wvdial         \
	/etc/dhclient-exit-hooks      \
	/etc/dhclient-eth0.conf       \
	/etc/ssh/moduli               \
	/etc/httpd/conf/httpd.conf    \
	/etc/httpd/conf.d/mime_olpc.conf \
	/etc/inittab                  \
	/etc/default/useradd          \
	/etc/autofs_ldap_auth.conf    \
 	/etc/isdn/vboxgetty.conf      \
	/etc/racoon/psk.txt           \
	/etc/racoon/racoon.conf       \
	/etc/isdn/vboxd.conf          \
	/etc/aiccu.conf               \
	/etc/lighttpd/lighttpd.conf   \
	/etc/libaudit.conf            \
	/etc/pki/nssdb/secmod.db      \
	/etc/smartd.conf              \
	/etc/rndc.key                 \
	/etc/xml/catalog              \
	/etc/radvd.conf               \
	/etc/sysconfig/authconfig     \
	/etc/sysconfig/firstboot      \
	/etc/sysconfig/ip6tables-config \
	/etc/sysconfig/dhcpd          \
	/etc/sysconfig/named          \
	/etc/sysconfig/init           \
	/etc/sysconfig/iptables-config \
	/etc/sysconfig/squid          \
	/etc/udev/rules.d/10-olpcmesh.rules \
	/etc/usbmount/usbmount.conf   \
	/etc/usbmount/mount.d/01_beep_on_mount  \
	/etc/usbmount/mount.d/99_beep_when_done \
                                                \
	/etc/yum.repos.olpc.d/stable.repo   \
	/etc/yum.repos.olpc.d/testing.repo  \
                                            \
	/etc/sysctl.conf  \
	/etc/yum.conf     \
	/etc/syslog.conf  \
	/etc/motd         \
	/etc/ssh/sshd_config 

%post

## RPM computes conflicts _before_ %pre so even if the symlinks were 
## removed in %pre, rpm will still divert files that it would have
## conflicted. So mv the rpmnew files into place if appropriate.
BADLINKS='%{BADLINKS}'
for FPATH in $BADLINKS; do
    if [ ! -e "%{DESTDIR}$FPATH" -a -e "%{DESTDIR}$FPATH.rpmnew" ]; then
       mv "%{DESTDIR}$FPATH.rpmnew" "%{DESTDIR}$FPATH"
    fi
done

## Some very specific files that we want to overwrite if they
## are old files with a known content
FPATH='/etc/yum.conf'
BADSHA1SUMS="2f12835cb11f100be169abcc8bff72525a25cff7 
             8970c4d97f3f90eb17520ea3d8590b24bc7f4691"
if [ -e "%{DESTDIR}$FPATH" -a -e "%{DESTDIR}$FPATH.rpmnew" ]; then
    SHA1SUM=`sha1sum "%{DESTDIR}$FPATH" | cut -d\  -f1`
    for BADCSUM in $BADSHA1SUMS; do
        if [ $SHA1SUM = $BADCSUM ]; then
            mv "%{DESTDIR}$FPATH.rpmnew" "%{DESTDIR}$FPATH"
        fi
    done
fi

## Rename old conffiles
if [ -e /etc/sysconfig/olpc-scripts/xs-domain-name ]; then
   mv /etc/sysconfig/olpc-scripts/xs-domain-name /etc/sysconfig/xs_domain_name
fi
if [ -e /etc/sysconfig/network-scripts/server_number ];then
   mv /etc/sysconfig/network-scripts/server_number /etc/sysconfig/xs_server_number
fi

###
### CLEANUP XS 0.4 to XS 0.5
###
# Remove old configs that are unambiguously old
OLDCONFIGS="/etc/sysconfig/network-scripts/ifcfg-dummy0
            /etc/sysconfig/network-scripts/ifcfg-mshbond0
            /etc/sysconfig/network-scripts/ifcfg-mshbond0:1
            /etc/sysconfig/network-scripts/ifcfg-mshbond1
            /etc/sysconfig/network-scripts/ifcfg-mshbond2
            /etc/sysconfig/network-scripts/ifcfg-msh0
            /etc/sysconfig/network-scripts/ifcfg-msh1
            /etc/sysconfig/network-scripts/ifcfg-msh2
            /etc/sysconfig/network-scripts/ifcfg-wmesh0
            /etc/sysconfig/network-scripts/ifcfg-wmesh1
            /etc/sysconfig/network-scripts/ifcfg-wmesh2
            /etc/sysconfig/network-scripts/route-eth0
            /etc/sysconfig/network-scripts/route-lanbond0
            /etc/modprobe.d/xs_bonding
            /etc/udev/rules.d/10-olpcmesh.rules
            /etc/udev/rules.d/65-xsmeshnames.rules
            /sbin/ifup-local
            /lib/udev/mesh-namer
            /etc/sysconfig/network-scripts/ifcfg-br0
            /etc/sysconfig/network-scripts/ifcfg-br1
            /etc/sysconfig/network-scripts/ifcfg-br2  "
for FPATH in $OLDCONFIGS; do
    if [ -e "%{DESTDIR}$FPATH" ];then
       /usr/bin/xs-commitchanged --remove -m 'Remove old conffile' "%{DESTDIR}$FPATH"
    fi
done
# Remove ifcfg-ethX files that refer to libertas devices
# these have been replaced with wmeshX devices
for FPATH in %{DESTDIR}/etc/sysconfig/network-scripts/ifcfg-eth*; do
    # Here the implicit ls has incorporated %{DESTDIR}
    if grep -q '^ESSID=\"school-mesh-' "$FPATH" ;then
        /usr/bin/xs-commitchanged --remove -m 'Remove old libertas conffile' "$FPATH"
    fi
done
# remove eth1:1 if it's the 'school server master address'
FPATH="%{DESTDIR}/etc/sysconfig/network-scripts/ifcfg-eth1:1"
if [ -e "$FPATH" ];then
    if grep -q '^IPADDR=172.18.1.1' "$FPATH" ;then
        /usr/bin/xs-commitchanged --remove -m 'Remove old conffile' "$FPATH"
    fi
fi

# Pg - prime the DB if needed.
if [ ! -e /library/pgsql-xs/data-8.3/PG_VERSION ];then
   /etc/init.d/pgsql-xs initdb
fi

# and set it to autostart
chkconfig --add pgsql-xs
chkconfig  postgresql off

# enable no-fsck-questions 
chkconfig --add no-fsck-questions

#service rsyslog condrestart

%pre

##
## clear the way for a better pkg
##
## remove olpcsave links and olpcnew symlinks in /etc
find /etc -type l -name '*.olpcnew'  -lname '*fsroot*' -print0 | xargs -0 --no-run-if-empty rm
find /etc -type l -name '*.olpcsave' -lname '*fsroot*' -print0 | xargs -0 --no-run-if-empty rm

### CLEANUP "old" to XS 0.4 upgrade
## Remove symlinks and reinstate original files
## if they exist. Note that removing the symlinks
## in %pre is not enough to avoid conflicts with the
## new files. See %post for further cleanup actions.
BADLINKS='%{BADLINKS}'
for FPATH in $BADLINKS; do
    if [ -L "%{DESTDIR}$FPATH" ]; then
       /bin/rm "%{DESTDIR}$FPATH"
       if [ -e "%{DESTDIR}/$FPATH.olpcsave" ]; then
       	  mv "%{DESTDIR}/$FPATH.olpcsave" "%{DESTDIR}/$FPATH"
       fi
    fi
done

## Prepare a .git directory so xs-commitchanged
## can store its database...
if [ ! -d /etc/.git ];then
   pushd /etc
   git init
   chmod 700 .git
   popd
fi

# remove old stale init scripts
if chkconfig --level 3 olpc-mesh-config ; then
      chkconfig --del olpc-mesh-config
fi
if chkconfig --level 3 olpc-network-config ; then
      chkconfig --del olpc-network-config
fi

# Change the network infra we use
# note that 'network' now defaults to off
chkconfig --level 345 network on
if chkconfig --level 3 NetworkManager ; then
   chkconfig --del NetworkManager
fi


%preun
if [ $1 = 0 ]; then
   /sbin/service pgsql-xs stop  > /dev/null 2>&1
   chkconfig --del pgsql-xs
fi

%files
%{_sysconfdir}/xs-config.make
%{_sysconfdir}/dhclient-exit-hooks
%{_sysconfdir}/usbmount/mount.d/01_beep_on_mount
%{_sysconfdir}/usbmount/mount.d/99_beep_when_done
%config(noreplace) /fsckoptions
%config(noreplace) %{_sysconfdir}/*.in
%config(noreplace) %{_sysconfdir}/ejabberd/ejabberd-xs.cfg.in
%config(noreplace) %{_sysconfdir}/ejabberd/ejabberd.pem
%config(noreplace) %{_sysconfdir}/httpd/conf/httpd-xs.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf.in
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/syslog-xslogs
%config(noreplace) %{_sysconfdir}/ssh/sshd_config.in
%config(noreplace) %{_sysconfdir}/sysconfig/*.in
%config(noreplace) %{_sysconfdir}/xinetd.d/*.in
%config(noreplace) %{_sysconfdir}/init.d/no-fsck-questions
%config(noreplace) %{_sysconfdir}/sysconfig/olpc-scripts/

%config(noreplace) /var/named-xs
%attr(750, root , named)   %dir /var/named-xs
%attr(770, named , named)  %dir /var/named-xs/data

#Pg
%config(noreplace) %{_sysconfdir}/pgsql-xs/p*.conf
%config(noreplace) %{_sysconfdir}/sysconfig/pgsql/pgsql-xs
%{_sysconfdir}/init.d/pgsql-xs
%attr(700, postgres, postgres)   %dir /library/pgsql-xs
%attr(700, postgres, postgres)   %dir /library/pgsql-xs/data-8.3

%attr(750, root , root)   %dir %{_sysconfdir}/sudoers.d
%attr(440, root , root) %config(noreplace) %{_sysconfdir}/sudoers.d/*

%{_bindir}/xs-commitchanged
%{_bindir}/cat-parts
%doc README.no-fsck-questions
%doc README 

%description
The default service configuration of an OLPC XS School server.

