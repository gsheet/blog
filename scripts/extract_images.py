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

def extract_pdf_to_images(pdf_file, output_dir):
    """
    Extracts all pages of the given pdf_file as PNG images in output_dir.
    Naming convention: {pdf_filename}_page_{index}.png
    """
    pdf_file = Path(pdf_file)
    article_name = pdf_file.stem
    img_path = Path(output_dir)
    
    if not img_path.exists():
        img_path.mkdir(parents=True)
    
    try:
        doc = fitz.open(pdf_file)
        print(f"Processing {pdf_file.name} ({doc.page_count} pages)...")
        print(f"Using prefix: {article_name}")
        
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x scale for better quality
            
            output_filename = f"{article_name}_page_{page_num + 1}.png"
            output_file = img_path / output_filename
            
            pix.save(output_file)
            print(f"  - Saved: {output_filename}")
            
        doc.close()
    except Exception as e:
        print(f"Error processing {pdf_file.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract pages of a specific PDF as images.")
    parser.add_argument("pdf", nargs="?", help="Path to the PDF file")
    args = parser.parse_args()

    # Determine project root (parent directory of this script)
    SCRIPT_DIR = Path(__file__).resolve().parent
    PROJECT_ROOT = SCRIPT_DIR.parent

    # Paths (absolute)
    PDF_INPUT_DIR = PROJECT_ROOT / "assets" / "pdf_sources"
    IMAGE_OUTPUT_DIR = PROJECT_ROOT / "assets" / "images"

    pdf_to_process = args.pdf
    
    if not pdf_to_process:
        # Get potential PDFs
        pdf_path = Path(PDF_INPUT_DIR)
        found_pdfs = sorted(list(pdf_path.glob("*.pdf")), key=os.path.getmtime, reverse=True)
        
        if not found_pdfs:
            print(f"No PDF files found in {PDF_INPUT_DIR}")
        else:
            print("\nSelect a PDF to extract images from:")
            for idx, pdf in enumerate(found_pdfs, 1):
                print(f"{idx}. {pdf.name}")

            choice = input(f"\nSelect (1-{len(found_pdfs)}): ").strip()
            
            try:
                choice_idx = int(choice)
                if 1 <= choice_idx <= len(found_pdfs):
                    pdf_to_process = found_pdfs[choice_idx - 1]
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Invalid input.")

    if pdf_to_process:
        extract_pdf_to_images(pdf_to_process, IMAGE_OUTPUT_DIR)
    else:
        print("No PDF selected. Exiting.")

