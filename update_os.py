import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract projects-grid
grid_match = re.search(r'<div class=\"projects-grid\">.*?</div>\s+<a href=\"https://github\.com/oguzaliozel\"', content, re.DOTALL)
projects_grid_html = grid_match.group(0).replace('<a href=\"https://github.com/oguzaliozel\"', '')

# 2. Inject CSS
css = '''
        /* OS Desktop Styles */
        #os-modal {
            display: none; position: fixed; z-index: 1000; left: 0; top: 0;
            width: 100vw; height: 100vh;
            background: url('https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?q=80&w=2564&auto=format&fit=crop') no-repeat center center/cover;
        }
        
        #os-desktop {
            position: relative; width: 100%; height: calc(100% - 48px);
            padding: 20px; display: flex; flex-direction: column; gap: 20px; flex-wrap: wrap; align-content: flex-start;
        }
        
        .desktop-icon {
            width: 80px; display: flex; flex-direction: column; align-items: center; gap: 5px;
            cursor: pointer; padding: 10px 5px; border-radius: 5px;
            transition: background 0.2s;
        }
        .desktop-icon:hover { background: rgba(255, 255, 255, 0.15); }
        .desktop-icon svg { width: 40px; height: 40px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5)); }
        .desktop-icon img { width: 40px; height: 40px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.5)); }
        .desktop-icon span { color: white; font-size: 12px; text-align: center; text-shadow: 0 1px 3px rgba(0,0,0,0.8); user-select: none; }
        
        #os-taskbar {
            position: absolute; bottom: 0; width: 100%; height: 48px;
            background: rgba(30, 30, 40, 0.85); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            display: flex; justify-content: center; align-items: center; gap: 15px; border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .taskbar-icon {
            width: 36px; height: 36px; border-radius: 4px; display: flex; justify-content: center; align-items: center;
            cursor: pointer; transition: all 0.2s;
        }
        .taskbar-icon:hover { background: rgba(255, 255, 255, 0.1); }
        .taskbar-icon.active { background: rgba(255, 255, 255, 0.15); box-shadow: inset 0 -2px 0 #4dabf7; }
        
        /* OS Window Styles */
        .os-window {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            width: 800px; max-width: 90vw; height: 600px; max-height: 85vh;
            background: rgba(20, 20, 30, 0.95); border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 8px; display: none; flex-direction: column;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.1);
            overflow: hidden;
            backdrop-filter: blur(20px);
            resize: both;
        }
        .os-window-header {
            height: 40px; background: rgba(0,0,0,0.2); display: flex; justify-content: space-between; align-items: center;
            padding: 0 15px; user-select: none; border-bottom: 1px solid rgba(255,255,255,0.05); cursor: move;
        }
        .os-window-title { color: white; font-size: 13px; font-weight: 500; display: flex; align-items: center; gap: 8px; }
        .os-window-controls { display: flex; gap: 8px; }
        .os-win-btn { width: 14px; height: 14px; border-radius: 50%; cursor: pointer; display: flex; justify-content: center; align-items: center; }
        .os-win-close { background: #ff5f56; }
        .os-win-min { background: #ffbd2e; }
        .os-win-max { background: #27c93f; }
        .os-window-content { flex: 1; overflow-y: auto; padding: 20px; }
'''

content = content.replace('    </style>', css + '\n    </style>', 1)

