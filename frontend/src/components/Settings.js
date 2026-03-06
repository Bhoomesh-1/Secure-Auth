import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import './Settings.css';

const Settings = () => {
  const { user } = useAuth();
  const [settings, setSettings] = useState({
    notifications: true,
    emailUpdates: true,
    darkMode: false,
    twoFactor: false
  });

  const handleToggle = (key) => {
    setSettings(prev => ({
      ...prev,
      [key]: !prev[key]
    }));
  };

  const handleSave = () => {
    // In a real app, this would save to backend
    alert('Settings saved successfully!');
  };

  return (
    <div className="settings-container">
      <div className="settings-card">
        <div className="settings-header">
          <h1>Settings</h1>
          <p>Manage your account settings and preferences</p>
        </div>

        <div className="settings-content">
          <div className="settings-section">
            <h2>Account Settings</h2>
            <div className="setting-item">
              <div className="setting-info">
                <h3>Email Notifications</h3>
                <p>Receive email notifications about your account</p>
              </div>
              <label className="toggle-switch">
                <input
                  type="checkbox"
                  checked={settings.notifications}
                  onChange={() => handleToggle('notifications')}
                />
                <span className="slider"></span>
              </label>
            </div>

            <div className="setting-item">
              <div className="setting-info">
                <h3>Email Updates</h3>
                <p>Get updates about new features and security</p>
              </div>
              <label className="toggle-switch">
                <input
                  type="checkbox"
                  checked={settings.emailUpdates}
                  onChange={() => handleToggle('emailUpdates')}
                />
                <span className="slider"></span>
              </label>
            </div>
          </div>

          <div className="settings-section">
            <h2>Security Settings</h2>
            <div className="setting-item">
              <div className="setting-info">
                <h3>Two-Factor Authentication</h3>
                <p>Add an extra layer of security to your account</p>
              </div>
              <label className="toggle-switch">
                <input
                  type="checkbox"
                  checked={settings.twoFactor}
                  onChange={() => handleToggle('twoFactor')}
                />
                <span className="slider"></span>
              </label>
            </div>

            <div className="security-actions">
              <button className="action-button change-password">
                Change Password
              </button>
              <button className="action-button view-sessions">
                View Active Sessions
              </button>
            </div>
          </div>

          <div className="settings-section">
            <h2>Appearance</h2>
            <div className="setting-item">
              <div className="setting-info">
                <h3>Dark Mode</h3>
                <p>Switch to dark theme</p>
              </div>
              <label className="toggle-switch">
                <input
                  type="checkbox"
                  checked={settings.darkMode}
                  onChange={() => handleToggle('darkMode')}
                />
                <span className="slider"></span>
              </label>
            </div>
          </div>

          <div className="settings-actions">
            <button onClick={handleSave} className="save-settings-button">
              Save Settings
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Settings;
