Summary:	/dev entries
Summary(fr):	Entrées de /dev.
Summary(de):	/dev-Einträge
Summary(pl):	Pliki specjalne /dev/*
Summary(tr):	/dev dizini
Name:		dev
Version:	2.7.3
Release:	1
#######		From ftp.redhat.com/rawhide
Source:		%{name}-%{version}.tar.gz
Copyright:	public domain
Group:		Base
Buildroot:	/tmp/%{name}-%{version}-root
Autoreqprov:	no
Prereq:		shadow-utils

%description
Unix and unix like systems (including Linux) use file system entries
to represent devices attached to the machine. All of these entries
are in the /dev tree (though they don't have to be), and this package
contains the most commonly used /dev entries. These files are essential
for a system to function properly.

%description -l pl
Wszystkie systemy Unix, jak na przyk³ad Linux, u¿ywaj± plików do przedstawienia 
urz±dzeñ pod³±czonych do komputera. Wszystkie te pliki znajduj± siê zwykle w 
katalogu /dev. Pakiet ten zawiera wiêkszo¶æ popularnych plików specjalnych, 
s± one jedn± z wa¿niejszych czê¶ci prawid³owo dzia³aj±cego systemu operacyjnego.

%description -l fr
Unix et les systèmes apparentés (dont Linux) utilise des fichiers pour
représenter les périphériques reliés à la machine. Toutes ces entrées
sont dans l'arborescence /dev (ce n'est pas obligatoire). Ce paquetage
contient les entrées /dev les plus courantes. Elles sont essentielles
pour qu'un système fonctionne correctement.

%description -l tr
Unix ve Unix benzeri sistemler (Linux da dahil olmak üzere), makinaya baðlý
aygýtlarý göstermek için özel dosyalar kullanýrlar. Bu özel dosyalarýn tümü
/dev dizin yapýsý altýndadýr. Bu paket en çok kullanýlan /dev dosyalarýný
içerir. Bu dosyalar, bir sistemin düzgün olarak iþleyebilmesi için temel
gereksinimlerdendir.

%description -l de
Unix und Unix-ähnliche Systeme (inkl. Linux) verwenden Dateisystem-
Einträge zum Darstellen angeschlossener Geräte. Diese Einträge befinden
sich (nicht notwendigerweise) im Verzeichnis /dev. Dieses Paket enthält
die üblichsten /dev-Einträge. Diese Dateien sind für das Funktionieren
eines Systems unbedingt erforderlich.

%prep
%setup -q -c -T
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT
BUILD_DIR=`pwd`

#add group for floppy and console
/usr/sbin/groupadd -g 19 -r -f floppy >/dev/null
/usr/sbin/groupadd -g 20 -f -r console >/dev/null

# do some cleanup in build root
cd $RPM_BUILD_ROOT
tar xpSzf $RPM_SOURCE_DIR/%{name}-%{version}.tar.gz

# tar doesn't save some permissions unless the p option is used
# this code protects against dev package updaters forgetting to
# use the p option when unpacking the souce tarball.
for dev in dev/zero dev/null dev/tty dev/ttyp0 ; do
  if [ ! $(ls -l $dev | awk '{print $1}') = crw-rw-rw- ] ; then
    echo bad permissions on device $dev 1>&2
    exit 1
  fi
done

%ifarch sparc
# SPARC specific devices
ln -s sunmouse dev/mouse
mknod dev/fb0 c 29 0
mknod dev/fb1 c 29 32
mknod dev/kbd c 11 0
mknod dev/openprom c 10 139
ln -s fb0 dev/fb
chmod 666 dev/fb*

# remove devices that will *never* exist on a SPARC
rm -f dev/hd* dev/aztcd dev/mcd dev/sbpcd1 dev/cdu31a dev/sbpcd2 dev/scd3
rm -f dev/sjcd dev/cdu535 dev/sbpcd3 dev/sonycd dev/cm206cd dev/sbpcd
rm -f dev/gscd dev/sbpcd0 dev/atibm dev/inportbm dev/logibm dev/psaux

%endif

%ifarch m68k                                                                    
# m68k specific devices                                                         
mknod amigamouse c 10 4                                                         
mknod atarimouse c 10 5                                                         
mknod apollomouse c 10 7                                                        
ln -s amigamouse mouse                                                          
mknod fdhd0 b 2 4                                                               
mknod fdhd1 b 2 5                                                               
mknod fb0 c 29 0                                                                
mknod fb1 c 29 32                                                               
mknod fb0current c 29 0                                                         
mknod fb1current c 29 32                                                        
mknod kbd c 11 0                                                                
ln -s fb0 fb                                                                    
chmod 666 fb*                                                                   
                                                                                
# remove devices that will *never* exist on a m68k                              
rm -f hd* aztcd mcd sbpcd1 cdu31a sbpcd2 scd3                                   
rm -f sjcd cdu535 sbpcd3 sonycd cm206cd sbpcd                                   
rm -f gscd sbpcd0 atibm inportbm logibm psaux                                   
                                                                                
%endif

chmod 660 dev/lp*
chgrp daemon dev/lp*

cd dev

chgrp floppy fd?*

# framebuffer support
mknod fb0 b 29 0
mknod fb1 b 29 32
mknod fb2 b 29 64
mknod fb3 b 29 96
mknod fb4 b 29 128
mknod fb5 b 29 160
mknod fb6 b 29 192
mknod fb7 b 29 224

ln -s fb0 fb0current
ln -s fb1 fb1current
ln -s fb2 fb2current
ln -s fb3 fb3current
ln -s fb4 fb4current
ln -s fb5 fb5current
ln -s fb6 fb6current
ln -s fb7 fb7current

# watchdog support
mknod watchdog c 10 130 

# route 
mknod route c 36 0

%pre
/usr/sbin/groupadd -g 19 -r -f floppy
/usr/sbin/groupadd -g 20 -r -f console

%post
if [ -f /etc/fstab ] ; then
  # add /dev/pts to fstab if fstab exists (install2 does it during install)
  if grep 'devpts' /etc/fstab >/dev/null 2>&1 ; then : ; else
    # note that we do not disallow comments; we wish to allow people
    # to comment it out if they so desire.
    TMP=$(mktemp /tmp/fstab.XXXXXX)
    sed '/\/proc/a\
none                    /dev/pts                devpts  mode=0622       0 0
        ' < /etc/fstab > $TMP && mv -f $TMP /etc/fstab || { echo "failed to add devpts filesystem to /etc/fstab" 1>&2 ; exit 1 ; }
    rm -f $TMP
  fi
fi

%postun

%clean 
#rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)

%dir /dev/pts

#a#
%attr(664,root,root) /dev/atibm
%attr(662,root, sys) /dev/audio
%attr(662,root, sys) /dev/audio1
%attr(664,root,root) /dev/aztcd

#b#
%attr(664,root,root) /dev/bpcd

#c#
%attr(664,root,root) /dev/cdu31a
%attr(640,root,disk) /dev/cdu535
%attr(664,root,root) /dev/cm206cd
%attr(600,root,root) /dev/console
%attr(666,root,root) /dev/cui*
%attr(600,root,root) /dev/cum*

#d#
%attr(662,root,sys) /dev/dsp
%attr(662,root,sys) /dev/dsp1

#e#

#f#
%attr(644,root,  root) /dev/fb*
%attr(664,root,floppy) /dev/fd*
%attr(-,root,root) /dev/ftape
%attr(-,root,root) /dev/full

#g#
%attr(664,root,root) /dev/gscd

#h#
%attr(660,root,disk) /dev/hd*
%attr(660,root,disk) /dev/ht0

#i#
%attr(664,root,root) /dev/ida/*
%attr(664,root,root) /dev/inportbm
%attr(600,root,root) /dev/ippp*
%attr(600,root,root) /dev/isctl
%attr(600,root,root) /dev/isdnctrl*
%attr(444,root,root) /dev/isdninfo

#j#

#k#
%attr(640,root,kmem) /dev/kmem

#l#
#%attr(666,root,root) /dev/log
%attr(664,root,root) /dev/logibm
%attr(660,root,disk) /dev/loop*

%attr(660,root,daemon) /dev/lp*

#m#
%attr(640,root,disk) /dev/mcd
%attr(640,root,kmem) /dev/mem
%attr(666,root, sys) /dev/midi*
%attr(666,root, sys) /dev/mixer
%attr(666,root, sys) /dev/mixer1

#n#
%attr(660,root,root) /dev/nb*
%attr(660,root,disk) /dev/nht0
%attr(660,root,disk) /dev/nrft*
%attr(660,root,disk) /dev/nst*
%attr(666,root,root) /dev/null

%attr(-,root,root) /dev/nftape

#o#
%attr(664,root,root) /dev/optcd

#p#
%attr(640,root,daemon) /dev/par*

%attr(660,root,disk) /dev/pcd*
%attr(660,root,disk) /dev/pd*
%attr(660,root,disk) /dev/pf*

%attr(640,root,kmem) /dev/port
%attr(600,root,root) /dev/printer
%attr(664,root,root) /dev/psaux

%attr(660,root,disk) /dev/pt0
%attr(660,root,disk) /dev/pt1
%attr(660,root,disk) /dev/pt2
%attr(660,root,disk) /dev/pt3

%attr(666,root,tty) /dev/ptmx
%attr(666,root,tty) /dev/pty*

#r#
%attr(640,root,disk) /dev/ram
%attr(660,root,disk) /dev/ram0
%attr(660,root,disk) /dev/ram1*
%attr(660,root,disk) /dev/ram2
%attr(660,root,disk) /dev/ram3
%attr(660,root,disk) /dev/ram4
%attr(660,root,disk) /dev/ram5
%attr(660,root,disk) /dev/ram6
%attr(660,root,disk) /dev/ram7
%attr(660,root,disk) /dev/ram8
%attr(660,root,disk) /dev/ram9

%attr(-,root,root) /dev/ramdisk

%attr(644,root,root) /dev/random
%attr(660,root,disk) /dev/rft*
%attr(644,root,root) /dev/route
%attr(664,root,root) /dev/rtc
%attr(600,root,root) /dev/rd/*

#s#
%attr(640,root,disk) /dev/sbpc*

%attr(660,root,disk) /dev/scd*

%attr(660,root,disk) /dev/sda*
%attr(660,root,disk) /dev/sdb*
%attr(660,root,disk) /dev/sdc*
%attr(660,root,disk) /dev/sdd*
%attr(660,root,disk) /dev/sde*
%attr(660,root,disk) /dev/sdf*
%attr(660,root,disk) /dev/sdg*

%attr(664,root,sys) /dev/sequencer

%attr(600,root,sys) /dev/sg*

%attr(664,root,root) /dev/sjcd
%attr(666,root, sys) /dev/sndstat

%attr(640,root,disk) /dev/sonycd

%attr(660,root,disk) /dev/st*

%attr(664,root,root) /dev/sunmouse
%attr(600,root,root) /dev/systty

#t#
%attr(666,root,root) /dev/tty

%attr(600,root, tty) /dev/tty0
%attr(600,root, tty) /dev/tty1*
%attr(600,root, tty) /dev/tty2
%attr(600,root, tty) /dev/tty3
%attr(600,root, tty) /dev/tty4
%attr(600,root, tty) /dev/tty5
%attr(600,root, tty) /dev/tty6
%attr(600,root, tty) /dev/tty7
%attr(600,root, tty) /dev/tty8
%attr(600,root, tty) /dev/tty9

%attr(666,root,root) /dev/ttyI*

%attr(600,root,root) /dev/ttyM*

%attr(644,root,root) /dev/ttyS*

%attr(666,root, tty) /dev/ttya*
%attr(666,root, tty) /dev/ttyb*
%attr(666,root, tty) /dev/ttyc*
%attr(666,root, tty) /dev/ttyd*
%attr(666,root, tty) /dev/ttye*
%attr(666,root, tty) /dev/ttyp*
%attr(666,root, tty) /dev/ttyq*
%attr(666,root, tty) /dev/ttyr*
%attr(666,root, tty) /dev/ttys*
%attr(666,root, tty) /dev/ttyt*
%attr(666,root, tty) /dev/ttyu*
%attr(666,root, tty) /dev/ttyv*
%attr(666,root, tty) /dev/ttyw*
%attr(666,root, tty) /dev/ttyx*
%attr(666,root, tty) /dev/ttyy*
%attr(666,root, tty) /dev/ttyz*

#u#
%attr(644,root,root) /dev/urandom

#v#
%attr(620,root,tty) /dev/vcs*

#w#
%attr(600,root,root) /dev/watchdog

#x#
%attr(640,root,disk) /dev/xd*

#y#

#z#
%attr(666,root,root) /dev/zero

%changelog
* Mon Apr 26 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [2.7.3-1]
- upgrade to 2.7.3,
- added pts update,
- added route, watchdog, framebuffer, console device,
- removed /dev/log, /dev/cua[0-3].
