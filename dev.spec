Summary:	/dev entries
Summary(de):	/dev-Einträge
Summary(fr):	Entrées de /dev
Summary(pl):	Pliki specjalne /dev/*
Summary(tr):	/dev dizini
Name:		dev
Version:	2.8.0
Release:	11
License:	public domain
Group:		Base
Group(cs):	Základ
Group(da):	Basal
Group(de):	Basis
Group(es):	Base
Group(fr):	Base
Group(is):	Grunnforrit
Group(it):	Base
Group(ja):	¥Ù¡¼¥¹
Group(no):	Basis
Group(pl):	Podstawowe
Group(pt):	Base
Group(pt_BR):	Base
Group(ru):	âÁÚÁ
Group(sl):	Osnova
Group(sv):	Bas
Group(uk):	âÁÚÁ
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	setup
BuildRequires:	shadow
PreReq:		setup >= 2.4.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Autoreqprov:	no

%define		perm_cdrom	660,root,disk

%description
Unix and unix like systems (including Linux) use file system entries
to represent devices attached to the machine. All of these entries are
in the /dev tree (though they don't have to be), and this package
contains the most commonly used /dev entries. These files are
essential for a system to function properly.

%description -l de
Unix und Unix-ähnliche Systeme (inkl. Linux) verwenden Dateisystem-
Einträge zum Darstellen angeschlossener Geräte. Diese Einträge
befinden sich (nicht notwendigerweise) im Verzeichnis /dev. Dieses
Paket enthält die üblichsten /dev-Einträge. Diese Dateien sind für das
Funktionieren eines Systems unbedingt erforderlich.

%description -l fr
Unix et les systèmes apparentés (dont Linux) utilise des fichiers pour
représenter les périphériques reliés à la machine. Toutes ces entrées
sont dans l'arborescence /dev (ce n'est pas obligatoire). Ce paquetage
contient les entrées /dev les plus courantes. Elles sont essentielles
pour qu'un système fonctionne correctement.

%description -l pl
Wszystkie systemy klasy unices, w tym Linux, u¿ywaj± plików do
przedstawiania urz±dzeñ pod³±czonych do komputera. Wszystkie te pliki
znajduj± siê zwykle w katalogu /dev. Pakiet ten zawiera wiêkszo¶æ
popularnych plików specjalnych, s± one jedn± z wa¿niejszych czê¶ci
prawid³owo dzia³aj±cego systemu operacyjnego.

%description -l tr
Unix ve Unix benzeri sistemler (Linux da dahil olmak üzere), makinaya
baðlý aygýtlarý göstermek için özel dosyalar kullanýrlar. Bu özel
dosyalarýn tümü /dev dizin yapýsý altýndadýr. Bu paket en çok
kullanýlan /dev dosyalarýný içerir. Bu dosyalar, bir sistemin düzgün
olarak iþleyebilmesi için temel gereksinimlerdendir.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT

mknode() {
# [ -e $1 ] || mknod $1 $2 $3 $4
	rm -f $1
	mknod $1 $2 $3 $4
}

install -d $RPM_BUILD_ROOT

# add group for floppy and console
# if setup contains this group then remove next 4 lines
#grep '^floppy:' /etc/group >/dev/null \
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
for dev in zero null tty ttyp0; do
	if [ ! $(ls -l $dev | awk '{print $1}') = crw-rw-rw- ]; then
		echo bad permissions on device $dev 1>&2
		exit 1
	fi
done

%ifarch sparc
# SPARC specific devices
ln -sf sunmouse mouse
mknode openprom c 10 139
%endif

%ifarch m68k
# m68k specific devices
mknode amigamouse c 10 4
mknode atarimouse c 10 5
mknode apollomouse c 10 7
ln -sf amigamouse mouse
mknode fdhd0 b 2 4
mknode fdhd1 b 2 5
%endif

%ifarch sparc m68k
# common sparc & m68k specific devices
mknode kbd c 11 0
chmod 666 fb*
# remove devices that will *never* exist on a SPARC or m68k
rm -f aztcd mcd sbpcd* cm206cd cdu31a cdu535 sonycd sjcd gscd
rm -f hd* atibm inportbm logibm psaux
%endif

# Coda support
mknode cfs0 c 67 0

# PPP support
mknode ppp c 108 0

for i in 0 1 2 3 4 5 6 7; do
	ln -sf fb$i fb${i}current
done

# watchdog support
mknode watchdog c 10 130
mknod temperature c 10 131


# agpgart
mknode agpgart c 10 175

%ifarch %{ix86}
# toshiba support
mknode toshiba c 10 181
%endif

# route
mknode route c 36 0

# ALSA support
rm -f mixer*
mknode mixer0 c 14 0
mknode mixer1 c 14 16
mknode mixer2 c 14 32
mknode mixer3 c 14 48
ln -sf mixer0 mixer

ln -sf midi00 midi

rm -f dsp*
mknode dsp0 c 14 3
mknode dsp1 c 14 19
mknode dsp2 c 14 35
mknode dsp3 c 14 51
ln -sf dsp0 dsp

rm -f audio*
mknode audio0 c 14 4
mknode audio1 c 14 20
mknode audio2 c 14 36
mknode audio3 c 14 52
ln -sf audio0 audio

mknode adsp0 c 14 12
mknode adsp1 c 14 28
mknode adsp2 c 14 44
mknode adsp3 c 14 60
ln -sf adsp0 adsp

mknode dmfm0 c 14 10
mknode dmfm1 c 14 26
mknode dmfm2 c 14 42
mknode dmfm3 c 14 58

mknode dmmidi0 c 14 9
mknode dmmidi1 c 14 25
mknode dmmidi2 c 14 41
mknode dmmidi3 c 14 57

mknode music c 14 8

mknode admmidi0 c 14 14
mknode admmidi1 c 14 30
mknode admmidi2 c 14 46
mknode admmidi3 c 14 62

mknode amidi0 c 14 13
mknode amidi1 c 14 29
mknode amidi2 c 14 45
mknode amidi3 c 14 61
ln -sf amidi0 amidi

ln -sf music sequencer2

mknode aloadC0 c 116 0
mknode aloadC1 c 116 32
mknode aloadC2 c 116 64
mknode aloadC3 c 116 96
mknode aloadSEQ c 116 1

mknode amixer0 c 14 11
mknode amixer1 c 14 27
mknode amixer2 c 14 43
mknode amixer3 c 14 59

# video4linux support
mknode video0 c 81 0
mknode radio0 c 81 64
mknode vtx0 c 81 192
mknode vbi0 c 81 224
ln -sf video0 video
ln -sf radio0 radio
ln -sf vtx0 vtx
ln -sf vbi0 vbi

# raid
for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
	mknode md$i b 9 $i
done

# ataraid
mkdir ataraid
for d in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
    mknod ataraid/d$d b 114 $(( $d * 16 ))
    for p in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
	mknod ataraid/d${d}p${p} b 114 $(( $d * 16 + $p ))
    done
done

# netfilter
mknode ipstate c 95 2

# arpd
mknod arpd c 36 8

# temporary
install -d $RPM_BUILD_ROOT/proc/asound
> $RPM_BUILD_ROOT/proc/asound/dev

ln -sf ../proc/asound/dev snd

# prepared for SysVinit
mknode initctl p

# prepared for Log Daemon
mkfifo --mode=666 syslog

# libsvga char dev helpers
mknode svga c 209 0
mknode svga1 c 209 1
mknode svga2 c 209 2
mknode svga3 c 209 3
mknode svga4 c 209 4

# ipsec character device
mknode ipsec c 36 10

# raw io devices
mknode rawctl c 162 0
mkdir $RPM_BUILD_ROOT/dev/raw
minor=1
while [ "$minor" -ne 256 ]; do
	mknode "raw/raw$minor" c 162 $minor
	minor=$(($minor +1))
done

# ltmodem
mknode ttyLT0 c 62 64

# XFree86-nvidia-kernel a.k.a. kernel(-smp)-video-nvidia
for i in 0 1 2 3; do
	mknode nvidia$i c 195 $i
done
mknode nvidiactl c 195 255

# kernel 2.4 requires /dev/js* with major 13
for f in 0 1 2 3; do
	mv -f js$f oldjs$f
	mknode js$f c 13 $f
done

# irda-utils
mknode ircomm0 c 161 0
mknode ircomm1 c 161 1
mknode irlpt0 c 161 16
mknode irlpt1 c 161 17

# lirc
mknode lirc c 61 0
mknode lircm p

# usb
mkdir $RPM_BUILD_ROOT/dev/input
mkdir $RPM_BUILD_ROOT/dev/usb
for i in 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
	mknode input/js$i c 13 $i
	mknode input/mouse$i c 13 $(( $i + 32 ))
	mknode input/event$i c 13 $(( $i + 64 ))
	mknode usb/ttyACM$i c 166 $i
	mknode usb/lp$i c 180 $i
	mknode usb/scanner$i c 180 $(( $i + 48 ))
	mknode usb/ez$i c 180 $(( $i + 64 ))
	mknode usb/ttyUSB$i c 188 $i
	mknode usb/ttyUB$i c 216 $i
done
mknode input/mice c 13 31
mknode usb/rio500 c 180 64

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

#a#
%dir /dev/ataraid
%attr(660,root,disk) /dev/ataraid/*
%attr(660,root,audio) /dev/admmidi*

%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/adsp
%attr(660,root,audio) /dev/adsp?*

%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/amidi
%attr(660,root,audio) /dev/amidi?*

%attr(644,root,root) /dev/agpgart
%attr(660,daemon,root) /dev/arpd

%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/audio
%attr(660,root,audio) /dev/audio?*

#b#
%attr(%{perm_cdrom}) /dev/bpcd

#c#
%attr(600,root,root) /dev/capi*
%attr(600,root,root) /dev/cfs0
%attr(660,root,console) /dev/console
%attr(664,root,root) /dev/cui*
%attr(600,root,root) /dev/cum*

#d#
%attr(600,root,root) /dev/dcbri*
%attr(660,root,sys) /dev/dcxx*
%attr(660,root,audio) /dev/dmfm*
%attr(660,root,audio) /dev/dmmidi*
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/dsp
%attr(660,root,audio) /dev/dsp?*

#e#
%attr(600,root,root) /dev/enskip

#f#
%config(noreplace) %verify(not link) %attr(644,root,root) /dev/fb
%attr(664,root,video) /dev/fb?*
%attr(660,root,floppy) /dev/fd*
%config(noreplace) %verify(not link) %attr(666,root,root) /dev/ftape
%attr(644,root,root) /dev/full

#g#

#h#
%attr(660,root,disk) /dev/ht0

#i#
%attr(600,root,root) /dev/i2c*
%dir /dev/ida
%attr(660,root,disk) /dev/ida/*
%attr(600,root,root) /dev/initctl
%dir /dev/input
%attr(660,root,root) /dev/input/event*
%attr(660,root,js) /dev/input/js*
%attr(660,root,root) /dev/input/mice
%attr(660,root,root) /dev/input/mouse*
%attr(600,root,root) /dev/ipauth
%attr(600,root,root) /dev/ipl
%attr(600,root,root) /dev/ipnat
%attr(600,root,root) /dev/ipstate
%attr(600,root,root) /dev/ippp*
%attr(664,root,ttyS) /dev/ircomm0
%attr(664,root,ttyS) /dev/ircomm1
%attr(664,root,ttyS) /dev/irlpt0
%attr(664,root,ttyS) /dev/irlpt1
%attr(660,root,sys) /dev/iscc*
%attr(600,root,root) /dev/isctl
%attr(600,root,root) /dev/isdn?
%attr(600,root,root) /dev/isdn??
%config(noreplace) %verify(not link) %attr(600,root,root) /dev/isdnctrl
%attr(600,root,root) /dev/isdnctrl?*
%attr(444,root,root) /dev/isdninfo

#j#
%attr(660,root,sys) /dev/js*

#k#
%attr(640,root,kmem) /dev/kmem

#l#
%attr(660,root,root) /dev/lirc
%attr(660,root,root) /dev/lircm
%attr(660,root,disk) /dev/loop*
%attr(660,root,lp) /dev/lp*

#m#
%attr(640,root,kmem) /dev/mem
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/midi
%attr(660,root,audio) /dev/midi?*
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/mixer
%attr(660,root,audio) /dev/mixer?*
%attr(660,root,sys) /dev/mmetfgrab
%attr(600,root,root) /dev/mpu401*
%attr(660,root,audio) /dev/music
%attr(660,root,disk) /dev/md*

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
%attr(666,root,root) /dev/nvidia*
%attr(660,root,disk) /dev/nzqft*

#o#
%attr(%{perm_cdrom}) /dev/optcd
%attr(660,root,sys) /dev/oldjs*

#p#
%attr(660,root,lp) /dev/par?
%attr(660,root,lp) /dev/parport*

%attr(%{perm_cdrom}) /dev/pcd*
%attr(660,root,disk) /dev/pd*
%attr(660,root,disk) /dev/pf*
%attr(600,root,root) /dev/pg*

%attr(640,root,kmem) /dev/port
%attr(644,root,root) /dev/ppp
%attr(600,root,root) /dev/printer

%attr(660,root,disk) /dev/pt0
%attr(660,root,disk) /dev/pt1
%attr(660,root,disk) /dev/pt2
%attr(660,root,disk) /dev/pt3

%attr(666,root,tty) /dev/ptmx
%attr(666,root,tty) /dev/pty*
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
%attr(660,root,audio) /dev/rmidi*
%attr(660,root,disk) /dev/rmt*
%attr(644,root,root) /dev/route
%attr(664,root,root) /dev/rtc
%dir /dev/rd
%attr(660,root,disk) /dev/rd/*
%attr(600,root,root) /dev/rawctl
%dir /dev/raw
%attr(660,root,disk) /dev/raw/*

%attr(660,root,video) /dev/radio0
%attr(660,root,video) /dev/radio

#s#
%attr(%{perm_cdrom}) /dev/scd*
%attr(660,root,disk) /dev/sd*

%attr(660,root,audio) /dev/sequencer
%attr(660,root,audio) /dev/sequencer2

%attr(600,root,root) /dev/sg*
%attr(600,root,root) /dev/smtpe*

%attr(444,root,root) /dev/snd
%attr(666,root,root) /dev/sndstat

%attr(600,root,root) /dev/srnd*

%attr(660,root,disk) /dev/st?
%attr(600,root,root) /dev/staliomem*
%attr(666,root,root) /dev/std*

%attr(664,root,root) /dev/svga*
%attr(666,root,root) /dev/syslog
%attr(600,root,root) /dev/systty

#t#
%attr(660,root,disk) /dev/tape*
%attr(600,root,root) /dev/tlk*
%ifarch %{ix86}
%attr(666,root,root) /dev/toshiba
%endif
%attr(660,root,disk) /dev/tpqic*

%attr(666,root,root) /dev/tty

%attr(600,root,root) /dev/tty0
%attr(600,root,root) /dev/tty1*
%attr(600,root,root) /dev/tty2
%attr(600,root,root) /dev/tty3
%attr(600,root,root) /dev/tty4
%attr(600,root,root) /dev/tty5
%attr(600,root,root) /dev/tty6
%attr(600,root,root) /dev/tty7
%attr(600,root,root) /dev/tty8
%attr(600,root,root) /dev/tty9

%attr(600,root,root) /dev/ttyC*
%attr(600,root,root) /dev/ttyD*
%attr(600,root,root) /dev/ttyE*
%attr(600,root,root) /dev/ttyI*
%attr(600,root,root) /dev/ttyM*
%attr(600,root,root) /dev/ttyP*
%attr(600,root,root) /dev/ttyR*

%attr(664,root,ttyS) /dev/ttyS*
%attr(664,root,ttyS) /dev/ttyLT*

%attr(666,root,tty) /dev/ttya*
%attr(666,root,tty) /dev/ttyb*
%attr(666,root,tty) /dev/ttyc*
%attr(666,root,tty) /dev/ttyd*
%attr(666,root,tty) /dev/ttye*
%attr(666,root,tty) /dev/ttyp*
%attr(666,root,tty) /dev/ttyq*
%attr(666,root,tty) /dev/ttyr*
%attr(666,root,tty) /dev/ttys*
%attr(666,root,tty) /dev/ttyt*
%attr(666,root,tty) /dev/ttyu*
%attr(666,root,tty) /dev/ttyv*
%attr(666,root,tty) /dev/ttyw*
%attr(666,root,tty) /dev/ttyx*
%attr(666,root,tty) /dev/ttyy*
%attr(666,root,tty) /dev/ttyz*

#u#
%attr(644,root,root) /dev/urandom
%dir /dev/usb
%attr(660,root,root) /dev/usb/ez*
%attr(660,root,lp) /dev/usb/lp*
%attr(660,root,root) /dev/usb/scanner*
%attr(664,root,ttyS) /dev/usb/rio500
%attr(664,root,ttyS) /dev/usb/ttyACM*
%attr(664,root,ttyS) /dev/usb/ttyUB*
%attr(664,root,ttyS) /dev/usb/ttyUSB*

#v#
%attr(620,root,tty) %verify(not user) /dev/vcs*

%attr(660,root,video) /dev/video0
%attr(660,root,video) /dev/video
%attr(660,root,video) /dev/vtx0
%attr(660,root,video) /dev/vtx
%attr(660,root,video) /dev/vbi0
%attr(660,root,video) /dev/vbi

#w#
%attr(600,root,root) /dev/watchdog
%attr(660,root,sys) /dev/wvisfgrab

#x#
%attr(660,root,disk) /dev/xd*

#y#

#z#
%attr(666,root,root) /dev/zero
%attr(660,root,disk) /dev/zqft*

# only on sparc or m68k
%ifarch sparc m68k
# XXX: which permissions???
%attr(600,root,root) /dev/kbd
%endif

# only on m68k
%ifarch m68k
# XXX: which permissions???
%attr(664,root,root) /dev/amigamouse
%attr(664,root,root) /dev/atarimouse
%attr(664,root,root) /dev/apollomouse
%endif

# only on sparc
%ifarch sparc
# XXX: which permissions ???
%attr(600,root,root) /dev/openprom
%attr(664,root,root) /dev/sunmouse
%endif

# not on sparc or m68k
%ifnarch sparc m68k
%attr(664,root,root) /dev/atibm
%attr(%{perm_cdrom}) /dev/aztcd
%attr(%{perm_cdrom}) /dev/cdu31a
%attr(%{perm_cdrom}) /dev/cdu535
%attr(%{perm_cdrom}) /dev/cm206cd
%attr(%{perm_cdrom}) /dev/gscd
%attr(660,root,disk) /dev/hd*
%attr(664,root,root) /dev/inportbm
%attr(664,root,root) /dev/logibm
%attr(%{perm_cdrom}) /dev/mcd
%attr(664,root,root) /dev/psaux
%attr(%{perm_cdrom}) /dev/sbpcd*
%attr(%{perm_cdrom}) /dev/sjcd
%attr(%{perm_cdrom}) /dev/sonycd
%endif
