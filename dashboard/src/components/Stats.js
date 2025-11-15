import React from 'react';
import './Stats.css';

function Stats() {
  return (
    <div className="stats-page">
      <h1 className="page-title">Statistics</h1>
      
      <div className="stats-overview">
        <div className="stat-box">
          <h3>Total Servers</h3>
          <p className="big-number">1</p>
          <span className="stat-label">Active</span>
        </div>
        
        <div className="stat-box">
          <h3>Total Users</h3>
          <p className="big-number">847</p>
          <span className="stat-label">Members</span>
        </div>
        
        <div className="stat-box">
          <h3>Commands Today</h3>
          <p className="big-number">142</p>
          <span className="stat-label">Executed</span>
        </div>
        
        <div className="stat-box">
          <h3>Moderation Actions</h3>
          <p className="big-number">28</p>
          <span className="stat-label">This Week</span>
        </div>
      </div>

      <div className="activity-section">
        <h2>Recent Activity</h2>
        <div className="activity-list">
          <div className="activity-item">
            <span className="activity-time">2 minutes ago</span>
            <span className="activity-text">User banned from server</span>
            <span className="activity-badge kick">Ban</span>
          </div>
          <div className="activity-item">
            <span className="activity-time">15 minutes ago</span>
            <span className="activity-text">Messages cleared in #general</span>
            <span className="activity-badge clear">Clear</span>
          </div>
          <div className="activity-item">
            <span className="activity-time">1 hour ago</span>
            <span className="activity-text">User muted for 30 minutes</span>
            <span className="activity-badge mute">Mute</span>
          </div>
          <div className="activity-item">
            <span className="activity-time">3 hours ago</span>
            <span className="activity-text">Server stats requested</span>
            <span className="activity-badge info">Info</span>
          </div>
          <div className="activity-item">
            <span className="activity-time">5 hours ago</span>
            <span className="activity-text">User kicked from server</span>
            <span className="activity-badge kick">Kick</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Stats;
