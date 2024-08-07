GhostBSD is based on FreeBSD, so the transition is relatively straightforward. You can upgrade your existing GhostBSD installation to FreeBSD by following these steps:
Open a terminal or command prompt.
Run the following commands:
```bash
sudo env ABI=FreeBSD:14:amd64 IGNORE_OSVERSION=yes pkg-static bootstrap -f
sudo env ABI=FreeBSD:14:amd64 pkg-static upgrade -f
```

This will update your system to FreeBSD 14.10.11.
