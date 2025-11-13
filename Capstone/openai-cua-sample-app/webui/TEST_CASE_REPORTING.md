# Test Case Reporting Feature

## Overview
This feature automatically captures and reports test case execution results in JSON format. Each test case is evaluated, and results (Pass/Fail) are stored with screenshots and terminal output.

## How It Works

### 1. Test Case Format
Your instructions must include a test case identifier:
```
TestCase Number - 1001.1.1.1, Valid Login Test: Verify that a valid user can log in successfully.
```

The format is:
- `TestCase Number - [NUMBER]` - The unique test case identifier
- `, [NAME]:` - A descriptive name for the test case
- Followed by test instructions

### 2. Automatic Detection
The system automatically:
- Extracts test case number and name from instructions
- Executes the test through the CUA agent
- Captures screenshots after each action
- Records terminal output
- Determines Pass/Fail based on agent verification
- Saves results to JSON report

### 3. Result Determination
The system looks for keywords in agent output:
- **Pass indicators**: "pass", "passed", "successful", "verified", "correct", "appears"
- **Fail indicators**: "fail", "failed", "error"

### 4. Report Structure
Results are stored in `webui/test_reports/test_case_report.json`:

```json
{
  "test_suite": "Sauce Demo Automation Test Suite",
  "execution_date": "2025-11-11 14:30:00",
  "summary": {
    "total_tests": 15,
    "passed": 13,
    "failed": 2,
    "unknown": 0,
    "pass_rate": "86.67%"
  },
  "test_cases": [
    {
      "test_case_number": "1001.1.1.1",
      "test_case_name": "Valid Login Test",
      "result": "Pass",
      "executed_at": "2025-11-11 14:30:15",
      "instructions": "Load https://www.saucedemo.com/v1/...",
      "terminal_output": "Agent output and actions...",
      "screenshot": "base64_encoded_screenshot..."
    }
  ]
}
```

## Usage

### Running Test Cases

1. **Start the Web UI**:
   ```powershell
   python webui/server.py
   ```

2. **Enter Test Instructions** in the Instructions box (from UI):
   - Paste one complete test case with the `TestCase Number` format
   - Click "Send"
   - Wait for execution and result

3. **View Real-time Progress**:
   - Screenshots appear in the Preview panel
   - Terminal output shows in the Terminal Output section
   - Test result is automatically saved when complete

### Viewing Reports

#### Option 1: Command Line Viewer
```powershell
python webui/view_report.py
```

This displays:
- Summary statistics (total, passed, failed, pass rate)
- Detailed results for each test case
- List of failed tests
- Option to export to CSV

#### Option 2: API Endpoint
```bash
# Get full report
curl http://localhost:5001/api/test-report

# Clear report (start fresh)
curl -X POST http://localhost:5001/api/test-report/clear
```

#### Option 3: Direct File Access
Open: `webui/test_reports/test_case_report.json`

## API Endpoints

### GET /api/test-report
Returns the complete test case report in JSON format.

### POST /api/test-report/clear
Clears the existing test report file.

### GET /api/task-status/<task_id>
Returns current task status including:
- `test_case_number` - Current test case number
- `test_case_name` - Current test case name
- `test_result` - Pass/Fail result when complete

## Example Test Case

```
Load https://www.saucedemo.com/v1/.
When the login page appears, type the username 'standard_user' and the password 'secret_sauce'.
Click on the Login button and wait for the Products page to fully load.
Verify that the header "Products" appears correctly and that all items are visible.
TestCase Number - 1001.1.1.1, Valid Login Test: Verify that a valid user can log in successfully.
Tell us if this test case is passed or failed? Update the result in one word (Pass/Fail) in report against this test case number.
```

## Important Notes

1. **One Test at a Time**: Execute one test case per submission
2. **Clear Instructions**: Include verification steps in your instructions
3. **Ask for Result**: End with "Tell us if this test case is passed or failed?"
4. **Auto-Save**: Results are automatically saved when test completes
5. **Screenshots**: Latest screenshot is captured and stored (truncated in JSON for size)
6. **Terminal Output**: Complete agent output is stored for debugging

## Troubleshooting

### Test Result Shows "Unknown"
- Ensure your instructions ask the agent to verify the test
- Add explicit "Tell us if this test case is passed or failed?" at the end
- Check that verification criteria are clear

### Report Not Generated
- Verify test case format includes "TestCase Number - X.X.X.X"
- Check that `webui/test_reports/` directory exists
- Look for errors in terminal output

### Test Hangs
- Agent may be waiting for user input
- Check the "Your Response" section in UI
- Provide response and click Send

## File Locations

```
webui/
├── server.py              # Main backend with test reporting logic
├── view_report.py         # Command-line report viewer
└── test_reports/
    ├── test_case_report.json   # Main test report
    └── test_report.csv          # CSV export (optional)
```

## Integration with Existing Features

The test reporting feature integrates seamlessly with:
- ✅ Interactive agent prompts
- ✅ Screenshot capture
- ✅ Terminal output logging
- ✅ Real-time status updates
- ✅ Error handling

All existing functionality remains unchanged!
