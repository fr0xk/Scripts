" Portable and Cross-Platform .vimrc

" Enable line numbers
set number

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

" Remap <F5> to save and <F9> to execute Python code
nnoremap <F5> :w<CR>
nnoremap <F9> :!python %<CR>

" Customize the background color for the 'Normal' highlight group
hi Normal ctermbg=black

" Use 'One Dark' colorscheme if available, or fallback to default
try
  colorscheme onedark
catch
  " Fallback to default colorscheme
  colorscheme default
endtry

" Define a simple status line
set laststatus=2
set statusline=%<%f\ %h%m%r\ %=%k\ %-14.(%l,%c%V%)\ %P

