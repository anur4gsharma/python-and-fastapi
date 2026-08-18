my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {"title": "foods", "content": "best food to try", "id": 2}]

def find_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            return post
    return None

print(find_post(2))