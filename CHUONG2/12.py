import requests
api_url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_url)
if response.status_code == 200:
    posts = response.json()
    print(f"Tổng số bài post: {len(posts)}\n")
    for post in posts:
        print(f"User ID: {post['userId']}")
        print(f"ID: {post['id']}")
        print(f"Tiêu đề: {post['title']}")
        print(f"Nội dung: {post['body']}\n")
else:
    print("Lỗi khi lấy dữ liệu từ API.")
