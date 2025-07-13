from Blog import Blog
from Posts import Posts

def main() -> None:
    """Main function to run the blog management system."""
    print("Welcome to the Blog Management System!")
    
    while True:
        print("\nMenu:")
        print("1. Create a new post")
        print("2. Modify a post")
        print("3. List all posts")
        print("4. Delete a post")
        print("5. create a blog")
        print("6. Modify a blog")
        print("7. List all blogs")
        print("8. Delete a blog")
        print("9. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            classification = input("Enter post classification (optional): ")
            blog_name = input("Enter the blog name to which this post belongs: ")
            post = Posts(title, content, classification)
            post.create_post(blog_name)
            print("Post created successfully.")
        
        elif choice == '2':
            # Placeholder for modifying a post
            print("Modify post functionality is not implemented yet.")
        
        elif choice == '3':
            # Placeholder for deleting a post
            print("Delete post functionality is not implemented yet.")
        
        elif choice == '5':
            blog_name = input("Enter blog name: ")
            description = input("Enter blog description: ")
            classification = input("Enter blog classification (optional): ")
            blog = Blog(blog_name, description, classification)
            blog.create_blog()
            print("Blog created successfully.")

        elif choice == '6':
            blog_name = input("Enter the name of the blog to modify: ")
            new_name = input("Enter new blog name: ")
            new_description = input("Enter new blog description: ")
            new_classification = input("Enter new blog classification (optional): ")
            blog = Blog(blog_name, "", "")
            blog.modify_blog(new_name, new_description, new_classification)
            print("Blog modified successfully.")

        elif choice == '7':
            Blog.list_blogs()
        
        elif choice == '8':
            blog_name = input("Enter the name of the blog to delete: ")
            blog = Blog(blog_name, "", "")
            blog.delete_blog()
            print("Blog deleted successfully.")

        elif choice == '9':
            print("Exiting the Blog Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()