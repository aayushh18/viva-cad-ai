const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let backendProcess;

function createWindow() {
    const win = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js'),
        },
        backgroundColor: '#0a0a0c',
        titleBarStyle: 'hiddenInset',
    });

    // In development, load from Vite dev server
    win.loadURL('http://localhost:5173');
}

function startBackend() {
    // Start the FastAPI backend
    backendProcess = spawn('python', ['../backend/main.py'], {
        shell: true,
        stdio: 'inherit'
    });
}

app.whenReady().then(() => {
    startBackend();
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
    if (backendProcess) {
        backendProcess.kill();
    }
});
