" Portable and Cross-Platform .vimrc

" Enable line numbers
set number
set relativenumber

" Enable syntax highlighting
syntax enable

" Enable auto-indentation
set autoindent
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab

" Enable mouse support for GUI versions of Vim
if has("gui_running")
  set mouse=a
endif

" Highlight search results as you type
set incsearch

" Remap <F5> to save
nnoremap <F5> :w<CR>

" Customize the background color for the 'Normal' highlight group
hi Normal ctermbg=black

" Use 'One Dark' colorscheme if available, or fallback to default
try
  colorscheme onedark
catch
  " Fallback to default colorscheme
  colorscheme desert
endtry

" Define a simple status line
set laststatus=2
set statusline=%<%f\ %h%m%r\ %=%k\ %-14.(%l,%c%V%)\ %P

" Additional Key Mappings
nnoremap <F9> :!python %<CR>

" Clipboard
set clipboard=unnamedplus   " Enable system clipboard integration

" Backup and Swap Files
set backup
set undofile
set undodir=~/.vim/undodir

" Save this file as ~/.vimrc

