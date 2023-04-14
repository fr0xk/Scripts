" Enable syntax highlighting
syntax on

" Enable mouse support for scrolling and selecting
set mouse=a

" Set the default tab size to 4 spaces
set tabstop=4
set shiftwidth=4
set expandtab

" Enable line numbers
set number

" Set colorscheme
colorscheme slate

function! RandomTheme()
    let themes = ['default', 'delek', 'evening', 'industry', 'koehler', 'murphy', 'ron', 'shine', 'slate', 'torte', 'zellner']
    let theme = themes[rand() % len(themes)]
    execute 'colorscheme ' . theme
    echo 'Selected theme: ' . theme
endfunction

nnoremap w :call RandomTheme()<CR>

" Set default font size
set guifont=Inconsolata:h14

" Set default file encoding
set encoding=utf-8

" Set default file format to Unix
set fileformat=unix

" Use the system clipboard
set clipboard=unnamedplus

" Use standard copy, cut, and paste commands
nnoremap <C-c> "+y
vnoremap <C-c> "+y
nnoremap <C-x> "+d
vnoremap <C-x> "+d
nnoremap <C-v> "+p
vnoremap <C-v> "+p

" Enable syntax checking for supported file types
autocmd FileType python,ruby,javascript,typescript,go,nim,nix,sh,yaml,json,html,css,lua setlocal makeprg=echo\ % && setlocal errorformat=%f:%l:%c:\ %m

" Set spellcheck options
set spell spelllang=en_us

" Set search options
set incsearch
set hlsearch
set ignorecase
set smartcase

" Set window splitting options
set splitbelow
set splitright

" Set visual options
set showmode
set relativenumber

" Check for missing plugins and install them if necessary
function! CheckAndInstallPlugins()
    let plugin_list = [
        \ ['vim-airline/vim-airline', 'airline'],
        \ ['vim-airline/vim-airline-themes', 'airline-themes'],
        \ ['tpope/vim-fugitive', 'fugitive'],
        \ ]

    for plugin in plugin_list
        let plugin_name = plugin[1]
        let plugin_path = plugin[0]

        if !isdirectory(expand('~/.vim/pack/plugins/start/'.plugin_name))
            try
                execute 'silent !git clone --depth=1 https://github.com/'.plugin_path.'.git ~/.vim/pack/plugins/start/'.plugin_name
                echo 'Installed plugin: '.plugin_name
            catch
                echo 'Error installing plugin: '.plugin_name
            endtry
        else
            echo 'Plugin already installed: '.plugin_name
        endif
    endfor
endfunction

call CheckAndInstallPlugins()

