"""This script contains the Posts class for managing blog posts."""
from typing import Optional
from pathlib import Path
from Blog import Blog

class Posts:
    """A class to represent a collection of blog posts."""

    def __init__(self, title:str, content:str, classification:Optional[str]=None):
        """Initializes a new post with a title and content.
        
        Args:
            title (str): The title of the post.
            content (str): The content of the post.
        """
        self.title = title
        self.content = content
        self.classification = classification
    
    def __str__(self) -> str:
        """Returns a string representation of the post."""
        return f"Title: {self.title}\nContent: {self.content}\nClassification: {self.classification if self.classification else 'Unclassified'}"
    
    def create_post(self, blog_name:str) -> None:
        """Creates a post file with the post's title and content.
        Args:
            blog_name (str): The name of the blog to which the post belongs.
        """
        if not Blog.blog_exists(blog_name):
            print(f"Blog '{blog_name}' does not exist. Please create the blog first.")
            blog_name = input("Enter blog name: ")
            blog_description = input("Enter blog description: ")
            blog_classification = input("Enter blog classification (optional): ")
            blog = Blog(blog_name, blog_description, blog_classification)
            blog.create_blog()

        blog_path = Path("folder")/blog_name
        post_filename = f"{self.title.replace(' ', '_')}.txt"
        post_path = blog_path / post_filename
        with post_path.open("w", encoding="utf-8") as file:
            file.write(str(f"{self.title} \n"))
            file.write(str(f"{self.classification}\n"))
            file.write(str(f"{self.content}\n"))

        