Summary:	/dev entries
Summary(fr):	Entrées de /dev.
Summary(de):	/dev-Einträge
Summary(pl):	Pliki specjalne /dev/*
Summary(tr):	/dev dizini
Name:		dev
Version:	2.5.9
Release:	3
#######		From ftp.redhat.com/rawhide
Source:		%{name}-%{version}.cpio
Copyright:	public domain
Group:		Base
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
rm -rf $RPM_BUILD_ROOT

%build
install -d $RPM_BUILD_ROOT
BUILD_DIR=`pwd`

# unpack in build root
( cd $RPM_BUILD_ROOT
  cpio -iumd < %{SOURCE0}
)

# do some cleanup in build root
cd $RPM_BUILD_ROOT

%ifarch sparc
# SPARC specific devices
ln -s sunmouse dev/mouse
mknod dev/kbd c 11 0
mknod dev/openprom c 10 139

# remove devices that will *never* exist on a SPARC
rm -f dev/hd* dev/aztcd dev/mcd dev/sbpcd1 dev/cdu31a dev/sbpcd2 dev/scd3
rm -f dev/sjcd dev/cdu535 dev/sbpcd3 dev/sonycd dev/cm206cd dev/sbpcd
rm -f dev/gscd dev/sbpcd0 dev/atibm dev/inportbm dev/logibm dev/psaux

%endif

#chmod 660 dev/lp*
#chgrp daemon dev/lp*

for I in 9 10 11 12; do
	mknod dev/tty$I c 4 $I
	chown root:tty dev/tty$I
#	chmod 600 dev/tty$I
done

cd dev

#chgrp floppy fd?*

ln -s ram0 ramdisk
ln -s ../proc/self/fd fd

mknod pda  b 45 0
mknod pda1 b 45 1
mknod pda2 b 45 2
mknod pda3 b 45 3
mknod pda4 b 45 4

mknod pdb  b 45 16
mknod pdb1 b 45 17
mknod pdb2 b 45 18
mknod pdb3 b 45 19
mknod pdb4 b 45 20

mknod pdc  b 45 32
mknod pdc1 b 45 33
mknod pdc2 b 45 34
mknod pdc3 b 45 35
mknod pdc4 b 45 36

mknod pdd  b 45 48
mknod pdd1 b 45 49
mknod pdd2 b 45 50
mknod pdd3 b 45 51
mknod pdd4 b 45 52

mknod pcd0 b 46 0
mknod pcd1 b 46 1
mknod pcd2 b 46 2
mknod pcd3 b 46 3

mknod pf0 b 47 0
mknod pf1 b 47 1
mknod pf2 b 47 2
mknod pf3 b 47 3

mknod pt0  c 96 0
mknod pt1  c 96 1
mknod pt2  c 96 2
mknod pt3  c 96 3

#chmod 0660      pd[a-d]* pcd[0-3] pf[0-3] pt[0-3]
#chown root:disk pd[a-d]* pcd[0-3] pf[0-3] pt[0-3]

# unix98 pty support 
mknod ptmx c 5 2
#chmod 666 ptmx; chown root.tty ptmx
install -d -m 755 pts

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
ln -s fb0 fb

# It's correct ?
#chmod 666 fb*

# watchdog support
mknod watchdog c 10 130 

# /dev/log support
touch log
# route 
mknod route c 36 0

# Coda support
mknod cfs0 c 67 0

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

#b#
%attr(664,root,root) /dev/bpcd

#c#
%attr(664,root,root) /dev/cdu31a
%attr(640,root,disk) /dev/cdu535
%attr(600,root,root) /dev/cfs0
%attr(664,root,root) /dev/cm206cd
%attr(600,root,root) /dev/console
%attr(666,root,root) /dev/cui*

#d#
%attr(662,root,sys) /dev/dsp
%attr(662,root,sys) /dev/dsp1

#e#

#f#
%attr(644,root,  root) /dev/fb*
%attr(664,root,floppy) /dev/fd*

#g#
%attr(664,root,root) /dev/gscd

#h#
%attr(660,root,disk) /dev/hd*
%attr(660,root,disk) /dev/ht0

#i#
%attr(664,root,root) /dev/inportbm
%attr(600,root,root) /dev/ippp*
%attr(600,root,root) /dev/isdnctrl*
%attr(444,root,root) /dev/isdninfo

#j#

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
%attr(666,root, sys) /dev/midi*
%attr(666,root, sys) /dev/mixer
%attr(666,root, sys) /dev/mixer1

#n#
%attr(660,root,disk) /dev/nht0
%attr(660,root,disk) /dev/nrft*
%attr(660,root,disk) /dev/nst*
%attr(666,root,root) /dev/null

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

%attr(644,root,root) /dev/random
%attr(660,root,disk) /dev/rft*
%attr(644,root,root) /dev/route
%attr(664,root,root) /dev/rtc

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
