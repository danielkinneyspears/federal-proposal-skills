#!/usr/bin/env bash
# Build a self-contained .zip for one skill (or all skills), with the shared
# knowledge base bundled in and its paths rewritten, so the skill can be
# uploaded individually to claude.ai or the Skills API.
#
# Usage:
#   scripts/package-skill.sh <skill-name>   # build dist/<skill-name>.zip
#   scripts/package-skill.sh --all          # build a zip for every skill
#
# The skills in this package reference ../../shared/ at runtime. That path only
# resolves when the whole repo (or plugin) is present. This script copies the
# shared/ knowledge base into the skill package as shared/ and rewrites the
# ../../shared/ references so the packaged skill is genuinely self-contained.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_dir="$repo_root/skills"
shared_dir="$repo_root/shared"
dist_dir="$repo_root/dist"

usage() {
  echo "Usage: scripts/package-skill.sh <skill-name> | --all"
  echo "Writes dist/<skill-name>.zip"
}

package_one() {
  local name="$1"
  local src="$skills_dir/$name"
  if [ ! -f "$src/SKILL.md" ]; then
    echo "error: no skill named '$name' (expected $src/SKILL.md)" >&2
    return 1
  fi

  local build pkg
  build="$(mktemp -d)"
  pkg="$build/$name"
  mkdir -p "$pkg"
  cp -R "$src/." "$pkg/"

  # Bundle the shared knowledge base inside the skill package.
  mkdir -p "$pkg/shared"
  cp -R "$shared_dir/." "$pkg/shared/"

  # Rewrite the repo-relative shared path (../../shared/) to the bundled
  # location (shared/) in every Markdown file in the package.
  find "$pkg" -name '*.md' -type f -exec \
    perl -pi -e 's{\.\./\.\./shared/}{shared/}g' {} +

  mkdir -p "$dist_dir"
  rm -f "$dist_dir/$name.zip"
  ( cd "$build" && zip -q -r "$dist_dir/$name.zip" "$name" )
  rm -rf "$build"
  echo "built dist/$name.zip"
}

main() {
  if [ $# -ne 1 ]; then usage; exit 1; fi
  case "$1" in
    -h|--help) usage ;;
    --all)
      for d in "$skills_dir"/*/; do
        package_one "$(basename "$d")"
      done
      ;;
    *) package_one "$1" ;;
  esac
}

main "$@"
