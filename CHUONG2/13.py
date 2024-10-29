import requests
api_url = "https://jsonplaceholder.typicode.com/comments?postId=1"
response = requests.get(api_url)
if response.status_code == 200:
    comments = response.json()
    print("Danh sách các bình luận nổi bật:\n")
    for index, comment in enumerate(comments[:3]):
        print(f"Bình luận {index + 1}:")
        print(f" - Email: {comment['email']}")
        print(f" - Tên: {comment['name']}")
        print(f" - Nội dung: {comment['body']}\n")
else:
    print("Lỗi khi lấy dữ liệu từ API.")
