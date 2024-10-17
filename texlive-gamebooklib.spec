Name:		texlive-gamebooklib
Version:	67772
Release:	1
Summary:	Macros for setting numbered entries in shuffled order
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gamebooklib
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebooklib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebooklib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebooklib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros and environments to allow the user
to typeset a series of cross-referenced, numbered "entries",
shuffled into random order, to produce an interactive novel or
"gamebook". This allows entries to be written in natural order
and shuffled automatically into a repeatable non-linear order.
Limited support is provided for footnotes to appear at the
natural position: the end of each entry, or the end of each
page, whichever is closest to the footnote mark. This is
unrelated to the gamebook package which is more concerned with
the formatting of entries rather than their order. The two
packages can be used together or separately.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gamebooklib
%{_texmfdistdir}/tex/latex/gamebooklib
%doc %{_texmfdistdir}/doc/latex/gamebooklib

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
