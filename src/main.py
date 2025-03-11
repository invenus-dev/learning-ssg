from dirops import delete_dir_contents, copy_dir
from generator import generate_page

def main():    
    delete_dir_contents("public")
    copy_dir("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()