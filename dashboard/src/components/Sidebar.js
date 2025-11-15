import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Sidebar.css';

function Sidebar() {
  const navigate = useNavigate();
  const location = useLocation();
  const { user, logout } = useAuth();

  const isActive = (path) => {
    return location.pathname === `/dashboard${path}`;
  };

  const handleLogout = async () => {
    await logout();
    navigate('/');
  };

  return (
    <div className="sidebar">
      <div className="logo">
        <h1>VAMP</h1>
        <div className="logo-glow"></div>
      </div>
      
      <nav className="nav-menu">
        <button
          className={isActive('') || isActive('/') ? 'active' : ''}
          onClick={() => navigate('/dashboard')}
        >
          <span className="nav-icon">📊</span>
          Dashboard
        </button>
        <button
          className={isActive('/commands') ? 'active' : ''}
          onClick={() => navigate('/dashboard/commands')}
        >
          <span className="nav-icon">⚡</span>
          Commands
        </button>
        <button
          className={isActive('/stats') ? 'active' : ''}
          onClick={() => navigate('/dashboard/stats')}
        >
          <span className="nav-icon">📈</span>
          Statistics
        </button>
      </nav>

      {user && (
        <div className="sidebar-user">
          <img src={user.avatar} alt={user.username} className="user-avatar" />
          <div className="user-info">
            <p className="user-name">{user.username}</p>
            <p className="user-id">#{user.discriminator}</p>
          </div>
          <button className="logout-btn" onClick={handleLogout}>
            Logout
          </button>
        </div>
      )}

      <div className="sidebar-footer">
        <p>Bot Status</p>
        <div className="status-indicator">
          <span className="status-dot"></span>
          Online
        </div>
      </div>
    </div>
  );
}

export default Sidebar;
