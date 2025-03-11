import os
from dirops import delete_dir_contents, copy_dir

def main():    
    delete_dir_contents("public")
    copy_dir("static", "public")
    

main()