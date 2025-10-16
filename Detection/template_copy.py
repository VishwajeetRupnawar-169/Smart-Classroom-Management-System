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
    <title>Attendance System - Final Version</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 15px;
        }
        .container { max-width: 1800px; margin: 0 auto; }
        .header {
            background: white;
            padding: 20px 25px;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            margin-bottom: 15px;
        }
        .header h1 { color: #667eea; font-size: 1.8em; margin-bottom: 5px; }
        .header p { color: #666; font-size: 0.9em; }
        
        /* COMPACT CAMERA SECTION */
        .camera-section {
            background: white;
            padding: 15px;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
        
        .config-row {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr auto;
            gap: 10px;
            margin-bottom: 10px;
            align-items: end;
        }
        
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        
        .form-group label {
            font-weight: 600;
            color: #555;
            font-size: 0.85em;
        }
        
        .form-group input,
        .form-group select {
            padding: 8px 10px;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 0.9em;
        }
        
        .btn {
            padding: 8px 16px;
            border: none;
            border-radius: 6px;
            font-size: 0.9em;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .btn-confirm { background: #3b82f6; color: white; }
        .btn-confirm:hover { background: #2563eb; }
        .btn:disabled { background: #9ca3af; cursor: not-allowed; opacity: 0.6; }
        
        .camera-controls {
            display: flex;
            gap: 10px;
            align-items: center;
        }
        
        .btn-start { background: #10b981; color: white; flex: 1; }
        .btn-start:hover:not(:disabled) { background: #059669; }
        .btn-stop { background: #ef4444; color: white; flex: 1; }
        .btn-stop:hover:not(:disabled) { background: #dc2626; }
        
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 12px;
            background: #f3f4f6;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.85em;
        }
        .status-dot {
            width: 10px;
            height: 10px;
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
        
        .video-row {
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 15px;
        }
        
        .video-container {
            background: #000;
            border-radius: 8px;
            overflow: hidden;
            height: 400px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .video-container img { 
            max-width: 100%; 
            max-height: 100%; 
            object-fit: contain;
        }
        .video-placeholder {
            color: #9ca3af;
            font-size: 1.1em;
            text-align: center;
        }
        
        .info-stats {
            display: flex;
            flex-direction: column;
            gap: 8px;
            min-width: 200px;
        }
        
        .stat-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 12px;
            border-radius: 8px;
            color: white;
            text-align: center;
        }
        .stat-box h3 {
            font-size: 0.7em;
            opacity: 0.9;
            margin-bottom: 4px;
        }
        .stat-box .value {
            font-size: 1.6em;
            font-weight: bold;
        }
        
        /* ATTENDANCE SECTION */
        .attendance-section {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }
        
        .section-header h2 {
            color: #333;
            font-size: 1.4em;
        }
        
        .action-buttons {
            display: flex;
            gap: 8px;
        }
        
        .btn-refresh {
            background: #667eea;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9em;
        }
        .btn-refresh:hover { background: #5568d3; }
        
        .btn-clear {
            background: #f59e0b;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            font-size: 0.9em;
        }
        .btn-clear:hover { background: #d97706; }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 12px;
            margin-bottom: 15px;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 15px;
            border-radius: 8px;
            color: white;
            text-align: center;
        }
        .stat-card h3 {
            font-size: 0.7em;
            text-transform: uppercase;
            margin-bottom: 6px;
            opacity: 0.9;
        }
        .stat-card .value {
            font-size: 1.8em;
            font-weight: bold;
        }
        
        .table-container {
            overflow-x: auto;
            max-height: 450px;
            overflow-y: auto;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85em;
        }
        table th {
            background: #f8f9fa;
            padding: 10px 8px;
            text-align: left;
            font-weight: bold;
            color: #333;
            position: sticky;
            top: 0;
            z-index: 10;
        }
        table td {
            padding: 10px 8px;
            border-bottom: 1px solid #eee;
        }
        table tr:hover { background: #f8f9fa; }
        .status-badge-table {
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 0.8em;
            font-weight: bold;
            display: inline-block;
        }
        .status-badge-table.present { background: #d1fae5; color: #065f46; }
        .status-badge-table.absent { background: #fee2e2; color: #991b1b; }
        .status-badge-table.temporary-absent { background: #fef3c7; color: #92400e; }
        .status-badge-table.permanently-absent { background: #fee2e2; color: #991b1b; }
        .status-toggle {
            padding: 4px 8px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.75em;
            font-weight: bold;
        }
        .status-toggle.to-present { background: #10b981; color: white; }
        .status-toggle.to-absent { background: #ef4444; color: white; }
        .manual-badge {
            background: #fbbf24;
            color: #78350f;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.7em;
            margin-left: 5px;
        }
        
        .config-confirmed {
            background: #d1fae5;
            border: 2px solid #10b981;
            padding: 10px;
            border-radius: 6px;
            margin-bottom: 10px;
            display: none;
        }
        .config-confirmed.show { display: block; }
        .config-confirmed strong { color: #065f46; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Enhanced Attendance System - Final</h1>
            <p>Robust Duration Tracking | Compact UI | Daily Documents with Embedded Sessions</p>
        </div>

        <div class="camera-section">
            <div id="configSection">
                <div class="config-row">
                    <div class="form-group">
                        <label>Year/Batch</label>
                        <input type="text" id="year" placeholder="e.g., 2025">
                    </div>
                    <div class="form-group">
                        <label>Department</label>
                        <input type="text" id="department" placeholder="e.g., CSE">
                    </div>
                    <div class="form-group">
                        <label>Classroom</label>
                        <input type="text" id="classroom" placeholder="e.g., CSE-301">
                    </div>
                    <div class="form-group">
                        <label>Teacher Name</label>
                        <input type="text" id="teacherInput" placeholder="e.g., Prof. Smith">
                    </div>
                    <button class="btn btn-confirm" onclick="confirmConfig()">Confirm & Load Students</button>
                </div>
            </div>
            
            <div class="config-confirmed" id="confirmedBanner">
                <strong>Configuration:</strong> <span id="confirmedText"></span>
            </div>
            
            <div class="camera-controls" style="margin-bottom: 10px;">
                <div class="form-group" style="flex: 0 0 150px;">
                    <label>Recognition Mode</label>
                    <select id="modeSelect">
                        <option value="1">By Name</option>
                        <option value="2">By Roll Number</option>
                    </select>
                </div>
                <button class="btn btn-start" id="startBtn" onclick="startCamera()" disabled>Start Camera</button>
                <button class="btn btn-stop" id="stopBtn" onclick="stopCamera()" disabled>Stop Camera</button>
                <div class="status-badge">
                    <div class="status-dot" id="statusDot"></div>
                    <span id="statusText">Camera Stopped</span>
                </div>
            </div>
            
            <div class="video-row">
                <div class="video-container" id="videoContainer">
                    <div class="video-placeholder">Configure class settings and confirm to begin</div>
                </div>
                
                <div class="info-stats">
                    <div class="stat-box">
                        <h3>Current Faces</h3>
                        <div class="value" id="currentFaces">0</div>
                    </div>
                    <div class="stat-box">
                        <h3>Session</h3>
                        <div class="value" style="font-size: 1.2em;" id="currentSession">-</div>
                    </div>
                    <div class="stat-box">
                        <h3>Total</h3>
                        <div class="value" id="quickTotal">-</div>
                    </div>
                    <div class="stat-box">
                        <h3>Present</h3>
                        <div class="value" id="quickPresent">-</div>
                    </div>
                    <div class="stat-box">
                        <h3>Absent</h3>
                        <div class="value" id="quickAbsent">-</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="attendance-section">
            <div class="section-header">
                <h2>Current Session Attendance</h2>
                <div class="action-buttons">
                    <button class="btn-refresh" onclick="refreshData()">Refresh</button>
                    <button class="btn-clear" onclick="clearSessionData()" id="clearBtn" disabled>Clear</button>
                </div>
            </div>

            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Total</h3>
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
                    <h3>Temp Absent</h3>
                    <div class="value" id="tempAbsentCount">-</div>
                </div>
                <div class="stat-card">
                    <h3>Attendance %</h3>
                    <div class="value" id="attendancePercentage">-</div>
                </div>
            </div>

            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Roll No</th>
                            <th>Name</th>
                            <th>Status</th>
                            <th>First Seen</th>
                            <th>Last Seen</th>
                            <th>Present Time</th>
                            <th>Absent Time</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody id="attendanceBody">
                        <tr><td colspan="8" style="text-align: center;">Configure and confirm settings to load students</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>

    <script>
        const API_BASE_URL = window.location.origin + '/api';
        let cameraRunning = false;
        let refreshInterval = null;
        let currentDate = null;
        let currentClassId = null;
        let currentSession = null;
        let configConfirmed = false;
        let configData = {};

        function confirmConfig() {
            const year = document.getElementById('year').value.trim();
            const department = document.getElementById('department').value.trim();
            const classroom = document.getElementById('classroom').value.trim();
            const teacher = document.getElementById('teacherInput').value.trim();
            
            if (!year || !department || !classroom || !teacher) {
                alert('Please fill in all fields');
                return;
            }
            
            configData = { year, department, classroom, teacher_name: teacher };
            currentClassId = `${year}_${department}_${classroom}`;
            configConfirmed = true;
            
            document.getElementById('confirmedText').textContent = 
                `${year} | ${department} | ${classroom} | ${teacher}`;
            document.getElementById('confirmedBanner').classList.add('show');
            document.getElementById('startBtn').disabled = false;
            
            // Load current session students
            loadCurrentSession();
        }

        async function startCamera() {
            if (!configConfirmed) {
                alert('Please confirm configuration first');
                return;
            }
            
            const mode = document.getElementById('modeSelect').value;
            const startBtn = document.getElementById('startBtn');
            const stopBtn = document.getElementById('stopBtn');
            
            startBtn.disabled = true;
            startBtn.textContent = 'Starting...';
            try {
                const response = await fetch(`${API_BASE_URL}/camera/start`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        mode: parseInt(mode),
                        ...configData
                    })
                });
                const data = await response.json();
                if (data.success) {
                    cameraRunning = true;
                    updateCameraStatus(true);
                    startBtn.disabled = true;
                    stopBtn.disabled = false;
                    startBtn.textContent = 'Start Camera';
                    document.getElementById('videoContainer').innerHTML = 
                        '<img src="' + API_BASE_URL + '/video_feed?t=' + Date.now() + '">';
                    startAutoRefresh();
                    await loadCurrentSession();
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
                statusText.textContent = 'Running';
            } else {
                statusDot.classList.remove('active');
                statusText.textContent = 'Stopped';
            }
        }

        async function updateCameraInfo() {
            try {
                const response = await fetch(`${API_BASE_URL}/camera/status`);
                const data = await response.json();
                document.getElementById('currentFaces').textContent = data.current_faces || 0;
                document.getElementById('currentSession').textContent = data.current_session || '-';
                
                if (data.current_session && data.current_session !== currentSession) {
                    currentSession = data.current_session;
                    await loadCurrentSession();
                }
            } catch (error) {
                console.error('Error updating camera info:', error);
            }
        }

        async function loadCurrentSession() {
            if (!configConfirmed) return;
            
            try {
                const response = await fetch(`${API_BASE_URL}/current-session`);
                const data = await response.json();
                if (data.success && data.active) {
                    currentDate = data.date;
                    currentClassId = data.class_id;
                    currentSession = data.session_name;
                    updateStats(data.summary);
                    displayAttendanceData(data.attendance);
                    document.getElementById('clearBtn').disabled = false;
                }
            } catch (error) {
                console.error('Error loading session:', error);
            }
        }

        function updateStats(summary) {
            document.getElementById('totalStudents').textContent = summary.total || 0;
            document.getElementById('presentCount').textContent = summary.present || 0;
            document.getElementById('absentCount').textContent = summary.absent || 0;
            document.getElementById('tempAbsentCount').textContent = summary.temporary_absent || 0;
            document.getElementById('attendancePercentage').textContent = 
                (summary.attendance_percentage || 0).toFixed(2) + '%';
            
            document.getElementById('quickTotal').textContent = summary.total || 0;
            document.getElementById('quickPresent').textContent = summary.present || 0;
            document.getElementById('quickAbsent').textContent = summary.absent || 0;
        }

        async function toggleAttendance(rollNo, currentStatus) {
            if (!currentDate || !currentClassId || !currentSession) {
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
                        date: currentDate,
                        class_id: currentClassId,
                        session_name: currentSession,
                        roll_no: rollNo,
                        status: newStatus
                    })
                });
                
                const data = await response.json();
                if (data.success) {
                    await refreshData();
                } else {
                    alert('Failed to update: ' + (data.error || 'Unknown error'));
                }
            } catch (error) {
                console.error('Error toggling attendance:', error);
                alert('Error: ' + error.message);
            } finally {
                button.disabled = false;
                button.textContent = currentStatus === 'Present' ? 'Mark Absent' : 'Mark Present';
            }
        }

        async function refreshData() {
            await loadCurrentSession();
        }

        async function clearSessionData() {
            if (!currentDate || !currentClassId || !currentSession) {
                alert('No active session to clear');
                return;
            }
            if (!confirm('Are you sure you want to clear all attendance data for this session?')) return;
            try {
                const response = await fetch(`${API_BASE_URL}/attendance/clear`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ 
                        date: currentDate,
                        class_id: currentClassId,
                        session_name: currentSession 
                    })
                });
                const data = await response.json();
                if (data.success) {
                    alert(data.message);
                    await refreshData();
                } else {
                    alert('Failed to clear data: ' + (data.error || 'Unknown error'));
                }
            } catch (error) {
                console.error('Error clearing session data:', error);
            }
        }

        function displayAttendanceData(records) {
            const tbody = document.getElementById('attendanceBody');
            if (!records || records.length === 0) {
                tbody.innerHTML = '<tr><td colspan="8" style="text-align:center;">No records found</td></tr>';
                return;
            }

            tbody.innerHTML = '';
            records.forEach(rec => {
                const row = document.createElement('tr');
                const status = rec.status || 'Absent';
                let badgeClass = 'absent';
                if (status === 'Present') badgeClass = 'present';
                else if (status === 'Temporary Absent') badgeClass = 'temporary-absent';
                else if (status === 'Permanently Absent') badgeClass = 'permanently-absent';

                const timestamps = rec.timestamps || {};
                const durations = rec.durations || {};
                const flags = rec.flags || {};

                row.innerHTML = `
                    <td>${rec.roll_no || '-'}</td>
                    <td>${rec.name || '-'}</td>
                    <td>
                        <span class="status-badge-table ${badgeClass}">${status}</span>
                        ${flags.manual_override ? '<span class="manual-badge">Manual</span>' : ''}
                    </td>
                    <td>${timestamps.first_seen || 'N/A'}</td>
                    <td>${timestamps.last_seen || 'N/A'}</td>
                    <td>${durations.total_present_human || '0 sec'}</td>
                    <td>${durations.total_absent_human || '0 sec'}</td>
                    <td>
                        <button class="status-toggle ${status === 'Present' ? 'to-absent' : 'to-present'}"
                            onclick="toggleAttendance('${rec.roll_no}', '${status}')">
                            ${status === 'Present' ? 'Mark Absent' : 'Mark Present'}
                        </button>
                    </td>`;
                tbody.appendChild(row);
            });
        }

        function startAutoRefresh() {
            if (refreshInterval) clearInterval(refreshInterval);
            updateCameraInfo();
            refreshInterval = setInterval(() => {
                updateCameraInfo();
                refreshData();
            }, 5000);
        }

        function stopAutoRefresh() {
            if (refreshInterval) clearInterval(refreshInterval);
        }

        window.onload = function() {
            updateCameraStatus(false);
        };
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