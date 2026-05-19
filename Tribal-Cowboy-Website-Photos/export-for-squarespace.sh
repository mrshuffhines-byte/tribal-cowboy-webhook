#!/bin/bash
# =============================================================
# Tribal Cowboy - Squarespace Image Export Script
# Resizes & optimizes edited photos for Squarespace upload
# =============================================================
# Squarespace specs: 2500px wide, sRGB, JPEG, under 500KB ideal

SOURCE_DIR="$HOME/Desktop/Tribal-Cowboy-Website-Photos"
EXPORT_DIR="$SOURCE_DIR/EXPORTED-FOR-SQUARESPACE"

echo "🐎 Tribal Cowboy - Squarespace Photo Exporter"
echo "=============================================="

mkdir -p "$EXPORT_DIR"

count=0

# Process all image files in subdirectories (skip EXPORTED folder)
find "$SOURCE_DIR" -maxdepth 2 -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.heic" -o -name "*.tiff" -o -name "*.tif" \) ! -path "*/EXPORTED-FOR-SQUARESPACE/*" | while read -r file; do
    filename=$(basename "$file")
    # Get parent folder name for context
    parent=$(basename "$(dirname "$file")")
    # Create export name: section_originalname_web.jpg
    export_name="${parent}_${filename%.*}_web.jpg"
    export_path="$EXPORT_DIR/$export_name"

    echo "  Processing: $parent/$filename"

    # Use macOS built-in sips to resize and convert
    # Resize longest edge to 2500px, convert to JPEG, sRGB
    sips --resampleHeightWidthMax 2500 \
         --matchTo "/System/Library/ColorSync/Profiles/sRGB Profile.icc" \
         -s format jpeg \
         -s formatOptions 80 \
         "$file" \
         --out "$export_path" 2>/dev/null

    if [ $? -eq 0 ]; then
        # Get file size
        size=$(stat -f%z "$export_path" 2>/dev/null)
        size_kb=$((size / 1024))

        # If over 500KB, recompress at lower quality
        if [ "$size_kb" -gt 500 ]; then
            echo "    ⚠️  ${size_kb}KB - recompressing..."
            sips -s formatOptions 65 "$export_path" --out "$export_path" 2>/dev/null
            size=$(stat -f%z "$export_path" 2>/dev/null)
            size_kb=$((size / 1024))
        fi

        echo "    ✅ Exported: $export_name (${size_kb}KB)"
        count=$((count + 1))
    else
        echo "    ❌ Failed to process: $filename"
    fi
done

echo ""
echo "=============================================="
echo "✅ Done! Exported files are in:"
echo "   $EXPORT_DIR"
echo ""
echo "📋 Squarespace Upload Tips:"
echo "   - Hero/banner images: upload at full 2500px width"
echo "   - Gallery images: these are already optimized"
echo "   - Upload via: Squarespace > Pages > Edit > Add Image"
echo "=============================================="
