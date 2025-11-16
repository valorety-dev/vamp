import React from 'react';
import { useAuth } from '../context/AuthContext';
import './Dashboard.css';

function Dashboard() {
  const { user } = useAuth();

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1 className="page-title">Dashboard Overview</h1>
        <p className="page-subtitle">Welcome back, {user?.username || 'Admin'}</p>
      </div>

      <div className="stats-grid">
        <div className="stat-card">
          <div className="stat-label">Total Servers</div>
          <div className="stat-value">1</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Total Members</div>
          <div className="stat-value">847</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Commands Used</div>
          <div className="stat-value">1,234</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">Bot Uptime</div>
          <div className="stat-value">99.9%</div>
        </div>
      </div>

      <div className="features-section">
        <h2 className="section-title">Quick Actions</h2>
        
        <div className="features-grid">
          <div className="feature-item">
            <div className="feature-info">
              <h3>Moderation Tools</h3>
              <p>Manage kicks, bans, and mutes</p>
            </div>
          </div>
          <div className="feature-item">
            <div className="feature-info">
              <h3>Server Analytics</h3>
              <p>View detailed server statistics</p>
            </div>
          </div>
          <div className="feature-item">
            <div className="feature-info">
              <h3>Command Management</h3>
              <p>Configure bot commands</p>
            </div>
          </div>
          <div className="feature-item">
            <div className="feature-info">
              <h3>Role Management</h3>
              <p>Assign and manage server roles</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
