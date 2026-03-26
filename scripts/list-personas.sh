#!/usr/bin/env bash
set -euo pipefail

INDEX_URL="https://raw.githubusercontent.com/decentraliser/personas/main/api/index.json"
tag_filter=""
search_filter=""

usage() {
  echo "Usage: $0 [--tag TAG] [--search TERM]" >&2
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tag)
      [[ $# -ge 2 ]] || { usage; exit 1; }
      tag_filter="$2"
      shift 2
      ;;
    --search)
      [[ $# -ge 2 ]] || { usage; exit 1; }
      search_filter="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage
      exit 1
      ;;
  esac
done

rows="$(
  curl -fsSL "$INDEX_URL" \
    | jq -r --arg tag "$tag_filter" --arg search "$search_filter" '
        .personas[]
        | select(
            ($tag == "")
            or (((.tags // []) | map(ascii_downcase) | index($tag | ascii_downcase)) != null)
          )
        | select(
            ($search == "")
            or (((.name // "" | ascii_downcase) + " " + (.tagline // "" | ascii_downcase)) | contains($search | ascii_downcase))
          )
        | [
            (.handle // ""),
            (.name // ""),
            (.tagline // ""),
            ((.tags // []) | join(", "))
          ]
        | @tsv
      '
)"

if [[ -z "$rows" ]]; then
  echo "No personas matched."
  exit 1
fi

{
  printf 'HANDLE\tNAME\tTAGLINE\tTAGS\n'
  printf '%s\n' "$rows"
} | column -t -s $'\t'
