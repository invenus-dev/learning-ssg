from dirops import delete_dir_contents, copy_dir
from generator import generate_pages_recursive

def main():    
    delete_dir_contents("public")
    copy_dir("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()