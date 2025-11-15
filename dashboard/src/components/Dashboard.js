import React from 'react';
import './Dashboard.css';

function Dashboard() {
  return (
    <div className="dashboard">
      <h1 className="page-title">Dashboard</h1>
      
      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-icon">🖥️</div>
          <div className="stat-info">
            <h3>Servers</h3>
            <p className="stat-value">1</p>
          </div>
          <div className="card-glow"></div>
        </div>

        <div className="stat-card">
          <div className="stat-icon">👥</div>
          <div className="stat-info">
            <h3>Total Users</h3>
            <p className="stat-value">847</p>
          </div>
          <div className="card-glow"></div>
        </div>

        <div className="stat-card">
          <div className="stat-icon">⚡</div>
          <div className="stat-info">
            <h3>Commands Used</h3>
            <p className="stat-value">1,234</p>
          </div>
          <div className="card-glow"></div>
        </div>

        <div className="stat-card">
          <div className="stat-icon">📊</div>
          <div className="stat-info">
            <h3>Uptime</h3>
            <p className="stat-value">99.9%</p>
          </div>
          <div className="card-glow"></div>
        </div>
      </div>

      <div className="info-section">
        <h2>Welcome to VAMP Bot Dashboard</h2>
        <p>Powerful moderation and utility bot for Discord servers</p>
        
        <div className="features">
          <div className="feature">
            <h3>Moderation</h3>
            <p>Kick, ban, mute, and manage your server members efficiently</p>
          </div>
          <div className="feature">
            <h3>Statistics</h3>
            <p>Track server activity and bot usage in real-time</p>
          </div>
          <div className="feature">
            <h3>Custom Commands</h3>
            <p>Full control over bot commands and permissions</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
