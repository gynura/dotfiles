# dotfiles

My configuration files for Linux and macOS systems.

## Install

Symlink these configs into place from this repo (backs up any conflicting
files first):

```bash
./install.sh --dry-run   # preview what would change
./install.sh --force     # create the symlinks (replaces existing files)
```

What gets managed:

| Tool      | Repo file             | Symlinked to                                    |
| --------- | --------------------- | ----------------------------------------------- |
| zsh       | `zsh/.zshrc`          | `~/.zshrc`                                      |
| ghostty   | `ghostty/config.txt`  | `~/Library/Application Support/com.mitchellh.ghostty/config` |
| herdr     | `herdr/config.toml`   | `~/.config/herdr/config.toml`                   |
| hunk      | `hunk/config.toml`    | `~/.config/hunk/config.toml`                    |

Ghostty is themed with **Vague**. herdr (`theme = "terminal"`) follows the
host terminal's ANSI palette, and hunk has a matching `vague` theme, so
everything stays in sync.

## Screenshots

![my kitty terminal](https://i.imgur.com/yLrFiUO.png)
