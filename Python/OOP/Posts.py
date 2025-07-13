"""This script contains the Posts class for managing blog posts."""
from typing import Optional
from pathlib import Path
from Blog import Blog

class Posts:
    """A class to represent a collection of blog posts."""

    def __init__(self, title:str, content:Optional[str]=None, classification:Optional[str]=None):
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

    def modify_post(self, blog_name:str, new_title:str, new_content:str, new_classification:Optional[str]=None) -> None:
        """Modifies an existing post's title, content, and classification.
        
        Args:
            blog_name (str): The name of the blog to which the post belongs.
            new_title (str): The new title for the post.
            new_content (str): The new content for the post.
            new_classification (Optional[str]): The new classification for the post.
        """
        if not self.post_exists(blog_name, self.title):
            print(f"Post '{self.title}' does not exist in blog '{blog_name}'.")
            return
        
        blog_path = Path("folder") / blog_name
        post_filename = f"{self.title.replace(' ', '_')}.txt"
        post_path = blog_path / post_filename

        self.title = new_title
        self.content = new_content
        self.classification = new_classification
        
        with post_path.open("w", encoding="utf-8") as file:
            file.write(str(f"{self.title} \n"))
            file.write(str(f"{self.classification}\n"))
            file.write(str(f"{self.content}\n"))

    @staticmethod
    def post_exists(blog_name:str, post_title:str) -> bool:
        """Checks if a post exists in the specified blog.
        
        Args:
            blog_name (str): The name of the blog.
            post_title (str): The title of the post to check.
        
        Returns:
            bool: True if the post exists, False otherwise.
        """
        blog_path = Path("folder") / blog_name
        post_filename = f"{post_title.replace(' ', '_')}.txt"
        return (blog_path / post_filename).exists()
    
    @staticmethod
    def list_posts(blog_name:str) -> None:
        """Lists all posts in the specified blog.
        
        Args:
            blog_name (str): The name of the blog to list posts from.
        """
        blog_path = Path("folder") / blog_name
        if not blog_path.exists():
            print(f"Blog '{blog_name}' does not exist.")
            return
        
        for post_file in blog_path.glob("*.txt"):
            with post_file.open("r", encoding="utf-8") as file:
                print(file.read())