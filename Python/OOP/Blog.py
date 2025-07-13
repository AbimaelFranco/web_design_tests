"""This script contains the Blog class for managing blog posts."""
from typing import Optional
from pathlib import Path
from Posts import Posts

class Blog:
    """A class to represent a blog with posts."""

    def __init__(self, blog_name:str, description:str, blog_classification:Optional[str]=None):
        self.blog_name = blog_name
        self.description = description
        self.blog_classification = blog_classification

    def add_post(self, post:Posts) -> None:
        """Adds a post to the blog.
        
        Args:
            post (object): The post object to add to the blog.
        """
        blog_path = Path("folder")/self.blog_name
        blog_path.mkdir(parents=True, exist_ok=True)
        post_path = blog_path / f"{post.title}.txt"
        with post_path.open("w", encoding="utf-8") as file:
            file.write(str(f"{post.title} \n"))
            file.write(str(f"{post.classification}\n"))
            file.write(str(f"{post.content}\n"))


    def get_posts(self) -> list:
        """Retrieves all posts from the blog.
        
        Returns:
            list: A list of all post objects in the blog.
        """
        pass
