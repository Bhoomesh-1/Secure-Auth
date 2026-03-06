import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import './Dashboard.css';

const Dashboard = () => {
  const { user } = useAuth();

  return (
    <div className="dashboard-container">
      <div className="dashboard-card">
        <div className="dashboard-header">
          <h1>Dashboard</h1>
          <p className="dashboard-subtitle">Welcome back, {user?.name}!</p>
        </div>

        <div className="dashboard-content">
          <div className="quick-actions">
            <Link to="/security" className="action-card security-card">
              <div className="action-icon">🛡️</div>
              <h3>Security</h3>
              <p>Real-time security status</p>
            </Link>
            <Link to="/profile" className="action-card">
              <div className="action-icon">👤</div>
              <h3>Profile</h3>
              <p>View and edit your profile</p>
            </Link>
            <Link to="/settings" className="action-card">
              <div className="action-icon">⚙️</div>
              <h3>Settings</h3>
              <p>Manage your preferences</p>
            </Link>
            {user?.role === 'admin' && (
              <Link to="/admin" className="action-card admin-card">
                <div className="action-icon">👑</div>
                <h3>Admin Panel</h3>
                <p>Manage users and system</p>
              </Link>
            )}
          </div>

          <div className="info-section">
            <div className="info-card">
              <div className="card-icon">🔒</div>
              <h3>Secure Authentication</h3>
              <p>Your account is protected with industry-standard security measures.</p>
            </div>

            <div className="info-card">
              <div className="card-icon">✅</div>
              <h3>Session Active</h3>
              <p>You are currently logged in and authenticated.</p>
            </div>

            <div className="info-card">
              <div className="card-icon">🛡️</div>
              <h3>Security Features</h3>
              <ul>
                <li>HTTP-Only Cookie Authentication</li>
                <li>Bcrypt Password Hashing</li>
                <li>Rate Limiting Protection</li>
                <li>JWT Token Security</li>
                <li>Protected Routes</li>
                <li>Role-Based Access Control</li>
              </ul>
            </div>
          </div>

          <div className="user-info-card">
            <h3>Account Information</h3>
            <div className="info-row">
              <span className="info-label">Name:</span>
              <span className="info-value">{user?.name}</span>
            </div>
            <div className="info-row">
              <span className="info-label">Email:</span>
              <span className="info-value">{user?.email}</span>
            </div>
            <div className="info-row">
              <span className="info-label">Role:</span>
              <span className={`role-badge ${user?.role}`}>
                {user?.role === 'admin' ? '👑 Administrator' : '👤 User'}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
