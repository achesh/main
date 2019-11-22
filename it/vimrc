
"$VIM/vimrc" 
"$HOME/.vimrc" 
"$HOME/.exrc" 
"$VIM/gvimrc" 
"$HOME/.gvimrc" 
"$VIMRUNTIME/menu.vim" 
"/usr/share/vim" 
"
"
set nocompatible

syntax on
set autoindent
set tabstop=2
set expandtab
set number
set ruler
set cursorline
set cursorcolumn
set hlsearch

set list 
set listchars=tab:>-,trail:-

set showmatch
set autoread

set title
set titlestring=%F

filetype on
set nocp
set nobackup
set noswapfile
set nowb
set mouse=a
set showcmd
set ignorecase

set cmdheight=3
set laststatus=2
set statusline=%F\ TL=%L
set completeopt=preview,menu

set path=.
set path+=/proj

colorscheme desert

let NERDChristmasTree=1

map <C-h> :tabp<CR>
map <C-l> :tabn<CR>
map <C-c> :tabc<CR>
map <C-e> :tabe

map <C-n> :NERDTree<CR>

"CtrlP
":CtrlP <DIR> - Search in <DIR>
":CtrlPMRU    - Search in MRU
":CtrlPBuffer - Serach in Buffer
":CtrlPMixed  - Search in Files,Buffers,MRU at the same time
"Ctrl+j - Navigate in file lists
"Ctrl+k - Navigate in file lists
"Reference: ctrlpvim.github.io/ctrlp.vim
map <C-m> :CtrlPMRU<CR>

"Create new C Shell File
autocmd BufNewFile *.csh exec ":call SetCshTitle()" 
func SetCshTitle() 
  call setline(1,"#!/usr/bin/csh -f")
  call setline(2,"#Filename:")
endfunc

"Create new B Shell File
autocmd BufNewFile *.sh exec ":call SetBashTitle()" 
func SetBashTitle() 
  call setline(1,"#!/usr/bin/bash -f")
  call setline(2,"#Filename:")
endfunc




