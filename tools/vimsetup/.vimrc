
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

colorscheme desert

let NERDChristmasTree=1

map <C-n> :NERDTree<CR>

