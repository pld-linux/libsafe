Summary:	Protecting Critical Elements of Stacks
Summary(pl):	Ochrona krytycznych elementów stosów.
Name:		libsafe
Version:	2.0
%define	sver	16
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.research.avayalabs.com/project/libsafe/src/%{name}-%{version}-%{sver}.tgz
# Source0-md5:	6b7b6e6df84d4afb469ccc66d04fc24d
URL:		http://www.research.avayalabs.com/project/libsafe/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libsafe library protects a process against the exploitation of
buffer overflow vulnerabilities in process stacks. Libsafe works with
any existing pre-compiled executable and can be used transparently,
even on a system-wide basis. The method intercepts all calls to
library functions that are known to be vulnerable. A substitute
version of the corresponding function implements the original
functionality, but in a manner that ensures that any buffer overflows
are contained within the current stack frame. Libsafe has been shown
to detect several known attacks and can potentially prevent yet
unknown attacks. Experiments indicate that the performance overhead of
libsafe is negligible.

%description -l pl
Biblioteka libsafe chroni procesy przed wykorzystaniem podatno¶ci na
przepe³nienie bufora w stosach procesu. Libsafe dzia³a z ka¿dym
prekompilowanym obiektem wykonywalnym i mo¿e byæ u¿ywana w sposób
przezroczysty, nawet jako podstawa systemu. Metod± dzia³ania jest
przechwytywanie wszystkich odwo³añ do funkcji bibliotecznych, które s±
znane jako podatne. Zastêpcza wersja odpowiadaj±cej funkcji
implementuje oryginaln± funkcjonalno¶æ, ale w sposób zapewniaj±cy, ¿e
jakiekolwiek przepe³nienia bufora zawieraj± siê wewn±trz bie¿±cej
ramki stosu. Libsafe zosta³a u¿yta do wykrycia kilku znanych ataków i
mo¿e potencjalnie zapobiegaæ jeszcze nieznanym. Eksperymenty wskazuj±,
¿e wp³yw libsafe na wydajno¶æ jest nieistotny.

%prep
%setup -q -n %{name}-%{version}-%{sver}

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib},%{_mandir}/man8}

install src/%{name}*.so* $RPM_BUILD_ROOT/%{_lib}
install doc/*.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README EMAIL_NOTIFICATION LIBPRELUDE ChangeLog
%attr(755,root,root) /%{_lib}/lib*.so*
%{_mandir}/man?/*
