# Unix File Operations (model references)

## Common & safe patterns

```bash
# Find large files (human readable)
du -ah . | sort -rh | head -20

# Safely remove only files older than N days (dry-run first!)
find . -type f -mtime +30 -print
# Then with -delete or -exec rm

# Atomic-ish move (across filesystems)
rsync -a --remove-source-files src/ dest/ && rm -rf src/

# Create dated backup dir
backup_dir="backup-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$backup_dir"
```

**Notes:** Always test destructive commands with echo or dry-run flags first.