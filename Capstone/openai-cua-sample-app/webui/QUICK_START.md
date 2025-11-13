# 🚀 Quick Start Guide - Test Case Reporting

## Start Testing in 3 Steps:

### 1️⃣ Start the Server
```powershell
cd "c:\Users\RAJAT JAISWAL\Desktop\Final_Shreeji\Capstone_instru\Capstone\openai-cua-sample-app"
python webui/server.py
```

### 2️⃣ Open Browser
```
http://localhost:5001
```

### 3️⃣ Copy & Paste Test Case
Open `FORMATTED_TEST_CASES.md` and copy **ONE** test case at a time into the Instructions box.

---

## 📝 Example: First Test Case

**Copy this exactly into the Instructions box:**

```
Load https://www.saucedemo.com/v1/.
When the login page appears, type the username 'standard_user'.
Type the password 'secret_sauce'.
Click on the Login button.
Wait for the Products page to fully load.
Verify that the header "Products" appears correctly.
Verify that all items are visible.
TestCase Number - 1001.1.1.1, Valid Login Test: Verify that a valid user can log in successfully.
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.
```

**Then:**
1. Click "Send"
2. Watch the browser automate
3. See screenshots update in real-time
4. Result automatically saved!

---

## 📊 View Results

### Quick View (Console):
```powershell
python webui/view_report.py
```

### API View:
```powershell
curl http://localhost:5001/api/test-report
```

### File View:
Open: `webui/test_reports/test_case_report.json`

---

## ✅ What Happens Automatically:

✓ Test case number extracted (e.g., 1001.1.1.1)  
✓ Browser launches and executes steps  
✓ Screenshots captured after each action  
✓ Terminal output recorded  
✓ Pass/Fail determined by agent  
✓ Result saved to JSON report  
✓ Summary statistics updated  
✓ Console shows confirmation  

---

## 📋 All 15 Test Cases Ready!

Located in: `FORMATTED_TEST_CASES.md`

1. Valid Login Test (1001.1.1.1)
2. Invalid Password Test (1001.1.1.2)
3. Blank Login Fields Test (1001.1.1.3)
4. Add Single Product Test (1001.1.1.4)
5. Add Multiple Products Test (1001.1.1.5)
6. Remove Product Test (1001.1.1.6)
7. Sort Low to High Test (1001.1.1.7)
8. Sort High to Low Test (1001.1.1.8)
9. Product Detail Page Test (1001.1.1.9)
10. Checkout Process Test (1001.1.1.10)
11. Logout Test (1001.1.1.11)
12. Continue Shopping Test (1001.1.1.12)
13. Cart Badge Count Test (1001.1.1.13)
14. Locked Out User Test (1001.1.1.14)
15. Social Media Link Test (1001.1.1.15)

---

## 🎯 Pro Tips:

💡 **Execute one test at a time** for best results  
💡 **Wait for completion** before starting next test  
💡 **Check console** for real-time status updates  
💡 **Review screenshots** in the Preview panel  
💡 **Use Reset button** between tests if needed  

---

## 📦 Report Contents:

Each test result includes:
- ✅ Test Case Number
- ✅ Test Case Name  
- ✅ Result (Pass/Fail)
- ✅ Execution Timestamp
- ✅ Full Instructions
- ✅ Terminal Output
- ✅ Screenshot (base64)

Plus summary statistics:
- Total Tests
- Passed Count
- Failed Count  
- Pass Rate %

---

## 🔄 Clear Report (Start Fresh):

```powershell
curl -X POST http://localhost:5001/api/test-report/clear
```

Or delete: `webui/test_reports/test_case_report.json`

---

## ✨ Ready to Go!

Everything is implemented and tested. Just:
1. Start server
2. Open browser  
3. Copy test case
4. Paste & Send
5. View results

**No configuration needed. No UI changes. Works immediately!** 🎉
