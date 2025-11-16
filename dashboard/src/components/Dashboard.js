import React from 'react';
import { useAuth } from '../context/AuthContext';
import './Dashboard.css';

function Dashboard() {
  const { user } = useAuth();

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <div>
          <h1 className="page-title">Welcome back, <span className="username">{user?.username || 'Admin'}</span></h1>
          <p className="page-subtitle">Here's what's happening with your server today • USD: #160</p>
        </div>
      </div>

      <div className="info-cards">
        <div className="info-card">
          <div className="card-label">Subscription</div>
          <div className="card-value">FREE</div>
          <button className="upgrade-btn">👑 Upgrade</button>
        </div>
        <div className="info-card">
          <div className="card-label">User ID</div>
          <div className="card-value">#160</div>
          <div className="card-meta">Account Creation Date:</div>
        </div>
        <div className="info-card">
          <div className="card-label">Profile URL</div>
          <div className="card-value">vamp.lol/</div>
        </div>
        <div className="info-card">
          <div className="card-label">Profile Status</div>
          <div className="card-value">Offline</div>
        </div>
      </div>

      <div className="stats-section">
        <h2 className="section-title">Server Statistics</h2>
        <p className="section-subtitle">Track your bot's performance over time</p>
        
        <div className="stats-grid">
          <div className="stat-card">
            <h3>Total Servers</h3>
            <div className="stat-value">1</div>
            <div className="stat-meta">0 unique servers</div>
          </div>
          <div className="stat-card">
            <h3>Total Members</h3>
            <div className="stat-value">847</div>
            <div className="stat-meta">Across all servers</div>
          </div>
          <div className="stat-card">
            <h3>Commands Used</h3>
            <div className="stat-value">1,234</div>
            <div className="stat-meta">Total command executions</div>
          </div>
          <div className="stat-card">
            <h3>Bot Uptime</h3>
            <div className="stat-value">99.9%</div>
            <div className="stat-meta">Last 30 days</div>
          </div>
        </div>
      </div>

      <div className="features-section">
        <h2 className="section-title">Bot Features</h2>
        <p className="section-subtitle">Complete your profile to increase visibility</p>
        
        <div className="progress-bar">
          <div className="progress-fill" style={{ width: '33%' }}></div>
        </div>
        <div className="progress-label">33%</div>

        <div className="features-grid">
          <div className="feature-item">
            <div className="feature-icon active">✓</div>
            <div className="feature-info">
              <h3>Moderation Tools</h3>
              <p>Kick, ban, mute members efficiently</p>
            </div>
          </div>
          <div className="feature-item">
            <div className="feature-icon">○</div>
            <div className="feature-info">
              <h3>Auto Moderation</h3>
              <p>Configure automated mod actions</p>
            </div>
          </div>
          <div className="feature-item">
            <div className="feature-icon">○</div>
            <div className="feature-info">
              <h3>Custom Commands</h3>
              <p>Create custom bot commands</p>
            </div>
          </div>
          <div className="feature-item">
            <div className="feature-icon">○</div>
            <div className="feature-info">
              <h3>Analytics Dashboard</h3>
              <p>View detailed server analytics</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
