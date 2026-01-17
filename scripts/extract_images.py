import os
import fitz  # PyMuPDF
import argparse
from pathlib import Path

def get_existing_posts(posts_dir):
    """Returns a list of filename stems from the _posts directory."""
    posts_path = Path(posts_dir)
    if not posts_path.exists():
        return []
    
    # Return sorted list of stems (filenames without .md)
    return sorted([f.stem for f in posts_path.glob("*.md")], reverse=True)

def extract_pdf_to_images(pdf_dir, output_dir, article_name):
    """
    Extracts the first page of each PDF in pdf_dir as a PNG image in output_dir.
    Naming convention: {article_name}-{index}.png
    PDFs are sorted by modification time (creation order).
    """
    pdf_path = Path(pdf_dir)
    img_path = Path(output_dir)
    
    if not img_path.exists():
        img_path.mkdir(parents=True)
    
    # Sort files by modification time (st_mtime)
    pdf_files = sorted([f for f in pdf_path.glob("*.pdf")], key=os.path.getmtime)
    
    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        return

    print(f"Using article name: {article_name}")
    print(f"Processing {len(pdf_files)} files in order of creation...")
    
    global_page_index = 1
    for pdf_file in pdf_files:
        try:
            doc = fitz.open(pdf_file)
            print(f"Processing {pdf_file.name} ({doc.page_count} pages)...")
            
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x scale for better quality
                
                output_filename = f"{article_name}-{global_page_index}.png"
                output_file = img_path / output_filename
                
                pix.save(output_file)
                print(f"  - Saved: {output_filename} (page {page_num + 1})")
                global_page_index += 1
                
            doc.close()
        except Exception as e:
            print(f"Error processing {pdf_file.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract first page of PDFs as images.")
    parser.add_argument("name", nargs="?", help="The article name to use for image filenames (e.g., '2026-01-17-sheet-web-app')")
    args = parser.parse_args()

    # Determine project root (parent directory of this script)
    SCRIPT_DIR = Path(__file__).resolve().parent
    PROJECT_ROOT = SCRIPT_DIR.parent

    # Paths (absolute)
    POSTS_DIR = PROJECT_ROOT / "_posts"
    PDF_INPUT_DIR = PROJECT_ROOT / "assets" / "pdf_sources"
    IMAGE_OUTPUT_DIR = PROJECT_ROOT / "assets" / "images"

    article_name = args.name
    if not article_name:
        existing_posts = get_existing_posts(POSTS_DIR)
        if existing_posts:
            print("\nSelect an existing article name:")
            for idx, post in enumerate(existing_posts, 1):
                print(f"{idx}. {post}")
            print(f"{len(existing_posts) + 1}. [Enter Custom Name]")
            
            choice = input(f"\nSelect (1-{len(existing_posts) + 1}): ").strip()
            
            try:
                choice_idx = int(choice)
                if 1 <= choice_idx <= len(existing_posts):
                    article_name = existing_posts[choice_idx - 1]
                else:
                    article_name = input("Enter the custom article name: ").strip()
            except ValueError:
                article_name = input("Enter the custom article name: ").strip()
        else:
            article_name = input("Enter the article name for image prefix: ").strip()

    if not article_name:
        article_name = "image" # Default fallback
    
    extract_pdf_to_images(PDF_INPUT_DIR, IMAGE_OUTPUT_DIR, article_name)
