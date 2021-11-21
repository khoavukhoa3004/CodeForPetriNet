# Code_1
Đọc kỹ note này nha mn:
- Tải python
- install graphviz (Dùng pip install graphviz)
- Sau khi tải package graphviz, tiến hành add PATH folder bin và file dot.exe (giống như 
cài c++ vậy)

file Petrinet: build 1 cái petri net
Chúng ta sẽ viết các code trong file main. Có 4 hàm đại diện cho 4 câu hỏi của đề
Trong mỗi hàm, tự tạo place, transition để build petri net, mn xem code bài 3 của tui để tham khảo nha
Nếu petrinet chạy theo chu trình khép kín (chạy vô hạn) cần built thêm phương thức mới
ở class PetriNet trong file PetriClass.py (đừng sửa phương thức run vì có thể ảnh hưởng đến
câu khác)
- Để tạo 1 petrinet:
  tập các place ( chứa list các Place và value)
  tập các transition kết nối với place ( gồm có list input Places và list output Places)
