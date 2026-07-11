%global tl_name gamebooklib
%global tl_revision 67772

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4
Release:	%{tl_revision}.1
Summary:	Macros for setting numbered entries in shuffled order
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gamebooklib
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebooklib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebooklib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gamebooklib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros and environments to allow the user to
typeset a series of cross-referenced, numbered "entries", shuffled into
random order, to produce an interactive novel or "gamebook". This allows
entries to be written in natural order and shuffled automatically into a
repeatable non-linear order. Limited support is provided for footnotes
to appear at the natural position: the end of each entry, or the end of
each page, whichever is closest to the footnote mark. This is unrelated
to the gamebook package which is more concerned with the formatting of
entries rather than their order. The two packages can be used together
or separately.

