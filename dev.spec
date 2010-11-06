Summary:	/dev entries
Summary(de.UTF-8):	/dev-Einträge
Summary(fr.UTF-8):	Entrées de /dev
Summary(pl.UTF-8):	Pliki specjalne /dev/*
Summary(tr.UTF-8):	/dev dizini
Name:		dev
Version:	3.4
Release:	7
License:	Public Domain
Group:		Base
Source0:	%{name}-list
Requires:	setup >= 2.6.1-1
Provides:	devfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unix and Unix-like systems (including Linux) use file system entries
to represent devices attached to the machine. All of these entries are
in the /dev tree (though they don't have to be), and this package
contains the most commonly used /dev entries. These files are
essential for a system to function properly.

%description -l de.UTF-8
Unix und Unix-ähnliche Systeme (inkl. Linux) verwenden Dateisystem-
Einträge zum Darstellen angeschlossener Geräte. Diese Einträge
befinden sich (nicht notwendigerweise) im Verzeichnis /dev. Dieses
Paket enthält die üblichsten /dev-Einträge. Diese Dateien sind für das
Funktionieren eines Systems unbedingt erforderlich.

%description -l fr.UTF-8
Unix et les systèmes apparentés (dont Linux) utilise des fichiers pour
représenter les périphériques reliés à la machine. Toutes ces entrées
sont dans l'arborescence /dev (ce n'est pas obligatoire). Ce paquetage
contient les entrées /dev les plus courantes. Elles sont essentielles
pour qu'un système fonctionne correctement.

%description -l pl.UTF-8
Wszystkie systemy klasy unices, w tym Linux, używają plików do
przedstawiania urządzeń podłączonych do komputera. Wszystkie te pliki
znajdują się zwykle w katalogu /dev. Pakiet ten zawiera większość
popularnych plików specjalnych, są one jedną z ważniejszych części
prawidłowo działającego systemu operacyjnego.

%description -l tr.UTF-8
Unix ve Unix benzeri sistemler (Linux da dahil olmak üzere), makinaya
bağlı aygıtları göstermek için özel dosyalar kullanırlar. Bu özel
dosyaların tümü /dev dizin yapısı altındadır. Bu paket en çok
kullanılan /dev dosyalarını içerir. Bu dosyalar, bir sistemin düzgün
olarak işleyebilmesi için temel gereksinimlerdendir.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/dev/{ataraid,cciss,cdemu,cdroms,cpu/{0,1,2,3,4,5,6,7},cgroup.cpuset} \
	$RPM_BUILD_ROOT/dev/{discs,dri,etherd,i2o,ida,input,mapper,net,pts,raw,rd,usb,shm,snd,zap}

install %{SOURCE0} .

cd $RPM_BUILD_ROOT/dev
ln -sf adsp0 adsp
ln -sf amidi0 amidi
ln -sf audio0 audio
ln -sf dsp0 dsp
ln -sf fb0 fb
ln -sf rft0 ftape
ln -sf isdnctrl0 isdnctrl
ln -sf midi00 midi
ln -sf mixer0 mixer
ln -sf nrft0 nftape
ln -sf ram0 ramdisk

ln -sf em8300-0		em8300
ln -sf em8300_ma-0	em8300_ma
ln -sf em8300_mv-0	em8300_mv
ln -sf em8300_sp-0	em8300_sp
for i in `seq 0 31`; do
	ln -sf fb$i fb${i}current
done
ln -sf /proc/self/fd fd
ln -sf fd/0 stdin
ln -sf fd/1 stdout
ln -sf fd/2 stderr
i=0;
for l in a b c d e f g h; do
	ln -sf sg$l sg$i
	i=$((i+1))
done
ln -sf radio0 radio
ln -sf music sequencer2
ln -sf vbi0 vbi
ln -sf video0 video
ln -sf vtx0 vtx

# prepared for SysVinit
mkfifo initctl

mkfifo lircm
mkfifo printer

# prepared for Log Daemon
mkfifo syslog

%ifarch m68k
ln -sf amigamouse mouse
%endif

%ifarch ppc
ln -sf adbmouse mouse
%endif

%ifarch sparc sparc64 sparcv9
ln -sf sunmouse mouse
%endif

# PLD-forklor:
ln -sf null drzewo

%clean
rm -rf $RPM_BUILD_ROOT

%files -f dev-list
%defattr(644,root,root,755)
%dir /dev/ataraid
%dir /dev/cciss
%dir /dev/cdemu
%dir /dev/cgroup
%dir /dev/cpu
%dir /dev/cpu/0
%dir /dev/cpu/1
%dir /dev/cpu/2
%dir /dev/cpu/3
%dir /dev/cpu/4
%dir /dev/cpu/5
%dir /dev/cpu/6
%dir /dev/cpu/7
%dir /dev/cpuset
%dir /dev/dri
%attr(750,root,disk) %dir /dev/cdroms
%attr(750,root,disk) %dir /dev/discs
%dir /dev/etherd
%dir /dev/i2o
%dir /dev/ida
%dir /dev/input
%dir /dev/mapper
%dir /dev/net
%dir /dev/pts
%dir /dev/raw
%dir /dev/rd
%dir /dev/usb
%dir /dev/zap
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/adsp
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/amidi
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/audio
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/dsp
%config(noreplace) %verify(not link) %attr(660,root,video) /dev/fb
%config(noreplace) %verify(not link) %attr(660,root,disk) /dev/ftape
%config(noreplace) %verify(not link) %attr(600,root,root) /dev/isdnctrl
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/midi
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/mixer
%config(noreplace) %verify(not link) %attr(660,root,disk) /dev/nftape
%config(noreplace) %verify(not link) %attr(660,root,disk) /dev/ramdisk
%attr(660,root,video) /dev/em8300*
%attr(660,root,video) /dev/fb[0-9]*current
/dev/fd
/dev/stdin
/dev/stdout
/dev/stderr
%attr(660,root,video) /dev/radio
%attr(660,root,audio) /dev/sequencer2
%attr(600,root,root) /dev/sg[0-7]
%attr(1777,root,root) %dir /dev/shm
%dir /dev/snd
%attr(660,root,video) /dev/vbi
%attr(660,root,video) /dev/video
%attr(660,root,video) /dev/vtx
%attr(600,root,root) /dev/initctl
%attr(660,root,root) /dev/lircm
%attr(600,root,root) /dev/printer
%attr(666,root,root) /dev/syslog
%attr(666,root,root) /dev/drzewo

%ifarch %{ix86}
%dev(c,10,181) %attr(666,root,root) /dev/toshiba
%dev(c,212,0) %attr(600,root,root) /dev/slamr0
%dev(c,213,0) %attr(600,root,root) /dev/slusb0
%dev(c,226,0) %attr(660,root,video) /dev/dri/card0
%dev(c,226,1) %attr(660,root,video) /dev/dri/card1
%dev(c,226,2) %attr(660,root,video) /dev/dri/card2
%dev(c,226,3) %attr(660,root,video) /dev/dri/card3
%dev(c,226,4) %attr(660,root,video) /dev/dri/card4
%dev(c,226,5) %attr(660,root,video) /dev/dri/card5
%dev(c,226,6) %attr(660,root,video) /dev/dri/card6
%dev(c,226,7) %attr(660,root,video) /dev/dri/card7
%endif

%ifarch %{ix86} %{x8664}
%dev(c,10,227) %attr(600,root,root) /dev/mcelog
%dev(c,10,184) %attr(666,root,root) /dev/cpu/microcode
%endif

%ifarch m68k
%dev(b,2,4) %attr(660,root,floppy) /dev/fdhd0
%dev(b,2,5) %attr(660,root,floppy) /dev/fdhd1
# XXX: which permissions???
%dev(c,10,4) %attr(664,root,root) /dev/amigamouse
%attr(664,root,root) /dev/mouse
%dev(c,10,5) %attr(664,root,root) /dev/atarimouse
%dev(c,10,7) %attr(664,root,root) /dev/apollomouse
%endif

%ifarch ppc
%dev(c,56,0) /dev/adb
%dev(c,10,10) /dev/adbmouse
/dev/mouse
%dev(c,10,154) /dev/pmu
%dev(c,10,198) /dev/sheep_net
%endif

%ifarch sparc sparc64 sparcv9
%dev(c,14,7) %attr(660,root,audio) /dev/audioctl
# XXX: which permissions ???
%dev(c,10,139) %attr(600,root,root) /dev/openprom
%dev(c,10,6) %attr(664,root,root) /dev/sunmouse
%attr(664,root,root) /dev/mouse
%endif

%ifarch m68k sparc sparc64 sparcv9
# XXX: which permissions???
%dev(c,11,00) %attr(600,root,root) /dev/kbd
%endif

%ifnarch m68k sparc sparc64 sparcv9
%dev(c,10,3) %attr(664,root,root) /dev/atibm
%dev(b,29,0) %attr(660,root,disk) /dev/aztcd
%dev(b,15,0) %attr(660,root,disk) /dev/cdu31a
%dev(b,24,0) %attr(660,root,disk) /dev/cdu535
%dev(b,32,0) %attr(660,root,disk) /dev/cm206cd
%dev(b,16,0) %attr(660,root,disk) /dev/gscd
%dev(c,10,2) %attr(664,root,root) /dev/inportbm
%dev(c,10,0) %attr(664,root,root) /dev/logibm
%dev(b,23,0) %attr(660,root,disk) /dev/mcd
%dev(c,10,1) %attr(664,root,root) /dev/psaux
%dev(b,25,0) %attr(660,root,disk) /dev/sbpcd
%dev(b,25,0) %attr(660,root,disk) /dev/sbpcd0
%dev(b,25,1) %attr(660,root,disk) /dev/sbpcd1
%dev(b,25,2) %attr(660,root,disk) /dev/sbpcd2
%dev(b,25,3) %attr(660,root,disk) /dev/sbpcd3
%dev(b,18,0) %attr(660,root,disk) /dev/sjcd
%dev(b,15,0) %attr(660,root,disk) /dev/sonycd
%endif
