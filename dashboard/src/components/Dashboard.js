import React from 'react';
import { motion } from 'framer-motion';
import './Dashboard.css';

function Dashboard() {
  const stats = [
    { icon: '🖥️', label: 'Active Servers', value: '1', color: '#8b5cf6' },
    { icon: '👥', label: 'Total Members', value: '847', color: '#3b82f6' },
    { icon: '⚡', label: 'Commands Run', value: '1.2K', color: '#f59e0b' },
    { icon: '🚀', label: 'Bot Uptime', value: '99.9%', color: '#10b981' }
  ];

  const features = [
    {
      icon: '🛡️',
      title: 'Advanced Moderation',
      description: 'Comprehensive tools for managing your community with precision',
      gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    },
    {
      icon: '📊',
      title: 'Real-Time Analytics',
      description: 'Monitor server health and member activity with live dashboards',
      gradient: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'
    },
    {
      icon: '⚙️',
      title: 'Custom Configuration',
      description: 'Tailor every aspect of VAMP to fit your server\'s unique needs',
      gradient: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)'
    }
  ];

  return (
    <div className="dashboard">
      <motion.div 
        className="dashboard-header"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div>
          <h1 className="page-title">Welcome Back</h1>
          <p className="page-subtitle">Here's what's happening with your server today</p>
        </div>
        <motion.div 
          className="quick-actions"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.3 }}
        >
          <button className="action-btn primary">
            <span>⚡</span> Quick Action
          </button>
          <button className="action-btn secondary">
            <span>📝</span> View Logs
          </button>
        </motion.div>
      </motion.div>

      <div className="stats-grid">
        {stats.map((stat, index) => (
          <motion.div
            key={index}
            className="stat-card"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1, duration: 0.5 }}
            whileHover={{ y: -5, transition: { duration: 0.2 } }}
          >
            <div className="stat-icon" style={{ background: stat.color }}>
              {stat.icon}
            </div>
            <div className="stat-content">
              <p className="stat-label">{stat.label}</p>
              <h3 className="stat-value">{stat.value}</h3>
            </div>
            <div className="stat-glow" style={{ background: `${stat.color}22` }}></div>
          </motion.div>
        ))}
      </div>

      <div className="dashboard-content">
        <motion.div 
          className="features-section"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5 }}
        >
          <h2 className="section-title">Powerful Features</h2>
          <div className="features-grid">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                className="feature-card"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.6 + index * 0.1 }}
                whileHover={{ scale: 1.02, transition: { duration: 0.2 } }}
              >
                <div className="feature-gradient" style={{ background: feature.gradient }}></div>
                <div className="feature-icon">{feature.icon}</div>
                <h3>{feature.title}</h3>
                <p>{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>

        <motion.div 
          className="activity-section"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.8 }}
        >
          <div className="activity-header">
            <h2 className="section-title">Recent Activity</h2>
            <button className="view-all-btn">View All →</button>
          </div>
          <div className="activity-list">
            {[
              { action: 'Member Joined', user: '@newuser', time: '2 minutes ago', type: 'success' },
              { action: 'Message Deleted', user: '@moderator', time: '15 minutes ago', type: 'warning' },
              { action: 'Role Assigned', user: '@admin', time: '1 hour ago', type: 'info' }
            ].map((activity, index) => (
              <motion.div 
                key={index}
                className="activity-item"
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: 0.9 + index * 0.1 }}
              >
                <div className={`activity-indicator ${activity.type}`}></div>
                <div className="activity-content">
                  <p className="activity-action">{activity.action}</p>
                  <p className="activity-meta">{activity.user} • {activity.time}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </div>
    </div>
  );
}

export default Dashboard;
