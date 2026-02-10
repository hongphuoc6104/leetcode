# 🗺️ Roadmap Chi Tiết - Interleaved Learning

## Tại sao Interleaved Learning?

### Blocked Practice (cách cũ) ❌
```
Tuần 1-4:  Array, Array, Array, Array...
Tuần 5-8:  Two Pointers, Two Pointers...
→ Quên Array khi học Two Pointers!
```

### Interleaved Practice (cách mới) ✅
```
Tuần 1: Array → TwoPtr → Sliding → Array → TwoPtr → Sliding → 🔄Review
Tuần 2: Array → TwoPtr → Sliding → Array → TwoPtr → Sliding → 🔄Review
→ Não liên tục kết nối, so sánh, phân biệt các kỹ thuật!
```

**Nghiên cứu khoa học** cho thấy Interleaved Practice:
- 📈 Tăng **43%** khả năng nhớ dài hạn so với Blocked Practice
- 🧠 Buộc não **phân biệt** khi nào dùng kỹ thuật nào
- 🔗 Tạo **liên kết** giữa các chủ đề liên quan

---

## Mindmap quan hệ giữa các chủ đề

```
                    ┌─────────────────────────────────────┐
                    │         PHASE 1: NỀN TẢNG MẢNG      │
                    │  Array ←→ Two Pointers ←→ Sliding   │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │    PHASE 2: TÌM KIẾM & TUYẾN TÍNH    │
                    │  BinarySearch ←→ LinkedList ←→ Stack  │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │      PHASE 3: TRA CỨU & CÂY         │
                    │    HashMap ←→ Tree ←→ Heap           │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │    PHASE 4: ĐỒ THỊ & QUY HOẠCH      │
                    │   Graph ←→ DP ←→ Backtracking        │
                    └──────────────┬──────────────────────┘
                                   │
                    ┌──────────────▼──────────────────────┐
                    │     PHASE 5: TỔNG HỢP & ÁP DỤNG     │
                    │  Greedy ←→ Sorting ←→ Ôn tổng hợp   │
                    └─────────────────────────────────────┘
```

### Tại sao nhóm lại như vậy?

| Phase | Lý do nhóm | Mối liên hệ |
|-------|-----------|-------------|
| 1 | Đều thao tác trên mảng | Two Pointers là kỹ thuật trên Array, Sliding Window mở rộng Two Pointers |
| 2 | CTDL tuyến tính + tìm kiếm | Binary Search cần sorted array, Stack/Queue là CTDL mới, Linked List dùng pointers |
| 3 | CTDL phân cấp + tra cứu | Hash hỗ trợ Tree, Heap là dạng tree đặc biệt |
| 4 | Thuật toán nâng cao | Graph mở rộng Tree, DP tối ưu, Backtracking vét cạn |
| 5 | Kết hợp mọi thứ | Greedy đối lập DP, Sorting tổng hợp CTDL |

---

## Cấu trúc mỗi Phase (12 tuần)

### 3 Vòng × 4 Tuần

```
Vòng 1 (Tuần 1-4):   🟢 Easy − 3 chủ đề xen kẽ
Vòng 2 (Tuần 5-8):   🟡 Medium − 3 chủ đề xen kẽ
Vòng 3 (Tuần 9-12):  🔴 Hard − 3 chủ đề xen kẽ
```

### Lịch 1 tuần (Chủ đề A, B, C)

| Ngày | Nội dung | Ghi chú |
|------|----------|---------|
| Thứ 2 | Chủ đề A | 1 bài mới |
| Thứ 3 | Chủ đề B | 1 bài mới |
| Thứ 4 | Chủ đề C | 1 bài mới |
| Thứ 5 | Chủ đề A | 1 bài mới |
| Thứ 6 | Chủ đề B | 1 bài mới |
| Thứ 7 | Chủ đề C | 1 bài mới |
| **CN** | **🔄 Review** | **Ôn Phase trước + ghi chú** |

### Ngày Review (Chủ nhật) làm gì?

1. **Ôn bài cũ**: Chọn 2-3 bài đã làm ở Phase trước, giải lại không nhìn code
2. **So sánh pattern**: Viết 3-5 dòng so sánh khi nào dùng A vs B vs C
3. **Flashcard**: Ghi lại 1-2 pattern mới học trong tuần vào ghi chú
4. **(Tùy chọn)**: Làm 1 bài Easy cũ nếu muốn luyện thêm

---

## ⏱️ Thời gian đề xuất

| Mức độ | Thời gian | Nếu kẹt |
|--------|-----------|---------|
| 🟢 Easy | 20-30 phút | Xem gợi ý, thử thêm 15 phút |
| 🟡 Medium | 30-45 phút | Xem solution, tự code lại |
| 🔴 Hard | 45-60 phút | Xem solution, ghi pattern, code lại sau 3 ngày |
| 🔄 Review | 30-45 phút | Ôn 2-3 bài cũ + ghi chú |

---

## 🎯 Mục tiêu theo Phase

| Phase | Mục tiêu | Kết quả mong đợi |
|-------|----------|-------------------|
| 1 | Thành thạo thao tác mảng | Giải Easy < 15 phút, Medium < 30 phút |
| 2 | Hiểu sâu CTDL tuyến tính | Tự tin dùng stack, linked list, binary search |
| 3 | Sử dụng CTDL phân cấp | Giải Tree, Hash problems thành thạo |
| 4 | Tư duy thuật toán nâng cao | Nhận diện pattern DP vs Backtracking vs Graph |
| 5 | Tổng hợp | Sẵn sàng phỏng vấn, giải Medium < 30 phút |

---

## 📊 Thống kê

| Metric | Giá trị |
|--------|---------|
| Tổng bài | 420 |
| Số Phase | 5 |
| Chủ đề/Phase | 3 (xen kẽ) |
| Tuần/Phase | 12 |
| Bài/tuần | 6 + 1 ngày Review |
| Tổng thời gian | ~60 tuần (~14 tháng) |
