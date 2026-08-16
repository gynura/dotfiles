#!/usr/bin/env bash
# Bootstrap: symlink this dotfiles repo into place on the local machine.
#
# Usage:
#   ./install.sh            create/repair symlinks
#   ./install.sh --dry-run  preview what would change
#   ./install.sh --force    replace existing regular files (after backing them up)
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DRY_RUN=0
FORCE=0

usage() {
    cat <<EOF
Usage: $(basename "$0") [--dry-run] [--force]

Create symlinks from this dotfiles repo to the local machine.

  --dry-run   print what would happen without changing anything
  --force     replace existing regular files (they are backed up first)
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --dry-run) DRY_RUN=1 ;;
        --force) FORCE=1 ;;
        -h|--help) usage; exit 0 ;;
        *) echo "error: unknown option: $1" >&2; usage >&2; exit 1 ;;
    esac
    shift
done

# link <target_path> <source_path_in_repo>
link() {
    local target="$1" source="$2"
    local target_dir current backup

    target_dir="$(dirname "$target")"

    if [[ -L "$target" ]]; then
        current="$(readlink "$target")"
        if [[ "$current" == "$source" ]]; then
            echo "ok    $target -> $source"
        else
            echo "skip  $target -> $current (points elsewhere)"
        fi
        return
    fi

    if [[ -e "$target" ]]; then
        if [[ $FORCE -eq 1 ]]; then
            backup="${target}.backup.$(date +%Y%m%d%H%M%S)"
            if [[ $DRY_RUN -eq 1 ]]; then
                echo "would backup $target -> $backup"
            else
                mv "$target" "$backup"
                echo "backup $target -> $backup"
            fi
        else
            echo "skip  $target (exists; use --force to replace)"
            return
        fi
    fi

    if [[ $DRY_RUN -eq 1 ]]; then
        echo "would link $target -> $source"
        return
    fi

    mkdir -p "$target_dir"
    ln -s "$source" "$target"
    echo "link  $target -> $source"
}

link "$HOME/.zshrc" "$REPO_DIR/zsh/.zshrc"
link "$HOME/Library/Application Support/com.mitchellh.ghostty/config" "$REPO_DIR/ghostty/config.txt"
link "$HOME/.config/herdr/config.toml" "$REPO_DIR/herdr/config.toml"
link "$HOME/.config/hunk/config.toml" "$REPO_DIR/hunk/config.toml"
link "$HOME/.config/colorls/dark_colors.yaml" "$REPO_DIR/colorls/dark_colors.yaml"

echo
echo "Done. See README.md for what is managed."
