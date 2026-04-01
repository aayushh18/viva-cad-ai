import { useState, useEffect, useRef } from 'react';
import Editor from '@monaco-editor/react';
import './index.css';

interface Design {
  id: number;
  prompt: string;
  schema_json: string;
  status: string;
  created_at: string;
}

interface Iteration {
  id: number;
  design_id: number;
  version: number;
  error_log: string | null;
  file_path: string | null;
}

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [designs, setDesigns] = useState<Design[]>([]);
  const [selectedDesign, setSelectedDesign] = useState<Design | null>(null);
  const [iterations, setIterations] = useState<Iteration[]>([]);
  const [loading, setLoading] = useState(false);
  const isExecutingRef = useRef(false);
  const [headless, setHeadless] = useState(true);
  const [editedCode, setEditedCode] = useState<string>("");

  useEffect(() => {
    fetchDesigns();
  }, []);

  const fetchDesigns = async () => {
    try {
      const resp = await fetch('http://localhost:8000/designs');
      const data = await resp.json();
      setDesigns(data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleGenerate = async () => {
    if (loading || isExecutingRef.current) return;
    setLoading(true);
    isExecutingRef.current = true;
    try {
      const resp = await fetch(`http://localhost:8000/designs/generate?prompt=${encodeURIComponent(prompt)}`, {
        method: 'POST'
      });
      const data = await resp.json();
      setDesigns(prev => [data, ...prev]);
      setSelectedDesign(data);
      try {
        const parsed = JSON.parse(data.schema_json);
        setEditedCode(parsed.code || parsed.python_script || "No code generated.");
      } catch(e) {
        setEditedCode("Error parsing script data.");
      }

      if (!headless) {
        try {
          const buildResp = await fetch(`http://localhost:8000/designs/${data.id}/build?headless=false`, { method: 'POST' });
          const buildData = await buildResp.json();
          setDesigns(prev => prev.map(d => d.id === data.id ? buildData.design : d));
          setSelectedDesign(buildData.design);
          fetchIterations(data.id);
        } catch(err) {
          console.error("Auto-execution error:", err);
        }
      }

      setPrompt("");
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
      isExecutingRef.current = false;
    }
  };

  const handleBuild = async (id: number) => {
    if (loading || isExecutingRef.current) return;
    setLoading(true);
    isExecutingRef.current = true;
    try {
      await fetch(`http://localhost:8000/designs/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ python_script: editedCode })
      });

      const resp = await fetch(`http://localhost:8000/designs/${id}/build?headless=${headless}`, { method: 'POST' });
      const data = await resp.json();
      setDesigns(prev => prev.map(d => d.id === id ? data.design : d));
      if (selectedDesign?.id === id) {
        setSelectedDesign(data.design);
        fetchIterations(id);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
      isExecutingRef.current = false;
    }
  };

  const fetchIterations = async (id: number) => {
    try {
      const resp = await fetch(`http://localhost:8000/designs/${id}/iterations`);
      const data = await resp.json();
      setIterations(data);
    } catch (err) {
      console.error(err);
    }
  };

  const selectDesign = (design: Design) => {
    setSelectedDesign(design);
    setPrompt(design.prompt);
    try {
      const parsed = JSON.parse(design.schema_json);
      setEditedCode(parsed.code || parsed.python_script || "No code generated.");
    } catch(e) {
      setEditedCode("Error parsing script data.");
    }
    fetchIterations(design.id);
  };

  const handleDeleteDesign = async (id: number, e: React.MouseEvent) => {
    e.stopPropagation();
    try {
      if (confirm('Delete this design?')) {
        await fetch(`http://localhost:8000/designs/${id}`, { method: 'DELETE' });
        setDesigns(prev => prev.filter(d => d.id !== id));
        if (selectedDesign?.id === id) {
          setSelectedDesign(null);
          setIterations([]);
        }
      }
    } catch (err) {
      console.error(err);
    }
  };

  const handleClearHistory = async () => {
    try {
      if (confirm('Clear all design history?')) {
        await fetch('http://localhost:8000/designs', { method: 'DELETE' });
        setDesigns([]);
        setSelectedDesign(null);
        setIterations([]);
      }
    } catch (err) {
      console.error(err);
    }
  };

  const ExamplePrompts = () => (
    <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap', marginBottom: '10px' }}>
      {[
        "Create a box with fillet edges",
        "Design a mounting plate with 4 corner holes",
        "Create a plate with slot and boss",
        "Create a cylinder with radius 10 and height 40"
      ].map((ex, i) => (
        <button 
          key={i} 
          onClick={() => setPrompt(ex)}
          style={{ 
            background: 'rgba(255,255,255,0.1)', 
            border: '1px solid rgba(255,255,255,0.2)', 
            borderRadius: '12px', 
            padding: '4px 10px', 
            fontSize: '0.8rem', 
            color: '#fff', 
            cursor: 'pointer' 
          }}
        >
          {ex.length > 25 ? ex.substring(0, 25) + "..." : ex}
        </button>
      ))}
    </div>
  );

  return (
    <div className="app-container">
      <header>
        <h1>VIVA <span>CAD AI</span> PRO</h1>
        <p className="subtitle">Enterprise AI-Driven Mechanical Design</p>
      </header>

      <div className="main-grid">
        <section className="input-section">
          <div className="glass-card prompt-box">
            <ExamplePrompts />
            <textarea
              placeholder="Describe your design... e.g., '120x80x10 base plate with M6 holes'"
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
            />
            <div className="actions">
              <label className="gui-toggle">
                <input
                  type="checkbox"
                  checked={!headless}
                  onChange={() => setHeadless(!headless)}
                />
                GUI Mode (Opens FreeCAD)
              </label>
              <button className="btn-primary" onClick={handleGenerate} disabled={loading}>
                {loading ? "Generating..." : "Generate Script"}
              </button>
            </div>
          </div>

          <div className="history-list">
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <h2 style={{ margin: 0 }}>Design History</h2>
              {designs.length > 0 && (
                <button 
                  onClick={handleClearHistory} 
                  style={{ background: 'rgba(255,50,50,0.2)', border: 'none', color: '#ffaaaa', padding: '4px 8px', borderRadius: '4px', cursor: 'pointer', fontSize: '0.8rem' }}
                >
                  Clear All
                </button>
              )}
            </div>
            {designs.map(d => (
              <div
                key={d.id}
                className={`history-item ${selectedDesign?.id === d.id ? 'active' : ''} ${loading ? 'disabled' : ''}`}
                onClick={() => !loading && selectDesign(d)}
                style={{ position: 'relative', paddingRight: '30px', opacity: loading ? 0.6 : 1, pointerEvents: loading ? 'none' : 'auto' }}
              >
                <button 
                  className="delete-btn"
                  onClick={(e) => handleDeleteDesign(d.id, e)}
                  style={{ 
                    position: 'absolute', 
                    top: '12px', 
                    right: '10px', 
                    background: 'transparent', 
                    border: 'none', 
                    color: '#ff4444', 
                    cursor: 'pointer', 
                    fontSize: '1rem',
                    opacity: 0.7 
                  }}
                  title="Delete Design"
                >
                  ✕
                </button>
                <p>{d.prompt.substring(0, 40)}...</p>
                <span className={`badge status-${d.status.toLowerCase()}`}>{d.status}</span>
              </div>
            ))}
          </div>
        </section>

        <section className="workspace">
          {selectedDesign ? (
            <div className="design-panel">
              <div className="workspace-header">
                <h2>{selectedDesign.prompt.substring(0, 30)}...</h2>
                <button
                  className="btn-build"
                  onClick={() => handleBuild(selectedDesign.id)}
                  disabled={loading}
                  title="Saves your script edits and runs it in FreeCAD"
                >
                  {loading ? "Running..." : "Save & Run in FreeCAD"}
                </button>
              </div>

              <div className="design-details">
                <div className="glass-card schema-viewer" style={{ display: 'flex', flexDirection: 'column', height: '400px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <h3 style={{ margin: 0 }}>Python Script</h3>
                    {(() => {
                      let stepFile = "";
                      try {
                        const parsed = JSON.parse(selectedDesign.schema_json);
                        stepFile = parsed.file || "";
                      } catch(e) {}
                      return stepFile ? (
                        <button onClick={() => window.open(`http://localhost:8000/download?file=${encodeURIComponent(stepFile)}`)} className="btn-secondary" style={{ fontSize: '0.8rem', padding: '6px 12px', borderRadius: '4px', cursor: 'pointer', backgroundColor: '#4a90e2', color: '#fff', border: 'none' }}>
                          Download {stepFile.split('/').pop()}
                        </button>
                      ) : null;
                    })()}
                  </div>
                  <div style={{ flex: 1, marginTop: '10px', borderRadius: '8px', overflow: 'hidden' }}>
                    <Editor
                      height="100%"
                      defaultLanguage="python"
                      theme="vs-dark"
                      value={editedCode}
                      onChange={(value) => setEditedCode(value || "")}
                      options={{ readOnly: false, minimap: { enabled: false } }}
                    />
                  </div>
                </div>

                <div className="iteration-log">
                  <h3>Execution Logs</h3>
                  {iterations.length > 0 ? (
                    iterations.map(it => (
                      <div key={it.id} className="log-item">
                        <p>Version {it.version}</p>
                        {it.error_log ? (
                          <pre className="error">{it.error_log}</pre>
                        ) : (
                          <p className="success">Success: {it.file_path}</p>
                        )}
                      </div>
                    ))
                  ) : (
                    <p>No build attempts yet.</p>
                  )}
                </div>
              </div>
            </div>
          ) : (
            <div className="empty-workspace">
              <p>Select a design from history or generate a new one.</p>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}
