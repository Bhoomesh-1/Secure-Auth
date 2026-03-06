import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import './Profile.css';

const Profile = () => {
  const { user } = useAuth();
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    name: user?.name || '',
    email: user?.email || ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    // In a real app, this would update the user profile via API
    alert('Profile update feature coming soon!');
    setIsEditing(false);
  };

  return (
    <div className="profile-container">
      <div className="profile-card">
        <div className="profile-header">
          <div className="profile-avatar">
            <span>{user?.name?.charAt(0).toUpperCase() || 'U'}</span>
          </div>
          <h1>Profile</h1>
        </div>

        <div className="profile-content">
          {!isEditing ? (
            <div className="profile-info">
              <div className="info-item">
                <label>Name</label>
                <div className="info-value">{user?.name}</div>
              </div>
              <div className="info-item">
                <label>Email</label>
                <div className="info-value">{user?.email}</div>
              </div>
              <div className="info-item">
                <label>Role</label>
                <div className="info-value">
                  <span className={`role-badge ${user?.role}`}>
                    {user?.role === 'admin' ? '👑 Admin' : '👤 User'}
                  </span>
                </div>
              </div>
              <div className="info-item">
                <label>User ID</label>
                <div className="info-value">#{user?.id}</div>
              </div>
              <button 
                onClick={() => setIsEditing(true)} 
                className="edit-button"
              >
                Edit Profile
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="profile-form">
              <div className="form-group">
                <label>Name</label>
                <input
                  type="text"
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                  required
                />
              </div>
              <div className="form-group">
                <label>Email</label>
                <input
                  type="email"
                  value={formData.email}
                  disabled
                  className="disabled-input"
                />
                <small>Email cannot be changed</small>
              </div>
              <div className="form-actions">
                <button type="submit" className="save-button">
                  Save Changes
                </button>
                <button 
                  type="button" 
                  onClick={() => setIsEditing(false)}
                  className="cancel-button"
                >
                  Cancel
                </button>
              </div>
            </form>
          )}

          <div className="profile-stats">
            <div className="stat-card">
              <div className="stat-icon">🔒</div>
              <div className="stat-info">
                <div className="stat-value">Active</div>
                <div className="stat-label">Session Status</div>
              </div>
            </div>
            <div className="stat-card">
              <div className="stat-icon">🛡️</div>
              <div className="stat-info">
                <div className="stat-value">Protected</div>
                <div className="stat-label">Account Security</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
