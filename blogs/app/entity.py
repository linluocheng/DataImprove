class RstBlog():
    def __init__(self,bid,user_id,title,des,content,created):
        self.bid = bid
        self.user_id = user_id
        self.title = title
        self.description = des
        self.content = content

from app.models import Login
Login.password='ljj'
Login.username='ljj'
Login.save()