# 3. Inject HTML
html = '''
    <!-- Sanal İşletim Sistemi Modalı -->
    <div id="os-modal">
        <div id="os-desktop">
            <div class="desktop-icon" onclick="openOSWindow('projects-window')">
                <img src="https://img.icons8.com/color/96/000000/folder-invoices.png" alt="Projelerim">
                <span>Projelerim</span>
            </div>
            <div class="desktop-icon" onclick="openOSWindow('games-window')">
                <img src="https://img.icons8.com/color/96/000000/controller.png" alt="Oyunlarım">
                <span>Oyunlarım</span>
            </div>
            
            <a href="https://github.com/oguzaliozel" target="_blank" style="text-decoration: none;">
                <div class="desktop-icon">
                    <img src="https://img.icons8.com/fluency/96/000000/github.png" alt="GitHub">
                    <span>GitHub</span>
                </div>
            </a>
        </div>
        
        <!-- Pencereler -->
        <div id="projects-window" class="os-window">
            <div class="os-window-header" onmousedown="dragOSWindow(event, 'projects-window')">
                <div class="os-window-title"><img src="https://img.icons8.com/color/48/000000/folder-invoices.png" width="16" height="16"> Projelerim</div>
                <div class="os-window-controls">
                    <div class="os-win-btn os-win-min" onclick="closeOSWindow('projects-window')"></div>
                    <div class="os-win-btn os-win-max"></div>
                    <div class="os-win-btn os-win-close" onclick="closeOSWindow('projects-window')"></div>
                </div>
            </div>
            <div class="os-window-content">
                <p class="modal-subtitle">Geliştirdiğim projelere ve kod çalışmalarıma buradan göz atabilirsin.</p>
''' + projects_grid_html + '''
            </div>
        </div>
        
        <div id="games-window" class="os-window" style="width: 650px; height: 500px;">
            <div class="os-window-header" onmousedown="dragOSWindow(event, 'games-window')">
                <div class="os-window-title"><img src="https://img.icons8.com/color/48/000000/controller.png" width="16" height="16"> Oyunlarım</div>
                <div class="os-window-controls">
                    <div class="os-win-btn os-win-min" onclick="closeOSWindow('games-window')"></div>
                    <div class="os-win-btn os-win-max"></div>
                    <div class="os-win-btn os-win-close" onclick="closeOSWindow('games-window')"></div>
                </div>
            </div>
            <div class="os-window-content">
                <p class="modal-subtitle">Boş zamanlarımda oynadığım favori oyunlar.</p>
                <div class="projects-grid">
                    <div class="project-card" style="text-align: center; padding: 25px 15px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/d/d8/League_of_Legends_2019_vector.svg" style="height: 50px; object-fit: contain; margin-bottom: 20px;">
                        <h3 style="margin-top:0;">League of Legends</h3>
                    </div>
                    <div class="project-card" style="text-align: center; padding: 25px 15px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/e/ec/Assetto_Corsa_logo.png" style="height: 50px; object-fit: contain; filter: invert(1); margin-bottom: 20px;">
                        <h3 style="margin-top:0;">Assetto Corsa</h3>
                    </div>
                    <div class="project-card" style="text-align: center; padding: 25px 15px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6d/Forza_Horizon_4_logo.svg" style="height: 50px; object-fit: contain; filter: invert(1); margin-bottom: 20px;">
                        <h3 style="margin-top:0;">Forza Horizon</h3>
                    </div>
                </div>
            </div>
        </div>

        <div id="os-taskbar">
            <!-- Windows 11 start menu icon placeholder -->
            <div class="taskbar-icon">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="#0078D4"><rect x="2" y="2" width="9" height="9"></rect><rect x="13" y="2" width="9" height="9"></rect><rect x="2" y="13" width="9" height="9"></rect><rect x="13" y="13" width="9" height="9"></rect></svg>
            </div>
            <div class="taskbar-icon" onclick="openOSWindow('projects-window')">
                <img src="https://img.icons8.com/color/48/000000/folder-invoices.png" width="24" height="24">
            </div>
            <div class="taskbar-icon" onclick="openOSWindow('games-window')">
                <img src="https://img.icons8.com/color/48/000000/controller.png" width="24" height="24">
            </div>
            <div style="flex: 1;"></div>
            <div class="taskbar-icon active" onclick="closeOSModal()" title="Bilgisayarı Kapat (Odaya Dön)">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ff5f56" stroke-width="2"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path><line x1="12" y1="2" x2="12" y2="12"></line></svg>
            </div>
        </div>
    </div>
'''

content = re.sub(r'<div id=\"project-modal\".*?<!-- Proje Detay Modalı', html + '\n    <!-- Proje Detay Modalı', content, flags=re.DOTALL)

# 4. Update JS logic
js = '''
        let activeZIndex = 1000;
        function openOSModal() {
            document.getElementById('os-modal').style.display = 'block';
        }
        function closeOSModal() {
            document.getElementById('os-modal').style.display = 'none';
            document.querySelectorAll('.os-window').forEach(w => w.style.display = 'none');
        }
        function openOSWindow(id) {
            const win = document.getElementById(id);
            if (win.style.display !== 'flex') {
                win.style.display = 'flex';
                // Reset position to center when opened
                win.style.top = "50%";
                win.style.left = "50%";
                win.style.transform = "translate(-50%, -50%)";
            }
            activeZIndex++;
            win.style.zIndex = activeZIndex;
        }
        function closeOSWindow(id) {
            document.getElementById(id).style.display = 'none';
        }
        
        function dragOSWindow(e, id) {
            const win = document.getElementById(id);
            activeZIndex++;
            win.style.zIndex = activeZIndex;
            
            // Only drag if clicking on the header itself, not the buttons
            if(e.target.classList.contains('os-win-btn')) return;
            
            let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
            pos3 = e.clientX;
            pos4 = e.clientY;
            
            document.onmouseup = closeDragElement;
            document.onmousemove = elementDrag;
            
            function elementDrag(e) {
                e.preventDefault();
                pos1 = pos3 - e.clientX;
                pos2 = pos4 - e.clientY;
                pos3 = e.clientX;
                pos4 = e.clientY;
                
                win.style.top = (win.offsetTop - pos2) + "px";
                win.style.left = (win.offsetLeft - pos1) + "px";
                win.style.transform = "none"; // Remove centering transform when dragging
            }
            
            function closeDragElement() {
                document.onmouseup = null;
                document.onmousemove = null;
            }
        }
'''

content = content.replace('function openProjectModal() {', js + '\n        function openProjectModal() {')
content = content.replace('projModal.style.display = "block";', 'openOSModal();')
content = content.replace("const projModal = document.getElementById('project-modal');", "")

# Remove references to projModal inside window click handler
content = content.replace("if (event.target == projModal) {", "if (false) {")
content = content.replace("projModal.style.display = \"none\";", "")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("SUCCESS")
