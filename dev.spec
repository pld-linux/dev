Summary:	/dev entries
Summary(fr):	Entrées de /dev.
Summary(de):	/dev-Einträge
Summary(pl):	Pliki specjalne /dev/*
Summary(tr):	/dev dizini
Name:		dev
Version:	2.7.7
Release:	5
#######		From ftp.redhat.com/rawhide
Source:		%{name}-%{version}.tar.gz
Copyright:	public domain
Group:		Base
Group(pl):	Podstawowe
#BuildPrereq:	setup
# remove shadow if floppy and console group exist in setup
#BuildPrereq:	shadow
#Prereq:		setup
Buildroot:	/tmp/%{name}-%{version}-root
Autoreqprov:	no

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

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT

#add group for floppy and console
# if setup contains this group then remove next 4 lines 
#grep '^floppy:' /etc/group  >/dev/null \
#	|| groupadd -g 19 -r -f floppy >/dev/null
#grep '^console:' /etc/group >/dev/null \
#	|| groupadd -g 20 -f -r console >/dev/null

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
mknod kbd c 11 0                                                                
chmod 666 fb*                                                                   
                                                                                
# remove devices that will *never* exist on a m68k                              
rm -f hd* aztcd mcd sbpcd1 cdu31a sbpcd2 scd3                                   
rm -f sjcd cdu535 sbpcd3 sonycd cm206cd sbpcd                                   
rm -f gscd sbpcd0 atibm inportbm logibm psaux                                   
                                                                                
%endif

# Coda support 
mknod cfs0 c 67 0

# PPP support
mknod ppp c 108 0

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

ln -s midi00 midi

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

#raid

mknod md0 b 9 0
mknod md1 b 9 1
mknod md2 b 9 2
mknod md3 b 9 3
mknod md4 b 9 4
mknod md5 b 9 5
mknod md6 b 9 6
mknod md7 b 9 7
mknod md8 b 9 8
mknod md9 b 9 9
mknod md10 b 9 10
mknod md11 b 9 11
mknod md12 b 9 12
mknod md13 b 9 13
mknod md14 b 9 14
mknod md15 b 9 15

#temporary
install -d $RPM_BUILD_ROOT/proc/asound
touch $RPM_BUILD_ROOT/proc/asound/snd

ln -s ../proc/asound/snd snd

# prepared for SysVinit
mknod initctl p

#prepared for Log Daemon
mkfifo --mode=666 syslog

%pre
# if setup contains groups floppy and console this mayby obsoletes
#%{_sbindir}/groupadd -g 19 -r -f floppy
#%{_sbindir}/groupadd -g 20 -r -f console

%post
if [ -f /etc/fstab ] ; then
  # add /dev/pts to fstab if fstab exists (install2 does it during install)
  if grep 'devpts' /etc/fstab >/dev/null 2>&1 ; then : ; else
    # note that we do not disallow comments; we wish to allow people
    # to comment it out if they so desire.
    TMP=$(mktemp /tmp/fstab.XXXXXX)
    sed '/\/proc/a\
pts                    /dev/pts                devpts  mode=0600       0 0
        ' < /etc/fstab > $TMP && mv -f $TMP /etc/fstab || { echo "failed to add devpts filesystem to /etc/fstab" 1>&2 ; exit 1 ; }
    rm -f $TMP
  fi
fi

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)

#a#
%attr(662,root, sys) /dev/admmidi*

%config(noreplace) %verify(not link) %attr(666,root, sys) /dev/adsp
%attr(662,root, sys) /dev/adsp?*

%config(noreplace) %verify(not link) %attr(662,root,root) /dev/amidi
%attr(662,root,root) /dev/amidi?*

%attr(664,root,root) /dev/atibm

%config(noreplace) %verify(not link) %attr(662,root, sys) /dev/audio
%attr(662,root, sys) /dev/audio?*

%attr(664,root,root) /dev/aztcd


#b#
%attr(664,root,root) /dev/bpcd

#c#
%attr(600,root,root)	/dev/capi*
%attr(664,root,root)    /dev/cdu31a
%attr(640,root,disk)    /dev/cdu535
%attr(600,root,root)    /dev/cfs0
%attr(664,root,root)    /dev/cm206cd
%attr(660,root,console) /dev/console
%attr(664,root,root)    /dev/cui*
%attr(600,root,root)    /dev/cum*

#d#
%attr(600,root,root) /dev/dcbri*
%attr(660,root, sys) /dev/dcxx*
%attr(662,root, sys) /dev/dmfm*
%attr(662,root, sys) /dev/dmmidi*
%config(noreplace) %verify(not link) %attr(662,root, sys) /dev/dsp
%attr(662,root, sys) /dev/dsp?*

#e#
%attr(600,root,root) /dev/enskip

#f#
%config(noreplace) %verify(not link) %attr(644,root,root)   /dev/fb
%attr(644,root,root)   /dev/fb?*
%attr(660,root,floppy) /dev/fd*
%config(noreplace) %verify(not link) %attr(666,root,root) /dev/ftape
%attr(644,root,root)   /dev/full

#g#
%attr(664,root,root) /dev/gscd

#h#
%attr(660,root,disk) /dev/hd*
%attr(660,root,disk) /dev/ht0

#i#
%attr(600,root,root) /dev/i2c*
%dir /dev/ida
%attr(660,root,disk) /dev/ida/*
%attr(600,root,root) /dev/initctl
%attr(664,root,root) /dev/inportbm
%attr(600,root,root) /dev/ipauth
%attr(600,root,root) /dev/ipl
%attr(600,root,root) /dev/ipnat
%attr(600,root,root) /dev/ippp*
%attr(660,root, sys) /dev/iscc*
%attr(600,root,root) /dev/isctl
%attr(600,root,root) /dev/isdn?
%attr(600,root,root) /dev/isdn??
%config(noreplace) %verify(not link) %attr(600,root,root) /dev/isdnctrl
%attr(600,root,root) /dev/isdnctrl?*
%attr(444,root,root) /dev/isdninfo

#j#
%attr(660,root, sys) /dev/js*

#k#
%attr(640,root,kmem) /dev/kmem

#l#
%attr(666,root,root) /dev/log
%attr(664,root,root) /dev/logibm
%attr(660,root,disk) /dev/loop*

%attr(660,root,daemon) /dev/lp*

#m#
%attr(640,root,disk) /dev/mcd
%attr(640,root,kmem) /dev/mem
%config(noreplace) %verify(not link) %attr(662,root,sys) /dev/midi
%attr(662,root, sys) /dev/midi?*
%config(noreplace) %verify(not link) %attr(662,root,sys) /dev/mixer
%attr(662,root, sys) /dev/mixer?*
%attr(660,root, sys) /dev/mmetfgrab
%attr(600,root,root) /dev/mpu401*
%attr(662,root, sys) /dev/music
%attr(600,root, root) /dev/md*

#n#
%attr(660,root,disk) /dev/nb*
%config(noreplace) %verify(not link) %attr(666,root,root) /dev/nftape
%attr(660,root,disk) /dev/nht*
%attr(660,root,disk) /dev/nqft*
%attr(660,root,disk) /dev/nrawqft*
%attr(660,root,disk) /dev/nrft*
%attr(660,root,disk) /dev/nst*
%attr(660,root,disk) /dev/ntpqic*
%attr(666,root,root) /dev/null
%attr(660,root,disk) /dev/nzqft*

#o#
%attr(664,root,root) /dev/optcd

#p#
%attr(640,root,daemon) /dev/par?
%attr(660,root,daemon) /dev/parport*

%attr(660,root,disk) /dev/pcd*
%attr(660,root,disk) /dev/pd*
%attr(660,root,disk) /dev/pf*
%attr(600,root,root) /dev/pg*

%attr(640,root,kmem) /dev/port
%attr(644,root,root) /dev/ppp
%attr(600,root,root) /dev/printer
%attr(664,root,root) /dev/psaux

%attr(660,root,disk) /dev/pt0
%attr(660,root,disk) /dev/pt1
%attr(660,root,disk) /dev/pt2
%attr(660,root,disk) /dev/pt3

%attr(666,root, tty) /dev/ptmx
%attr(666,root, tty) /dev/pty*
%dir /dev/pts

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

%config(noreplace) %verify(not link) %attr(660,root,disk) /dev/ramdisk

%attr(644,root,root) /dev/random
%attr(660,root,disk) /dev/rawqft*
%attr(660,root,disk) /dev/rft*
%attr(660,root, sys) /dev/rmidi*
%attr(660,root,disk) /dev/rmt*
%attr(644,root,root) /dev/route
%attr(664,root,root) /dev/rtc
%dir /dev/rd
%attr(660,root,disk) /dev/rd/*

#s#
%attr(640,root,disk) /dev/sbpc*
%attr(660,root,disk) /dev/scd*
%attr(660,root,disk) /dev/sd*

%attr(662,root,sys)  /dev/sequencer
%attr(662,root,sys)  /dev/sequencer2

%attr(600,root,root) /dev/sg*
%attr(664,root,root) /dev/sjcd
%attr(600,root,root) /dev/smtpe*

%attr(444,root,root) /dev/snd
%attr(666,root,root) /dev/sndstat

%attr(640,root,disk) /dev/sonycd

%attr(600,root,root) /dev/srnd*

%attr(660,root,disk) /dev/st?
%attr(600,root,root) /dev/staliomem*
%attr(666,root,root) /dev/std*

%attr(664,root,root) /dev/sunmouse
%attr(666,root,root) /dev/syslog
%attr(600,root,root) /dev/systty

#t#
%attr(660,root,disk) /dev/tape*
%attr(600,root,root) /dev/tlk*
%attr(660,root,disk) /dev/tpqic*

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

%attr(600,root,root) /dev/ttyC*
%attr(600,root,root) /dev/ttyD*
%attr(600,root,root) /dev/ttyE*
%attr(600,root,root) /dev/ttyI*
%attr(600,root,root) /dev/ttyM*
%attr(600,root,root) /dev/ttyP*
%attr(600,root,root) /dev/ttyR*

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
%attr(660,root, sys) /dev/wvisfgrab

#x#
%attr(660,root,disk) /dev/xd*

#y#

#z#
%attr(666,root,root) /dev/zero
%attr(660,root,disk) /dev/zqft*
