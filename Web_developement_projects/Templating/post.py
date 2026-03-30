class Post:
    def __init__(self,blog_posts,id):
        self.posts = blog_posts
        self.body = ""
        self.title = ""
        self.subtitle = ""
        self.id = id

    def render(self):
        for blog in self.posts:
            if blog["id"] == self.id:
                self.body = blog["body"]
                self.title = blog["title"]
                self.subtitle = blog["subtitle"]
        return self.body,self.title,self.subtitle

