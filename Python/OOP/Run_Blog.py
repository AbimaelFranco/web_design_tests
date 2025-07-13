from Blog import Blog
from Posts import Posts

blog_name = input("Enter blog name: ")
blog_description = input("Enter blog description: ")

post_title = input("Enter post title: ")
post_content = input("Enter post content: ")
post_classification = input("Enter post classification (optional): ")

blog = Blog(blog_name, blog_description)
post = Posts(post_title, post_content, post_classification)
blog.add_post(post)