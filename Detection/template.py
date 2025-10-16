"""
HTML Templates for Attendance System
Save this as template.py in the same directory as your main server file
"""

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attendance System Dashboard</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1600px; margin: 0 auto; }
        .header {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header h1 { color: #667eea; font-size: 2.5em; }
        .nav-links { display: flex; gap: 15px; }
        .nav-links a {
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            transition: background 0.3s;
        }
        .nav-links a:hover { background: #5568d3; }
        .control-panel {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }
        .control-buttons {
            display: flex;
            gap: 15px;
            align-items: center;
            flex-wrap: wrap;
        }
        .btn {
            padding: 12px 30px;
            border: none;
            border-radius: 8px;
            font-size: 1em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .btn-start { background: #10b981; color: white; }
        .btn-start:hover:not(:disabled) { background: #059669; }
        .btn-stop { background: #ef4444; color: white; }
        .btn-stop:hover:not(:disabled) { background: #dc2626; }
        .btn:disabled { background: #9ca3af; cursor: not-allowed; }
        .status-indicator {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 8px 16px;
            background: #f3f4f6;
            border-radius: 20px;
            font-weight: bold;
        }
        .status-dot {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #ef4444;
        }
        .status-dot.active {
            background: #10b981;
            animation: pulse 2s infinite;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }
        .main-grid {
            display: grid;
            grid-template-columns: 1fr 2fr;
            gap: 20px;
            margin-bottom: 20px;
        }
        .video-panel, .panel {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .video-container {
            position: relative;
            width: 100%;
            background: #000;
            border-radius: 10px;
            overflow: hidden;
        }
        .video-container img { width: 100%; height: auto; display: block; }
        .video-placeholder {
            width: 100%;
            height: 400px;
            background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #9ca3af;
            font-size: 1.2em;
            border-radius: 10px;
            text-align: center;
            padding: 20px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
            margin-bottom: 20px;
        }
        .stat-card {
            background: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .stat-card h3 {
            color: #666;
            font-size: 0.85em;
            text-transform: uppercase;
            margin-bottom: 8px;
        }
        .stat-card .value {
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }
        .table-container {
            overflow-x: auto;
            max-height: 500px;
            overflow-y: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table th {
            background: #f8f9fa;
            padding: 12px;
            text-align: left;
            font-weight: bold;
            color: #333;
            position: sticky;
            top: 0;
            font-size: 0.9em;
            z-index: 10;
        }
        table td {
            padding: 12px;
            border-bottom: 1px solid #eee;
            font-size: 0.9em;
        }
        table tr:hover { background: #f8f9fa; }
        .status-badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
            display: inline-block;
        }
        .status-badge.present {
            background: #d1fae5;
            color: #065f46;
        }
        .status-badge.absent {
            background: #fee2e2;
            color: #991b1b;
        }
        .status-badge.temporary-absent {
            background: #fef3c7;
            color: #92400e;
        }
        .status-badge.permanently-absent {
            background: #fee2e2;
            color: #7f1d1d;
        }
        .status-toggle {
            padding: 4px 8px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.8em;
            font-weight: bold;
            transition: all 0.3s;
        }
        .status-toggle.to-present {
            background: #10b981;
            color: white;
        }
        .status-toggle.to-absent {
            background: #ef4444;
            color: white;
        }
        .refresh-btn {
            background: #667eea;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: bold;
            margin-bottom: 15px;
            transition: background 0.3s;
        }
        .refresh-btn:hover { background: #5568d3; }
        .manual-override-badge {
            background: #fbbf24;
            color: #78350f;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.7em;
            margin-left: 5px;
        }
        .session-change-notice {
            background: #fef3c7;
            border: 2px solid #f59e0b;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 15px;
            text-align: center;
            font-weight: bold;
            color: #92400e;
            animation: slideDown 0.5s ease;
            display: none;
        }
        @keyframes slideDown {
            from { transform: translateY(-20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1>Attendance System</h1>
                <p>Real-time Face Recognition</p>
            </div>
            <div class="nav-links">
                <a href="/">Dashboard</a>
                <a href="/reports">Reports</a>
                <a href="/student">Student View</a>
            </div>
        </div>

        <div class="control-panel">
            <h2>Camera Control</h2>
            <div class="control-buttons">
                <select id="modeSelect">
                    <option value="1">Recognition by Name</option>
                    <option value="2">Recognition by Roll Number</option>
                </select>
                <button class="btn btn-start" id="startBtn" onclick="startCamera()">Start Camera</button>
                <button class="btn btn-stop" id="stopBtn" onclick="stopCamera()" disabled>Stop Camera</button>
                <div class="status-indicator">
                    <div class="status-dot" id="statusDot"></div>
                    <span id="statusText">Camera Stopped</span>
                </div>
            </div>
        </div>

        <div class="main-grid">
            <div class="video-panel">
                <h2>Live Camera Feed</h2>
                <div class="video-container" id="videoContainer">
                    <div class="video-placeholder">Camera not started<br>Click "Start Camera" to begin</div>
                </div>
                <div class="stats-grid" style="margin-top: 20px;">
                    <div class="stat-card">
                        <h3>Current Faces</h3>
                        <div class="value" id="currentFaces">0</div>
                    </div>
                    <div class="stat-card">
                        <h3>Session</h3>
                        <div class="value" style="font-size: 1em;" id="currentSession">None</div>
                    </div>
                </div>
            </div>

            <div>
                <div class="stats-grid" style="margin-bottom: 20px;">
                    <div class="stat-card">
                        <h3>Total Students</h3>
                        <div class="value" id="totalStudents">-</div>
                    </div>
                    <div class="stat-card">
                        <h3>Present</h3>
                        <div class="value" id="presentCount">-</div>
                    </div>
                    <div class="stat-card">
                        <h3>Absent</h3>
                        <div class="value" id="absentCount">-</div>
                    </div>
                    <div class="stat-card">
                        <h3>Attendance %</h3>
                        <div class="value" id="attendancePercentage">-</div>
                    </div>
                </div>

                <div class="panel">
                    <h2>Current Session Attendance</h2>
                    <button class="refresh-btn" onclick="refreshData()">Refresh Data</button>
                    <div class="table-container">
                        <table id="attendanceTable">
                            <thead>
                                <tr>
                                    <th>Roll No</th>
                                    <th>Name</th>
                                    <th>Status</th>
                                    <th>First Seen</th>
                                    <th>Last Seen</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody id="attendanceBody">
                                <tr><td colspan="6" style="text-align: center;">No data available</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        const API_BASE_URL = window.location.origin + '/api';
        let cameraRunning = false;
        let refreshInterval = null;
        let currentSessionId = null;
        let currentSessionName = null;
        let sessionChangeNoticeTimeout = null;

        async function startCamera() {
            const mode = document.getElementById('modeSelect').value;
            const startBtn = document.getElementById('startBtn');
            const stopBtn = document.getElementById('stopBtn');
            startBtn.disabled = true;
            startBtn.textContent = 'Starting...';
            try {
                const response = await fetch(`${API_BASE_URL}/camera/start`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ mode: parseInt(mode) })
                });
                const data = await response.json();
                if (data.success) {
                    cameraRunning = true;
                    updateCameraStatus(true);
                    startBtn.disabled = true;
                    stopBtn.disabled = false;
                    startBtn.textContent = 'Start Camera';
                    document.getElementById('videoContainer').innerHTML = 
                        '<img src="' + API_BASE_URL + '/video_feed?t=' + Date.now() + '" alt="Live Feed">';
                    startAutoRefresh();
                } else {
                    throw new Error(data.message || data.error);
                }
            } catch (error) {
                alert('Error: ' + error.message);
                startBtn.disabled = false;
                startBtn.textContent = 'Start Camera';
            }
        }

        async function stopCamera() {
            const startBtn = document.getElementById('startBtn');
            const stopBtn = document.getElementById('stopBtn');
            stopBtn.disabled = true;
            stopBtn.textContent = 'Stopping...';
            try {
                const response = await fetch(`${API_BASE_URL}/camera/stop`, { method: 'POST' });
                const data = await response.json();
                if (data.success) {
                    cameraRunning = false;
                    updateCameraStatus(false);
                    startBtn.disabled = false;
                    stopBtn.disabled = true;
                    stopBtn.textContent = 'Stop Camera';
                    document.getElementById('videoContainer').innerHTML = 
                        '<div class="video-placeholder">Camera stopped</div>';
                    stopAutoRefresh();
                }
            } catch (error) {
                alert('Error: ' + error.message);
                stopBtn.disabled = false;
                stopBtn.textContent = 'Stop Camera';
            }
        }

        function updateCameraStatus(isRunning) {
            const statusDot = document.getElementById('statusDot');
            const statusText = document.getElementById('statusText');
            if (isRunning) {
                statusDot.classList.add('active');
                statusText.textContent = 'Camera Running';
            } else {
                statusDot.classList.remove('active');
                statusText.textContent = 'Camera Stopped';
            }
        }

        async function updateCameraInfo() {
            try {
                const response = await fetch(`${API_BASE_URL}/camera/status`);
                const data = await response.json();
                document.getElementById('currentFaces').textContent = data.current_faces || 0;
                document.getElementById('currentSession').textContent = data.current_session || 'None';
            } catch (error) {
                console.error('Error updating camera info:', error);
            }
        }

        async function loadCurrentSession() {
            try {
                const response = await fetch(`${API_BASE_URL}/current-session`);
                const data = await response.json();
                
                console.log('Current session response:', data);
                
                if (data.success && data.active) {
                    const newSessionId = data.session_id;
                    const newSessionName = data.session_name;
                    
                    if (currentSessionId && currentSessionId !== newSessionId) {
                        console.log(`Session changed from ${currentSessionName} to ${newSessionName}`);
                        showSessionChangeNotice(newSessionName);
                    }
                    
                    currentSessionId = newSessionId;
                    currentSessionName = newSessionName;
                    
                    updateStats(data.summary);
                    displayAttendanceData(data.attendance);
                } else {
                    if (currentSessionId !== null) {
                        console.log('No active session - clearing data');
                        currentSessionId = null;
                        currentSessionName = null;
                        clearDisplay();
                    }
                }
            } catch (error) {
                console.error('Error loading session:', error);
            }
        }

        function clearDisplay() {
            document.getElementById('totalStudents').textContent = '-';
            document.getElementById('presentCount').textContent = '-';
            document.getElementById('absentCount').textContent = '-';
            document.getElementById('attendancePercentage').textContent = '-';
            document.getElementById('attendanceBody').innerHTML = 
                '<tr><td colspan="6" style="text-align: center;">No active session</td></tr>';
        }

        function showSessionChangeNotice(newSessionName) {
            const panel = document.querySelector('.panel');
            let notice = document.getElementById('sessionChangeNotice');
            
            if (!notice) {
                notice = document.createElement('div');
                notice.id = 'sessionChangeNotice';
                notice.className = 'session-change-notice';
                panel.insertBefore(notice, panel.querySelector('.refresh-btn'));
            }
            
            notice.textContent = `New session started: ${newSessionName}. Data refreshed!`;
            notice.style.display = 'block';
            
            if (sessionChangeNoticeTimeout) {
                clearTimeout(sessionChangeNoticeTimeout);
            }
            
            sessionChangeNoticeTimeout = setTimeout(() => {
                notice.style.display = 'none';
            }, 5000);
        }

        function updateStats(summary) {
            document.getElementById('totalStudents').textContent = summary.total || 0;
            document.getElementById('presentCount').textContent = summary.present || 0;
            document.getElementById('absentCount').textContent = summary.absent || 0;
            document.getElementById('attendancePercentage').textContent = 
                (summary.attendance_percentage || 0).toFixed(2) + '%';
        }

        async function toggleAttendance(docId, currentStatus) {
            if (!currentSessionId) {
                alert('No active session');
                return;
            }
            
            const newStatus = currentStatus === 'Present' ? 'Absent' : 'Present';
            const button = event.target;
            button.disabled = true;
            button.textContent = 'Updating...';
            
            try {
                const response = await fetch(`${API_BASE_URL}/attendance/update`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        session_id: currentSessionId,
                        doc_id: docId,
                        status: newStatus
                    })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    await refreshData();
                } else {
                    alert('Failed to update: ' + (data.error || 'Unknown error'));
                    button.disabled = false;
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error: ' + error.message);
                button.disabled = false;
            }
        }

        function displayAttendanceData(data) {
            const tbody = document.getElementById('attendanceBody');
            
            if (!data || data.length === 0) {
                tbody.innerHTML = '<tr><td colspan="6" style="text-align: center;">No data available</td></tr>';
                return;
            }
            
            const firstRecord = data[0];
            const rollFields = ['Roll_No', 'RollNo', 'Roll_Number', 'Roll'];
            const nameFields = ['Name', 'Student_Name', 'StudentName'];
            let rollField = rollFields.find(f => firstRecord.hasOwnProperty(f)) || 'Roll_No';
            let nameField = nameFields.find(f => firstRecord.hasOwnProperty(f)) || 'Name';
            
            tbody.innerHTML = data.map(record => {
                const statusClass = (record.Status || 'absent').toLowerCase().replace(/ /g, '-');
                const isManual = record.Manual_Override;
                const buttonClass = record.Status === 'Present' ? 'to-absent' : 'to-present';
                const buttonText = record.Status === 'Present' ? 'Mark Absent' : 'Mark Present';
                
                return `
                    <tr>
                        <td>${record[rollField] || '-'}</td>
                        <td>${record[nameField] || '-'}</td>
                        <td>
                            <span class="status-badge ${statusClass}">${record.Status || 'Absent'}</span>
                            ${isManual ? '<span class="manual-override-badge">MANUAL</span>' : ''}
                        </td>
                        <td>${record.First_Seen || 'N/A'}</td>
                        <td>${record.Last_Seen || 'N/A'}</td>
                        <td>
                            <button class="status-toggle ${buttonClass}" 
                                onclick="toggleAttendance('${record._id}', '${record.Status}')">
                                ${buttonText}
                            </button>
                        </td>
                    </tr>
                `;
            }).join('');
        }

        function refreshData() {
            loadCurrentSession();
            if (cameraRunning) updateCameraInfo();
        }

        function startAutoRefresh() {
            if (refreshInterval) clearInterval(refreshInterval);
            refreshInterval = setInterval(refreshData, 2000);
        }

        function stopAutoRefresh() {
            if (refreshInterval) {
                clearInterval(refreshInterval);
                refreshInterval = null;
            }
        }

        document.addEventListener('DOMContentLoaded', function() {
            loadCurrentSession();
        });

        window.addEventListener('beforeunload', () => {
            stopAutoRefresh();
            if (cameraRunning) {
                fetch(`${API_BASE_URL}/camera/stop`, { method: 'POST' });
            }
        });
    </script>
</body>
</html>
'''

REPORTS_HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Attendance Reports</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1600px; margin: 0 auto; }
        .header {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header h1 { color: #667eea; font-size: 2.5em; }
        .nav-links a {
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            margin-left: 10px;
        }
        .control-panel {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .date-selector {
            display: flex;
            gap: 15px;
            align-items: end;
            flex-wrap: wrap;
        }
        .form-group {
            flex: 1;
            min-width: 200px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1em;
        }
        .btn {
            padding: 10px 30px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s;
        }
        .btn-primary {
            background: #667eea;
            color: white;
        }
        .btn-primary:hover { background: #5568d3; }
        .btn-success {
            background: #10b981;
            color: white;
        }
        .btn-success:hover { background: #059669; }
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
            margin-bottom: 20px;
        }
        .chart-panel {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .chart-panel h3 {
            margin-bottom: 20px;
            color: #333;
        }
        .sessions-panel {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .session-card {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 15px;
            border-left: 5px solid #667eea;
        }
        .session-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        .session-title {
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
        }
        .session-stats {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 15px;
        }
        .stat-item {
            text-align: center;
        }
        .stat-item .label {
            font-size: 0.8em;
            color: #666;
            margin-bottom: 5px;
        }
        .stat-item .value {
            font-size: 1.5em;
            font-weight: bold;
            color: #667eea;
        }
        .table-container {
            overflow-x: auto;
            max-height: 400px;
            overflow-y: auto;
            margin-top: 15px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table th {
            background: #f8f9fa;
            padding: 12px;
            text-align: left;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }
        table td {
            padding: 12px;
            border-bottom: 1px solid #eee;
            font-size: 0.9em;
        }
        table tr:hover { background: #f8f9fa; }
        .status-badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
            display: inline-block;
        }
        .status-badge.present {
            background: #d1fae5;
            color: #065f46;
        }
        .status-badge.absent {
            background: #fee2e2;
            color: #991b1b;
        }
        .no-data {
            text-align: center;
            padding: 60px 20px;
            color: #666;
        }
        .toggle-btn {
            background: #f3f4f6;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.3s;
        }
        .toggle-btn:hover { background: #e5e7eb; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1>Attendance Reports</h1>
                <p>Visual Analytics & Excel Export</p>
            </div>
            <div class="nav-links">
                <a href="/">Dashboard</a>
                <a href="/student">Student View</a>
            </div>
        </div>

        <div class="control-panel">
            <h2>Select Date for Report</h2>
            <div class="date-selector">
                <div class="form-group">
                    <label>Report Date</label>
                    <input type="date" id="reportDate">
                </div>
                <div class="form-group">
                    <button class="btn btn-primary" onclick="loadReport()">Load Report</button>
                    <button class="btn btn-success" onclick="exportExcel()" style="margin-left: 10px;">Export to Excel</button>
                </div>
            </div>
        </div>

        <div id="reportContainer" style="display: none;">
            <div class="charts-grid">
                <div class="chart-panel">
                    <h3>Overall Attendance Distribution</h3>
                    <canvas id="pieChart"></canvas>
                </div>
                <div class="chart-panel">
                    <h3>Session-wise Comparison</h3>
                    <canvas id="barChart"></canvas>
                </div>
            </div>

            <div class="sessions-panel">
                <h2>Session Details</h2>
                <div id="sessionsContainer"></div>
            </div>
        </div>

        <div id="noData" class="no-data" style="display: none;">
            <h3>No data available for selected date</h3>
            <p>Please select a different date</p>
        </div>
    </div>

    <script>
        const API_BASE_URL = window.location.origin + '/api';
        let currentDate = null;
        let reportData = null;
        let pieChart = null;
        let barChart = null;

        document.getElementById('reportDate').valueAsDate = new Date();

        async function loadReport() {
            const dateInput = document.getElementById('reportDate').value;
            if (!dateInput) {
                alert('Please select a date');
                return;
            }

            currentDate = dateInput;
            console.log('Loading report for:', currentDate);

            try {
                const response = await fetch(`${API_BASE_URL}/reports/daily/${dateInput}`);
                const data = await response.json();
                console.log('Report response:', data);

                if (data.success && data.data && data.data.length > 0) {
                    reportData = data.data;
                    displayReport(reportData);
                } else {
                    showNoData();
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error loading report: ' + error.message);
                showNoData();
            }
        }

        function displayReport(data) {
            document.getElementById('reportContainer').style.display = 'block';
            document.getElementById('noData').style.display = 'none';
            createCharts(data);
            displaySessions(data);
        }

        function createCharts(data) {
            const totalPresent = data.reduce((sum, s) => sum + (s.summary.present || 0), 0);
            const totalAbsent = data.reduce((sum, s) => sum + (s.summary.absent || 0), 0);

            if (pieChart) pieChart.destroy();
            const pieCtx = document.getElementById('pieChart').getContext('2d');
            pieChart = new Chart(pieCtx, {
                type: 'doughnut',
                data: {
                    labels: ['Present', 'Absent'],
                    datasets: [{
                        data: [totalPresent, totalAbsent],
                        backgroundColor: ['#10b981', '#ef4444'],
                        borderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    plugins: { legend: { position: 'bottom' } }
                }
            });

            if (barChart) barChart.destroy();
            const barCtx = document.getElementById('barChart').getContext('2d');
            barChart = new Chart(barCtx, {
                type: 'bar',
                data: {
                    labels: data.map(s => s.session_name),
                    datasets: [
                        {
                            label: 'Present',
                            data: data.map(s => s.summary.present || 0),
                            backgroundColor: '#10b981'
                        },
                        {
                            label: 'Absent',
                            data: data.map(s => s.summary.absent || 0),
                            backgroundColor: '#ef4444'
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: true,
                    plugins: { legend: { position: 'bottom' } },
                    scales: { y: { beginAtZero: true } }
                }
            });
        }

        function displaySessions(data) {
            const container = document.getElementById('sessionsContainer');
            container.innerHTML = data.map((session, index) => {
                const summary = session.summary;
                return `
                    <div class="session-card">
                        <div class="session-header">
                            <div class="session-title">${session.session_name} - ${session.start_time}</div>
                            <button class="toggle-btn" onclick="toggleDetails(${index})">
                                <span id="toggle-${index}">Show Details</span>
                            </button>
                        </div>
                        <div class="session-stats">
                            <div class="stat-item">
                                <div class="label">Total</div>
                                <div class="value">${summary.total}</div>
                            </div>
                            <div class="stat-item">
                                <div class="label">Present</div>
                                <div class="value" style="color: #10b981;">${summary.present}</div>
                            </div>
                            <div class="stat-item">
                                <div class="label">Absent</div>
                                <div class="value" style="color: #ef4444;">${summary.absent}</div>
                            </div>
                            <div class="stat-item">
                                <div class="label">Attendance %</div>
                                <div class="value">${summary.attendance_percentage}%</div>
                            </div>
                        </div>
                        <div id="details-${index}" style="display: none;">
                            ${generateAttendanceTable(session.attendance)}
                        </div>
                    </div>
                `;
            }).join('');
        }

        function generateAttendanceTable(attendance) {
            if (!attendance || attendance.length === 0) {
                return '<p style="text-align: center; padding: 20px;">No data available</p>';
            }

            const firstRecord = attendance[0];
            const rollFields = ['Roll_No', 'RollNo', 'Roll_Number', 'Roll'];
            const nameFields = ['Name', 'Student_Name', 'StudentName'];
            let rollField = rollFields.find(f => firstRecord.hasOwnProperty(f)) || 'Roll_No';
            let nameField = nameFields.find(f => firstRecord.hasOwnProperty(f)) || 'Name';

            return `
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Roll No</th>
                                <th>Name</th>
                                <th>Status</th>
                                <th>First Seen</th>
                                <th>Last Seen</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${attendance.map(record => {
                                const statusClass = (record.Status || 'absent').toLowerCase().replace(/ /g, '-');
                                return `
                                    <tr>
                                        <td>${record[rollField] || '-'}</td>
                                        <td>${record[nameField] || '-'}</td>
                                        <td><span class="status-badge ${statusClass}">${record.Status || 'Absent'}</span></td>
                                        <td>${record.First_Seen || 'N/A'}</td>
                                        <td>${record.Last_Seen || 'N/A'}</td>
                                    </tr>
                                `;
                            }).join('')}
                        </tbody>
                    </table>
                </div>
            `;
        }

        function toggleDetails(index) {
            const details = document.getElementById(`details-${index}`);
            const toggle = document.getElementById(`toggle-${index}`);
            if (details.style.display === 'none') {
                details.style.display = 'block';
                toggle.textContent = 'Hide Details';
            } else {
                details.style.display = 'none';
                toggle.textContent = 'Show Details';
            }
        }

        function showNoData() {
            document.getElementById('reportContainer').style.display = 'none';
            document.getElementById('noData').style.display = 'block';
        }

        async function exportExcel() {
            if (!currentDate) {
                alert('Please load a report first');
                return;
            }
            window.location.href = `${API_BASE_URL}/reports/export/${currentDate}`;
        }
    </script>
</body>
</html>
'''

STUDENT_HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Attendance View</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        .header {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header h1 { color: #667eea; font-size: 2.5em; }
        .nav-links a {
            padding: 10px 20px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
        }
        .search-panel {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .search-form {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            align-items: end;
        }
        .form-group {
            flex: 1;
            min-width: 200px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #333;
        }
        .form-group input, .form-group select {
            width: 100%;
            padding: 10px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 1em;
        }
        .btn-search {
            padding: 10px 30px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s;
        }
        .btn-search:hover { background: #5568d3; }
        .stats-panel {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-top: 20px;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            color: white;
            text-align: center;
        }
        .stat-card h3 { font-size: 0.9em; margin-bottom: 10px; opacity: 0.9; }
        .stat-card .value { font-size: 2.5em; font-weight: bold; }
        .history-panel {
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .table-container {
            overflow-x: auto;
            max-height: 600px;
            overflow-y: auto;
            margin-top: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table th {
            background: #f8f9fa;
            padding: 12px;
            text-align: left;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }
        table td {
            padding: 12px;
            border-bottom: 1px solid #eee;
        }
        table tr:hover { background: #f8f9fa; }
        .status-badge {
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
            display: inline-block;
        }
        .status-badge.present {
            background: #d1fae5;
            color: #065f46;
        }
        .status-badge.absent {
            background: #fee2e2;
            color: #991b1b;
        }
        .no-data {
            text-align: center;
            padding: 40px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1>Student Attendance View</h1>
                <p>Check your attendance history</p>
            </div>
            <div class="nav-links">
                <a href="/">Dashboard</a>
            </div>
        </div>

        <div class="search-panel">
            <h2>Search Your Attendance</h2>
            <div class="search-form">
                <div class="form-group">
                    <label>Search By</label>
                    <select id="searchBy">
                        <option value="name">Name</option>
                        <option value="roll">Roll Number</option>
                    </select>
                </div>
                <div class="form-group">
                    <label>Enter Your Name/Roll Number</label>
                    <input type="text" id="identifier" placeholder="Enter here...">
                </div>
                <div class="form-group">
                    <button class="btn-search" onclick="searchAttendance()">Search</button>
                </div>
            </div>
        </div>

        <div id="resultsContainer" style="display: none;">
            <div class="stats-panel">
                <h2>Your Attendance Statistics</h2>
                <div class="stats-grid">
                    <div class="stat-card">
                        <h3>Total Sessions</h3>
                        <div class="value" id="totalSessions">0</div>
                    </div>
                    <div class="stat-card">
                        <h3>Present</h3>
                        <div class="value" id="presentSessions">0</div>
                    </div>
                    <div class="stat-card">
                        <h3>Absent</h3>
                        <div class="value" id="absentSessions">0</div>
                    </div>
                    <div class="stat-card">
                        <h3>Attendance %</h3>
                        <div class="value" id="attendancePercent">0%</div>
                    </div>
                </div>
            </div>

            <div class="history-panel">
                <h2>Attendance History</h2>
                <div class="table-container">
                    <table>
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Session</th>
                                <th>Status</th>
                                <th>First Seen</th>
                                <th>Last Seen</th>
                            </tr>
                        </thead>
                        <tbody id="historyBody">
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="noResults" class="no-data" style="display: none;">
            <h3>No records found</h3>
            <p>Please check your name/roll number and try again</p>
        </div>
    </div>

    <script>
        const API_BASE_URL = window.location.origin + '/api';

        async function searchAttendance() {
            const identifier = document.getElementById('identifier').value.trim();
            const searchBy = document.getElementById('searchBy').value;

            if (!identifier) {
                alert('Please enter your name or roll number');
                return;
            }

            try {
                const response = await fetch(`${API_BASE_URL}/student/${encodeURIComponent(identifier)}?search_by=${searchBy}`);
                const data = await response.json();

                if (data.success) {
                    displayResults(data);
                } else {
                    showNoResults();
                }
            } catch (error) {
                alert('Error: ' + error.message);
            }
        }

        function displayResults(data) {
            document.getElementById('resultsContainer').style.display = 'block';
            document.getElementById('noResults').style.display = 'none';

            const stats = data.statistics;
            document.getElementById('totalSessions').textContent = stats.total_sessions;
            document.getElementById('presentSessions').textContent = stats.present;
            document.getElementById('absentSessions').textContent = stats.absent;
            document.getElementById('attendancePercent').textContent = stats.attendance_percentage.toFixed(2) + '%';

            const tbody = document.getElementById('historyBody');
            if (data.history.length === 0) {
                tbody.innerHTML = '<tr><td colspan="5" style="text-align: center;">No attendance history found</td></tr>';
                return;
            }

            tbody.innerHTML = data.history.map(record => {
                const statusClass = record.status.toLowerCase().replace(/ /g, '-');
                return `
                    <tr>
                        <td>${record.date}</td>
                        <td>${record.session}</td>
                        <td><span class="status-badge ${statusClass}">${record.status}</span></td>
                        <td>${record.first_seen}</td>
                        <td>${record.last_seen}</td>
                    </tr>
                `;
            }).join('');
        }

        function showNoResults() {
            document.getElementById('resultsContainer').style.display = 'none';
            document.getElementById('noResults').style.display = 'block';
        }

        document.getElementById('identifier').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchAttendance();
            }
        });
    </script>
</body>
</html>
'''