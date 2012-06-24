Summary:	/dev entries
Summary(de):	/dev-Eintr�ge
Summary(fr):	Entr�es de /dev
Summary(pl):	Pliki specjalne /dev/*
Summary(tr):	/dev dizini
Name:		dev
Version:	2.9.0
Release:	16
License:	Public Domain
Group:		Base
Source0:	dev-list
PreReq:		setup >= 2.4.1-2
Provides:	devfs
AutoReqProv:	no
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unix and unix like systems (including Linux) use file system entries
to represent devices attached to the machine. All of these entries are
in the /dev tree (though they don't have to be), and this package
contains the most commonly used /dev entries. These files are
essential for a system to function properly.

%description -l de
Unix und Unix-�hnliche Systeme (inkl. Linux) verwenden Dateisystem-
Eintr�ge zum Darstellen angeschlossener Ger�te. Diese Eintr�ge
befinden sich (nicht notwendigerweise) im Verzeichnis /dev. Dieses
Paket enth�lt die �blichsten /dev-Eintr�ge. Diese Dateien sind f�r das
Funktionieren eines Systems unbedingt erforderlich.

%description -l fr
Unix et les syst�mes apparent�s (dont Linux) utilise des fichiers pour
repr�senter les p�riph�riques reli�s � la machine. Toutes ces entr�es
sont dans l'arborescence /dev (ce n'est pas obligatoire). Ce paquetage
contient les entr�es /dev les plus courantes. Elles sont essentielles
pour qu'un syst�me fonctionne correctement.

%description -l pl
Wszystkie systemy klasy unices, w tym Linux, u�ywaj� plik�w do
przedstawiania urz�dze� pod��czonych do komputera. Wszystkie te pliki
znajduj� si� zwykle w katalogu /dev. Pakiet ten zawiera wi�kszo��
popularnych plik�w specjalnych, s� one jedn� z wa�niejszych cz�ci
prawid�owo dzia�aj�cego systemu operacyjnego.

%description -l tr
Unix ve Unix benzeri sistemler (Linux da dahil olmak �zere), makinaya
ba�l� ayg�tlar� g�stermek i�in �zel dosyalar kullan�rlar. Bu �zel
dosyalar�n t�m� /dev dizin yap�s� alt�ndad�r. Bu paket en �ok
kullan�lan /dev dosyalar�n� i�erir. Bu dosyalar, bir sistemin d�zg�n
olarak i�leyebilmesi i�in temel gereksinimlerdendir.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/dev/{ataraid,cciss,cdroms,cpu/{0,1,2,3,4,5,6,7}} \
	$RPM_BUILD_ROOT/dev/{discs,i2o,ida,input,net,pts,raw,rd,usb,shm,snd,zap} \
	$RPM_BUILD_ROOT/dev/{mapper,dri,cdemu}

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
%dir /dev/cpu
%dir /dev/cpu/0
%dir /dev/cpu/1
%dir /dev/cpu/2
%dir /dev/cpu/3
%dir /dev/cpu/4
%dir /dev/cpu/5
%dir /dev/cpu/6
%dir /dev/cpu/7
%dir /dev/ataraid
%dir /dev/cciss
%dir /dev/dri
%attr(750,root,disk) %dir /dev/cdroms
%attr(750,root,disk) %dir /dev/discs
%dir /dev/i2o
%dir /dev/ida
%dir /dev/input
%dir /dev/net
%dir /dev/pts
%dir /dev/raw
%dir /dev/rd
%dir /dev/usb
%dir /dev/mapper
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
%dir /dev/shm
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
%dev(c,10,184) %attr(666,root,root) /dev/cpu/microcode
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
%dev(c,56,0) %attr(644,root,root) /dev/adb
%dev(c,10,10) %attr(644,root,root) /dev/adbmouse
%attr(644,root,root) /dev/mouse
%dev(c,10,154) %attr(644,root,root) /dev/pmu
%dev(c,10,198) %attr(644,root,root) /dev/sheep_net
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
