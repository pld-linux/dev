Summary: /dev entries
Name: dev
Version: 2.5.9
Release: 1
Source: dev-%{PACKAGE_VERSION}.cpio
Copyright: public domain
Group: Base
Buildroot: /var/tmp/dev-root
Autoreqprov: no
Prefix: /dev
Requires: shadow-utils >= 970616-7
Prereq: shadow-utils
Summary(fr): Entrées de /dev.
Summary(tr): /dev dizini
Summary(de): /dev-Einträge

%description
Unix and unix like systems (including Linux) use file system entries
to represent devices attached to the machine. All of these entries
are in the /dev tree (though they don't have to be), and this package
contains the most commonly used /dev entries. These files are essential
for a system to function properly.

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

%changelog
* Fri May 08 1998 Michael K. Johnson <johnsonm@redhat.com>

- added paride devices

* Tue May 05 1998 Erik Troan <ewt@redhat.com>

- uses a filelist
- ghosts /dev/log

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- fixed groupadd call in the %install

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Apr 23 1998 Prospector System <bugs@redhat.com>
- translations modified for fr, tr

* Thu Apr 23 1998 Erik Troan <ewt@redhat.com>
- fixed preinstall script

* Tue Apr 21 1998 Erik Troan <ewt@redhat.com>
- updated groupadd to work with upgrades where the floppy group already exists

* Mon Nov 10 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added more ramdisk entries

* Wed Oct 29 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added fd and ramdisk symlinks

* Fri Oct 24 1997 Michael K. Johnson <johnsonm@redhat.com>
- Added floppy group for floppies; made them group-writable.

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- added bpcd device

* Thu Apr 10 1997 Erik Troan <ewt@redhat.com>
- Added ftape devices

* Tue Mar 25 1997 Erik Troan <ewt@redhat.com>
- Fixed stdin, stdout devices.
- Moved rtc to cpio archive
- Added ISDN devices

%prep
%setup -c -T
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
BUILD_DIR=`pwd`

# Make sure that the floppy group exists on the build machine
/usr/sbin/groupadd -g 19 -r -f floppy > /dev/null

# unpack in build root
( cd $RPM_BUILD_ROOT
  cpio -iumd < $RPM_SOURCE_DIR/dev-%{PACKAGE_VERSION}.cpio
)

# do some cleanup in build root
cd $RPM_BUILD_ROOT

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

chmod 660 dev/lp*
chgrp daemon dev/lp*

for I in 9 10 11 12; do
	mknod dev/tty$I c 4 $I
	chown root:tty dev/tty$I
	chmod 600 dev/tty$I
done

cd dev

chgrp floppy fd?*

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

chmod 0660      pd[a-d]* pcd[0-3] pf[0-3] pt[0-3]
chown root:disk pd[a-d]* pcd[0-3] pf[0-3] pt[0-3]

# build the file list
cd $BUILD_DIR
ls $RPM_BUILD_ROOT/dev | sed 's,^,/dev/,' > filelist
touch $RPM_BUILD_ROOT/dev/log
chown 0.0 $RPM_BUILD_ROOT/dev/log
chmod 666 $RPM_BUILD_ROOT/dev/log
echo "%ghost /dev/log" >> filelist


%clean 
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -g 19 -r -f floppy

%files -f filelist
