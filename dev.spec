Summary:	/dev entries
Summary(de):	/dev-Eintr�ge
Summary(fr):	Entr�es de /dev
Summary(pl):	Pliki specjalne /dev/*
Summary(tr):	/dev dizini
Name:		dev
Version:	2.9.0
Release:	0.1
License:	Public Domain
Group:		Base
Source0:	dev-list.bz2
# Source0-md5:	4808891f6317383850ff826c31a1e797
PreReq:		setup >= 2.4.1-2
Provides:	devfs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Autoreqprov:	no

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
install -d $RPM_BUILD_ROOT/dev/cpu/{0,1,2,3,4,5,6,7} \
	$RPM_BUILD_ROOT/dev/{ataraid,cciss,cdroms,discs,i2o,ida,input,net,pts,raw,rd,usb}

bunzip2 -dc %{SOURCE0} > dev-list

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

%ifarch sparc
ln -sf sunmouse mouse
%endif

%ifarch m68k
ln -sf amigamouse mouse
%endif

%ifarch ppc
ln -sf adbmouse mouse
%endif

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
%dir /dev/cdroms
%dir /dev/discs
%dir /dev/i2o
%dir /dev/ida
%dir /dev/input
%dir /dev/net
%dir /dev/pts
%dir /dev/raw
%dir /dev/rd
%dir /dev/usb
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/adsp
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/amidi
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/audio
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/dsp
%config(noreplace) %verify(not link) %attr(644,root,root) /dev/fb
%config(noreplace) %verify(not link) %attr(666,root,root) /dev/ftape
%config(noreplace) %verify(not link) %attr(600,root,root) /dev/isdnctrl
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/midi
%config(noreplace) %verify(not link) %attr(660,root,audio) /dev/mixer
%config(noreplace) %verify(not link) %attr(666,root,root) /dev/nftape
%config(noreplace) %verify(not link) %attr(660,root,disk) /dev/ramdisk

%ifarch %{ix86}
%dev(c,10,184) %attr(666,root,root) /dev/cpu/microcode
%dev(c,10,181) %attr(666,root,root) /dev/toshiba
%endif

%ifarch sparc m68k
# XXX: which permissions???
%dev(c,11,00 %attr(600,root,root) /dev/kbd
%endif

%ifarch m68k
# XXX: which permissions???
%dev(c,10,4) %attr(664,root,root) /dev/amigamouse
%dev(c,10,5) %attr(664,root,root) /dev/atarimouse
%dev(c,10,7) %attr(664,root,root) /dev/apollomouse
# XXX: what's that???
%dev(b,2,4) /dev/fdhd0
%dev(b,2,5) /dev/fdhd1 
%endif

%ifarch ppc
%dev(c,56,0) %attr(644,root,root) /dev/adb*
%dev(c,10,10) %attr(644,root,root) /dev/adbmouse
%dev(c,10.154) %attr(644,root,root) /dev/pmu
%dev(c,10,198) %attr(644,root,root) /dev/sheep_net
%endif

%ifarch sparc
# XXX: which permissions ???
%dev(c,10,139) %attr(600,root,root) /dev/openprom
%dev(c,10,6) %attr(664,root,root) /dev/sunmouse
%endif

%ifnarch sparc m68k
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
