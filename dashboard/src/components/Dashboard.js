import React from 'react';
import { useAuth } from '../context/AuthContext';
import './Dashboard.css';

function Dashboard() {
  const { user } = useAuth();

  return (
    <div className="dashboard">
      <div className="page-header">
        <div>
          <h1>Dashboard</h1>
          <p>Welcome back, {user?.username || 'Admin'}</p>
        </div>
      </div>

      <div className="stats-container">
        <div className="stat-box">
          <div className="stat-header">Servers</div>
          <div className="stat-number">1</div>
          <div className="stat-footer">Active servers</div>
        </div>
        
        <div className="stat-box">
          <div className="stat-header">Members</div>
          <div className="stat-number">847</div>
          <div className="stat-footer">Total members</div>
        </div>
        
        <div className="stat-box">
          <div className="stat-header">Commands</div>
          <div className="stat-number">1,234</div>
          <div className="stat-footer">Total executed</div>
        </div>
        
        <div className="stat-box">
          <div className="stat-header">Uptime</div>
          <div className="stat-number">99.9%</div>
          <div className="stat-footer">Last 30 days</div>
        </div>
      </div>

      <div className="content-section">
        <div className="section-header">
          <h2>Quick Actions</h2>
        </div>
        
        <div className="action-grid">
          <button className="action-box">
            <div className="action-title">Moderation</div>
            <div className="action-description">Manage members and permissions</div>
          </button>
          
          <button className="action-box">
            <div className="action-title">Analytics</div>
            <div className="action-description">View detailed statistics</div>
          </button>
          
          <button className="action-box">
            <div className="action-title">Commands</div>
            <div className="action-description">Configure bot commands</div>
          </button>
          
          <button className="action-box">
            <div className="action-title">Settings</div>
            <div className="action-description">Manage bot configuration</div>
          </button>
        </div>
      </div>

      <div className="content-section">
        <div className="section-header">
          <h2>Recent Activity</h2>
        </div>
        
        <div className="activity-container">
          <div className="activity-item">
            <div className="activity-dot"></div>
            <div className="activity-content">
              <div className="activity-title">Member joined</div>
              <div className="activity-time">2 minutes ago</div>
            </div>
          </div>
          
          <div className="activity-item">
            <div className="activity-dot"></div>
            <div className="activity-content">
              <div className="activity-title">Command executed</div>
              <div className="activity-time">15 minutes ago</div>
            </div>
          </div>
          
          <div className="activity-item">
            <div className="activity-dot"></div>
            <div className="activity-content">
              <div className="activity-title">Role updated</div>
              <div className="activity-time">1 hour ago</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
