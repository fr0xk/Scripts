" Set file type and encoding
autocmd BufRead,BufNewFile *.{py,html,css,js} set ft=python
set encoding=utf-8
set fileformat=unix

" Enable features
syntax on
set number
set wrap
set linebreak
set nolist
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set autoindent
set incsearch
set ignorecase
set smartcase
set wildmenu
set wildmode=list:longest
set shortmess+=c
set wildmode=longest,list,full
set wildignorecase
if has("unix")
  set wildignore+=*/tmp/*,*.so,*.swp,*.zip,*.pyc,*.class
else
  set wildignore+=*/tmp/*,*.so,*.dll
endif

" Use Plug to manage plugins
" Install Plug.vim if it's not already installed
" if empty(glob('~/.vim/autoload/plug.vim'))
"   silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
"         \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
"   autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
" endif

" List your plugins here
" call plug#begin('~/.vim/plugged')
" Plug 'tpope/vim-fugitive'
" call plug#end()

" Set colors and font
if has('termguicolors')
  set termguicolors
endif

" Check if the color scheme exists before setting it
if has('gui_running') || &t_Co > 256
  if exists('+termguicolors')
    set termguicolors
  endif
  colorscheme gruvbox
else
  colorscheme default
endif

if has('gui_running')
  set guifont=Monospace\ 10
endif
if has('gui_running')
  set background=light
else
  set background=dark
endif

" Set status line
set statusline=%<%f\ %h%m%r%{strftime('\ \ %b\ %d\ %H:%M\ ')}%=%-14.(%l,%c%V%)\ %P

" Tab completion
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
