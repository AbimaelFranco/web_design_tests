"""This script contains the Blog class for managing blog posts."""
from typing import Optional
from pathlib import Path

class Blog:
    """A class to represent a blog with posts."""

    def __init__(self, blog_name:str, description:Optional[str]=None, blog_classification:Optional[str]=None):
        self.blog_name = blog_name
        self.description = description
        self.blog_classification = blog_classification

    def __str__(self) -> str:
        """Returns a string representation of the blog."""
        return f"Blog Name: {self.blog_name}\nDescription: {self.description}\nClassification: {self.blog_classification if self.blog_classification else 'Unclassified'}"

    def create_blog(self) -> None:
        """Creates a blog directory with the blog name."""
        blog_path = Path("folder") / self.blog_name
        blog_path.mkdir(parents=True, exist_ok=True)
        with (blog_path / "blog_info.txt").open("w", encoding="utf-8") as file:
            file.write(str(self))

    def modify_blog(self, new_name:str, new_description:str, new_classification:Optional[str]=None) -> None:
        """Modifies the blog's name, description, and classification.
        
        Args:
            new_name (str): The new name for the blog.
            new_description (str): The new description for the blog.
            new_classification (Optional[str]): The new classification for the blog.
        """
        if not Blog.blog_exists(self.blog_name):
            print(f"Blog '{blog_name}' does not exist. Please create the blog first.")
            blog_name = input("Enter blog name: ")
            blog_description = input("Enter blog description: ")
            blog_classification = input("Enter blog classification (optional): ")
            blog = Blog(blog_name, blog_description, blog_classification)
            blog.create_blog()
        else:
            blog_path = Path("folder") / self.blog_name
            blog_path.rename(Path("folder") / new_name)
            self.blog_name = new_name
            self.description = new_description
            self.blog_classification = new_classification
            with (Path("folder") / new_name / "blog_info.txt").open("w", encoding="utf-8") as file:
                file.write(str(self))

    def delete_blog(self) -> None:
        """Deletes the blog directory."""
        # if blog_name == self.blog_name:
        blog_path = Path("folder") / self.blog_name
        if blog_path.exists():
            for item in blog_path.iterdir():
                item.unlink()
            blog_path.rmdir()
        else:
            print(f"Blog '{self.blog_name}' does not exist.")

    @staticmethod
    def list_blogs() -> None:
        """Lists all blogs in the 'folder' directory."""
        folder_path = Path("folder")
        if folder_path.exists():
            for blog in folder_path.iterdir():
                if blog.is_dir():
                    print(blog.name)
        else:
            print("No blogs found.")

    @staticmethod
    def blog_exists(blog_name: str) -> bool:
        """Checks if a blog exists in the 'folder' directory.
        
        Args:
            blog_name (str): The name of the blog to check.
        
        Returns:
            bool: True if the blog exists, False otherwise.
        """
        folder_path = Path("folder")
        if folder_path.exists():
            return (folder_path / blog_name).exists()
        return False    