# Vocabulary Quiz Generator  
โปรเจกต์นี้เป็นส่วนหนึ่งของรายวิชา **CS436 – Software Engineering**  
วัตถุประสงค์คือพัฒนาโปรแกรมฝึกคำศัพท์ภาษาอังกฤษโดยใช้ขั้นตอน SDLC แบบครบวงจร ตั้งแต่ Requirement → Design → Implementation → Testing → Deployment Review

ระบบถูกพัฒนาเป็น **Console Application (Python)** และใช้ไฟล์ CSV เป็นฐานข้อมูลคำศัพท์

---

# ฟีเจอร์หลัก (Features)

- โหลดไฟล์คำศัพท์จากไฟล์ CSV  
- แสดงคำถามแบบตัวเลือก **5 ตัวเลือกสุ่มลำดับ**  
- ตรวจสอบคำตอบทันที  
- ป้องกันข้อผิดพลาดของผู้ใช้ เช่น ใส่ตัวอักษรหรือเลขผิดช่วง  
- แสดงผลคะแนนรวมและคำศัพท์ที่ตอบผิด  
- ใช้งานง่ายผ่านหน้า Terminal

---

# เทคโนโลยีที่ใช้ (Technology Stack)

| ส่วน | รายละเอียด |
|------|-------------|
| ภาษาโปรแกรม | Python 3.11+ |
| ข้อมูล | CSV File |
| Platform | macOS / Windows / Linux |
| Tools | Terminal, VS Code, GitHub |

---

# โครงสร้างโปรเจกต์ (Project Structure)

```
Vocabulary-Quiz-Project-SE/
├── 01_Requirements/
│     ├── Scope_Document.md
│     └── User_Stories.md
│
├── 02_UX_UI_Design/
│     ├── Design_Rationale.md
│     └── Prototype/
│           ├── 01_Main_Menu.png
│           ├── 02_Load_File.png
│           ├── 03_Quiz_Screen.png
│           └── 04_Summary_Screen.png
│
├── 03_System_Design/
│     ├── Architecture_Diagram.png
│     ├── Data_Model_Diagram.png
│     ├── Sequence_Diagram_QuizFlow.png
│     └── Technology_Stack_Justification.md
│
├── 04_Implementation/
│     └── src/
│           ├── main.py
│           └── vocab.csv
│
├── 05_Testing/
│     ├── Test_Case_Report.md
│     └── Test_Evidence/
│           ├── TC01_Main_Menu.png
│           ├── TC02_Invalid_Menu_Option.png
│           ├── TC03_Load_File_Success.png
│           ├── TC04_Load_File_NotFound.png
│           ├── TC05_Start_Quiz_NoFile_Error.png
│           ├── TC06_Question1.png
│           ├── TC07_Answer_Correct.png
│           ├── TC08_Answer_Incorrect.png
│           ├── TC09_Invalid_Answer_NotNumber.png
│           ├── TC10_Invalid_Answer_OutOfRange.png
│           ├── TC11_Quiz_Summary.png
│           └── TC12_Exit_Program.png
│
├── 06_Deployment_Review/
│     ├── User_Manual.md
│     ├── Presentation_Slides.pdf (optional)
│     └── Deployment_Link.txt (optional)
│
└── README.md
```

---

# วิธีรันโปรแกรม (How to Run)

## 1) เปิด Terminal แล้วไปที่โฟลเดอร์ src  
```bash
cd 04_Implementation/src
```

## 2) รันคำสั่ง
```bash
python3 main.py
```

## 3) เมนูหลักที่มีให้เลือก
```
1. Load vocabulary file
2. Start quiz
3. Exit
```

---

# รูปแบบไฟล์ vocab.csv ที่รองรับ

ต้องอยู่ในรูปแบบ:

```
word,correct_choice,choice2,choice3,choice4,choice5
```

ตัวอย่าง:

```
ancient,โบราณ,ใหม่,สะอาด,เร็ว,สด
rapid,เร็ว,ช้า,เก่า,หนา,เบา
```

✔ รองรับภาษาไทย  
✔ ต้องเป็น UTF-8

---

# Testing Summary

มีการออกแบบ Test Case ตามหลัก SDLC  
รวมทั้งหมด **12 Test Cases** ครอบคลุม:

- เมนูหลัก  
- โหลดไฟล์สำเร็จ / ผิดพลาด  
- เริ่มทำแบบทดสอบโดยไม่โหลดไฟล์  
- ตอบถูก / ตอบผิด  
- ใส่ข้อมูลผิด เช่น ตัวอักษร  
- Quiz Summary  

หลักฐานผลลัพธ์อยู่ในโฟลเดอร์:

```
05_Testing/Test_Evidence/
```

---

# Documentation ที่จัดทำตาม SDLC

| Phase | Deliverable |
|-------|-------------|
| Requirements | Scope Document, User Stories |
| Design | Prototype, UX/UI Rationale, Architecture, Data Model, Sequence Diagram |
| Implementation | main.py, vocab.csv |
| Testing | Test Case Report + Evidence |
| Deployment Review | User Manual, Slides |

---

# ผู้พัฒนา (Developer)
- ชื่อ: นายอานุภาพ ชิดชาญกิจ
- รหัสนักศึกษา: 1670703873
- คณะ/สาขา: คณะเทคโนโลยีสารสนเทศและนวัตกรรม สาขาวิชาวิทยาการคอมพิวเตอร์
- มหาวิทยาลัยกรุงเทพ (Bangkok University)

---

# License
โปรเจกต์นี้พัฒนาเพื่อการศึกษาเท่านั้น  
สามารถนำไปปรับปรุงหรือศึกษาเพิ่มเติมได้
