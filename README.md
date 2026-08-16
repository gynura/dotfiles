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
| colorls   | `colorls/dark_colors.yaml` | `~/.config/colorls/dark_colors.yaml`        |

Ghostty is themed with **Vague**. herdr (`theme = "terminal"`) follows the
host terminal's ANSI palette, hunk has a matching `vague` theme, and colorls
uses ANSI color names (rendered through the terminal's Vague palette), so
everything stays in sync.

## Dependencies

Tools used across these configs:

| Tool                 | Role                                          |
| -------------------- | --------------------------------------------- |
| [Ghostty](https://ghostty.org) | terminal emulator (themed with Vague)  |
| [herdr](https://herdr.dev)     | terminal workspace manager / multiplexer |
| [hunk](https://hunk.dev)       | terminal diff viewer                    |
| zsh + [Oh My Zsh](https://ohmyz.sh) | shell + framework                |
| [spaceship-prompt](https://spaceship-prompt.sh) | zsh prompt theme     |
| zsh-autosuggestions  | zsh plugin (suggestions)                       |
| zsh-syntax-highlighting | zsh plugin (Homebrew-installed)            |
| [colorls](https://github.com/athityakumar/colorls) | custom `ls` (Ruby gem, Vague scheme) |
| [bat](https://github.com/sharkdp/bat) | `cat` replacement (`alias cat='bat --paging=never'`) |
| [SDKMAN](https://sdkman.io) | JVM toolchain manager                    |
| Go                   | language toolchain (`~/go/bin` on PATH)       |
| docker / docker-compose | container tooling                           |
| [opencode](https://opencode.ai) | AI coding CLI (`~/.opencode/bin` on PATH) |
| Sublime Text         | editor (`sublt` alias)                         |

## Screenshots

![my kitty terminal](https://i.imgur.com/yLrFiUO.png)
