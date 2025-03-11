import sys
from dirops import delete_dir_contents, copy_dir
from generator import generate_pages_recursive

def main():  
    basepath = '/'    
    if len(sys.argv) > 1 and sys.argv[1]:
        basepath = sys.argv[1]    
    delete_dir_contents("docs")
    copy_dir("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()