Summary:	/dev entries
Summary(fr):	Entrées de /dev.
Summary(de):	/dev-Einträge
Summary(pl):	Pliki specjalne /dev/*
Summary(tr):	/dev dizini
Name:		dev
Version:	2.7.3
Release:	2
#######		From ftp.redhat.com/rawhide
Source:		%{name}-%{version}.tar.gz
Copyright:	public domain
Group:		Base
Buildroot:	/tmp/%{name}-%{version}-root
Autoreqprov:	no
Prereq:		setup

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

cd dev

# tar doesn't save some permissions unless the p option is used
# this code protects against dev package updaters forgetting to
# use the p option when unpacking the souce tarball.
for dev in zero null tty ttyp0 ; do
  if [ ! $(ls -l $dev | awk '{print $1}') = crw-rw-rw- ] ; then
    echo bad permissions on device $dev 1>&2
    exit 1
  fi
done

%ifarch sparc
# SPARC specific devices
ln -s sunmouse mouse
mknod kbd c 11 0
mknod openprom c 10 139
chmod 666 fb*

# remove devices that will *never* exist on a SPARC
rm -f hd* aztcd mcd sbpcd1 cdu31a sbpcd2 scd3
rm -f sjcd cdu535 sbpcd3 sonycd cm206cd sbpcd
rm -f gscd sbpcd0 atibm inportbm logibm psaux

%endif

%ifarch m68k                                                                    
# m68k specific devices                                                         
mknod amigamouse c 10 4                                                         
mknod atarimouse c 10 5                                                         
mknod apollomouse c 10 7                                                        
ln -s amigamouse mouse                                                          
mknod fdhd0 b 2 4                                                               
mknod fdhd1 b 2 5                                                               
mknod fb0current c 29 0                                                         
mknod fb1current c 29 32                                                        
mknod kbd c 11 0                                                                
chmod 666 fb*                                                                   
                                                                                
# remove devices that will *never* exist on a m68k                              
rm -f hd* aztcd mcd sbpcd1 cdu31a sbpcd2 scd3                                   
rm -f sjcd cdu535 sbpcd3 sonycd cm206cd sbpcd                                   
rm -f gscd sbpcd0 atibm inportbm logibm psaux                                   
                                                                                
%endif

mknod fb0 c 29 0
mknod fb1 c 29 32

ln -s fb0 fb                                                                    

# Coda support 
mknod cfs0 c 67 0

# framebuffer support
mknod fb0 c 29 0
mknod fb1 c 29 32
mknod fb2 c 29 64
mknod fb3 c 29 96
mknod fb4 c 29 128
mknod fb5 c 29 160
mknod fb6 c 29 192
mknod fb7 c 29 224

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

#ALSA support
rm -f mixer*
mknod mixer0 c 14 0
mknod mixer1 c 14 16
mknod mixer2 c 14 32
mknod mixer3 c 14 48
ln -s mixer0 mixer

mknod midi0 c 14 2
mknod midi1 c 14 18
mknod midi2 c 14 34
mknod midi3 c 14 50
ln -s midi0 midi

rm -f dsp*
mknod dsp0 c 14 3
mknod dsp1 c 14 19
mknod dsp2 c 14 35
mknod dsp3 c 14 51
ln -s dsp0 dsp

rm -f audio*
mknod audio0 c 14 4
mknod audio1 c 14 20
mknod audio2 c 14 36
mknod audio3 c 14 52
ln -s audio0 audio

mknod adsp0 c 14 12
mknod adsp1 c 14 28
mknod adsp2 c 14 44
mknod adsp3 c 14 60
ln -s adsp0 adsp

mknod dmfm0 c 14 10
mknod dmfm1 c 14 26
mknod dmfm2 c 14 42
mknod dmfm3 c 14 58

mknod dmmidi0 c 14 9
mknod dmmidi1 c 14 25
mknod dmmidi2 c 14 41
mknod dmmidi3 c 14 57

mknod music c 14 8

mknod admmidi0 c 14 14
mknod admmidi1 c 14 30 
mknod admmidi2 c 14 46
mknod admmidi3 c 14 62

mknod amidi0 c 14 13
mknod amidi1 c 14 29
mknod amidi2 c 14 45
mknod amidi3 c 14 61
ln -s amidi0 amidi

ln -s music sequencer2

#temporary
install -d $RPM_BUILD_ROOT/proc/asound
touch $RPM_BUILD_ROOT/proc/asound/snd

ls -s ../proc/asound/snd snd

# prepared for SysVinit
mknod initctl p

#prepared for Log Daemon
mkfifo --mode=666 syslog

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
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)

%dir /dev/pts

#a#
%attr(664,root,root) /dev/atibm
%attr(662,root, sys) /dev/audio
%attr(662,root, sys) /dev/audio1
%attr(664,root,root) /dev/aztcd

%attr(666,root,root) /dev/adsp*
%attr(666,root,root) /dev/audio*
%attr(666,root,root) /dev/admmidi*
%attr(666,root,root) /dev/amidi*

#b#
%attr(664,root,root) /dev/bpcd

#c#
%attr(664,root,root) /dev/cdu31a
%attr(640,root,disk) /dev/cdu535
%attr(664,root,root) /dev/cm206cd
%attr(600,root,root) /dev/console
%attr(666,root,root) /dev/cui*
%attr(600,root,root) /dev/cum*
%attr(600,root,root) /dev/cfs0

#d#
%attr(666,root,root) /dev/dsp*
%attr(666,root,root) /dev/dmfm*
%attr(666,root,root) /dev/dmmidi*

#e#

#f#
%attr(644,root,  root) /dev/fb*
%attr(664,root,floppy) /dev/fd*
%attr(666,root,root) /dev/ftape
%attr(644,root,root) /dev/full

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
%attr(600,root,root) /dev/initctl

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
%attr(666,root,root) /dev/mixer*
%attr(666,root,root) /dev/music

#n#
%attr(660,root,root) /dev/nb*
%attr(660,root,disk) /dev/nht0
%attr(660,root,disk) /dev/nrft*
%attr(660,root,disk) /dev/nst*
%attr(666,root,root) /dev/null

%attr(666,root,root) /dev/nftape

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

%attr(660,root,disk) /dev/ramdisk

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

%attr(666,root,root) /dev/sequencer
%attr(666,root,root) /dev/sequencer2

%attr(444,root,root) /dev/snd

%attr(600,root,sys) /dev/sg*

%attr(664,root,root) /dev/sjcd
%attr(666,root,root) /dev/sndstat

%attr(640,root,disk) /dev/sonycd

%attr(660,root,disk) /dev/st*

%attr(664,root,root) /dev/sunmouse
%attr(600,root,root) /dev/systty

%attr(666,root,root) /dev/syslog

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
* Mon Apr 27 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [2.7.3-2]
- added /dev/initctl,
- added pts device to /etc/fstab,
- added /dev/syslog.

* Mon Apr 26 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
  [2.7.3-1]
- upgrade to 2.7.3,
- removed /dev/log, /dev/cua[0-3].

* Tue Apr 20 1999 Artur Frysiak <wiget@pld.org.pl>
  [2.5.9-3]
- compiled on rpm 3
- fixed framebuffer support
- added coda support

* Sat Dec 12 1998 Sergiusz Paw³owicz <ser@hyperreal.art.pl>
  [2.5.9-1d]
- added polish translation to spec (regards to PLD Team),
- added handles to Unix98 pty support,
- added handles to framebuffer support,
- revised spec file, adding group 'floppy' removed.
- removed initctl -- SysVinit provides it.
- start at RH spec file.
