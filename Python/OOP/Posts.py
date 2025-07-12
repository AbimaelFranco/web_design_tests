"""This script contains the Posts class for managing blog posts."""
from typing import Optional

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