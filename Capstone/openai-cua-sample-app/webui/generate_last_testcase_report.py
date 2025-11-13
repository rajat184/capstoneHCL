#!/usr/bin/env python3
"""
Generate HTML Report for Last Test Case
Creates a professional, presentable HTML report showing only the most recently executed test case.
"""

import json
import os
from datetime import datetime


def generate_html_report(json_file_path, output_html_path=None):
    """
    Generate HTML report for the last test case from the JSON report file.
    
    Args:
        json_file_path: Path to test_case_report.json
        output_html_path: Optional path for output HTML file (default: last_testcase_report.html)
    """
    # Read the JSON report
    with open(json_file_path, 'r', encoding='utf-8') as f:
        report_data = json.load(f)
    
    # Get the last test case
    if not report_data.get('test_cases'):
        print("No test cases found in the report.")
        return
    
    last_test_case = report_data['test_cases'][-1]
    
    # Determine output path
    if output_html_path is None:
        output_html_path = os.path.join(
            os.path.dirname(json_file_path),
            'last_testcase_report.html'
        )
    
    # Parse instructions to extract steps
    instructions = last_test_case.get('instructions', '')
    steps_lines = []
    for line in instructions.split('\n'):
        line = line.strip()
        if line.startswith('- '):
            steps_lines.append(line[2:])
    
    # Determine status color and icon
    result = last_test_case.get('result', 'Unknown')
    if result == 'Pass':
        status_color = '#10b981'
        status_icon = '✓'
        status_bg = '#d1fae5'
    elif result == 'Fail':
        status_color = '#ef4444'
        status_icon = '✗'
        status_bg = '#fee2e2'
    else:
        status_color = '#f59e0b'
        status_icon = '?'
        status_bg = '#fef3c7'
    
    # Build HTML
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Test Case Report - {last_test_case.get('test_case_number', 'N/A')}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px 40px;
            border-bottom: 4px solid rgba(255, 255, 255, 0.2);
        }}
        
        .header h1 {{
            font-size: 28px;
            font-weight: 600;
            margin-bottom: 8px;
        }}
        
        .header .subtitle {{
            font-size: 14px;
            opacity: 0.9;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .test-info {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .info-card {{
            background: #f9fafb;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }}
        
        .info-card .label {{
            font-size: 12px;
            font-weight: 600;
            color: #6b7280;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }}
        
        .info-card .value {{
            font-size: 16px;
            color: #1f2937;
            font-weight: 500;
        }}
        
        .status-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 14px;
            background: {status_bg};
            color: {status_color};
        }}
        
        .status-icon {{
            font-size: 18px;
            font-weight: bold;
        }}
        
        .section {{
            margin-bottom: 30px;
        }}
        
        .section-title {{
            font-size: 20px;
            font-weight: 600;
            color: #1f2937;
            margin-bottom: 16px;
            padding-bottom: 8px;
            border-bottom: 2px solid #e5e7eb;
        }}
        
        .steps-list {{
            list-style: none;
            counter-reset: step-counter;
        }}
        
        .steps-list li {{
            counter-increment: step-counter;
            position: relative;
            padding-left: 45px;
            margin-bottom: 16px;
            line-height: 1.6;
            color: #4b5563;
        }}
        
        .steps-list li::before {{
            content: counter(step-counter);
            position: absolute;
            left: 0;
            top: 0;
            width: 30px;
            height: 30px;
            background: #667eea;
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 600;
            font-size: 14px;
        }}
        
        .terminal-output {{
            background: #1f2937;
            color: #10b981;
            padding: 20px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            line-height: 1.6;
            white-space: pre-wrap;
            word-wrap: break-word;
            overflow-x: auto;
        }}
        
        .screenshot-container {{
            margin-top: 20px;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        
        .screenshot-container img {{
            width: 100%;
            height: auto;
            display: block;
        }}
        
        .no-screenshot {{
            background: #f3f4f6;
            color: #6b7280;
            padding: 40px;
            text-align: center;
            border-radius: 8px;
            font-style: italic;
        }}
        
        .footer {{
            background: #f9fafb;
            padding: 20px 40px;
            text-align: center;
            color: #6b7280;
            font-size: 14px;
            border-top: 1px solid #e5e7eb;
        }}
        
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
                border-radius: 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧪 Test Case Execution Report</h1>
            <div class="subtitle">{report_data.get('test_suite', 'Test Suite')}</div>
        </div>
        
        <div class="content">
            <!-- Test Case Information -->
            <div class="test-info">
                <div class="info-card">
                    <div class="label">Test Case Number</div>
                    <div class="value">{last_test_case.get('test_case_number', 'N/A')}</div>
                </div>
                
                <div class="info-card">
                    <div class="label">Test Case Name</div>
                    <div class="value">{last_test_case.get('test_case_name', 'N/A')}</div>
                </div>
                
                <div class="info-card">
                    <div class="label">Execution Date</div>
                    <div class="value">{last_test_case.get('executed_at', 'N/A')}</div>
                </div>
                
                <div class="info-card">
                    <div class="label">Result</div>
                    <div class="value">
                        <span class="status-badge">
                            <span class="status-icon">{status_icon}</span>
                            {result}
                        </span>
                    </div>
                </div>
            </div>
            
            <!-- Test Steps -->
            <div class="section">
                <h2 class="section-title">Test Steps</h2>
                <ol class="steps-list">
"""
    
    # Add test steps
    if steps_lines:
        for step in steps_lines:
            html_content += f"                    <li>{step}</li>\n"
    else:
        html_content += "                    <li>No detailed steps available</li>\n"
    
    html_content += """                </ol>
            </div>
            
            <!-- Terminal Output -->
            <div class="section">
                <h2 class="section-title">Terminal Output</h2>
                <div class="terminal-output">"""
    
    terminal_output = last_test_case.get('terminal_output', 'No terminal output recorded')
    html_content += f"{terminal_output}"
    
    html_content += """</div>
            </div>
            
            <!-- Screenshot -->
            <div class="section">
                <h2 class="section-title">Screenshot</h2>
                <div class="screenshot-container">
"""
    
    # Add screenshot if available
    screenshot_data = last_test_case.get('screenshot')
    if screenshot_data:
        html_content += f'                    <img src="data:image/png;base64,{screenshot_data}" alt="Test execution screenshot">\n'
    else:
        html_content += '                    <div class="no-screenshot">No screenshot available</div>\n'
    
    html_content += """                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>Generated on """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """ | Sauce Demo Automation Test Suite</p>
        </div>
    </div>
</body>
</html>
"""
    
    # Write HTML file
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✓ HTML report generated successfully!")
    print(f"  Location: {output_html_path}")
    print(f"  Test Case: {last_test_case.get('test_case_number')} - {last_test_case.get('test_case_name')}")
    print(f"  Result: {result}")
    
    return output_html_path


if __name__ == '__main__':
    # Default paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(script_dir, 'test_reports', 'test_case_report.json')
    
    if not os.path.exists(json_file):
        print(f"Error: Test report file not found at {json_file}")
        exit(1)
    
    # Generate report
    output_file = generate_html_report(json_file)
    
    # Try to open in browser
    try:
        import webbrowser
        webbrowser.open(f'file://{os.path.abspath(output_file)}')
        print(f"\n✓ Opening report in browser...")
    except Exception as e:
        print(f"\nNote: Could not auto-open browser: {e}")
        print(f"Please open the file manually: {output_file}")
